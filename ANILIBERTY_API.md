# Документация к модулю AnilibertyAPI из библиотеки anime_parsers_ru

Данный модуль является оберткой для официального апи Aniliberty (aka Anilibria).
Официальная документация доступна по ссылке: https://anilibria.top/api/docs/v1 или https://aniliberty.top/api/docs/v1

Данная документация написана к версии апи 1.0.0 (OAS 3.0) и версии данной библиотеки 1.18.0

# Инициализация

Инициализировать требуется только класс AnilibertyAPI. Все остальные подклассы (которые наследуются от того-же шаблонного класса что и основой) будут инициализированы автоматически.

```python
from src.anime_parsers_ru import AnilibertyAPI

api = AnilibertyAPI(
    api_path='https://aniliberty.top/api/v1', # URL к апи эндпоинту (по умолчанию https://aniliberty.top/api/v1)
    proxy=None # http или socks5 прокси (`http://host:port` или `socks5://user:pass@host:port`) по умолчанию None
)
```

# Использование

Для использования функций апи вам нужно определить, какая функция в библиотеке соответствует требуемому эндпоинту указанному в документации.
Сделать это можно использя раздел [Эндпоинты](#эндпоинты).

Также большинство функций расположены в подклассах соответствующих описанию в документации. Пример:
Функция по эндпоинту `/anime/catalog/references/genres` в документации расположена по пути `Аниме.Каталог.Справочники`.
В библиотеке данная функция вызывается как: `api.Anime.Catalog.References.genres()`

!!! Не все функции следуют данному правилу, рекомендуется обратится к разделу [Эндпоинты](#эндпоинты) в случае если вы не нашли как вызвать нужную функцию

# Эндпоинты

## Содержание

* [Аккаунты (Авторизация)](#аккаунты-авторизация)
  * [Аккаунты.ОдноразовыеПароли](#аккаунтыодноразовыепароли)
  * [Аккаунты.Пользователи.Авторизация](#аккаунтыпользователиавторизация)
  * [Аккаунты.Пользователи.Авторизация.СоциальныеСети](#аккаунтыпользователиавторизациясоциальныесети)
  * [Аккаунты.Пользователи.Авторизация.Пароль](#аккаунтыпользователиавторизацияпароль)
* [Аккаунты (Пользователь)](#аккаунты-пользователь)
  * [Аккаунты.Пользователи.Мое.Коллекции.Справочники](#аккаунтыпользователимоеколлекциисправочники)
  * [Аккаунты.Пользователи.Мое.Коллекции](#аккаунтыпользователимоеколлекции)
  * [Аккаунты.Пользователи.Мое.Избранное.Справочники](#аккаунтыпользователимоеизбранноесправочники)
  * [Аккаунты.Пользователи.Мое.Избранное](#аккаунтыпользователимоеизбранное)
  * [Аккаунты.Пользователи.Мое.Профиль](#аккаунтыпользователимоепрофиль)
  * [Аккаунты.Пользователи.Мое.Просмотры](#аккаунтыпользователимоепросмотры)
* [Реклама.Vasts](#рекламаvasts)
* [Аниме](#аниме)
  * [Аниме.Каталог](#анимекаталог)
  * [Аниме.Каталог.Справочники](#анимекаталогсправочники)
  * [Аниме.Франшизы](#анимефраншизы)
  * [Аниме.Жанры](#анимежанры)
  * [Аниме.Релизы](#анимерелизы)
  * [Аниме.Релизы.Эпизоды](#анимерелизыэпизоды)
  * [Аниме.Релизы.РасписаниеРелизов](#анимерелизырасписаниерелизов)
  * [Аниме.Торренты](#аниметорренты)
* [Приложение](#приложение)
  * [Приложение.Поиск](#приложениепоиск)
  * [Приложение.Статус](#приложениестатус)
* [Медиа](#медиа)
  * [Медиа.Промо](#медиапромо)
  * [Медиа.Видеоконтент](#медиавидеоконтент)
* [Команды](#команды)

## Аккаунты (Авторизация)

### Аккаунты.ОдноразовыеПароли
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9E%D0%B4%D0%BD%D0%BE%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%D0%9F%D0%B0%D1%80%D0%BE%D0%BB%D0%B8)

Нет реализации в библиотеке

### Аккаунты.Пользователи.Авторизация
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
#### **>>> Авторизация пользователя** 

Url: `/accounts/users/auth/login`

Реализация в библиотеке:
```python
api.login(
    login="login", # Логин (не почта, именно логин, посмотреть можно в настрофках аккаунта на сайте)
    password="password123" # Пароль
) # Возвращает True если успешно
```
> Примечание: При вызове данной функции код получает токен авторизации и передает с помощью функции `set_auth_token` во все подклассы (вызывается автоматически)

#### **>>> Деавторизация пользователя**

Url: `/accounts/users/auth/logout`

Реализация в библиотеке:
```python
api.logout()
# Возвращает True если успешно
```
> Примечание: При вызове данной функции используется токен авторизации и после выполнения он перестает быть рабочим. Для очистки токена в подклассах используется функция `clear_auth_token` (вызывается автоматически)

### Аккаунты.Пользователи.Авторизация.СоциальныеСети
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.%D0%A1%D0%BE%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%D0%A1%D0%B5%D1%82%D0%B8)

Нет реализации в библиотеке

### Аккаунты.Пользователи.Авторизация.Пароль
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.%D0%9F%D0%B0%D1%80%D0%BE%D0%BB%D1%8C)

Нет реализации в библиотеке

## Аккаунты (Пользователь)

### Аккаунты.Пользователи.Мое.Коллекции.Справочники
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8.%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8)

#### **>>> Список возрастных рейтингов в коллекциях пользователя**

Url: `/accounts/users/me/collections/references/age-ratings`

Реализация в библиотеке:
```python
data = api.User.Collections.References.age_ratings()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "R0_PLUS",
    "label": "string",
    "description": "string"
  }
]
```

#### **>>> Cписок жанров в коллекциях текущего пользователя**

Url: `/accounts/users/me/collections/references/genres`

Реализация в библиотеке:
```python
data = api.User.Collections.References.genres()
```

Пример возвращаемых данных:
```json
[
  {
    "id": 0,
    "name": "string"
  }
]
```

#### **>>> Cписок типов в коллекциях текущего пользователя**

Url: `/accounts/users/me/collections/references/types`

Реализация в библиотеке:
```python
data = api.User.Collections.References.types()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "TV",
    "description": "string"
  }
]
```

#### **>>> Список годов в коллекциях текущего пользователя**

Url: `/accounts/users/me/collections/references/years`

Реализация в библиотеке:
```python
data = api.User.Collections.References.years()
```

Пример возвращаемых данных:
```json
[
  2020,
  2021,
  2022,
  2023
]
```

### Аккаунты.Пользователи.Мое.Коллекции

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8)

#### **>>> Список идентификаторов релизов добавленных в коллекции**

Url: `/accounts/users/me/collections/ids`

Реализация в библиотеке:
```python
data = api.User.Collections.ids()
```

Пример возвращаемых данных:
```json
[
  [
    8345,
    "PLANNED"
  ]
]
```

#### **>>> Список релизов добавленных в коллекцию [GET]**

Url: `/accounts/users/me/collections/releases` (GET)

Реализация в библиотеке:
```python
data = api.User.Collections.releases(
    type_of_collection=AnilibertyAPI.CollectionTypes.WATCHED, # Тип коллекции (Строка). Доступные значения описаны в AnilibertyAPI.CollectionTypes.types. Также можно указывать подклассы (AnilibertyAPI.CollectionTypes.PLANNED, ...) они автоматически будут переведены в соответствующие значения
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    genres=[AnilibertyAPI.Genres.Исекай, 15], # Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
    types=[AnilibertyAPI.Types.ONA, 'TV'], # Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
    years=[2021, 2022], # Минимальный год выхода релиза (Список целых чисел). По умолчанию отсутствует
    search="Поиск", # Поисковый запрос (Строка). По умолчанию отсутствует
    age_ratings=[AnilibertyAPI.AgeRatings.R0_PLUS, 'R6_PLUS'], # Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12,
      "genres": [
        {
          "id": 21,
          "name": "Комедия",
          "image": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "total_releases": 10
        }
      ],
      "episodes": [
        {
          "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
          "name": "Пролог",
          "ordinal": 12.5,
          "ending": {
            "start": 6,
            "stop": 125
          },
          "opening": {
            "start": 6,
            "stop": 125
          },
          "preview": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "hls_480": "string",
          "hls_720": "string",
          "hls_1080": "string",
          "duration": 1432,
          "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
          "youtube_id": "dQw4w9WgXcQ",
          "updated_at": "2021-11-25T18:46:30+00:00",
          "sort_order": 12,
          "release_id": 9324,
          "name_english": "Prologue"
        }
      ]
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Список релизов добавленных в коллекцию [POST]**

Url: `/accounts/users/me/collections/releases` (POST)

Реализация в библиотеке:
```python
data = api.User.Collections.releases_raw(
    params={
        "page": 1,
        "limit": 15,
        "type_of_collection": "PLANNED",
        "f": {
            "genres": "15,20",
            "types": [
            "TV",
            "WEB"
            ],
            "years": "2016, 2018, 2019",
            "search": "Мастера меча",
            "age_ratings": [
            "R6_PLUS",
            "R12_PLUS"
            ]
        },
        "include": "id,type.description",
        "exclude": "season.value,description"
    }   
)
```

Возвращаемые данные совпадают с GET запросом

#### **>>> Добавить релизы в коллекцию [POST]**

Url: `/accounts/users/me/collections` (POST)

Реализация в библиотеке:
```python
api.User.Collections.add_release(
    release_id=123, # ID Релиза (Целое число)
    type_of_collection=AnilibertyAPI.CollectionTypes.WATCHED # Тип коллекции (Строка). Доступные значения описаны в AnilibertyAPI.CollectionTypes.types. Также можно указывать подклассы (AnilibertyAPI.CollectionTypes.PLANNED, ...) они автоматически будут переведены в соответствующие значения
)

api.User.Collections.add_multiple_releases(
    data=[
        {
            "release_id": 123,
            "type_of_collection": "WATCHED"  
        }
    ], # Данные в виде: [ { "release_id": ID релиза (Целое число), "type_of_collection": Тип коллекции. Доступные значения описаны в AnilibertyAPI.CollectionTypes.types }, ... ]
    bypass_validation=False # Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)
)
```

Ничего не возвращает

#### **>>> Удалить релизы из коллекций [DELETE]**

Url: `/accounts/users/me/collections` (DELETE)

Реализация в библиотеке:
```python
api.User.Collections.remove_release(
    release_id=123 # ID Релиза (Целое число)
)

api.User.Collections.remove_multiple_releases(
    ids=[123, 321] # Список ID Релизов (Список целых чисесл)
)
```

Ничего не возвращает

### Аккаунты.Пользователи.Мое.Избранное.Справочники

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5.%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8)

