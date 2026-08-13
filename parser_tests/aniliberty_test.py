from time import sleep

def api_sync_test(delay: float, login: str, password: str, proxy: str | None = None):
    from src.anime_parsers_ru.api_aniliberty import AnilibertyAPI
    from src.anime_parsers_ru import errors
    
    try_errors = 0
    try_success = 0

    try:
        api = AnilibertyAPI(proxy=proxy)
    except Exception as ex:
        raise RuntimeError(f"Can't initialize Api! Exception: {ex}")
    else:
        try_success += 1
        print('[OK] Api init')

    try:
        api.login(login, password)
    except Exception as ex:
        raise RuntimeError(f"Can't login! Exception: {ex}")
    else:
        try_success += 1
        print('[OK] Login')

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (without any params). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (without any params)")

    sleep(delay)
    
    try:
        data = api.Anime.Catalog.catalog_releases(page=3, limit=1, genres=[AnilibertyAPI.Genres.Исекай])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if not any([x['id'] == AnilibertyAPI.Genres.Исекай._r for x in data['data'][0]['genres']]):
            raise AssertionError(f"Isekai genre is not found in release data. Genres: {data['data'][0]['genres']}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (Isekai). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (Isekai)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, genres=[AnilibertyAPI.Genres.Демоны], types=[AnilibertyAPI.Types.TV])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if not any([x['id'] == AnilibertyAPI.Genres.Демоны._r for x in data['data'][0]['genres']]):
            raise AssertionError(f"Demons genre is not found in release data. Genres: {data['data'][0]['genres']}")
        if data['data'][0]['type']['value'] != AnilibertyAPI.Types.TV._r:
            raise AssertionError(f'Type of release is not TV. Type: {data['data'][0]['type']['value']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (demons tv). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (demons tv)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, seasons=['winter', 'summer'], from_year=2019, to_year=2019)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if data['data'][0]['year'] != 2019:
            raise AssertionError(f'Year of release is not 2019. Year: {data['data'][0]['year']}')
        if data['data'][0]['season']['value'] not in ['winter', 'summer']:
            raise AssertionError(f'Season is not winter or summer. Season: {data['data'][0]['season']['value']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (2019 winter & summer). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (2019 winter & summer)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, search="Мастера меча онлайн", to_year=2022, sorting=AnilibertyAPI.Sorting.RATING_DESC)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if data['data'][0]['year'] > 2022:
            raise AssertionError(f'Year of release is greater than 2022. Year: {data['data'][0]['year']}')
        if 'sword-art-online' not in data['data'][0]['alias']:
            raise AssertionError(f'Alias does not contain sword-art-online. Alias: {data['data'][0]['alias']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (SAO to 2022 sort). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (SAO to 2022 sort)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, publish_statuses=['IS_ONGOING'])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if not data['data'][0]['is_ongoing']:
            raise AssertionError(f'Publish status is not ongoing. Is ongoing: {data['data'][0]['is_ongoing']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (ongoing). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (ongoing)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, production_statuses=['IS_NOT_IN_PRODUCTION'], sorting=AnilibertyAPI.Sorting.FRESH_AT_DESC, age_ratings=[AnilibertyAPI.AgeRatings.R12_PLUS])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if data['data'][0]['is_in_production']:
            raise AssertionError(f'Production status is "in production". Is in production: {data['data'][0]['is_in_production']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (not in production r12). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (not in production r12)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, include=['id', 'year'])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if list(data['data'][0].keys()) != ['id', 'year']:
            raise AssertionError(f'Got keys other than specified in include (id, year). Keys: {data['data'][0].keys()}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (include id, year). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (include id, year)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.catalog_releases(page=1, limit=1, exclude=['id', 'year'])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError(f'Length of data["data"] = 0')
        if 'id' in data['data'][0].keys() or 'year' in data['data'][0].keys():
            raise AssertionError(f'Got keys than specified in exclude (id, year). Keys: {data['data'][0].keys()}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog (exclude id, year). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog (exclude id, year)")

    sleep(delay)

    try:
        data = api.Anime.Catalog.References.age_ratings()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        vals = [x['value'] for x in data]
        if set(vals) != set(AnilibertyAPI.AgeRatings.ratings):
            raise AssertionError(f"Returned list of age ratings is not equal to AnilibertyAPI.AgeRatings.ratings. Returned list: {vals}. Local: {AnilibertyAPI.AgeRatings.ratings}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references age ratings. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references age ratings")

    sleep(delay)

    try:
        data = api.Anime.Catalog.References.genres()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        for x in data:
            if x['name'] not in AnilibertyAPI.Genres.genres.keys():
                raise AssertionError(f"Genre \"{x['name']}\" is not in AnilibertyAPI.Genres.genres.keys")
            if AnilibertyAPI.Genres.genres[x['name']] != x['id']:
                raise AssertionError(f"Genre \"{x['name']}\" id from server ({x['id']}) is not equal to local ({AnilibertyAPI.Genres.genres[x['name']]})")
        subtypes = sorted([(x.__name__, x._r) for x in AnilibertyAPI.Genres._Genre.__subclasses__()], key=lambda x: x[1])
        vals = sorted([(x['name'].replace(' ', '_').replace('-', '_'), x['id']) for x in data], key=lambda x: x[1])
        if vals != subtypes:
            raise AssertionError(f"Returned list of genres is not equal to local\nReturned: {vals}\nLocal: {subtypes}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references genres. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references genres")

    sleep(delay)
    
    try:
        data = api.Anime.Catalog.References.production_statuses()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if set([x['value'] for x in data]) != set(['IS_IN_PRODUCTION', 'IS_NOT_IN_PRODUCTION']):
            raise AssertionError(f'Returned data of production statuses is not equal to local preset.\nReturned: {[x['value'] for x in data]}\nLocal preset: {['IS_IN_PRODUCTION', 'IS_NOT_IN_PRODUCTION']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references production statuses. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references production statuses")

    sleep(delay)

    try:
        data = api.Anime.Catalog.References.publish_statuses()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if set([x['value'] for x in data]) != set(['IS_ONGOING', 'IS_NOT_ONGOING']):
            raise AssertionError(f'Returned data of publish statuses is not equal to local preset.\nReturned: {[x['value'] for x in data]}\nLocal preset: {['IS_ONGOING', 'IS_NOT_ONGOING']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references publish statuses. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references publish statuses")
    
    sleep(delay)

    try:
        data = api.Anime.Catalog.References.seasons()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if set([x['value'] for x in data]) != set(['winter', 'summer', 'spring', 'autumn']):
            raise AssertionError(f'Returned data of seasons is not equal to local preset.\nReturned: {[x['value'] for x in data]}\nLocal preset: {['winter', 'summer', 'spring', 'autumn']}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references seasons. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references seasons")
    
    sleep(delay)

    try:
        data = api.Anime.Catalog.References.sorting()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if set([x['value'] for x in data]) != set([x.__name__ for x in AnilibertyAPI.Sorting._Sort.__subclasses__()]):
            raise AssertionError(f'Returned data of sorting is not equal to list of subclasses.\nReturned: {[x['value'] for x in data]}\nLocal preset: {[x.__name__ for x in AnilibertyAPI.Sorting._Sort.__subclasses__()]}')
        if set([x['value'] for x in data]) != set(AnilibertyAPI.Sorting.sorts):
            raise AssertionError(f'Returned data of sorting is not equal to local list.\nReturned: {[x['value'] for x in data]}\nLocal preset: {AnilibertyAPI.Sorting.sorts}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references sorting. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references sorting")
    
    sleep(delay)

    try:
        data = api.Anime.Catalog.References.types()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if set([x['value'] for x in data]) != set([x.__name__ for x in AnilibertyAPI.Types._Type.__subclasses__()]):
            raise AssertionError(f'Returned data of types is not equal to list of subclasses.\nReturned: {[x['value'] for x in data]}\nLocal preset: {[x.__name__ for x in AnilibertyAPI.Types._Type.__subclasses__()]}')
        if set([x['value'] for x in data]) != set(AnilibertyAPI.Types.types):
            raise AssertionError(f'Returned data of types is not equal to local list.\nReturned: {[x['value'] for x in data]}\nLocal preset: {AnilibertyAPI.Types.types}')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references types. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references types")
    
    sleep(delay)

    try:
        data = api.Anime.Catalog.References.years()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Catalog references years. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Catalog references years")
    
    sleep(delay)

    try:
        data = api.Anime.Franchises.franchises()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchises (no include/exclude). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchises (no include/exclude)")
    
    sleep(delay)

    try:
        data = api.Anime.Franchises.franchises(include=['id', 'name'])
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
        if set(list(data[0].keys())) != set(['id', 'name']):
            raise AssertionError(f"Returned data contains keys other than specified in include. Specified: ['id', 'name']. Returned: {list(data[0].keys())}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchises (include id, name). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchises (include id, name)")

    sleep(delay)

    try:
        data = api.Anime.Franchises.franchises(exclude=['id', 'name'])
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
        if 'id' in list(data[0].keys()) or 'name' in list(data[0].keys()):
            raise AssertionError(f"Returned data contains keys that were specified in exclude. Specified: ['id', 'name']. Returned: {list(data[0].keys())}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchises (exclude id, name). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchises (exclude id, name)")
    
    sleep(delay)

    try:
        data = api.Anime.Franchises.franchise_by_id('5e99a1ff-e7b7-400a-8e56-b01aa572bfb7')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchise by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchise by id")
    
    sleep(delay)

    try:
        data = api.Anime.Franchises.random(limit=2)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchises random. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchises random")
    
    sleep(delay)

    try:
        data = api.Anime.Franchises.franchises_by_release_id('9067')
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Franchises by release id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Franchises by release id")
    
    sleep(delay)

    try:
        data = api.Anime.Genres.genres()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Genres. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Genres")
    
    sleep(delay)

    try:
        data = api.Anime.Genres.genre_by_id(AnilibertyAPI.Genres.Вампиры)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['id'] != AnilibertyAPI.Genres.Вампиры._r:
            raise AssertionError(f"Id of returned genre is not equal to local id. Returned: {data['id']}. Local: {AnilibertyAPI.Genres.Вампиры._r}")
        if data['name'] != 'Вампиры':
            raise AssertionError(f"Name of returned genre is not equal to requested 'Вампиры'. Returned: {data['name']}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Genres genre by id vampires. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Genres genre by id vampires")
    
    sleep(delay)

    try:
        data = api.Anime.Genres.random_genres(limit=2)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Genres random genres. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Genres random genres")
    
    sleep(delay)

    try:
        data = api.Anime.Genres.releases_by_genre_id(AnilibertyAPI.Genres.Комедия, limit=1)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError("Length of data['data'] = 0")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Genres releases by genre id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Genres releases by genre id")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.latest(limit=1)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases latest. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases latest")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.random(limit=1)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases random. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases random")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.recommended(8632, limit=1)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases random. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases random")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.releases_list(ids=[8632, 9067])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['data'][0]['id'] != 8632 and data['data'][0]['id'] != 9067:
            raise AssertionError(f"Returned release (0) id is not in specified list. Returned (0) id: {data['data'][0]['id']}. Specified: [8632, 9067]")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases releases list ids. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases releases list ids")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.releases_list(aliases=['dr-stone-science-future-part-3', 'code-geass-hangyaku-no-lelouch-r2'])
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['data'][0]['alias'] != 'dr-stone-science-future-part-3' and data['data'][0]['alias'] != 'code-geass-hangyaku-no-lelouch-r2':
            raise AssertionError(f"Returned release (0) alias is not in specified list. Returned (0) alias: {data['data'][0]['alias']}. Specified: ['dr-stone-science-future-part-3', 'code-geass-hangyaku-no-lelouch-r2']")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases releases list aliases. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases releases list aliases")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.by_id(8632)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['id'] != 8632:
            raise AssertionError(f"Returned release id \"{data['id']}\" is not equal to requested 8632")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases release by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases release by id")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.by_alias('dr-stone-science-future-part-3')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['alias'] != 'dr-stone-science-future-part-3':
            raise AssertionError(f"Returned release alias \"{data['alias']}\" is not equal to requested 'dr-stone-science-future-part-3'")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases release by alias. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases release by alias")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.members_by_id_or_alias(8632)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases members by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases members by id")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.members_by_id_or_alias('dr-stone-science-future-part-3')
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases members by alias. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases members by alias")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.episodes_timecodes_by_id_or_alias(8632)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases episodes timecodes by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases episodes timecodes by id")
    
    sleep(delay)
    
    try:
        data = api.Anime.Releases.episodes_timecodes_by_id_or_alias('dr-stone-science-future-part-3')
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases episodes timecodes by alias. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases episodes timecodes by alias")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.Episodes.episode_by_id('a27be410-409e-45bb-a068-3e60fdaf2e66')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases.Episodes by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases.Episodes by id")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.Episodes.episode_timecodes('a27be410-409e-45bb-a068-3e60fdaf2e66')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except errors.NoResults:
        try_success += 1
        print("[OK] Releases.Episodes timecodes by id (No results because user did not watch this episode)")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases.Episodes timecodes by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases.Episodes timecodes by id")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.ReleasesSchedule.now()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases.ReleasesSchedule now. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases.ReleasesSchedule now")
    
    sleep(delay)

    try:
        data = api.Anime.Releases.ReleasesSchedule.week()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Releases.ReleasesSchedule week. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Releases.ReleasesSchedule week")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.torrents(limit=1)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if len(data['data']) == 0:
            raise AssertionError('Length of data[\'data\'] = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents torrents. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents torrents")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.by_hash_or_id(39480)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents by id")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.by_hash_or_id('fb47b073d35467e48b4e423fac7a414bba99cc21')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents by hash. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents by hash")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.file(39480)
        if type(data) != str:
            raise AssertionError(f"Type of data is not str. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents file by id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents file by id")
    
    sleep(delay)
    
    try:
        data = api.Anime.Torrents.file('fb47b073d35467e48b4e423fac7a414bba99cc21')
        if type(data) != str:
            raise AssertionError(f"Type of data is not str. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents file by hash. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents file by hash")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.by_release_id(10233)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
        if len(data) == 0:
            raise AssertionError('Length of data = 0')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents by release id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents by release id")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.rss(limit = 1)
        if type(data) != str:
            raise AssertionError(f"Type of data is not str. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents rss. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents rss")
    
    sleep(delay)

    try:
        data = api.Anime.Torrents.rss_by_release_id(10233)
        if type(data) != str:
            raise AssertionError(f"Type of data is not str. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Torrents rss by release id. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Torrents rss by release id")
    
    sleep(delay)

    try:
        data = api.App.search('Кулинарные скитания')
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] App.Search. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] App.Search")
    
    sleep(delay)

    try:
        data = api.App.status()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if not data['is_alive']: # Хз как это должно получится что запрос проходит но апи мертв, но допустим
            raise AssertionError("Api status \'is_alive\' is false")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] App.Status. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] App.Status")
    
    sleep(delay)

    try:
        data = api.Media.videos(limit=1)
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Media.Videos. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Media.Videos")
    
    sleep(delay)

    try:
        data = api.Media.promotions()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Media.Promotions. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Media.Promotions")
    
    sleep(delay)

    try:
        data = api.Teams.teams()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Teams teams. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Teams teams")
    
    sleep(delay)

    try:
        data = api.Teams.roles()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Teams roles. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Teams roles")
    
    sleep(delay)

    try:
        data = api.Teams.users()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Teams users. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Teams users")
    
    sleep(delay)

    # Для данных пользователя проверок на "правильность" запрошенного контента не будет
    # т.к. нельзя гарантировать наличие таковых в библиотеках пользователя
    # Поэтому просто проверка работоспособности эндпоинта

    try:
        data = api.User.Collections.ids()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections ids. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections ids")
    
    sleep(delay)

    try:
        data = api.User.Collections.releases(AnilibertyAPI.CollectionTypes.WATCHED)
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections releases watched (type). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections releases watched (type)")
    
    sleep(delay)

    try:
        data = api.User.Collections.releases('ABANDONED')
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections releases abandoned (str). Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections releases abandoned (str)")
    
    sleep(delay)

    try:
        api.User.Collections.add_release(10233, AnilibertyAPI.CollectionTypes.POSTPONED)
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections add release. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections add release")
    
    sleep(delay)

    try:
        api.User.Collections.remove_release(10233)
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections remove release. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections remove release")
    
    sleep(delay)

    try:
        data = api.User.Collections.References.age_ratings()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections.References age_ratings. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections.References age_ratings")
    
    sleep(delay)

    try:
        data = api.User.Collections.References.genres()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections.References genres. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections.References genres")
    
    sleep(delay)

    try:
        data = api.User.Collections.References.types()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections.References types. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections.References types")
    
    sleep(delay)

    try:
        data = api.User.Collections.References.years()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Collections.References years. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Collections.References years")
    
    sleep(delay)

    try:
        data = api.User.Favorites.ids()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites ids. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites ids")
    
    sleep(delay)

    try:
        data = api.User.Favorites.releases()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites releases. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites releases")
    
    sleep(delay)

    try:
        data = api.User.Favorites.add_release(10233)
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites add_release. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites add_release")
    
    sleep(delay)

    try:
        data = api.User.Favorites.remove_release(10233)
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites remove_release. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites remove_release")
    
    sleep(delay)

    try:
        data = api.User.Favorites.References.age_ratings()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites.References age_ratings. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites.References age_ratings")
    
    sleep(delay)
    
    try:
        data = api.User.Favorites.References.genres()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites.References genres. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites.References genres")
    
    sleep(delay)
    
    try:
        data = api.User.Favorites.References.types()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites.References types. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites.References types")
    
    sleep(delay)
    
    try:
        data = api.User.Favorites.References.years()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites.References years. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites.References years")
    
    sleep(delay)

    try:
        data = api.User.Favorites.References.sorting()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Favorites.References sorting. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Favorites.References sorting")
    
    sleep(delay)

    try:
        data = api.User.profile()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
        if data['login'] != login:
            raise AssertionError(f'Returned login \"{data['login']}\" is not equal to login used to authenticate \"{login}\"')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User profile. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User profile")
    
    sleep(delay)

    try:
        data = api.User.Views.history()
        if type(data) != dict:
            raise AssertionError(f"Type of data is not dict. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Views history. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Views history")
    
    sleep(delay)

    try:
        data = api.User.Views.timecodes('2025-05-12T07:20:50.52Z')
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Views timecodes. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Views timecodes")
    
    sleep(delay)

    try:
        data = api.User.Views.update_timecode(release_episode_id='a27be410-409e-45bb-a068-3e60fdaf2e66', time=123, is_watched=False)
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Views update_timecode. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Views update_timecode")
    
    sleep(delay)

    try:
        data = api.User.Views.delete_timecode(release_episode_id='a27be410-409e-45bb-a068-3e60fdaf2e66')
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] User.Views delete_timecode. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] User.Views delete_timecode")
    
    sleep(delay)

    try:
        data = api.Media.vasts()
        if type(data) != list:
            raise AssertionError(f"Type of data is not list. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Media vasts. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Media vasts")
    
    sleep(delay)

    try:
        data = api.Media.manifest_xml()
        if type(data) != str:
            raise AssertionError(f"Type of data is not str. Type: {type(data)}")
    except Exception as ex:
        try_errors += 1
        print(f"[FAIL] Media manifest_xml. Exception: {ex}")
    else:
        try_success += 1
        print("[OK] Media manifest_xml")
    
    sleep(delay)

    try:
        api.logout()
    except Exception as ex:
        raise RuntimeError(f"Can't logout! Exception: {ex}")
    else:
        try_success += 1
        print('[OK] Logout')

    return (try_errors, try_success)
