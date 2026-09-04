from urllib.parse import urlsplit

import requests

from . import errors


class AnixartParser:
    """Синхронный клиент каталога Anixart."""

    _TITLE_FIELDS = ("title", "title_ru", "title_original", "title_alt")

    _HEADERS = {
        "Accept": "application/json",
        "API-Version": "v2",
        "User-Agent": "anime-parsers-ru/AnixartParser",
    }

    def __init__(
        self,
        base_url: str = "https://api-s.anixsekai.com/",
        proxy: str | None = None,
        timeout: float = 10,
        session: requests.Session | None = None,
    ) -> None:
        if not isinstance(base_url, str):
            raise TypeError("base_url должен быть строкой.")
        if not base_url.strip():
            raise ValueError("base_url не должен быть пустым.")
        if proxy is not None and not isinstance(proxy, str):
            raise TypeError("proxy должен быть строкой или None.")
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)):
            raise TypeError("timeout должен быть числом.")
        if timeout <= 0:
            raise ValueError("timeout должен быть больше нуля.")
        if session is not None and not all(
            callable(getattr(session, method, None)) for method in ("get", "post")
        ):
            raise TypeError("session должен поддерживать методы get и post.")

        self.base_url = base_url.strip().rstrip("/") + "/"
        self.proxies = {"http": proxy, "https": proxy} if proxy else None
        self.timeout = timeout
        self.session = session if session is not None else requests.Session()

    def _request(self, method: str, path: str, **kwargs) -> dict:
        try:
            response = getattr(self.session, method)(
                f"{self.base_url}{path}",
                headers=self._HEADERS,
                proxies=self.proxies,
                timeout=self.timeout,
                **kwargs,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            raise errors.ServiceError(f"Ошибка HTTP-запроса к Anixart: {exc}") from exc
        try:
            payload = response.json()
        except ValueError as exc:
            raise errors.UnexpectedBehavior(
                "Anixart вернул ответ, который не является корректным JSON."
            ) from exc
        if not isinstance(payload, dict):
            raise errors.UnexpectedBehavior("Anixart вернул ответ неверного формата.")
        code = payload.get("code")
        if type(code) is not int:
            raise errors.UnexpectedBehavior("В ответе Anixart отсутствует корректный код.")
        if code in (402, 403):
            raise errors.ContentBlocked(f"Anixart вернул код блокировки {code}.")
        if code != 0:
            raise errors.ServiceError(f"Anixart вернул код ошибки {code}.")
        return payload

    @staticmethod
    def _extract(payload: dict, key: str, expected_type: type):
        value = payload.get(key)
        if not isinstance(value, expected_type):
            raise errors.UnexpectedBehavior(
                f'В ответе Anixart отсутствует корректное поле "{key}".'
            )
        return value

    @classmethod
    def _extract_items(
        cls,
        payload: dict,
        key: str,
        required_keys: tuple,
        integer_keys: tuple,
        string_keys: tuple = (),
    ) -> list:
        items = cls._extract(payload, key, list)
        for item in items:
            if not isinstance(item, dict) or not all(
                required_key in item for required_key in required_keys
            ):
                raise errors.UnexpectedBehavior(
                    f'В ответе Anixart поле "{key}" содержит некорректный элемент.'
                )
            if any(type(item[integer_key]) is not int for integer_key in integer_keys):
                raise errors.UnexpectedBehavior(
                    f'В ответе Anixart поле "{key}" содержит некорректный числовой ID.'
                )
            if any(not isinstance(item[string_key], str) for string_key in string_keys):
                raise errors.UnexpectedBehavior(
                    f'В ответе Anixart поле "{key}" содержит некорректную строку.'
                )
        return items

    @staticmethod
    def _validate_int(name: str, value: int, minimum: int | None = None) -> None:
        if type(value) is not int:
            raise TypeError(f"{name} должен быть целым числом.")
        if minimum is not None and value < minimum:
            raise ValueError(f"{name} должен быть не меньше {minimum}.")

    def search(self, query: str, page: int = 0, search_by: int = 0) -> list:
        if not isinstance(query, str):
            raise TypeError("query должен быть строкой.")
        if not query.strip():
            raise ValueError("query не должен быть пустым.")
        self._validate_int("page", page, 0)
        self._validate_int("search_by", search_by, 0)
        payload = self._request(
            "post",
            f"search/releases/{page}",
            json={"query": query, "searchBy": search_by},
        )
        releases = self._extract(payload, "releases", list)
        if not releases:
            raise errors.NoResults(f'По запросу "{query}" ничего не найдено.')
        for release in releases:
            if (
                not isinstance(release, dict)
                or type(release.get("id")) is not int
                or not any(
                    isinstance(release.get(field), str)
                    and bool(release[field].strip())
                    for field in self._TITLE_FIELDS
                )
            ):
                raise errors.UnexpectedBehavior(
                    'В ответе Anixart поле "releases" содержит некорректный элемент.'
                )
        return releases

    def anime_info(self, release_id: int, extended: bool = True) -> dict:
        self._validate_int("release_id", release_id, 1)
        if type(extended) is not bool:
            raise TypeError("extended должен быть логическим значением.")
        payload = self._request(
            "get",
            f"release/{release_id}?extended_mode={str(extended).lower()}",
        )
        release = self._extract(payload, "release", dict)
        if (
            not release
            or type(release.get("id")) is not int
            or release["id"] != release_id
        ):
            raise errors.UnexpectedBehavior(
                'В ответе Anixart отсутствует корректное поле "release".'
            )
        return release

    def get_types(self, release_id: int) -> list:
        self._validate_int("release_id", release_id, 1)
        payload = self._request("get", f"episode/{release_id}")
        return self._extract_items(
            payload, "types", ("id", "name"), ("id",), ("name",)
        )

    def get_sources(self, release_id: int, type_id: int) -> list:
        self._validate_int("release_id", release_id, 1)
        self._validate_int("type_id", type_id, 1)
        payload = self._request("get", f"episode/{release_id}/{type_id}")
        return self._extract_items(
            payload, "sources", ("id", "name"), ("id",), ("name",)
        )

    def get_episodes(
        self,
        release_id: int,
        type_id: int,
        source_id: int,
        sort: int | None = None,
    ) -> list:
        self._validate_int("release_id", release_id, 1)
        self._validate_int("type_id", type_id, 1)
        self._validate_int("source_id", source_id, 1)
        if sort is not None:
            self._validate_int("sort", sort)
        kwargs = {}
        if sort is not None:
            kwargs["params"] = {"sort": sort}
        payload = self._request(
            "get",
            f"episode/{release_id}/{type_id}/{source_id}",
            **kwargs,
        )
        episodes = self._extract_items(
            payload,
            "episodes",
            (
                "position",
                "name",
                "iframe",
                "quality",
                "url",
                "sourceId",
                "releaseId",
            ),
            ("position", "sourceId", "releaseId"),
            ("name",),
        )
        for episode in episodes:
            quality = episode["quality"]
            url = episode["url"]
            try:
                parsed_url = urlsplit(url) if isinstance(url, str) else None
            except ValueError:
                parsed_url = None
            if (
                episode["releaseId"] != release_id
                or episode["sourceId"] != source_id
                or type(episode["iframe"]) is not bool
                or (quality is not None and type(quality) is not int)
                or parsed_url is None
                or parsed_url.scheme.lower() not in ("http", "https")
                or not parsed_url.netloc
            ):
                raise errors.UnexpectedBehavior(
                    'В ответе Anixart поле "episodes" содержит некорректный элемент.'
                )
        return episodes

    def get_player_urls(self, release_id: int) -> list:
        """Возвращает плоский список внешних плееров в порядке ответа сервера.

        Каждый элемент содержит ровно ключи ``type_id``, ``type_name``,
        ``source_id``, ``source_name``, ``episode_position``, ``episode_name``,
        ``iframe``, ``quality`` и ``url``.
        """
        self._validate_int("release_id", release_id, 1)
        result = []
        for type_item in self.get_types(release_id):
            type_id = type_item["id"]
            type_name = type_item["name"]
            for source in self.get_sources(release_id, type_id):
                source_id = source["id"]
                source_name = source["name"]
                for episode in self.get_episodes(release_id, type_id, source_id):
                    result.append(
                        {
                            "type_id": type_id,
                            "type_name": type_name,
                            "source_id": source_id,
                            "source_name": source_name,
                            "episode_position": episode["position"],
                            "episode_name": episode["name"],
                            "iframe": episode["iframe"],
                            "quality": episode["quality"],
                            "url": episode["url"],
                        }
                    )
        return result