#### **>>> Список возрастных рейтингов в избранном текущего пользователя**

Url: `/accounts/users/me/favorites/references/age-ratings`

Реализация в библиотеке:
```python
data = api.User.Favorites.References.age_ratings()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "R0_PLUS",
    "label": "string",
    "description": "string"
  }
]
```

#### **>>> Список жанров в избранном текущего пользователя**

Url: `/accounts/users/me/favorites/references/genres`

Реализация в библиотеке:
```python
data = api.User.Favorites.References.genres()
```

Пример возвращаемых данных:
```json
[
  {
    "id": 0,
    "name": "string"
  }
]
```

#### **>>> Список опций сортировки в избранном текущего пользователя**

Url: `/accounts/users/me/favorites/references/sorting`

Реализация в библиотеке:
```python
data = api.User.Favorites.References.sorting()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "CREATED_AT_DESC",
    "label": "string",
    "description": "string"
  }
]
```

#### **>>> Список типов релизов в избранном текущего пользователя**

Url: `/accounts/users/me/favorites/references/types`

Реализация в библиотеке:
```python
data = api.User.Favorites.References.types()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "TV",
    "description": "string"
  }
]
```

#### **>>> Список годов выхода в избранном текущего пользователя**

Url: `/accounts/users/me/favorites/references/years`

Реализация в библиотеке:
```python
data = api.User.Favorites.References.years()
```

Пример возвращаемых данных:
```json
[
  2020,
  2021,
  2022,
  2023
]
```

### Аккаунты.Пользователи.Мое.Избранное
[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5)

#### **>>> Список идентификаторов релизов добавленных в избранное**

Url: `/accounts/users/me/favorites/ids`

Реализация в библиотеке:
```python
data = api.User.Favorites.ids()
```

Пример возвращаемых данных:
```json
[
  9023,
  9024,
  9025
]
```

#### **>>> Список релизов в избранном пользователя [GET]**

Url: `/accounts/users/me/favorites/releases` (GET)

Реализация в библиотеке:
```python
data = api.User.Favorites.releases(
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    genres=[AnilibertyAPI.Genres.Исекай, 15], # Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
    types=[AnilibertyAPI.Types.ONA, 'TV'], # Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
    years=[2021, 2022], # Минимальный год выхода релиза (Список целых чисел). По умолчанию отсутствует
    search=['Поиск'], # Поисковый запрос (Строка). По умолчанию отсутствует
    age_ratings=[AnilibertyAPI.AgeRatings.R0_PLUS, 'R6_PLUS'], # Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'], # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    bypass_validation=False # Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)
)
```

Пример возвращаемых данных:
```python
{
  "data": [
    {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12,
      "genres": [
        {
          "id": 21,
          "name": "Комедия",
          "image": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "total_releases": 10
        }
      ],
      "episodes": [
        {
          "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
          "name": "Пролог",
          "ordinal": 12.5,
          "ending": {
            "start": 6,
            "stop": 125
          },
          "opening": {
            "start": 6,
            "stop": 125
          },
          "preview": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "hls_480": "string",
          "hls_720": "string",
          "hls_1080": "string",
          "duration": 1432,
          "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
          "youtube_id": "dQw4w9WgXcQ",
          "updated_at": "2021-11-25T18:46:30+00:00",
          "sort_order": 12,
          "release_id": 9324,
          "name_english": "Prologue"
        }
      ]
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Список релизов в избранном пользователя [POST]**

Url: `/accounts/users/me/favorites/releases` (POST)

Реализация в библиотеке:
```python
data = api.User.Favorites.releases_raw(
    params={
    "page": 1,
    "limit": 15,
    "f": {
        "years": "2016, 2018, 2019",
        "types": [
        "TV",
        "WEB"
        ],
        "genres": "15,20",
        "search": "Мастера меча",
        "sorting": "CREATED_AT_DESC",
        "age_ratings": [
        "R6_PLUS",
        "R12_PLUS"
        ]
    },
    "include": "id,type.description",
    "exclude": "season.value,description"
    }
)
```

Возвращает то же что и GET запрос

#### **>>> Добавить релизы в избранное [POST]**

Url: `/accounts/users/me/favorites` (POST)

Реализация в библиотеке:
```python
api.User.Favorites.add_release(
    release_id=123, # ID Релиза (Целое число)
)

api.User.Favorites.add_multiple_releases(
    ids=[123, 321], # Список ID Релизов (Список целых чисесл)
)
```

Ничего не возвращает

#### **>>> Удалить релизы из избранного [DELETE]**

Url: `/accounts/users/me/favorites` (DELETE)

Реализация в библиотеке:
```python
api.User.Favorites.remove_release(
    release_id=123 # ID Релиза (Целое число)
)

