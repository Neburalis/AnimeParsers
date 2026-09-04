import importlib.util
import sys
import types
from pathlib import Path
from unittest.mock import Mock

import pytest


PACKAGE_PATH = Path(__file__).parents[1] / "src" / "anime_parsers_ru"
package = types.ModuleType("anime_parsers_ru")
package.__path__ = [str(PACKAGE_PATH)]
sys.modules.setdefault("anime_parsers_ru", package)
spec = importlib.util.spec_from_file_location(
    "anime_parsers_ru.parser_anixart", PACKAGE_PATH / "parser_anixart.py"
)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
AnixartParser = module.AnixartParser
from anime_parsers_ru import errors


def response(payload, status_code=200):
    result = Mock()
    result.status_code = status_code
    result.json.return_value = payload
    result.raise_for_status.return_value = None
    return result


def test_search_sends_expected_request_and_returns_releases():
    session = Mock()
    releases = [{"id": 42, "title": "Наруто"}]
    session.post.return_value = response({"code": 0, "releases": releases})
    parser = AnixartParser(
        base_url="https://example.test/api/",
        proxy="socks5://proxy.test:1080",
        timeout=7,
        session=session,
    )

    assert parser.search("Наруто", page=2, search_by=1) == releases
    session.post.assert_called_once_with(
        "https://example.test/api/search/releases/2",
        json={"query": "Наруто", "searchBy": 1},
        headers={
            "Accept": "application/json",
            "API-Version": "v2",
            "User-Agent": "anime-parsers-ru/AnixartParser",
        },
        proxies={
            "http": "socks5://proxy.test:1080",
            "https": "socks5://proxy.test:1080",
        },
        timeout=7,
    )


def test_anime_info_uses_release_path_and_extended_mode():
    session = Mock()
    release = {"id": 42, "title": "Наруто"}
    session.get.return_value = response({"code": 0, "release": release})
    parser = AnixartParser(base_url="https://example.test/api", session=session)

    assert parser.anime_info(42, extended=False) == release
    session.get.assert_called_once_with(
        "https://example.test/api/release/42?extended_mode=false",
        headers=parser._HEADERS,
        proxies=None,
        timeout=10,
    )


def test_episode_catalog_methods_extract_payloads_and_optional_sort():
    session = Mock()
    types = [{"id": 1, "name": "Озвучка"}]
    sources = [{"id": 2, "name": "Студия"}]
    episodes = [
        {
            "position": 1,
            "name": "Серия 1",
            "iframe": True,
            "quality": 720,
            "url": "https://external.test/1",
            "sourceId": 2,
            "releaseId": 42,
        }
    ]
    session.get.side_effect = [
        response({"code": 0, "types": types}),
        response({"code": 0, "sources": sources}),
        response({"code": 0, "episodes": episodes}),
        response({"code": 0, "episodes": episodes}),
    ]
    parser = AnixartParser(base_url="https://example.test/", session=session)

    assert parser.get_types(42) == types
    assert parser.get_sources(42, 1) == sources
    assert parser.get_episodes(42, 1, 2) == episodes
    assert parser.get_episodes(42, 1, 2, sort=1) == episodes
    assert [call.args[0] for call in session.get.call_args_list] == [
        "https://example.test/episode/42",
        "https://example.test/episode/42/1",
        "https://example.test/episode/42/1/2",
        "https://example.test/episode/42/1/2",
    ]
    assert "params" not in session.get.call_args_list[2].kwargs
    assert session.get.call_args_list[3].kwargs["params"] == {"sort": 1}


def test_empty_successful_search_raises_no_results():
    session = Mock()
    session.post.return_value = response({"code": 0, "releases": []})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.NoResults, match="ничего не найдено"):
        parser.search("Несуществующее аниме")


@pytest.mark.parametrize(
    "release",
    [
        None,
        [],
        {},
        {"id": True, "title": "Наруто"},
        {"id": "42", "title": "Наруто"},
        {"id": 42},
        {"id": 42, "title": "  "},
        {"id": 42, "title": None, "title_ru": ""},
    ],
)
def test_search_rejects_malformed_release_items(release):
    session = Mock()
    session.post.return_value = response({"code": 0, "releases": [release]})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="releases"):
        parser.search("Наруто")


@pytest.mark.parametrize("release", [{}, {"id": True}, {"id": "42"}])
def test_anime_info_rejects_empty_or_invalid_release_metadata(release):
    session = Mock()
    session.get.return_value = response({"code": 0, "release": release})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="release"):
        parser.anime_info(42)


def test_anime_info_rejects_release_id_that_differs_from_request():
    session = Mock()
    session.get.return_value = response({"code": 0, "release": {"id": 43}})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="release"):
        parser.anime_info(42)


