import os
import pytest

import google_custom_search
from dotenv import load_dotenv


load_dotenv()
ENGINE_ID = os.environ.get("GOOGLE_ENGINE_ID")
API_KEY = os.environ.get("GOOGLE_API_KEY")


@pytest.mark.skipif(not ENGINE_ID or not API_KEY, reason="API keys not set")
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