api.User.Favorites.remove_multiple_releases(
    ids=[123, 321] # Список ID Релизов (Список целых чисесл)
)
```

Ничего не возвращает

### Аккаунты.Пользователи.Мое.Профиль

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%9F%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D1%8C)

#### **>>> Профиль авторизованного пользователя**

Url: `/accounts/users/me/profile`

Реализация в библиотеке:
```python
data = api.User.profile(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
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
```

### Аккаунты.Пользователи.Мое.Просмотры

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%9F%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D1%8B)

#### **>>> История просмотренных эпизодов**

Url: `/accounts/users/me/views/history`

Реализация в библиотеке:
```python
data = api.User.Views.history(
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 123,
      "time": 127.45,
      "user_id": 42,
      "is_watched": true,
      "updated_at": "2025-06-23T14:00:00+00:00",
      "release_episode_id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
      "release_episode": {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue",
        "release": {
          "id": 7439,
          "type": {
            "value": "TV",
            "description": "ТВ"
          },
          "year": 2018,
          "name": {
            "main": "Мастера Меча Онлайн: Алисизация",
            "english": "Sword Art Online: Alicization",
            "alternative": "Война в Андерворлде, War of Underworld"
          },
          "alias": "sword-art-online-alicization",
          "season": {
            "value": "winter",
            "description": "Осень"
          },
          "poster": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "fresh_at": "2019-12-29T23:06:39+00:00",
          "created_at": "2019-12-29T23:06:39+00:00",
          "updated_at": "2023-08-20T15:08:20+00:00",
          "is_ongoing": false,
          "age_rating": {
            "value": "R0_PLUS",
            "label": "16+",
            "is_adult": false,
            "description": "Для людей, достигших возраста шестнадцати лет (16+)"
          },
          "publish_day": {
            "value": 1,
            "description": "Воскресенье"
          },
          "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
          "notification": "Серии выходят по воскресеньям",
          "episodes_total": 36,
          "external_player": "//kodik.info/serial/...",
          "is_in_production": false,
          "is_blocked_by_geo": false,
          "is_blocked_by_copyrights": false,
          "added_in_users_favorites": 25557,
          "average_duration_of_episode": 25,
          "added_in_planned_collection": 2457,
          "added_in_watched_collection": 467,
          "added_in_watching_collection": 346,
          "added_in_postponed_collection": 212,
          "added_in_abandoned_collection": 12
        }
      }
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Таймкоды просмотренных эпизодов [GET]**

Url: `/accounts/users/me/views/timecodes` (GET)

Реализация в библиотеке:
```python
data = api.User.Views.timecodes(
    since='2025-05-12T07:20:50.52Z' # Возвращает только таймкоды, которые были добавлены после указанного времени (в iso формате)
)
```

Пример возвращаемых данных:
```json
[
  [
    "68d4d5c5-e3d5-419f-a21c-c511b6b251f5", // ID эпизода
    743, // Кол-во секунд с начала
    true // Просмотрено
  ]
]
```

#### **>>> Обновление таймкодов прогресса просмотренного эпизода [POST]**

Url: `/accounts/users/me/views/timecodes` (POST)

Реализация в библиотеке:
```python
api.User.Views.update_timecode(
    release_episode_id='123wf-wefwef-wefaf', # ID эпизода (строка)
    time=123.1, # Время в секундах с начала эпизода (Дробное или целое число)
    is_watched=False # Просмотрено ли (True или False)
)

api.User.Views.update_multiple_timecodes(
    params=[
        {
            "release_episode_id": "123wf-wefwef-wefaf",
            "time": 123.1,
            "is_watched": False 
        }
    ]
)
```

Ничего не возвращает

#### **>>> Удаление таймкодов просмотра эпизода [DELETE]**

Url: `/accounts/users/me/views/timecodes` (DELETE)

Реализация в библиотеке:
```python
api.User.Views.remove_timecode(
    release_episode_id="123wf-wefwef-wefaf", # ID эпизода (строка)
)

api.User.Views.remove_multiple_timecodes(
    ids=[
        "123wf-wefwef-wefaf", "456wf-wefwef-wefaf"
    ]
)
```

Ничего не возвращает

## Реклама.Vasts

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%A0%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%B0.Vasts)

#### **>>> Список возможных VAST реклам**

Url: `/media/vasts`

Реализация в библиотеке:
```python
data = api.Media.vasts()
```

Пример возвращаемых данных:
```json
[
  {
    "id": "17974e6e-da62-427b-9937-9021cf4cafe4",
    "url": "https://example.com/vast.xml",
    "ad_erid": "ERID123456789",
    "ad_company_itn": "1234567890",
    "ad_company_name": "Company XYZ"
  }
]
```

#### **>>> VAST XML с цепочкой реклам**

Url: `/media/manifest.xml`

Реализация в библиотеке:
```python
data = api.Media.manifest_xml()
```

Возвращает строку - контент xml документа.

## Аниме

### Аниме.Каталог

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3)

#### **>>> Список релизов в каталоге [GET]**

Url: `/anime/catalog/releases` (GET)

Реализация в библиотеке:
```python
data = api.Anime.Catalog.releases(
    page=1, # Номер страницы. (По умолчанию 1)
    limit=10, # Ограничение на количество элементов. (По умолчанию 10)
    genres=[AnilibertyAPI.Genres.Исекай, 15], # Список идентификаторов жанров (Список целых чисел). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения. (По умолчанию пустой список)
    types=[AnilibertyAPI.Types.ONA, 'TV'], # Список типов релизов (Список строк). Доступные значения: TV, ONA, WEB, OVA, OAD, MOVIE, DORAMA, SPECIAL. Также они описаны в AnilibertyAPI.Types.types и можно указывать подклассы (AnilibertyAPI.Types.TV, ...). (По умолчанию пустой список)
    seasons=['winter', 'spring'], # Список сезонов релизов (Список строк). Доступные значения: winter, spring, summer, autumn. (По умолчанию пусто)
    from_year=2019, # Минимальный год выхода релиза (Целое число). (По умолчанию отсутствует)
    to_year=2022, # Максимальный год выхода релиза (Целое число). (По умолчанию отсутствует)
    search='Поиск', # Поисковой запрос / Название (Строка). (По умолчанию отсутствует)
    sorting=AnilibertyAPI.Sorting.FRESH_AT_DESC, # Тип сортировки (строка). Доступные значения: FRESH_AT_DESC, FRESH_AT_ASC, RATING_DESC, RATING_ASC, YEAR_DESC, YEAR_ASC. Также они описаны в AnilibertyAPI.Sorting.sorts и можно указывать подклассы (AnilibertyAPI.Sorting.FRESH_AT_DESC, ...). (По умолчанию отсутствует)
    age_ratings=[AnilibertyAPI.AgeRatings.R0_PLUS, 'R6_PLUS'], # Список возрастных рейтингов (список строк). Доступные значения: R0_PLUS, R6_PLUS, R12_PLUS, R16_PLUS, R18_PLUS. Также они описаны в AnilibertyAPI.AgeRatings.ratings и можно указывать подклассы (AnilibertyAPI.AgeRatings.R0_PLUS, ...). (По умолчанию отсутствует)
    publish_statuses=["IS_ONGOING", "IS_NOT_ONGOING"], # Список статусов релизов (список строк). Доступные значения: IS_ONGOING, IS_NOT_ONGOING
    production_statuses=["IS_IN_PRODUCTION", "IS_NOT_IN_PRODUCTION"], # Список статусов релизов (список строк). Доступные значения: IS_IN_PRODUCTION, IS_NOT_IN_PRODUCTION
    include=['id'], # Список включаемых полей (Список строк). Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'], # Список исключаемых полей (Список строк). Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    bypass_validation=False # Отключение проверки корректности данных (перед запросом). (По умолчанию False - проверка проводится)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12,
      "genres": [
        {
          "id": 21,
          "name": "Комедия",
          "image": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "total_releases": 10
        }
      ]
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Список релизов в каталоге [POST]**

Url: `/anime/catalog/releases` (POST)

Реализация в библиотеке:
```python
data = api.Anime.Catalog.releases_raw(
    params={
  "page": 1,
  "limit": 15,
  "f": {
    "genres": [
      15,
      20
    ],
    "types": [
      "TV",
      "WEB"
    ],
    "seasons": [
      "winter",
      "autumn"
    ],
    "years": {
      "from_year": 2016,
      "to_year": 2020
    },
    "search": "Мастера меча",
    "sorting": "FRESH_AT_DESC",
    "age_ratings": [
      "R6_PLUS",
      "R12_PLUS"
    ],
    "publish_statuses": [
      "IS_ONGOING"
    ],
    "production_statuses": [
      "IS_IN_PRODUCTION"
    ]
  },
  "include": "id,type.description",
  "exclude": "season.value,description"
}
)
```

Возвращает то же что и GET запрос.

### Аниме.Каталог.Справочники

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3.%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8)

#### **>>> Cписок возрастных рейтингов в каталоге**

Url: `/anime/catalog/references/age-ratings`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.age_ratings()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "R0_PLUS",
    "label": "PG-17",
    "description": "PG"
  }
]
```

