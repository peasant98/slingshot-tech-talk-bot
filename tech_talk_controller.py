import requests
import os
import numpy as np


class TechTalkNewsController():
    def __init__(self):
        self.base_url = "https://rapidapi.p.rapidapi.com/api/search/NewsSearchAPI"
        rapid_api_key = os.getenv('RAPID_API_KEY')

        self.headers = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': rapid_api_key
        }

    def get_tech_news(self, keyword, pagesize: int = 10):
        querystring = {"pageSize": pagesize,
                       "q": keyword,
                       "autoCorrect": "true",
                       "pageNumber": "1",
                       "toPublishedDate": "null",
                       "fromPublishedDate": "null"}

        response = requests.request("GET", self.base_url, headers=self.headers, params=querystring)
        response_json = response.json()
        values = response_json['value']
        value = np.random.choice(values)
        brief_description = value['description'].split('.')[0]
        return value['url'], value['title'], brief_description
