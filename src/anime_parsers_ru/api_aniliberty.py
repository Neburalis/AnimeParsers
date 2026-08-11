try:
    from . import errors # Импорт если библиотека установлена
except ImportError:
    import errors # Импорт если библиотека не установлена и файл лежит локально

import requests
import json

class _BaseApi:
    def __init__(self, api_path: str = 'https://aniliberty.top/api/v1', proxy: str | None = None, auth_token: str | None = None):
        """
        :api_path: URL к апи эндпоинту (по умолчанию https://aniliberty.top/api/v1)
        :proxy: http или socks5 прокси (`http://host:port` или `socks5://user:pass@host:port`) по умолчанию None
        """
        self._api_path = api_path.rstrip('/')
        self._headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self._xml_headers = {
            'accept': 'application/xml',
            'Content-Type': 'application/json'
        }
        self._torrent_headers = {
            'accept': 'application/x-bittorrent',
            'Content-Type': 'application/json'
        }
        self._auth_token = auth_token
        self._proxies = {"http": proxy, "https": proxy} if proxy else None
    
    def _request(self, *args, **kwargs) -> requests.Response:
        auth_required = False
        if 'auth_required' in kwargs.keys():
            auth_required = kwargs['auth_required']
            del kwargs['auth_required'] # Убираем поле
        if self._auth_token and auth_required:
            if 'headers' not in kwargs.keys():
                kwargs['headers'] = {}
            kwargs['headers']['Authorization'] = f'Bearer {self._auth_token}'

        return requests.request(*args, **kwargs, proxies=self._proxies)

    def _login(self, login: str, password: str) -> bool:
        """
        Автоматически получает и устанавливает токен авторизации.
        Вернет True если успешно.

        :login: Логин (не почта, именно логин, посмотреть можно в настройках аккаунта на сайте)
        :password: Пароль
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        data = requests.request("POST", self._api_path+"/accounts/users/auth/login", headers=headers, data=json.dumps({
            "login": login,
            "password": password
        }))
        if data.status_code == 401:
            raise errors.PostArgumentsError("Код 401. Неверный логин или пароль")
        elif data.status_code == 422:
            raise errors.PostArgumentsError("Код 422. Сервер указал что логин или пароль не указаны")
        elif data.status_code != 200:
            raise errors.UnexpectedBehavior(f"Ожидались коды 200, 401 или 422. Получен: \"{data.status_code}\"")
        data = data.json()
        if 'token' not in data.keys():
            raise errors.UnexpectedBehavior(f"Получен код 200, но токен не найден в ответе сервера. Ответ: \"{data}\"")
        self._auth_token = data['token']
        return True

    def _logout(self) -> bool:
        """
        Выходит из аккаунта. Токен авторизации становится неактуальным.
        Возвращает True если успешно.
        """
        if self._auth_token == None:
            raise ValueError("Нет токена авторизации для выхода")
        
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self._auth_token}',
        }

        data = requests.request("POST", self._api_path+"/accounts/users/auth/logout", headers=headers)

        if data.status_code == 401:
            raise ValueError("Получен код 401. Невозможно выйти, пользователь не авторизован")
        elif data.status_code != 200:
            raise errors.UnexpectedBehavior(f'Ожидались коды 200 или 401. Получены: \"{data.status_code}\"')
        self._auth_token = None
        return True
    
    def set_auth_token(self, token: str):
        self._auth_token = token

    def clear_auth_token(self):
        self._auth_token = None

class AnilibertyAPI(_BaseApi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Инициализация базового апи
        self.Anime = AnilibertyAPI.Anime(*args, **kwargs) # Инициализация всех подклассов (чтобы можно было пользоваться Anime.Catalog.func без инициализации)
        self.Anime.Catalog = self.Anime.Catalog(*args, **kwargs)
        self.Anime.Franchises = self.Anime.Franchises(*args, **kwargs)
        self.Anime.Genres = self.Anime.Genres(*args, **kwargs)
        self.Anime.Releases = self.Anime.Releases(*args, **kwargs)
        self.Anime.Torrents = self.Anime.Torrents(*args, **kwargs)
        self.App = AnilibertyAPI.App(*args, **kwargs)
        self.Media = AnilibertyAPI.Media(*args, **kwargs)
        self.Teams = AnilibertyAPI.Teams(*args, **kwargs)
        self.User = AnilibertyAPI.User(*args, **kwargs)
        self.User.Collections = self.User.Collections(*args, **kwargs)
        self.User.Collections.References = self.User.Collections.References(*args, **kwargs)
        self.User.Favorites = self.User.Favorites(*args, **kwargs)
        self.User.Favorites.References = self.User.Favorites.References(*args, **kwargs)
        self.User.Views = self.User.Views(*args, **kwargs)

    def login(self, login: str, password: str) -> bool:
        """
        Автоматически получает и устанавливает токен авторизации.
        Вернет True если успешно.
        
        :login: Логин (не почта, именно логин, посмотреть можно в настрофках аккаунта на сайте)
        :password: Пароль
        """
        self._login(login, password)
        self.set_auth_token(self._auth_token)
        return True

    def set_auth_token(self, token: str):
        self._auth_token = token
        self.Anime.set_auth_token(self._auth_token)
        self.Anime.Catalog.set_auth_token(self._auth_token)
        self.Anime.Franchises.set_auth_token(self._auth_token)
        self.Anime.Genres.set_auth_token(self._auth_token)
        self.Anime.Releases.set_auth_token(self._auth_token)
        self.Anime.Torrents.set_auth_token(self._auth_token)
        self.User.set_auth_token(self._auth_token)
        self.User.Collections.set_auth_token(self._auth_token)
        self.User.Collections.References.set_auth_token(self._auth_token)
        self.User.Favorites.set_auth_token(self._auth_token)
        self.User.Favorites.References.set_auth_token(self._auth_token)
        self.User.Views.set_auth_token(self._auth_token)

    def logout(self):
        """
        Выходит из аккаунта. Токен авторизации становится неактуальным.
        Возвращает True если успешно.
        """
        self._logout()
        self.clear_auth_token()
        return True

    def clear_auth_token(self):
        self._auth_token = None
        self.Anime.clear_auth_token()
        self.Anime.Catalog.clear_auth_token()
        self.Anime.Franchises.clear_auth_token()
        self.Anime.Genres.clear_auth_token()
        self.Anime.Releases.clear_auth_token()
        self.Anime.Torrents.clear_auth_token()
        self.User.clear_auth_token()
        self.User.Collections.clear_auth_token()
        self.User.Collections.References.clear_auth_token()
        self.User.Favorites.clear_auth_token()
        self.User.Favorites.References.clear_auth_token()
        self.User.Views.clear_auth_token()
        
    class Sorting:
        """
        Типы сортировки. Доступные параметры (и подклассы): FRESH_AT_DESC, FRESH_AT_ASC, RATING_DESC, RATING_ASC, YEAR_DESC, YEAR_ASC
        """
        sorts = ['FRESH_AT_DESC', 'FRESH_AT_ASC', 'RATING_DESC', 'RATING_ASC', 'YEAR_DESC', 'YEAR_ASC']
        class _Sort:
            pass
        class FRESH_AT_DESC(_Sort):
            _r = 'FRESH_AT_DESC'
        class FRESH_AT_ASC(_Sort):
            _r = 'FRESH_AT_ASC'
        class RATING_DESC(_Sort):
            _r = 'RATING_DESC'
        class RATING_ASC(_Sort):
            _r = 'RATING_ASC'
        class YEAR_DESC(_Sort):
            _r = 'YEAR_DESC'
        class YEAR_ASC(_Sort):
            _r = 'YEAR_ASC'

    class AgeRatings:
        """
        Возрастные рейтинги. Доступные параметры (и подклассы): R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS
        """
        ratings = ['R0_PLUS', 'R6_PLUS', 'R12_PLUS', 'R16_PLUS', 'R18_PLUS']
        class _AgeRating:
            pass
        class R0_PLUS(_AgeRating):
            _r = 'R0_PLUS'
        class R6_PLUS(_AgeRating):
            _r = 'R6_PLUS'
        class R12_PLUS(_AgeRating):
            _r = 'R12_PLUS'
        class R16_PLUS(_AgeRating):
            _r = 'R16_PLUS'
        class R18_PLUS(_AgeRating):
            _r = 'R18_PLUS'

    class Types:
        """
        Типы. Доступные типы (и подклассы): TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL
        """
        types = ['TV', 'ONA', 'WEB', 'OVA', 'OAD', 'MOVIE', 'DORAMA', 'SPECIAL']
        class _Type:
            pass
        class TV(_Type):
            _r = 'TV'
        class ONA(_Type):
            _r = 'ONA'
        class WEB(_Type):
            _r = 'WEB'
        class OVA(_Type):
            _r = 'OVA'
        class OAD(_Type):
            _r = 'OAD'
        class MOVIE(_Type):
            _r = 'MOVIE'
        class DORAMA(_Type):
            _r = 'DORAMA'
        class SPECIAL(_Type):
            _r = 'SPECIAL'

    class Genres:
        """
        Жанры.
        Доступные жанры описаны в параметре genres
        Подклассы названы на русском языке потому что так они названы в апи (ну и потому что можно)
        """
        class _Genre:
            pass
        class Боевые_Искусства(_Genre):
            _r = 15
        class Вампиры(_Genre):
            _r = 24
        class Гарем(_Genre):
            _r = 32
        class Демоны(_Genre):
            _r = 16
        class Детектив(_Genre):
            _r = 25
        class Дзёсей(_Genre):
            _r = 33
        class Драма(_Genre):
            _r = 8
        class Игры(_Genre):
            _r = 17
        class Исекай(_Genre):
            _r = 34
        class Исторический(_Genre):
            _r = 26
        class Киберпанк(_Genre):
            _r = 30
        class Комедия(_Genre):
            _r = 1
        class Магия(_Genre):
            _r = 18
        class Меха(_Genre):
            _r = 2
        class Мистика(_Genre):
            _r = 9
        class Музыка(_Genre):
            _r = 19
        class Пародия(_Genre):
            _r = 36
        class Повседневность(_Genre):
            _r = 10
        class Приключения(_Genre):
            _r = 27
        class Психологическое(_Genre):
            _r = 3
        class Романтика(_Genre):
            _r = 11
        class Сверхъестественное(_Genre):
            _r = 28
        class Сёдзе(_Genre):
            _r = 20
        class Сёдзе_ай(_Genre):
            _r = 31
        class Сейнен(_Genre):
            _r = 5
        class Сёнен(_Genre):
            _r = 4
        class Спорт(_Genre):
            _r = 12
        class Супер_сила(_Genre):
            _r = 21
        class Триллер(_Genre):
            _r = 6
        class Ужасы(_Genre):
            _r = 13
        class Фантастика(_Genre):
            _r = 22
        class Фэнтези(_Genre):
            _r = 29
        class Школа(_Genre):
            _r = 7
        class Экшен(_Genre):
            _r = 14
        class Этти(_Genre):
            _r = 23

        genres = {
            'Боевые искусства': Боевые_Искусства._r,
            'Вампиры': Вампиры._r,
            'Гарем': Гарем._r,
            'Демоны': Демоны._r,
            'Детектив': Детектив._r,
            'Дзёсей': Дзёсей._r,
            'Драма': Драма._r,
            'Игры': Игры._r,
            'Исекай': Исекай._r,
            'Исторический': Исторический._r,
            'Киберпанк': Киберпанк._r,
            'Комедия': Комедия._r,
            'Магия': Магия._r,
            'Меха': Меха._r,
            'Мистика': Мистика._r,
            'Музыка': Музыка._r,
            'Пародия': Пародия._r,
            'Повседневность': Повседневность._r,
            'Приключения': Приключения._r,
            'Психологическое': Психологическое._r,
            'Романтика': Романтика._r,
            'Сверхъестественное': Сверхъестественное._r,
            'Сёдзе': Сёдзе._r,
            'Сёдзе-ай': Сёдзе_ай._r,
            'Сейнен': Сейнен._r,
            'Сёнен': Сёнен._r,
            'Спорт': Спорт._r,
            'Супер сила': Супер_сила._r,
            'Триллер': Триллер._r,
            'Ужасы': Ужасы._r,
            'Фантастика': Фантастика._r,
            'Фэнтези': Фэнтези._r,
            'Школа': Школа._r,
            'Экшен': Экшен._r,
            'Этти': Этти._r,
        }

    class CollectionTypes:
        """
        Типы коллекций. Доступные типы (и подклассы): PLANNED, WATCHED, WATCHING, POSTPONED, ABANDONED
        """
        class _ColType:
            pass
        class PLANNED(_ColType):
            _r = 'PLANNED'
        class WATCHED(_ColType):
            _r = 'WATCHED'
        class WATCHING(_ColType):
            _r = 'WATCHING'
        class POSTPONED(_ColType):
            _r = 'POSTPONED'
        class ABANDONED(_ColType):
            _r = 'ABANDONED'

        types = ['PLANNED', 'WATCHED', 'WATCHING', 'POSTPONED', 'ABANDONED']

    class Anime(_BaseApi):
        class Catalog(_BaseApi):
            """
            Аниме.Каталог
            """
            def catalog_releases(self, page: int = 1, limit: int = 10, 
                                genres: list[int | str | type['AnilibertyAPI.Genres']] = [],
                                types: list[str | type['AnilibertyAPI.Types.TV'] | type['AnilibertyAPI.Types.ONA']
                                            | type['AnilibertyAPI.Types.WEB'] | type['AnilibertyAPI.Types.OVA']
                                            | type['AnilibertyAPI.Types.OAD'] | type['AnilibertyAPI.Types.MOVIE']
                                            | type['AnilibertyAPI.Types.DORAMA'] | type['AnilibertyAPI.Types.SPECIAL']] = [], 
                                seasons: list[str] = [], from_year: int | None = None,
                                to_year: int | None = None, search: str | None = None, 
                                sorting: str | type['AnilibertyAPI.Sorting.FRESH_AT_DESC'] | type['AnilibertyAPI.Sorting.FRESH_AT_ASC']
                                    | type['AnilibertyAPI.Sorting.RATING_DESC'] | type['AnilibertyAPI.Sorting.RATING_ASC']
                                    | type['AnilibertyAPI.Sorting.YEAR_DESC'] | type['AnilibertyAPI.Sorting.YEAR_ASC'] | None = None,
                                age_ratings: list[str | type['AnilibertyAPI.AgeRatings.R0_PLUS'] | type['AnilibertyAPI.AgeRatings.R6_PLUS']
                                                | type['AnilibertyAPI.AgeRatings.R12_PLUS'] | type['AnilibertyAPI.AgeRatings.R16_PLUS'] | type['AnilibertyAPI.AgeRatings.R18_PLUS']] = [],
                                publish_statuses: list[str] = [], production_statuses: list[str] = [],
                                include: list[str] = [], exclude: list[str] = [], bypass_validation: bool = False) -> dict:
                """
                Возвращает список релизов по заданными параметрам

                :page: Номер страницы. (По умолчанию 1)
                :limit: Ограничение на количество элементов. (По умолчанию 10)
                :genres: Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
                :types: Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
                :seasons: Список сезонов релизов (Список строк). Доступные значения: winter, spring, summer, autumn. (По умолчанию пусто)
                :from_year: Минимальный год выхода релиза (Целое число). (По умолчанию отсутствует)
                :to_year: Максимальный год выхода релиза (Целое число). (По умолчанию отсутствует)
                :search: Поисковой запрос / Название (Строка). (По умолчанию отсутствует)
                :sorting: Тип сортировки (строка). Доступные значения: FRESH_AT_DESC, FRESH_AT_ASC, RATING_DESC, RATING_ASC, YEAR_DESC, YEAR_ASC. Также они описаны в AnilibertyAPI.Sorting.sorts и можно указывать подклассы (AnilibertyAPI.Sorting.FRESH_AT_DESC, ...). (По умолчанию отсутствует)
                :age_ratings: Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
                :publish_statuses: Список статусов релизов (список строк). Доступные значения: IS_ONGOING, IS_NOT_ONGOING
                :production_statuses: Список статусов релизов (список строк). Доступные значения: IS_IN_PRODUCTION, IS_NOT_IN_PRODUCTION
                :include: Список включаемых полей (Список строк). Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей (Список строк). Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :bypass_validation: Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)

                Возвращает словарь: {'data': list, 'meta: dict}
                """
                params = {
                    'page': page,
                    'limit': limit
                }
                if len(genres) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['genres'] = []
                    for g in genres:
                        if type(g) == type and issubclass(g, AnilibertyAPI.Genres._Genre):
                            params['f']['genres'].append(g._r)
                        elif type(g) == str and (g in AnilibertyAPI.Genres.genres.keys() or bypass_validation):
                            params['f']['genres'].append(AnilibertyAPI.Genres.genres[g])
                        else:
                            raise KeyError(f'Неизвестный жанр \"{g}\"! Вы можете посмотреть доступные жанры в AnilibertyAPI.Genres.genres')
                if len(types) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['types'] = []
                    for t in types:
                        if type(t) == type and issubclass(t, AnilibertyAPI.Types._Type):
                            params['f']['types'].append(t._r)
                        elif type(t) == str and (t in AnilibertyAPI.Types.types or bypass_validation):
                            params['f']['types'].append(t)
                        else:
                            raise KeyError(f'Неизвестный тип \"{t}\"! Вы можете посмотреть доступные типы в AnilibertyAPI.Types.types')
                if len(seasons) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    if not bypass_validation and not all([(s in ['winter', 'spring', 'summer', 'autumn']) for s in seasons]):
                        raise KeyError(f"Указан неизвестный сезон в 'seasons'. Доступные значения: 'winter', 'spring', 'summer', 'autumn'. Указанный список: {seasons}")
                    params['f']['seasons'] = list(set(seasons))
                if from_year is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    if 'years' not in params['f'].keys(): params['f']['years'] = {}
                    params['f']['years']['from_year'] = from_year
                if to_year is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    if 'years' not in params['f'].keys(): params['f']['years'] = {}
                    params['f']['years']['to_year'] = to_year
                if search is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['search'] = search
                if sorting is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    if type(sorting) == str and (sorting in AnilibertyAPI.Sorting.sorts or bypass_validation):
                        params['f']['sorting'] = sorting
                    elif type(t) == type and issubclass(t, AnilibertyAPI.Sorting._Sort):
                        params['f']['sorting'] = sorting._t
                    else:
                        raise KeyError(f'Неизвестный параметр сортировки \'{sorting}\'. Вы можете посмотреть доступные параметры в AnilibertyAPI.Sorting.sorts')
                if len(age_ratings) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['age_ratings'] = []
                    for r in age_ratings:
                        if type(r) == str and (r in AnilibertyAPI.AgeRatings.ratings or bypass_validation):
                            params['f']['age_ratings'].append(r)
                        elif type(r) == type and issubclass(r, AnilibertyAPI.AgeRatings._AgeRating):
                            params['f']['age_ratings'].append(r._r)
                        else:
                            raise KeyError(f'Неизвестный возрастной рейтинг \"{t}\". Вы можете посмотреть доступные параметры в AnilibertyAPI.AgeRatings.ratings')
                if len(publish_statuses) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    if not bypass_validation and not all([(st in ['IS_ONGOING', 'IS_NOT_ONGOING']) for st in publish_statuses]):
                        raise KeyError(f'Неизвестный параметр публикации в указанных параметрах: "{publish_statuses}". Доступные параметры: \'IS_ONGOING\', \'IS_NOT_ONGOING\'')
                    params['f']['publish_statuses'] = publish_statuses
                if len(production_statuses) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    if not bypass_validation and not all([(st in ['IS_IN_PRODUCTION', 'IS_NOT_IN_PRODUCTION']) for st in production_statuses]):
                        raise KeyError(f'Неизвестный статус продакшена в указанных параметрах: "{production_statuses}". Доступные параметры: \'IS_IN_PRODUCTION\', \'IS_NOT_IN_PRODUCTION\'')
                    params['f']['production_statuses'] = production_statuses
                if len(include) > 0:
                    params['include'] = ",".join(include)
                if len(exclude) > 0:
                    params['exclude'] = ",".join(exclude)

                return self.catalog_releases_raw(params)
                

            def catalog_releases_raw(self, params: dict) -> dict:
                """
                Возвращает список релизов по заданными параметрам.
                В данную функцию параметры передаются в виде словаря.
                Рекомендуется ознакомиться с официальной документацией к апи aniliberty и в каком виде нужно передавать словарь.
                
                Возвращает словарь: {'data': list, 'meta: dict}
                """
                
                data = self._request("POST", self._api_path+'/anime/catalog/releases/', data=json.dumps(params), headers=self._headers)
                if data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 422. Получен: {data.status_code}")
                return data.json()

            class References(_BaseApi):
                """
                Аниме.Каталог.Справочники
                """
                def age_ratings(self) -> list[dict]:
                    """
                    Возвращает список возможных возрастных рейтингов в каталоге
                    """
                    return self._req('/anime/catalog/references/age-ratings')

                def genres(self) -> list[dict]:
                    """
                    Возвращает список всех жанров в каталоге
                    """
                    return self._req('/anime/catalog/references/genres')

                def production_statuses(self) -> list[dict]:
                    """
                    Возвращает список возможных статусов озвучки релиза в каталоге
                    """
                    return self._req('/anime/catalog/references/production-statuses')

                def publish_statuses(self) -> list[dict]:
                    """
                    Возвращает список возможных статусов выхода релиза в каталоге
                    """
                    return self._req('/anime/catalog/references/publish-statuses')

                def seasons(self) -> list[dict]:
                    """
                    Возвращает список возможных сезонов релизов в каталоге
                    """
                    return self._req('/anime/catalog/references/season')

                def sorting(self) -> list[dict]:
                    """
                    Возвращает список возможных типов сортировок в каталоге
                    """
                    return self._req('/anime/catalog/references/sorting')

                def types(self) -> list[dict]:
                    """
                    Возвращает список возможных типов релизов в каталоге
                    """
                    return self._req('/anime/catalog/references/types')

                def years(self) -> list[int]:
                    """
                    Возвращает список годов в каталоге
                    """
                    return self._req('/anime/catalog/references/years')

                def _req(self, path: str) -> list:
                    data = self._request("GET", self._api_path+path, headers=self._headers)
                    if data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 422. Получен: {data.status_code}")
                    return data.json()
        
        class Franchises(_BaseApi):
            """
            Аниме.Франшизы
            """
            def franchises(self, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает список франшиз.

                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/franchises/', headers=self._headers, data=json.dumps(params))
                if data.status_code == 404:
                    raise errors.NoResults("Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def franchise_by_id(self, franchise_id: str, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные франшизы.

                :franchise_id: ID франшизы
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/franchises/'+franchise_id, headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для id франшизы \"{franchise_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def random(self, limit: int = 5, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает список случайных франшиз.
                
                :limit: Количество случайных франшиз в выдаче. По умолчанию 5
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/franchises/random', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults("Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def franchises_by_release_id(self, release_id: str, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает список франшиз, в которых участвует релиз

                :release_id: ID релиза
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/franchises/release/'+release_id, headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для id релиза \"{release_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

        class Genres(_BaseApi):
            """
            Аниме.Жанры
            """
            def genres(self, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает список всех жанров
                
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/genres/', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def genre_by_id(self, genre_id: int, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по жанру

                :genre_id: ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/genres/'+genre_id, headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для id жанра \"{genre_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def random_genres(self, limit: int = 5, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает список случайных жанров

                :limit: Количество жанров в выдаче (целое число). По умолчанию 5
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/genres/random/', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def releases_by_genre_id(self, genre_id: int, page: int = 1, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает список всех релизов жанра

                :genre_id: ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'genreId': genre_id, 'page': page, 'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/genres/random/', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для id жанра \"{genre_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

        class Releases(_BaseApi):
            """
            Аниме.Релизы
            """
            def latest(self, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает данные по последним релизам

                :limit: Количество последних релизов в выдаче (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/latest', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def random(self, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает данные по случайным релизам
            
                :limit: Количество последних релизов в выдаче (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/random', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def recommended(self, release_id: int, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает данные по рекомендованным релизам

                :release_id: Идентификатор релиза, для которого рекомендуем
                :limit: Количество последних релизов в выдаче (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'limit': limit, 'release_id': release_id}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/recommended', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def releases_list(self, ids: list[int] | None = None, aliases: list[str] | None = None, page: int = 1, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по списку релизов
        
                :ids: Список ID релизов (Список целых чисел). По умолчангию отсутствует
                :aliases: Список alias релизов (Список строк, пример: ['darling-in-the-franxx']). По умолчанию отсутствует
                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                if ids == None and aliases == None:
                    raise errors.PostArgumentsError("Требуется указать как минимум один id либо alias")
                params = {'page': page, 'limit': limit}
                if len(ids) > 0:
                    params['ids'] = ','.join(map(str, ids))
                if len(aliases) > 0:
                    params['aliases'] = ','.join(aliases)
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/list', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 422 или 404. Получен: {data.status_code}")
                return data.json()

            def by_id(self, release_id: int, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по релизу по id
                
                :release_id: id релиза
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                
                Возвращает словарь.
                """
                return self.release_by_id_or_alias(release_id, include, exclude)

            def by_alias(self, alias: str, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по релизу по alias
                
                :alias: alias релиза (Пример: darling-in-the-franxx)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                
                Возвращает словарь.
                """
                return self.by_id_or_alias(alias, include, exclude)

            def by_id_or_alias(self, id_or_alias: str | int, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по релизу

                :id_or_alias: id или alias релиза
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                
                Возвращает словарь.
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/'+id_or_alias, headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для id или alias \"{id_or_alias}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def members_by_id_or_alias(self, id_or_alias: str | int, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает данные по участникам релиза

                :id_or_alias: id или alias релиза (Пример alias: darling-in-the-franxx)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/'+id_or_alias+'/members', headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует on members for release with id or alias \"{id_or_alias}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def episodes_timecodes_by_id_or_alias(self, id_or_alias: str | int, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
                """
                Возвращает данные по всем существующим таймкодам просмотра эпизодов релиза. Имеет 1-2-x минутный кэш.

                :id_or_alias: id или alias релиза (Пример alias: darling-in-the-franxx)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/releases/'+id_or_alias+'/members', headers=self._headers, params=params, auth_required=True)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует on episodes timecodes for release with id or alias \"{id_or_alias}\"")
                elif data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 404 или 403. Получен: {data.status_code}")
                return data.json()

            class Episodes(_BaseApi):
                """
                Аниме.Релизы.Эпизоды
                """
                def episode_by_id(self, release_episode_id: str, include: list[str] = [], exclude: list[str] = []) -> dict:
                    """
                    Возвращает данные по эпизоду.

                    :release_episode_id: Идентификатор эпизода (Строка). (Пример: cf31fe87-fad8-11eb-b2fa-0242ac120004)
                    :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    """
                    params = {}
                    if len(include) > 0:
                        params['include'] = ','.join(include)
                    if len(exclude) > 0:
                        params['exclude'] = ','.join(exclude)
                    data = self._request("GET", self._api_path+'/anime/releases/episodes/'+release_episode_id, headers=self._headers, params=params)
                    if data.status_code == 404:
                        raise errors.NoResults(f"Результат отсутствует для эпизода с id \"{release_episode_id}\"")
                    elif data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                    return data.json()

                def episode_timecodes(self, release_episode_id: str, include: list[str] = [], exclude: list[str] = []) -> dict:
                    """
                    Возвращает данные по просмотру указанного эпизода авторизованным пользователем. Имеет 1-2-x минутный кэш.

                    :release_episode_id: Идентификатор эпизода (Строка). (Пример: cf31fe87-fad8-11eb-b2fa-0242ac120004)
                    :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    """
                    params = {}
                    if len(include) > 0:
                        params['include'] = ','.join(include)
                    if len(exclude) > 0:
                        params['exclude'] = ','.join(exclude)
                    data = self._request("GET", self._api_path+'/anime/releases/episodes/'+release_episode_id+'/timecode', headers=self._headers, params=params, auth_required=True)
                    if data.status_code == 404:
                        raise errors.NoResults(f"Результат отсутствует для таймкодов эпизода с id \"{release_episode_id}\"")
                    elif data.status_code == 403:
                        raise errors.ContentBlocked("Получен код 403. Требуется авторизация")
                    elif data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидались коды 200, 404 или 403. Получен: {data.status_code}")
                    return data.json()

            class ReleasesSchedule(_BaseApi):
                """
                Аниме.Релизы.РасписаниеРелизов
                """
                def now(self, include: list[str] = [], exclude: list[str] = []) -> dict:
                    """
                    Возвращает список релизов в расписании на текущую дату

                    :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    """
                    params = {}
                    if len(include) > 0:
                        params['include'] = ','.join(include)
                    if len(exclude) > 0:
                        params['exclude'] = ','.join(exclude)
                    data = self._request("GET", self._api_path+'/anime/schedule/now', headers=self._headers, params=params)
                    if data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                    return data.json()

                def week(self, include: list[str] = [], exclude: list[str] = []) -> dict:
                    """
                    Возвращает список релизов в расписании на текущую неделю
                
                    :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                    """
                    params = {}
                    if len(include) > 0:
                        params['include'] = ','.join(include)
                    if len(exclude) > 0:
                        params['exclude'] = ','.join(exclude)
                    data = self._request("GET", self._api_path+'/anime/schedule/week', headers=self._headers, params=params)
                    if data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                    return data.json()

        class Torrents(_BaseApi):
            """
            Аниме.Торренты
            """
            def torrents(self, page: int = 1, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по последним торрентам

                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {'page': page, 'limit': limit}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/torrents', headers=self._headers, params=params)
                if data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                return data.json()

            def by_hash_or_id(self, hash_or_id: str | int, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает данные по торренту по hash или id
                
                :hash_or_id: ID или Hash торрента (Целое число или строка)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/torrents/'+str(hash_or_id), headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует для торрента с id или hash \"{hash_or_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def file(self, hash_or_id: str | int, pk: str | None = None) -> str:
                """
                Возвращает торрент-файл
                
                :hash_or_id: ID или Hash торрента (Целое число или строка)
                :pk: passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован). (Пока работает и пустой)

                Возвращает контент файла торрента
                """
                params = {}
                if pk: params['pk'] = pk
                data = self._request("GET", self._api_path+'/anime/torrents/'+str(hash_or_id)+'/file', headers=self._torrent_headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует for torrent with id or hash \"{hash_or_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.text

            def by_release_id(self, release_id: int, include: list[str] = [], exclude: list[str] = []):
                """
                Возвращает данные по торрентам релиза

                :release_id: ID релиза (Целое число)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                """
                params = {}
                if len(include) > 0:
                    params['include'] = ','.join(include)
                if len(exclude) > 0:
                    params['exclude'] = ','.join(exclude)
                data = self._request("GET", self._api_path+'/anime/torrents/release/'+str(release_id), headers=self._headers, params=params)
                if data.status_code == 404:
                    raise errors.NoResults(f"Результат отсутствует for torrents by release id \"{release_id}\"")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 404. Получен: {data.status_code}")
                return data.json()

            def rss(self, limit: int = 10, pk: str | None = None) -> str:
                """
                Возвращает данные по последним торрентам в виде XML документа

                :limit: Количество торрентов в выдаче. По умолчанию 10
                :pk: Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики. (По умолчанию пустой)

                Возвращает xml документ
                """ 
                params = {'limit': limit}
                if pk: params['pk'] = pk
                data = self._request("GET", self._api_path+'/anime/torrents/rss', headers=self._xml_headers, params=params)
                if data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                return data.text

            def rss_by_release_id(self, release_id: int, pk: str | None = None) -> str:
                """
                Возвращает данные по торрентам релиза в виде RSS ленты
        
                :release_id: ID релиза (Целое число)
                :pk: Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики. (По умолчанию пустой)
        
                Возвращает xml документ
                """ 
                params = {}
                if pk: params['pk'] = pk
                data = self._request("GET", self._api_path+'/anime/torrents/rss/release/'+str(release_id), headers=self._xml_headers, params=params)
                if data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                return data.text

    class App(_BaseApi):
        def search(self, query: str, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
            """
            Возвращает данные по релизам, которые удовлетворяют поисковому запросу.

            :query: Поисковая строка
            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {'query': query}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/app/search/releases', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

        def status(self) -> dict:
            """
            Возвращает информацию о статусе API

            Возвращает:
            {
            "request": {
                "ip": "192.168.1.1",
                "country": "Russia",
                "iso_code": "RU",
                "timezone": "Europe/Moscow"
            },
            "is_alive": true,
            "available_api_endpoints": [
                "https://aniliberty.top"
            ]
            }
            """
            data = self._request("GET", self._api_path+'/app/status', headers=self._headers)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

    class Media(_BaseApi):
        def promotions(self, include: list[str] = [], exclude: list[str] = []) -> dict:
            """
            Возвращает список промо-материалов или рекламные кампании в случайном порядке

            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/media/promotions', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

        def videos(self, limit: int = 5, include: list[str] = [], exclude: list[str] = []) -> dict:
            """
            Возвращает список последних видео-роликов

            :limit: Количество роликов в выдаче (Целое число). По умолчанию 5
            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {'limit': limit}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/media/videos', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

    class Teams(_BaseApi):
        """
        Команды
        """
        def teams(self, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
            """
            Возвращает список всех команд

            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/teams/', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

        def roles(self, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
            """
            Возвращает список всех ролей в командах
    
            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/teams/roles', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

        def users(self, include: list[str] = [], exclude: list[str] = []) -> list[dict]:
            """
            Возвращает список всех анилибрийцов с указанием команды и своих ролей
    
            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            """
            params = {}
            if len(include) > 0:
                params['include'] = ','.join(include)
            if len(exclude) > 0:
                params['exclude'] = ','.join(exclude)
            data = self._request("GET", self._api_path+'/teams/roles', headers=self._headers, params=params)
            if data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
            return data.json()

    class User(_BaseApi):
        class Collections(_BaseApi):
            """
            Аккаунты.Пользователи.Мое.Коллекции
            """
            def ids(self) -> list[list]:
                """
                Возвращает данные по идентификаторам релизов и типов коллекций авторизованного пользователя

                Пример:
                [
                    [
                        8345,
                        "PLANNED"
                    ],
                    ...
                ]
                """
                data = self._request("GET", self._api_path+'/accounts/users/me/collections/ids', headers=self._headers, auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                return data.json()

            def releases(self, type_of_collection: str | type['AnilibertyAPI.CollectionTypes.PLANNED'] | type['AnilibertyAPI.CollectionTypes.WATCHED']
                                    | type['AnilibertyAPI.CollectionTypes.WATCHING'] | type['AnilibertyAPI.CollectionTypes.POSTPONED'] | type['AnilibertyAPI.CollectionTypes.ABANDONED'], 
                         page: int = 1, limit: int = 10,  
                         genres: list[int | str | type['AnilibertyAPI.Genres']] = [],
                         types: list[str | type['AnilibertyAPI.Types.TV'] | type['AnilibertyAPI.Types.ONA']
                                     | type['AnilibertyAPI.Types.WEB'] | type['AnilibertyAPI.Types.OVA']
                                     | type['AnilibertyAPI.Types.OAD'] | type['AnilibertyAPI.Types.MOVIE']
                                     | type['AnilibertyAPI.Types.DORAMA'] | type['AnilibertyAPI.Types.SPECIAL']] = [], 
                         years: list[int] = [], search: str | None = None,
                         age_ratings: list[str | type['AnilibertyAPI.AgeRatings.R0_PLUS'] | type['AnilibertyAPI.AgeRatings.R6_PLUS']
                                         | type['AnilibertyAPI.AgeRatings.R12_PLUS'] | type['AnilibertyAPI.AgeRatings.R16_PLUS'] | type['AnilibertyAPI.AgeRatings.R18_PLUS']] = [],
                         include: list[str] = [], exclude: list[str] = [], bypass_validation: bool = False) -> dict:
                """
                Возвращает данные по релизам из определенной коллекции авторизованного пользователя

                :type_of_collection: Тип коллекции (Строка). Доступные значения описаны в AnilibertyAPI.CollectionTypes.types. Также можно указывать подклассы (AnilibertyAPI.CollectionTypes.PLANNED, ...) они автоматически будут переведены в соответствующие значения
                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :genres: Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
                :types: Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
                :years: Минимальный год выхода релиза (Список целых чисел). По умолчанию отсутствует
                :search: Поисковый запрос (Строка). По умолчанию отсутствует
                :age_ratings: Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :bypass_validation: Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)
                
                """
                params = {
                    'page': page,
                    'limit': limit,
                }
                if type(type_of_collection) == type and issubclass(type_of_collection, AnilibertyAPI.CollectionTypes._ColType):
                    params['type_of_collection'] = type_of_collection._r
                elif type(type_of_collection) == str and (type_of_collection in AnilibertyAPI.CollectionTypes.types or bypass_validation):
                    params['type_of_collection'] = type_of_collection
                else:
                    raise KeyError(f'Неизвестный тип коллекции "{type_of_collection}"! Вы можете посмотреть доступные параметры в AnilibertyAPI.CollectionTypes.types')
                if len(genres) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['genres'] = []
                    for g in genres:
                        if type(g) == type and issubclass(g, AnilibertyAPI.Genres._Genre):
                            params['f']['genres'].append(g._r)
                        elif type(g) == str and (g in AnilibertyAPI.Genres.genres.keys() or bypass_validation):
                            params['f']['genres'].append(AnilibertyAPI.Genres.genres[g])
                        else:
                            raise KeyError(f'Неизвестный жанр \"{g}\"! Вы можете посмотреть доступные жанры в AnilibertyAPI.Genres.genres')
                if len(types) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['types'] = []
                    for t in types:
                        if type(t) == type and issubclass(t, AnilibertyAPI.Types._Type):
                            params['f']['types'].append(t._r)
                        elif type(t) == str and (t in AnilibertyAPI.Types.types or bypass_validation):
                            params['f']['types'].append(t)
                        else:
                            raise KeyError(f'Неизвестный тип \"{t}\"! Вы можете посмотреть доступные типы в AnilibertyAPI.Types.types')
                if len(years) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['years'] = ','.join(map(str, years))
                if search is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['search'] = search
                if len(age_ratings) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['age_ratings'] = []
                    for r in age_ratings:
                        if type(r) == str and (r in AnilibertyAPI.AgeRatings.ratings or bypass_validation):
                            params['f']['age_ratings'].append(r)
                        elif type(r) == type and issubclass(r, AnilibertyAPI.AgeRatings._AgeRating):
                            params['f']['age_ratings'].append(r._r)
                        else:
                            raise KeyError(f'Неизвестный возрастной рейтинг \"{t}\". Вы можете посмотреть доступные параметры в AnilibertyAPI.AgeRatings.ratings')
                if len(include) > 0:
                    params['include'] = ",".join(include)
                if len(exclude) > 0:
                    params['exclude'] = ",".join(exclude)
                return self.releases_raw(params)

            def releases_raw(self, params: dict) -> dict:
                """
                Возвращает данные по релизам из определенной коллекции авторизованного пользователя

                :params: Словарь с данными запроса

                Рекомендуется обратиться к официальной документации апи aniliberty
                """
                
                data = self._request("POST", self._api_path+"/accounts/users/me/collections/releases", headers=self._headers, data=json.dumps(params), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 422. Получен: {data.status_code}")
                return data.json()

            def add_release(self, release_id: int, type_of_collection: str | type['AnilibertyAPI.CollectionTypes.PLANNED'] | type['AnilibertyAPI.CollectionTypes.WATCHED']
                            | type['AnilibertyAPI.CollectionTypes.WATCHING'] | type['AnilibertyAPI.CollectionTypes.POSTPONED'] | type['AnilibertyAPI.CollectionTypes.ABANDONED']):
                """
                Добавляет релиз в соответствующую коллекцию авторизованного пользователя

                :release_id: ID Релиза (Целое число)
                :type_of_collection: Тип коллекции (Строка). Доступные значения описаны в AnilibertyAPI.CollectionTypes.types. Также можно указывать подклассы (AnilibertyAPI.CollectionTypes.PLANNED, ...) они автоматически будут переведены в соответствующие значения
                
                Ничего не возвращает
                """
                params = {
                    'release_id': release_id,
                    'type_of_collection': type_of_collection
                }
                return self.add_multiple_releases([params, ])
                

            def add_multiple_releases(self, data: list[dict]):
                """
                Добавляет несколько релизов в соответствующие коллекции авторизованного пользователя
                
                :data: Данные в виде:
                    [
                        {
                            "release_id": ID релиза (Целое число),
                            "type_of_collection": Тип коллекции. Доступные значения описаны в AnilibertyAPI.CollectionTypes.types
                        },
                        ...
                    ]

                Ничего не возвращает
                """
                data = self._request("POST", self._api_path+"/accounts/users/me/collections", headers=self._headers, data=json.dumps(data), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 422. Получен: {data.status_code}")

            def remove_release(self, release_id: int):
                """
                Удаляет релиз из соответствующей коллекции авторизованного пользователя

                :release_id: ID Релиза (Целое число)

                Ничего не возвращает
                """
                return self.remove_multiple_releases([release_id, ])

            def remove_multiple_releases(self, ids: list[int]):
                """
                Удаляет несколько релизов из соответствующих коллекций авторизованного пользователя

                :ids: Список ID Релизов (Список целых чисесл)

                Ничего не возвращает
                """
                data = self._request("DELETE", self._api_path+"/accounts/users/me/collections", headers=self._headers, data=json.dumps([{'release_id': x} for x in ids]), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 422. Получен: {data.status_code}")

            class References(_BaseApi):
                """
                Аккаунты.Пользователи.Мое.Коллекции.Справочники
                """
                def age_ratings(self) -> list[dict]:
                    """
                    Возвращает список возрастных рейтингов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/collections/references/age-ratings')

                def genres(self) -> list[dict]:
                    """
                    Возвращает список жанров в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/collections/references/genres')

                def types(self) -> list[dict]:
                    """
                    Возвращает список типов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/collections/references/types')

                def years(self) -> list[int]:
                    """
                    Возвращает список годов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/collections/references/years')

                def _req(self, path):
                    data = self._request("GET", self._api_path+path, headers=self._headers, auth_required=True)
                    if data.status_code == 403:
                        raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                    elif data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 40{data.status_code}")
                    return data.json()

        class Favorites(_BaseApi):
            """
            Аккаунты.Пользователи.Мое.Избранное
            """
            def ids(self) -> list:
                """
                Возвращает данные по идентификаторам релизов из избранного авторизованного пользователя
            
                Пример:
                [
                9023,
                9024,
                9025
                ]
                """
                data = self._request("GET", self._api_path+'/accounts/users/me/favorites/ids', headers=self._headers, auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидася код 200. Получен: {data.status_code}")
                return data.json()
            
            def releases(self, page: int = 1, limit: int = 10,  
                         genres: list[int | str | type['AnilibertyAPI.Genres']] = [],
                         types: list[str | type['AnilibertyAPI.Types.TV'] | type['AnilibertyAPI.Types.ONA']
                                     | type['AnilibertyAPI.Types.WEB'] | type['AnilibertyAPI.Types.OVA']
                                     | type['AnilibertyAPI.Types.OAD'] | type['AnilibertyAPI.Types.MOVIE']
                                     | type['AnilibertyAPI.Types.DORAMA'] | type['AnilibertyAPI.Types.SPECIAL']] = [], 
                         years: list[int] = [], search: str | None = None,
                         age_ratings: list[str | type['AnilibertyAPI.AgeRatings.R0_PLUS'] | type['AnilibertyAPI.AgeRatings.R6_PLUS']
                                         | type['AnilibertyAPI.AgeRatings.R12_PLUS'] | type['AnilibertyAPI.AgeRatings.R16_PLUS'] | type['AnilibertyAPI.AgeRatings.R18_PLUS']] = [],
                         include: list[str] = [], exclude: list[str] = [], bypass_validation: bool = False) -> dict:
                """
                Возвращает данные по релизам из избранного текущего пользователя
            
                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :genres: Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
                :types: Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
                :years: Минимальный год выхода релиза (Список целых чисел). По умолчанию отсутствует
                :search: Поисковый запрос (Строка). По умолчанию отсутствует
                :age_ratings: Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :bypass_validation: Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)
            
                """
                params = {
                    'page': page,
                    'limit': limit,
                }
                if len(genres) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['genres'] = []
                    for g in genres:
                        if type(g) == type and issubclass(g, AnilibertyAPI.Genres._Genre):
                            params['f']['genres'].append(g._r)
                        elif type(g) == str and (g in AnilibertyAPI.Genres.genres.keys() or bypass_validation):
                            params['f']['genres'].append(AnilibertyAPI.Genres.genres[g])
                        else:
                            raise KeyError(f'Неизвестный жанр \"{g}\"! Вы можете посмотреть доступные жанры в AnilibertyAPI.Genres.genres')
                if len(types) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['types'] = []
                    for t in types:
                        if type(t) == type and issubclass(t, AnilibertyAPI.Types._Type):
                            params['f']['types'].append(t._r)
                        elif type(t) == str and (t in AnilibertyAPI.Types.types or bypass_validation):
                            params['f']['types'].append(t)
                        else:
                            raise KeyError(f'Неизвестный тип \"{t}\"! Вы можете посмотреть доступные типы в AnilibertyAPI.Types.types')
                if len(years) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['years'] = ','.join(map(str, years))
                if search is not None:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['search'] = search
                if len(age_ratings) > 0:
                    if 'f' not in params.keys(): params['f'] = {}
                    params['f']['age_ratings'] = []
                    for r in age_ratings:
                        if type(r) == str and (r in AnilibertyAPI.AgeRatings.ratings or bypass_validation):
                            params['f']['age_ratings'].append(r)
                        elif type(r) == type and issubclass(r, AnilibertyAPI.AgeRatings._AgeRating):
                            params['f']['age_ratings'].append(r._r)
                        else:
                            raise KeyError(f'Неизвестный возрастной рейтинг \"{t}\". Вы можете посмотреть доступные параметры в AnilibertyAPI.AgeRatings.ratings')
                if len(include) > 0:
                    params['include'] = ",".join(include)
                if len(exclude) > 0:
                    params['exclude'] = ",".join(exclude)
                return self.releases_raw(params)
            
            def releases_raw(self, params: dict) -> dict:
                """
                Возвращает данные по релизам из избранного текущего пользователя
            
                :params: Словарь с данными запроса
            
                Рекомендуется обратиться к официальной документации апи aniliberty
                """
            
                data = self._request("POST", self._api_path+"/accounts/users/me/favorites/releases", headers=self._headers, data=json.dumps(params), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 422. Получен: {data.status_code}")
                return data.json()
            
            def add_release(self, release_id: int):
                """
                Добавляет релиз в избранное авторизованного пользователя
            
                :release_id: ID Релиза (Целое число)
                
                Ничего не возвращает
                """
                return self.add_multiple_releases([{'release_id': release_id}, ])
            
            
            def add_multiple_releases(self, ids: list[int]):
                """
                Добавляет несколько релизов в избранное авторизованного пользователя
            
                :ids: Список ID Релизов (Список целых чисесл)
            
                Ничего не возвращает
                """
                data = self._request("POST", self._api_path+"/accounts/users/me/favorites", headers=self._headers, data=json.dumps([{'release_id': x} for x in ids]), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")
            
            def remove_release(self, release_id: int):
                """
                Удаляет релиз из избранного авторизованного пользователя
            
                :release_id: ID Релиза (Целое число)
            
                Ничего не возвращает
                """
                return self.remove_multiple_releases([release_id, ])
            
            def remove_multiple_releases(self, ids: list[int]):
                """
                Удаляет несколько релизов из избранного авторизованного пользователя
            
                :ids: Список ID Релизов (Список целых чисесл)
            
                Ничего не возвращает
                """
                data = self._request("DELETE", self._api_path+"/accounts/users/me/favorites", headers=self._headers, data=json.dumps([{'release_id': x} for x in ids]), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")

            class References(_BaseApi):
                """
                Аккаунты.Пользователи.Мое.Избранное.Справочники
                """
                def age_ratings(self) -> list[dict]:
                    """
                    Возвращает список возрастных рейтингов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/favorites/references/age-ratings')

                def genres(self) -> list[dict]:
                    """
                    Возвращает список жанров в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/favorites/references/genres')

                def types(self) -> list[dict]:
                    """
                    Возвращает список типов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/favorites/references/types')

                def years(self) -> list[int]:
                    """
                    Возвращает список годов в коллекциях текущего пользователя
                    """
                    return self._req('/accounts/users/me/favorites/references/years')

                def sorting(self) -> list[dict]:
                    """
                    Возвращает список опций сортировки в избранном текущего пользователя
                    """
                    return self._req('/accounts/users/me/favorites/references/sorting')

                def _req(self, path):
                    data = self._request("GET", self._api_path+path, headers=self._headers, auth_required=True)
                    if data.status_code == 403:
                        raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                    elif data.status_code != 200:
                        raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")
                    return data.json()

        class Views(_BaseApi):
            """
            Аккаунты.Пользователи.Мое.Просмотры
            """
            def history(self, page: int = 1, limit: int = 10, include: list[str] = [], exclude: list[str] = []) -> dict:
                """
                Возвращает историю просмотров эпизодов авторизованного пользователя

                :page: Номер страницы (Целое число). По умолчанию 1
                :limit: Ограничение на количество элементов (Целое число). По умолчанию 10
                :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
                
                """
                params = {
                    'page': page,
                    'limit': limit
                }
                if len(include) > 0:
                    params['include'] = ",".join(include)
                if len(exclude) > 0:
                    params['exclude'] = ",".join(exclude)
                data = self._request("GET", self._api_path+"/accounts/users/me/views/history", headers=self._headers, data=json.dumps(params), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code == 422:
                    data = data.json()
                    if 'errors' in data.keys():
                        raise errors.PostArgumentsError(f"Некоторые из указанных параметров неверны. Ошибки:\n{data['errors']}")
                    raise errors.UnexpectedBehavior(f"Получен код 422 указывающий об ошибке валидации входных параметров, но в ответе сервера отсутствует поле 'errors'. Ответ: {data}")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 422. Получен: {data.status_code}")
                return data.json()

            def timecodes(self, since: str) -> list[list]:
                """
                Возвращает таймкоды по прогрессу просмотренных эпизодов (Список таймкодов просмотренных эпизодов)

                :since: Возвращает только таймкоды, которые были добавлены после указанного времени (в iso формате) (Пример: 2025-05-12T07:20:50.52Z)

                Пример:
                [
                [
                    "68d4d5c5-e3d5-419f-a21c-c511b6b251f5", # ID эпизода
                    743, # Время в секундах
                    true # Просмотрено ли
                ],
                ...
                ]
                """
                params = {
                    'since': since
                }
                data = self._request("GET", self._api_path+"/accounts/users/me/views/timecodes", headers=self._headers, data=json.dumps(params), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")
                return data.json()

            def update_timecode(self, release_episode_id: str, time: float | int, is_watched: bool):
                """
                Обновляет таймкод просмотренного эпизода

                :release_episode_id: ID эпизода (строка)
                :time: Время в секундах с начала эпизода (Дробное или целое число)
                :is_watched: Просмотрено ли (True или False)
                
                Ничего не возвращает
                """
                return self.update_multiple_timecodes([{"time": time, "is_watched": is_watched, "release_episode_id": release_episode_id}, ])

            def update_multiple_timecodes(self, params: list[dict]):
                """
                Обновляет таймкоды просмотренных эпизодов

                :params: Список словарей. Пример:
                    [
                        {
                            "time": 743.5, # Время в секундах с начала эпизода (Дробное или целое число)
                            "is_watched": true, # Просмотрено ли (True или False)
                            "release_episode_id": "68d4d5c5-e3d5-419f-a21c-c511b6b251f5"
                        }
                    ]
                
                Ничего не возвращает
                """
                data = self._request("POST", self._api_path+"/accounts/users/me/views/timecodes", headers=self._headers, data=json.dumps(params), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")

            def delete_timecode(self, release_episode_id: str):
                """
                Удаляет данные по таймкоду просмотров для указанного эпизода

                :release_episode_id: ID эпизода (строка)

                Ничего не возвращает
                """
                return self.delete_multiple_timecodes([release_episode_id, ])

            def delete_multiple_timecodes(self, ids: list[str]):
                """
                Удаляет данные по таймкодам просмотров для указанных эпизодов

                :ids: Список ID эпизодов (список строк)

                Ничего не возвращает
                """
                data = self._request("DELETE", self._api_path+"/accounts/users/me/views/timecodes", headers=self._headers, data=json.dumps([{"release_episode_id": x} for x in ids]), auth_required=True)
                if data.status_code == 403:
                    raise errors.Unauthorized("Получен код 403. Требуется авторизация")
                elif data.status_code != 200:
                    raise errors.UnexpectedBehavior(f"Ожидались коды 200 или 403. Получен: {data.status_code}")


        def profile(self, include: list[str] = [], exclude: list[str] = []) -> dict:
            """
            Возвращает данные профиля авторизованного пользователя

            :include: Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            :exclude: Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
            
            Пример:
            {
            "id": 4837362,
            "login": "animeshnik_488",
            "email": "animeshnik_488@protonmail.com",
            "nickname": "Animeshnik488",
            "avatar": {
                "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
                "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
                "optimized": {
                "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
                "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
                }
            },
            "torrents": {
                "passkey": "xBSmRDA95bJXPk3E",
                "uploaded": 998234623,
                "downloaded": 2397162874432
            },
            "is_banned": true,
            "created_at": "2019-03-31T20:43:52+00:00",
            "is_with_ads": false
            }
            """
            params = {}
            if len(include) > 0:
                params['include'] = ",".join(include)
            if len(exclude) > 0:
                params['exclude'] = ",".join(exclude)
            data = self._request("GET", self._api_path+'/accounts/users/me/profile', headers=self._headers, data=json.dumps(params), auth_required=True)
            if data.status_code == 403 or data.status_code == 404: # Почему 403 и 404 на "Не авторизован" - в душе не чаю, спросите того кто доку к апи писал
                raise errors.Unauthorized(f"Получен код {data.status_code}. Требуется авторизация")
            elif data.status_code != 200:
                raise errors.UnexpectedBehavior(f"Ожидались коды 200, 403 или 404. Получен: {data.status_code}")
            return data.json()