#### **>>> Список всех жанров в каталоге**

Url: `/anime/catalog/references/genres`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.genres()
```

Пример возвращаемых данных:
```json
[
  {
    "id": 23,
    "name": "Мистика"
  }
]
```

#### **>>> Список возможных статусов озвучки релиза в каталоге**

Url: `/anime/catalog/references/production-statuses`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.production_statuses()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "IS_IN_PRODUCTION",
    "description": "Сейчас в озвучке"
  }
]
```

#### **>>> Список возможных статусов выхода релиза в каталоге**

Url: `/anime/catalog/references/publish-statuses`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.publish_statuses()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "IS_ONGOING",
    "description": "Онгоинг"
  }
]
```

#### **>>> Список возможных сезонов релизов в каталоге**

Url: `/anime/catalog/references/seasons`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.seasons()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "winter",
    "description": "Зима"
  }
]
```

#### **>>> Список возможных типов сортировок в каталоге**

Url: `/anime/catalog/references/sorting`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.sorting()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "FRESH_AT_DESC",
    "label": "Самый низкий рейтинг",
    "description": "Сначала отобразятся самые непопулярные релизы"
  }
]
```

#### **>>> Список возможных типов релизов в каталоге**

Url: `/anime/catalog/references/types`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.types()
```

Пример возвращаемых данных:
```json
[
  {
    "value": "TV",
    "description": "ТВ"
  }
]
```

#### **>>> Список годов в каталоге**

Url: `/anime/catalog/references/years`

Реализация в библиотеке:
```python
data = api.Anime.Catalog.References.years()
```

Пример возвращаемых данных:
```json
[
  2020,
  2021,
  2022,
  2023
]
```

### Аниме.Франшизы

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%A4%D1%80%D0%B0%D0%BD%D1%88%D0%B8%D0%B7%D1%8B)

#### **>>> Получить список франшиз**

Url: `/anime/franchises`

Реализация в библиотеке:
```python
data = api.Anime.Franchises.franchises(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "116e17d2-e89f-4ffc-bfa4-b45ae4c41e92",
    "name": "Re: Жизнь в другом мире с нуля",
    "name_english": "Re: Zero kara Hajimeru Isekai Seikatsu",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "rating": 8.45,
    "last_year": 2023,
    "first_year": 2010,
    "total_releases": 10,
    "total_episodes": 25,
    "total_duration": "2 дня 5 часов",
    "total_duration_in_seconds": 183600
  }
]
```

#### **>>> Получить франшизу**

Url: `/anime/franchises/{franchiseId}`

