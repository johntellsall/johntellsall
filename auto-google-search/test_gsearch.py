import json
import sys
import gsearch
import os
import google_custom_search


# def test_format_query():
#     query = {
#         "search": ["flask", "django"],
#         "location": ["remote", "puerto rico"],
#         "sites": ["stackoverflow.com", "github.com"],
#         "require": ["django"],
#     }
#     result = gsearch.format_query(query)
#     assert (
#         '("flask" OR "django") AND ("remote" OR "puerto rico")'
#         ' AND ("site:stackoverflow.com" OR "site:github.com")'
#         ' AND "django"'
#     ) == result


def test_google_custom_search():
    ENGINE_ID = os.environ["GOOGLE_ENGINE_ID"]
    API_KEY = os.environ["GOOGLE_API_KEY"]
    
    google = google_custom_search.CustomSearch(apikey=API_KEY, engine_id=ENGINE_ID)

    query = ('("data science") AND ("los angeles" OR "remote")'
             ' AND ("site:boards.greenhouse.io")')

    results = google.search(query)

    assert len(results) > 0
    assert results[0].title > ''
    assert 'boards.greenhouse.io' in results[0].url