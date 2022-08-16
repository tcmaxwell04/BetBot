import requests
import pandas as pd
from pandas import DataFrame, Series
import json


#API Key
API_KEY = 'e5e0e29848503955751461d8ea3f3e74'

SPORT = '/americanfootball_ncaaf'

REGIONS = 'us'

MARKETS = 'h2h,spreads,totals'

ODDS_FORMAT = 'american'

DATE_FORMAT = 'iso'

BOOKMAKERS = 'fanduel'


odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
        'bookmakers': BOOKMAKERS,
    }
)
odds_list = json.loads(odds_response.text)
odds_df = DataFrame(odds_list)
odds_df.head()