Реализация в библиотеке:
```python
data = api.Anime.Franchises.franchise_by_id(
    franchise_id="1234-ffff", # ID франшизы
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Привер возвращаемых данных:
```json
{
  "id": "116e17d2-e89f-4ffc-bfa4-b45ae4c41e92",
  "name": "Re: Жизнь в другом мире с нуля",
  "name_english": "Re: Zero kara Hajimeru Isekai Seikatsu",
  "image": {
    "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "optimized": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
    }
  },
  "rating": 8.45,
  "last_year": 2023,
  "first_year": 2010,
  "total_releases": 10,
  "total_episodes": 25,
  "total_duration": "2 дня 5 часов",
  "total_duration_in_seconds": 183600,
  "franchise_releases": [
    {
      "id": "db1ebabd-b4b8-4391-85f3-79294515641a",
      "sort_order": 2,
      "release_id": 9045,
      "franchise_id": "3f69ea9b-c202-4522-96b9-07a5de8aa963",
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      }
    }
  ]
}
```

#### **>>> Получить список случайных франшиз**

Url: `/anime/franchises/random`

Реализация в библиотеке:
```python
data = api.Anime.Franchises.random(
    limit=5, # Количество случайных франшиз в выдаче. По умолчанию 5
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "116e17d2-e89f-4ffc-bfa4-b45ae4c41e92",
    "name": "Re: Жизнь в другом мире с нуля",
    "name_english": "Re: Zero kara Hajimeru Isekai Seikatsu",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "rating": 8.45,
    "last_year": 2023,
    "first_year": 2010,
    "total_releases": 10,
    "total_episodes": 25,
    "total_duration": "2 дня 5 часов",
    "total_duration_in_seconds": 183600
  }
]
```

#### **>>> Получить список франшиз для релиза**

Url: `/anime/franchises/release/{releaseId}`

Реализация в библиотеке:
```python
data = api.Anime.Franchises.franchises_by_release_id(
    release_id="1234-ffff", # ID релиза
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "116e17d2-e89f-4ffc-bfa4-b45ae4c41e92",
    "name": "Re: Жизнь в другом мире с нуля",
    "name_english": "Re: Zero kara Hajimeru Isekai Seikatsu",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "rating": 8.45,
    "last_year": 2023,
    "first_year": 2010,
    "total_releases": 10,
    "total_episodes": 25,
    "total_duration": "2 дня 5 часов",
    "total_duration_in_seconds": 183600,
    "franchise_releases": [
      {
        "id": "db1ebabd-b4b8-4391-85f3-79294515641a",
        "sort_order": 2,
        "release_id": 9045,
        "franchise_id": "3f69ea9b-c202-4522-96b9-07a5de8aa963",
        "release": {
          "id": 7439,
          "type": {
            "value": "TV",
            "description": "ТВ"
          },
          "year": 2018,
          "name": {
            "main": "Мастера Меча Онлайн: Алисизация",
            "english": "Sword Art Online: Alicization",
            "alternative": "Война в Андерворлде, War of Underworld"
          },
          "alias": "sword-art-online-alicization",
          "season": {
            "value": "winter",
            "description": "Осень"
          },
          "poster": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "fresh_at": "2019-12-29T23:06:39+00:00",
          "created_at": "2019-12-29T23:06:39+00:00",
          "updated_at": "2023-08-20T15:08:20+00:00",
          "is_ongoing": false,
          "age_rating": {
            "value": "R0_PLUS",
            "label": "16+",
            "is_adult": false,
            "description": "Для людей, достигших возраста шестнадцати лет (16+)"
          },
          "publish_day": {
            "value": 1,
            "description": "Воскресенье"
          },
          "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
          "notification": "Серии выходят по воскресеньям",
          "episodes_total": 36,
          "external_player": "//kodik.info/serial/...",
          "is_in_production": false,
          "is_blocked_by_geo": false,
          "is_blocked_by_copyrights": false,
          "added_in_users_favorites": 25557,
          "average_duration_of_episode": 25,
          "added_in_planned_collection": 2457,
          "added_in_watched_collection": 467,
          "added_in_watching_collection": 346,
          "added_in_postponed_collection": 212,
          "added_in_abandoned_collection": 12
        }
      }
    ]
  }
]
```

### Аниме.Жанры

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%96%D0%B0%D0%BD%D1%80%D1%8B)

#### **>>> Список всех жанров**

Url: `/anime/genres`

Реализация в библиотеке:
```python
data = api.Anime.Genres.genres(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 21,
    "name": "Комедия",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "total_releases": 10
  }
]
```

#### **>>> Данные по жанру**

Url: `/anime/genres/{genreId}`

Реализация в библиотеке:
```python
data = api.Anime.Genres.genre_by_id(
    genre_id=AnilibertyAPI.Genres.Исекай, # ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)

# ИЛИ

data = api.Anime.Genres.genre_by_id(
    genre_id=15, # ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "id": 21,
  "name": "Комедия",
  "image": {
    "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "optimized": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
    }
  },
  "total_releases": 10
}
```

#### **>>> Список случайных жанров**

Url: `/anime/genres/random`

Реализация в библиотеке:
```python
data = api.Anime.Genres.random(
    limit=5, # Количество жанров в выдаче (целое число). По умолчанию 5
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 21,
    "name": "Комедия",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "total_releases": 10
  }
]
```

#### **>>> Список релизов жанра**

Url: `/anime/genres/{genreId}/releases`

Реализация в библиотеке:
```python
data = api.Anime.Genres.releases_by_genre_id(
    genre_id=AnilibertyAPI.Genres.Исекай, # ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)

# ИЛИ

data = api.Anime.Genres.releases_by_genre_id(
    genre_id=15, # ID Жанра (Целое число). Доступные значения описаны в AnilibertyAPI.Genres.genres, также можно указывать подклассы (AnilibertyAPI.Genres.Приключения, AnilibertyAPI.Genres.Ужасы, ...) они автоматически будут переведены в соответствующие значения.
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

### Аниме.Релизы

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%A0%D0%B5%D0%BB%D0%B8%D0%B7%D1%8B)

#### **>>> Последние релизы**

Url: `/anime/releases/latest`

Реализация в библиотеке:
```python
data = api.Anime.Releases.latest(
    limit=10, # Количество последних релизов в выдаче (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаеых данных:
```json
[
  {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12,
    "genres": [
      {
        "id": 21,
        "name": "Комедия",
        "image": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "total_releases": 10
      }
    ],
    "latest_episode": {
      "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
      "name": "Пролог",
      "ordinal": 12.5,
      "ending": {
        "start": 6,
        "stop": 125
      },
      "opening": {
        "start": 6,
        "stop": 125
      },
      "preview": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "hls_480": "string",
      "hls_720": "string",
      "hls_1080": "string",
      "duration": 1432,
      "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
      "youtube_id": "dQw4w9WgXcQ",
      "updated_at": "2021-11-25T18:46:30+00:00",
      "sort_order": 12,
      "release_id": 9324,
      "name_english": "Prologue"
    }
  }
]
```

#### **>>> Данные по случайным релизам**

Url: `/anime/releases/random`

Реализация в библиотеке:
```python
data = api.Anime.Releases.random(
    limit=10, # Количество случайных релизов в выдаче (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12
  }
]
```

#### **>>> Данные по рекомендованным релизам**

Url: `/anime/releases/recommended`

Реализация в библиотеке:
```python
data = api.Anime.Releases.recommended(
    release_id="1234-ffff", # Идентификатор релиза, для которого рекомендуем
    limit=10, # Количество рекомендованных релизов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12
  }
]
```

#### **>>> Данные по списку релизов**

Url: `/anime/releases/list`

Реализация в библиотеке:
```python
data = api.Anime.Releases.releases_list(
    ids=[1234, 56789], # Список ID релизов (Список целых чисел). По умолчангию отсутствует
    aliases=["alias1", "alias2"], # Список alias релизов (Список строк, пример: ['darling-in-the-franxx']). По умолчанию отсутствует
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12,
      "genres": [
        {
          "id": 21,
          "name": "Комедия",
          "image": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "total_releases": 10
        }
      ],
      "members": [
        {
          "id": "uuid...",
          "role": {
            "value": "poster",
            "description": "Озвучка"
          },
          "user": {
            "id": 2346,
            "avatar": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "optimized": {
                "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
                "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
              }
            }
          },
          "nickname": "Zvukar"
        }
      ],
      "episodes": [
        {
          "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
          "name": "Пролог",
          "ordinal": 12.5,
          "ending": {
            "start": 6,
            "stop": 125
          },
          "opening": {
            "start": 6,
            "stop": 125
          },
          "preview": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          },
          "hls_480": "string",
          "hls_720": "string",
          "hls_1080": "string",
          "duration": 1432,
          "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
          "youtube_id": "dQw4w9WgXcQ",
          "updated_at": "2021-11-25T18:46:30+00:00",
          "sort_order": 12,
          "release_id": 9324,
          "name_english": "Prologue"
        }
      ],
      "torrents": [
        {
          "id": 18523,
          "hash": "8a8fb94b1bd22b44a116336bab6bf209d0ac3a90",
          "size": 7356495551,
          "type": {
            "value": "BDRip",
            "description": "WEBRip"
          },
          "color": {
            "value": "8bit",
            "description": "8-bit"
          },
          "codec": {
            "value": "AV1",
            "label": "AVC",
            "description": "x264/AVC",
            "label_color": "#FFF",
            "label_is_visible": true
          },
          "label": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p]",
          "quality": {
            "value": "360p",
            "description": "1080p"
          },
          "magnet": "magnet:?xt=urn:btih:QPYNLG5Y2LA2KHB7SZCQF2W3...",
          "filename": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p].torrent",
          "seeders": 234,
          "bitrate": 3400,
          "leechers": 58,
          "sort_order": 2,
          "updated_at": "2021-09-22T16:20:38+00:00",
          "is_hardsub": true,
          "description": "1-17 + OVA(1-4)",
          "created_at": "2021-09-21T11:45:00+00:00",
          "completed_times": 13538
        }
      ],
      "sponsors": [
        {
          "id": "UUID",
          "title": "Sponsor name",
          "description": "Лучший спонсор в мире!",
          "url_title": "Переходи по ссылке",
          "url": "https://yandex.ru"
        }
      ]
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Данные по релизу**

Url: `/anime/releases/{idOrAlias}`