def test_http_errors_raise_service_error():
    failed_response = response({}, status_code=503)
    failed_response.raise_for_status.side_effect = module.requests.HTTPError(
        "503 Server Error"
    )
    session = Mock()
    session.get.return_value = failed_response
    parser = AnixartParser(session=session)

    with pytest.raises(errors.ServiceError, match="HTTP"):
        parser.get_types(42)


@pytest.mark.parametrize(
    ("code", "error_type"),
    [
        (1, errors.ServiceError),
        (402, errors.ContentBlocked),
        (403, errors.ContentBlocked),
    ],
)
def test_nonzero_application_codes_raise_project_errors(code, error_type):
    session = Mock()
    session.get.return_value = response({"code": code, "types": []})
    parser = AnixartParser(session=session)

    with pytest.raises(error_type, match=str(code)):
        parser.get_types(42)


@pytest.mark.parametrize(
    "payload",
    [
        ValueError("invalid json"),
        [],
        {},
        {"code": False, "types": []},
        {"code": 0},
        {"code": 0, "types": {}},
    ],
)
def test_malformed_responses_raise_unexpected_behavior(payload):
    malformed_response = response(payload)
    if isinstance(payload, Exception):
        malformed_response.json.side_effect = payload
    session = Mock()
    session.get.return_value = malformed_response
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="ответ"):
        parser.get_types(42)


@pytest.mark.parametrize(
    ("payload_key", "path", "call"),
    [
        ("types", "episode/42", lambda parser: parser.get_types(42)),
        (
            "sources",
            "episode/42/1",
            lambda parser: parser.get_sources(42, 1),
        ),
    ],
)
def test_type_and_source_names_must_be_strings(payload_key, path, call):
    session = Mock()
    session.get.return_value = response(
        {"code": 0, payload_key: [{"id": 1, "name": None}]}
    )
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match=payload_key):
        call(parser)
    assert session.get.call_args.args[0].endswith(path)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("position", True),
        ("sourceId", "10"),
        ("releaseId", 42.0),
        ("iframe", 1),
        ("iframe", "https://player.test/1"),
        ("quality", True),
        ("quality", "720p"),
        ("name", None),
        ("url", ""),
        ("url", "   "),
        ("url", "/player/1"),
        ("url", "ftp://external.test/1"),
        ("url", "http://[invalid"),
    ],
)
def test_episodes_reject_malformed_field_values(field, value):
    episode = {
        "position": 1,
        "name": "Серия 1",
        "iframe": True,
        "quality": 720,
        "url": "https://external.test/1",
        "sourceId": 10,
        "releaseId": 42,
    }
    episode[field] = value
    session = Mock()
    session.get.return_value = response({"code": 0, "episodes": [episode]})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="episodes"):
        parser.get_episodes(42, 1, 10)


@pytest.mark.parametrize(
    ("field", "value"),
    [("releaseId", 43), ("sourceId", 11)],
)
def test_episodes_reject_ids_that_differ_from_the_request(field, value):
    episode = {
        "position": 1,
        "name": "Серия 1",
        "iframe": True,
        "quality": 720,
        "url": "https://external.test/1",
        "sourceId": 10,
        "releaseId": 42,
    }
    episode[field] = value
    session = Mock()
    session.get.return_value = response({"code": 0, "episodes": [episode]})
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="episodes"):
        parser.get_episodes(42, 1, 10)


@pytest.mark.parametrize(
    ("kwargs", "error_type"),
    [
        ({"base_url": 1}, TypeError),
        ({"base_url": "  "}, ValueError),
        ({"proxy": 1}, TypeError),
        ({"timeout": True}, TypeError),
        ({"timeout": 0}, ValueError),
        ({"session": object()}, TypeError),
    ],
)
def test_constructor_rejects_invalid_arguments(kwargs, error_type):
    with pytest.raises(error_type):
        AnixartParser(**kwargs)


def test_constructor_keeps_the_exact_injected_session():
    session = Mock()
    session.__bool__ = Mock(return_value=False)

    parser = AnixartParser(session=session)

    assert parser.session is session