Реализация в библиотеке:
```python
data = api.Anime.Releases.by_id(
    release_id=12345, # id релиза
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)

data = api.Anime.Releases.by_alias(
    alias="alias", # alias релиза (Пример: darling-in-the-franxx)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)

data = api.Anime.Releases.by_id_or_alias(
    id_or_alias="alias", # id или alias релиза
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "id": 7439,
  "type": {
    "value": "TV",
    "description": "ТВ"
  },
  "year": 2018,
  "name": {
    "main": "Мастера Меча Онлайн: Алисизация",
    "english": "Sword Art Online: Alicization",
    "alternative": "Война в Андерворлде, War of Underworld"
  },
  "alias": "sword-art-online-alicization",
  "season": {
    "value": "winter",
    "description": "Осень"
  },
  "poster": {
    "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "optimized": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
    }
  },
  "fresh_at": "2019-12-29T23:06:39+00:00",
  "created_at": "2019-12-29T23:06:39+00:00",
  "updated_at": "2023-08-20T15:08:20+00:00",
  "is_ongoing": false,
  "age_rating": {
    "value": "R0_PLUS",
    "label": "16+",
    "is_adult": false,
    "description": "Для людей, достигших возраста шестнадцати лет (16+)"
  },
  "publish_day": {
    "value": 1,
    "description": "Воскресенье"
  },
  "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
  "notification": "Серии выходят по воскресеньям",
  "episodes_total": 36,
  "external_player": "//kodik.info/serial/...",
  "is_in_production": false,
  "is_blocked_by_geo": false,
  "is_blocked_by_copyrights": false,
  "added_in_users_favorites": 25557,
  "average_duration_of_episode": 25,
  "added_in_planned_collection": 2457,
  "added_in_watched_collection": 467,
  "added_in_watching_collection": 346,
  "added_in_postponed_collection": 212,
  "added_in_abandoned_collection": 12,
  "genres": [
    {
      "id": 21,
      "name": "Комедия",
      "image": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "total_releases": 10
    }
  ],
  "members": [
    {
      "id": "uuid...",
      "role": {
        "value": "poster",
        "description": "Озвучка"
      },
      "user": {
        "id": 2346,
        "avatar": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        }
      },
      "nickname": "Zvukar"
    }
  ],
  "episodes": [
    {
      "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
      "name": "Пролог",
      "ordinal": 12.5,
      "ending": {
        "start": 6,
        "stop": 125
      },
      "opening": {
        "start": 6,
        "stop": 125
      },
      "preview": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "hls_480": "string",
      "hls_720": "string",
      "hls_1080": "string",
      "duration": 1432,
      "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
      "youtube_id": "dQw4w9WgXcQ",
      "updated_at": "2021-11-25T18:46:30+00:00",
      "sort_order": 12,
      "release_id": 9324,
      "name_english": "Prologue"
    }
  ],
  "torrents": [
    {
      "id": 18523,
      "hash": "8a8fb94b1bd22b44a116336bab6bf209d0ac3a90",
      "size": 7356495551,
      "type": {
        "value": "BDRip",
        "description": "WEBRip"
      },
      "color": {
        "value": "8bit",
        "description": "8-bit"
      },
      "codec": {
        "value": "AV1",
        "label": "AVC",
        "description": "x264/AVC",
        "label_color": "#FFF",
        "label_is_visible": true
      },
      "label": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p]",
      "quality": {
        "value": "360p",
        "description": "1080p"
      },
      "magnet": "magnet:?xt=urn:btih:QPYNLG5Y2LA2KHB7SZCQF2W3...",
      "filename": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p].torrent",
      "seeders": 234,
      "bitrate": 3400,
      "leechers": 58,
      "sort_order": 2,
      "updated_at": "2021-09-22T16:20:38+00:00",
      "is_hardsub": true,
      "description": "1-17 + OVA(1-4)",
      "created_at": "2021-09-21T11:45:00+00:00",
      "completed_times": 13538
    }
  ],
  "sponsors": [
    {
      "id": "UUID",
      "title": "Sponsor name",
      "description": "Лучший спонсор в мире!",
      "url_title": "Переходи по ссылке",
      "url": "https://yandex.ru"
    }
  ]
}
```

#### **>>> Список участников, которые работали над релизом**

Url: `/anime/releases/{idOrAlias}/members`

Реализация в библиотеке:
```python
data = api.Anime.Releases.members(
    id_or_alias="alias", # id или alias релиза (Пример alias: darling-in-the-franxx)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "uuid...",
    "role": {
      "value": "poster",
      "description": "Озвучка"
    },
    "user": {
      "id": 2346,
      "avatar": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      }
    },
    "nickname": "Zvukar"
  }
]
```

#### **>>> Данные по таймкодам просмотра эпизодов релиза**

Url: `/anime/releases/{idOrAlias}/episodes/timecodes`

Реализация в библиотеке:
```python
data = api.Anime.Releases.episodes_timecodes(
    id_or_alias="alias", # id или alias релиза (Пример alias: darling-in-the-franxx)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 123,
    "time": 127.45,
    "user_id": 42,
    "is_watched": true,
    "updated_at": "2025-06-23T14:00:00+00:00",
    "release_episode_id": "9b5e26ee-598f-4b8b-b77e-188d3e456318"
  }
]
```

### Аниме.Релизы.Эпизоды

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%A0%D0%B5%D0%BB%D0%B8%D0%B7%D1%8B.%D0%AD%D0%BF%D0%B8%D0%B7%D0%BE%D0%B4%D1%8B)

#### **>>> Данные по эпизоду**

Url: `/anime/releases/episodes/{releaseEpisodeId}`

Реализация в библиотеке:
```python
data = api.Anime.Releases.Episodes.by_id(
    release_episode_id="1234-ffff", # Идентификатор эпизода (Строка). (Пример: cf31fe87-fad8-11eb-b2fa-0242ac120004)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
  "name": "Пролог",
  "ordinal": 12.5,
  "ending": {
    "start": 6,
    "stop": 125
  },
  "opening": {
    "start": 6,
    "stop": 125
  },
  "preview": {
    "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
    "optimized": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
    }
  },
  "hls_480": "string",
  "hls_720": "string",
  "hls_1080": "string",
  "duration": 1432,
  "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
  "youtube_id": "dQw4w9WgXcQ",
  "updated_at": "2021-11-25T18:46:30+00:00",
  "sort_order": 12,
  "release_id": 9324,
  "name_english": "Prologue",
  "release": {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12,
    "episodes": [
      {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue"
      }
    ]
  }
}
```

#### **>>> Данные по просмотру эпизода**

Url: `/anime/releases/episodes/{releaseEpisodeId}/timecode`

Реализация в библиотеке:
```python
data = api.Anime.Releases.Episodes.timecodes(
    release_episode_id="1234-ffff", # Идентификатор эпизода (Строка). (Пример: cf31fe87-fad8-11eb-b2fa-0242ac120004)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "id": 123,
  "time": 127.45,
  "user_id": 42,
  "is_watched": true,
  "updated_at": "2025-06-23T14:00:00+00:00",
  "release_episode_id": "9b5e26ee-598f-4b8b-b77e-188d3e456318"
}
```

### Аниме.Релизы.РасписаниеРелизов

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%A0%D0%B5%D0%BB%D0%B8%D0%B7%D1%8B.%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%D0%A0%D0%B5%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2)

#### **>>> Данные по расписанию релизов на текущую дату**

Url: `/anime/schedule/now`

Реализация в библиотеке:
```python
data = api.Anime.Releases.ReleasesSchedule.now(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "today": [
    {
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      },
      "full_season_is_released": true,
      "published_release_episode": {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue"
      },
      "next_release_episode_number": 8
    }
  ],
  "tomorrow": [
    {
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      },
      "full_season_is_released": true,
      "published_release_episode": {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue"
      },
      "next_release_episode_number": 8
    }
  ],
  "yesterday": [
    {
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      },
      "full_season_is_released": true,
      "published_release_episode": {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue"
      },
      "next_release_episode_number": 8
    }
  ]
}
```

#### **>>> Данные по расписанию на текущую неделю**

Url: `/anime/schedule/week`

Реализация в библиотеке:
```python
data = api.Anime.Releases.ReleasesSchedule.week(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      },
      "full_season_is_released": true,
      "published_release_episode": {
        "id": "9b5e26ee-598f-4b8b-b77e-188d3e456318",
        "name": "Пролог",
        "ordinal": 12.5,
        "ending": {
          "start": 6,
          "stop": 125
        },
        "opening": {
          "start": 6,
          "stop": 125
        },
        "preview": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "hls_480": "string",
        "hls_720": "string",
        "hls_1080": "string",
        "duration": 1432,
        "rutube_id": "c6cc4d620b1d4338901770a44b3e82f4",
        "youtube_id": "dQw4w9WgXcQ",
        "updated_at": "2021-11-25T18:46:30+00:00",
        "sort_order": 12,
        "release_id": 9324,
        "name_english": "Prologue"
      },
      "next_release_episode_number": 8
    }
  ]
}
```

### Аниме.Торренты

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5.%D0%A2%D0%BE%D1%80%D1%80%D0%B5%D0%BD%D1%82%D1%8B)

#### **>>> Данные по торрентам**

Url: `/anime/torrents`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.torrents(
    page=1, # Номер страницы (Целое число). По умолчанию 1
    limit=10, # Ограничение на количество элементов (Целое число). По умолчанию 10
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "data": [
    {
      "id": 18523,
      "hash": "8a8fb94b1bd22b44a116336bab6bf209d0ac3a90",
      "size": 7356495551,
      "type": {
        "value": "BDRip",
        "description": "WEBRip"
      },
      "color": {
        "value": "8bit",
        "description": "8-bit"
      },
      "codec": {
        "value": "AV1",
        "label": "AVC",
        "description": "x264/AVC",
        "label_color": "#FFF",
        "label_is_visible": true
      },
      "label": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p]",
      "quality": {
        "value": "360p",
        "description": "1080p"
      },
      "magnet": "magnet:?xt=urn:btih:QPYNLG5Y2LA2KHB7SZCQF2W3...",
      "filename": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p].torrent",
      "seeders": 234,
      "bitrate": 3400,
      "leechers": 58,
      "sort_order": 2,
      "updated_at": "2021-09-22T16:20:38+00:00",
      "is_hardsub": true,
      "description": "1-17 + OVA(1-4)",
      "created_at": "2021-09-21T11:45:00+00:00",
      "completed_times": 13538,
      "torrent_members": [
        {
          "id": "6240acf7-4f62-4de9-9cc0-b3984ccc2b35",
          "role": {
            "value": "HEVC",
            "description": "HEVC"
          },
          "nickname": "Tuxoid",
          "external_url": "https://t.me/Animeshnik488",
          "user": {
            "id": 2346,
            "avatar": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "optimized": {
                "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
                "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
              }
            }
          }
        }
      ],
      "release": {
        "id": 7439,
        "type": {
          "value": "TV",
          "description": "ТВ"
        },
        "year": 2018,
        "name": {
          "main": "Мастера Меча Онлайн: Алисизация",
          "english": "Sword Art Online: Alicization",
          "alternative": "Война в Андерворлде, War of Underworld"
        },
        "alias": "sword-art-online-alicization",
        "season": {
          "value": "winter",
          "description": "Осень"
        },
        "poster": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        },
        "fresh_at": "2019-12-29T23:06:39+00:00",
        "created_at": "2019-12-29T23:06:39+00:00",
        "updated_at": "2023-08-20T15:08:20+00:00",
        "is_ongoing": false,
        "age_rating": {
          "value": "R0_PLUS",
          "label": "16+",
          "is_adult": false,
          "description": "Для людей, достигших возраста шестнадцати лет (16+)"
        },
        "publish_day": {
          "value": 1,
          "description": "Воскресенье"
        },
        "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
        "notification": "Серии выходят по воскресеньям",
        "episodes_total": 36,
        "external_player": "//kodik.info/serial/...",
        "is_in_production": false,
        "is_blocked_by_geo": false,
        "is_blocked_by_copyrights": false,
        "added_in_users_favorites": 25557,
        "average_duration_of_episode": 25,
        "added_in_planned_collection": 2457,
        "added_in_watched_collection": 467,
        "added_in_watching_collection": 346,
        "added_in_postponed_collection": 212,
        "added_in_abandoned_collection": 12
      }
    }
  ],
  "meta": {
    "pagination": {
      "total": 1704,
      "count": 10,
      "per_page": 10,
      "current_page": 5,
      "total_pages": 171,
      "links": {
        "previous": "/api/version/path-to-resource?page=1",
        "next": "/api/version/path-to-resource?page=3"
      }
    }
  }
}
```

#### **>>> Данные по торренту**

Url: `/anime/torrents/{hashOrId}`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.by_hash_or_id(
    hash_or_id=123456789, # ID или Hash торрента (Целое число или строка)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
{
  "id": 18523,
  "hash": "8a8fb94b1bd22b44a116336bab6bf209d0ac3a90",
  "size": 7356495551,
  "type": {
    "value": "BDRip",
    "description": "WEBRip"
  },
  "color": {
    "value": "8bit",
    "description": "8-bit"
  },
  "codec": {
    "value": "AV1",
    "label": "AVC",
    "description": "x264/AVC",
    "label_color": "#FFF",
    "label_is_visible": true
  },
  "label": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p]",
  "quality": {
    "value": "360p",
    "description": "1080p"
  },
  "magnet": "magnet:?xt=urn:btih:QPYNLG5Y2LA2KHB7SZCQF2W3...",
  "filename": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p].torrent",
  "seeders": 234,
  "bitrate": 3400,
  "leechers": 58,
  "sort_order": 2,
  "updated_at": "2021-09-22T16:20:38+00:00",
  "is_hardsub": true,
  "description": "1-17 + OVA(1-4)",
  "created_at": "2021-09-21T11:45:00+00:00",
  "completed_times": 13538,
  "torrent_members": [
    {
      "id": "6240acf7-4f62-4de9-9cc0-b3984ccc2b35",
      "role": {
        "value": "HEVC",
        "description": "HEVC"
      },
      "nickname": "Tuxoid",
      "external_url": "https://t.me/Animeshnik488",
      "user": {
        "id": 2346,
        "avatar": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "optimized": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
          }
        }
      }
    }
  ],
  "release": {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12
  }
}
```

#### **>>> Торрент файл по его hash или id**

Url: `/anime/torrents/{hashOrId}/file`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.file(
    hash_or_id=123456, # ID или Hash торрента (Целое число или строка)
    pk="passkey" # passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован). (Пока работает и пустой)
)
```

Возвращает котент файла-торрента (строка)

#### **>>> Данные по торрентам для релиза**

Url: `/anime/torrents/release/{releaseId}`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.by_release_id(
    release_id=123456, # ID релиза (Целое число)
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 18523,
    "hash": "8a8fb94b1bd22b44a116336bab6bf209d0ac3a90",
    "size": 7356495551,
    "type": {
      "value": "BDRip",
      "description": "WEBRip"
    },
    "color": {
      "value": "8bit",
      "description": "8-bit"
    },
    "codec": {
      "value": "AV1",
      "label": "AVC",
      "description": "x264/AVC",
      "label_color": "#FFF",
      "label_is_visible": true
    },
    "label": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p]",
    "quality": {
      "value": "360p",
      "description": "1080p"
    },
    "magnet": "magnet:?xt=urn:btih:QPYNLG5Y2LA2KHB7SZCQF2W3...",
    "filename": "Shaman King (2021) - AniLiberty.TOP [WEB-Rip 1080p].torrent",
    "seeders": 234,
    "bitrate": 3400,
    "leechers": 58,
    "sort_order": 2,
    "updated_at": "2021-09-22T16:20:38+00:00",
    "is_hardsub": true,
    "description": "1-17 + OVA(1-4)",
    "created_at": "2021-09-21T11:45:00+00:00",
    "completed_times": 13538,
    "torrent_members": [
      {
        "id": "6240acf7-4f62-4de9-9cc0-b3984ccc2b35",
        "role": {
          "value": "HEVC",
          "description": "HEVC"
        },
        "nickname": "Tuxoid",
        "external_url": "https://t.me/Animeshnik488",
        "user": {
          "id": 2346,
          "avatar": {
            "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
            "optimized": {
              "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
              "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
            }
          }
        }
      }
    ],
    "release": {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12
    }
  }
]
```

#### **>>> RSS лента последних торрентов**