@pytest.mark.parametrize(
    ("call", "error_type"),
    [
        (lambda parser: parser.search(1), TypeError),
        (lambda parser: parser.search("  "), ValueError),
        (lambda parser: parser.search("x", page=True), TypeError),
        (lambda parser: parser.search("x", page=-1), ValueError),
        (lambda parser: parser.search("x", search_by=False), TypeError),
        (lambda parser: parser.anime_info(0), ValueError),
        (lambda parser: parser.anime_info(1, extended=1), TypeError),
        (lambda parser: parser.get_types(True), TypeError),
        (lambda parser: parser.get_sources(1, "2"), TypeError),
        (lambda parser: parser.get_episodes(1, 2, False), TypeError),
        (lambda parser: parser.get_episodes(1, 2, 3, sort=True), TypeError),
    ],
)
def test_public_methods_validate_arguments_before_request(call, error_type):
    session = Mock()
    parser = AnixartParser(session=session)

    with pytest.raises(error_type):
        call(parser)
    session.get.assert_not_called()
    session.post.assert_not_called()


def test_player_urls_preserve_server_order_context_and_fail_fast():
    session = Mock()
    session.get.side_effect = [
        response(
            {
                "code": 0,
                "types": [
                    {"id": 2, "name": "Субтитры"},
                    {"id": 1, "name": "Озвучка"},
                ],
            }
        ),
        response({"code": 0, "sources": [{"id": 20, "name": "Source A"}]}),
        response(
            {
                "code": 0,
                "episodes": [
                    {
                        "position": 2,
                        "name": "Серия 2",
                        "iframe": True,
                        "quality": 1080,
                        "url": "https://external.test/2",
                        "sourceId": 20,
                        "releaseId": 42,
                    },
                    {
                        "position": 1,
                        "name": "Серия 1",
                        "iframe": False,
                        "quality": 720,
                        "url": "https://external.test/1",
                        "sourceId": 20,
                        "releaseId": 42,
                    },
                ],
            }
        ),
        response({"code": 0, "sources": [{"id": 10, "name": "Source B"}]}),
        response(
            {
                "code": 0,
                "episodes": [
                    {
                        "position": 1,
                        "name": "Эпизод",
                        "iframe": True,
                        "quality": None,
                        "url": "https://external.test/voice",
                        "sourceId": 10,
                        "releaseId": 42,
                    }
                ],
            }
        ),
    ]
    parser = AnixartParser(base_url="https://example.test/", session=session)

    assert parser.get_player_urls(42) == [
        {
            "type_id": 2,
            "type_name": "Субтитры",
            "source_id": 20,
            "source_name": "Source A",
            "episode_position": 2,
            "episode_name": "Серия 2",
            "iframe": True,
            "quality": 1080,
            "url": "https://external.test/2",
        },
        {
            "type_id": 2,
            "type_name": "Субтитры",
            "source_id": 20,
            "source_name": "Source A",
            "episode_position": 1,
            "episode_name": "Серия 1",
            "iframe": False,
            "quality": 720,
            "url": "https://external.test/1",
        },
        {
            "type_id": 1,
            "type_name": "Озвучка",
            "source_id": 10,
            "source_name": "Source B",
            "episode_position": 1,
            "episode_name": "Эпизод",
            "iframe": True,
            "quality": None,
            "url": "https://external.test/voice",
        },
    ]
    assert [call.args[0] for call in session.get.call_args_list] == [
        "https://example.test/episode/42",
        "https://example.test/episode/42/2",
        "https://example.test/episode/42/2/20",
        "https://example.test/episode/42/1",
        "https://example.test/episode/42/1/10",
    ]

    failing_session = Mock()
    failing_session.get.side_effect = [
        response({"code": 0, "types": [{"id": 1, "name": "Озвучка"}]}),
        response({"code": 0, "sources": [{"id": 10, "name": "Source"}]}),
        response({"code": 1, "episodes": []}),
        response({"code": 0, "episodes": []}),
    ]
    failing_parser = AnixartParser(session=failing_session)

    with pytest.raises(errors.ServiceError):
        failing_parser.get_player_urls(42)
    assert failing_session.get.call_count == 3


def test_malformed_catalog_items_raise_without_partial_aggregation():
    session = Mock()
    session.get.side_effect = [
        response({"code": 0, "types": [{"id": 1, "name": "Озвучка"}]}),
        response({"code": 0, "sources": [{"id": 10, "name": "Source"}]}),
        response(
            {
                "code": 0,
                "episodes": [
                    {
                        "position": 1,
                        "name": "Серия 1",
                        "iframe": True,
                        "quality": 720,
                        "url": "https://external.test/1",
                        "sourceId": 10,
                        "releaseId": 42,
                    },
                    {
                        "position": 2,
                        "name": "Серия 2",
                        "iframe": False,
                        "quality": 720,
                        "sourceId": 10,
                        "releaseId": 42,
                    },
                ],
            }
        ),
        response({"code": 0, "sources": []}),
    ]
    parser = AnixartParser(session=session)

    with pytest.raises(errors.UnexpectedBehavior, match="episodes"):
        parser.get_player_urls(42)
    assert session.get.call_count == 3