Url: `/anime/torrents/rss`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.rss(
    limit=10, # Количество торрентов в выдаче. По умолчанию 10
    pk="passkey" # Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики. (По умолчанию пустой)
)
```

Возвращает контент XML документа (строка)

#### **>>> RSS лента торрентов релиза**

Url: `/anime/torrents/rss/release/{releaseId}`

Реализация в библиотеке:
```python
data = api.Anime.Torrents.rss_by_release_id(
    release_id=123465, # ID релиза (Целое число)
    pk="passkey" # Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики. (По умолчанию пустой)
)
```

Возвращает контент XML документа (строка)

## Приложение

### Приложение.Поиск

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.%D0%9F%D0%BE%D0%B8%D1%81%D0%BA)

#### **>>> Поиск релизов**

Url: `/app/search/releases`

Реализация в библиотеке:
```python
data = api.App.search(
    query="search auery", # Поисковая строка
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
) 
```

Пример возвращаемых данных:
```json
[
  {
    "id": 7439,
    "type": {
      "value": "TV",
      "description": "ТВ"
    },
    "year": 2018,
    "name": {
      "main": "Мастера Меча Онлайн: Алисизация",
      "english": "Sword Art Online: Alicization",
      "alternative": "Война в Андерворлде, War of Underworld"
    },
    "alias": "sword-art-online-alicization",
    "season": {
      "value": "winter",
      "description": "Осень"
    },
    "poster": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "fresh_at": "2019-12-29T23:06:39+00:00",
    "created_at": "2019-12-29T23:06:39+00:00",
    "updated_at": "2023-08-20T15:08:20+00:00",
    "is_ongoing": false,
    "age_rating": {
      "value": "R0_PLUS",
      "label": "16+",
      "is_adult": false,
      "description": "Для людей, достигших возраста шестнадцати лет (16+)"
    },
    "publish_day": {
      "value": 1,
      "description": "Воскресенье"
    },
    "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
    "notification": "Серии выходят по воскресеньям",
    "episodes_total": 36,
    "external_player": "//kodik.info/serial/...",
    "is_in_production": false,
    "is_blocked_by_geo": false,
    "is_blocked_by_copyrights": false,
    "added_in_users_favorites": 25557,
    "average_duration_of_episode": 25,
    "added_in_planned_collection": 2457,
    "added_in_watched_collection": 467,
    "added_in_watching_collection": 346,
    "added_in_postponed_collection": 212,
    "added_in_abandoned_collection": 12
  }
]
```

### Приложение.Статус

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81)

#### **>>> Статус API**

Url: `/app/status`

Реализация в библиотеке:
```python
data = api.App.status()
```

Пример возвращаемых данных:
```json
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
```

## Медиа

### Медиа.Промо

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0.%D0%9F%D1%80%D0%BE%D0%BC%D0%BE)

#### **>>> Список промо-материалов**

Url: `/media/promotions`

Реализация в библиотеке:
```python
data = api.Media.promotions(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "bad864a4-d1b9-473f-898f-da8ee800ef87",
    "url": "https://espritgames.ru/dragoncontract/promotions/getdragon",
    "url_label": "Перейти на сайт",
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "title": "Dragon Contract",
    "description": "ИСПЫТАЙ СВОЮ ПАМЯТЬ! Собери все пары карточек правильно, и получи дракона на старте!",
    "is_ad": true,
    "ad_erid": "string",
    "ad_origin": "string",
    "release": {
      "id": 7439,
      "type": {
        "value": "TV",
        "description": "ТВ"
      },
      "year": 2018,
      "name": {
        "main": "Мастера Меча Онлайн: Алисизация",
        "english": "Sword Art Online: Alicization",
        "alternative": "Война в Андерворлде, War of Underworld"
      },
      "alias": "sword-art-online-alicization",
      "season": {
        "value": "winter",
        "description": "Осень"
      },
      "poster": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      },
      "fresh_at": "2019-12-29T23:06:39+00:00",
      "created_at": "2019-12-29T23:06:39+00:00",
      "updated_at": "2023-08-20T15:08:20+00:00",
      "is_ongoing": false,
      "age_rating": {
        "value": "R0_PLUS",
        "label": "16+",
        "is_adult": false,
        "description": "Для людей, достигших возраста шестнадцати лет (16+)"
      },
      "publish_day": {
        "value": 1,
        "description": "Воскресенье"
      },
      "description": "Underworld - мир, ранее недоступный человеческому пониманию...",
      "notification": "Серии выходят по воскресеньям",
      "episodes_total": 36,
      "external_player": "//kodik.info/serial/...",
      "is_in_production": false,
      "is_blocked_by_geo": false,
      "is_blocked_by_copyrights": false,
      "added_in_users_favorites": 25557,
      "average_duration_of_episode": 25,
      "added_in_planned_collection": 2457,
      "added_in_watched_collection": 467,
      "added_in_watching_collection": 346,
      "added_in_postponed_collection": 212,
      "added_in_abandoned_collection": 12
    },
    "has_overlay": true
  }
]
```

### Медиа.Видеоконтент

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0.%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82)

#### **>>> Список видео-роликов**

Url: `/media/videos`

Реализация в библиотеке:
```python
data = api.Media.videos(
    limit=5, # Количество роликов в выдаче (Целое число). По умолчанию 5
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": 57,
    "url": "https://www.youtube.com/watch?v=8f6FpV4sB0I",
    "title": "ТОП 10 САМЫХ ОЖИДАЕМЫХ АНИМЕ ОСЕНИ 2021",
    "views": 34456,
    "image": {
      "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
      "optimized": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
      }
    },
    "comments": 532,
    "video_id": "8f6FpV4sB0I",
    "created_at": "2021-09-22T16:20:38+00:00",
    "updated_at": "2021-09-28T19:40:26+00:00",
    "is_announce": true,
    "origin": {
      "id": "e8fd32be-7f14-4c02-bf00-dbd26ecabfdb",
      "url": "https://www.youtube.com/playlist?list=PL8_g6JPJBRglxkyQfNGugDyyQP11hL0-Q",
      "type": {
        "value": "YOUTUBE_PLAYLIST",
        "description": "YouTube плейлист"
      },
      "title": "Анонсы аниме-сезонов",
      "description": "Плейлист с анонсами",
      "is_announce": true
    }
  }
]
```

## Команды

[Ссылка на документацию](https://aniliberty.top/api/docs/v1#/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B)

#### **>>> Список команд АниЛибрии**

Url: `/teams/`

Реализация в библиотеке:
```python
data = api.Teams.teams(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "string",
    "title": "string",
    "sort_order": 0,
    "description": "string"
  }
]
```

#### **>>> Список ролей**

Url: `/teams/roles`

Реализация в библиотеке:
```python
data = api.Teams.roles(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "string",
    "title": "string",
    "color": "string",
    "sort_order": 0
  }
]
```

#### **>>> Список анилибрийцев**

Url: `/teams/users`

Реализация в библиотеке:
```python
data = api.Teams.users(
    include=['id'], # Список включаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
    exclude=['id'] # Список исключаемых полей. Поддерживается вложенность через точку. (Пример: id, type.genres) (По умолчанию пустой список - не учитывается)
)
```

Пример возвращаемых данных:
```json
[
  {
    "id": "string",
    "nickname": "string",
    "is_intern": true,
    "sort_order": 0,
    "is_vacation": true,
    "team": {
      "id": "string",
      "title": "string",
      "sort_order": 0,
      "description": "string"
    },
    "user": {
      "id": 0,
      "nickname": "string",
      "avatar": {
        "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
        "optimized": {
          "preview": "/...GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)",
          "thumbnail": "/.../GoH5bzLFS7A21DzacgUApScj7qJY1iMz.(jpg|webp)"
        }
      }
    },
    "roles": [
      {
        "id": "string",
        "title": "string",
        "color": "string",
        "sort_order": 0
      }
    ]
  }
]
```