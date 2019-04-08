# toi_sc.py : Scraper
# v07 : 2019/02/23
import sys
import requests
from bs4 import BeautifulSoup
import json
import re

class Cuisine:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


class Scraper:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug('__init__() called.')

    def get_html(self, url):
        self.logger.debug('get_html() called.')
        self.logger.debug('url: ' + url)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as err:
            self.logger.error(err.args)
            self.logger.error(type(err))
            sys.exit()
        else:
            status_code = str(response.status_code)
            self.logger.debug('status_code: ' + status_code)
            if status_code != '200':
                self.logger.error('status_code: ' + status_code)
                sys.exit()
        return response.text

    def get_ingredients(self, html):
        self.logger.debug('get_ingredients() called.')
        soup = BeautifulSoup(html, "html.parser")

        # find <script type="application/ld+json"> tags
        scr_all = soup.find_all('script',type='application/ld+json')
        self.logger.debug('scr_all: ' + str(scr_all))

        # The contents of script tag are json format.
        for scr_01 in scr_all:
            scr_01 = json.loads(scr_01.text)
        self.logger.debug('--scr_01--')
        self.logger.debug("{}".format(json.dumps(scr_01, \
                          indent=4,ensure_ascii=False)))

        # Get cuisine name
        cuisine_name = str(scr_01['name'])

        # Get cuisine ingredients
        ingredients = ''
        for val in scr_01['recipeIngredient']:
            self.logger.debug(val)
            val2 = val.strip()
            if not val2:
                continue
            mt = re.match(r'^[【|◉]|○|※|〔|《',val) # remove category words
            if mt is None:
                # remove bullet, additional information, space, ...
                val3 = re.sub('●|◆|◇|☆|★|◎|△|A|♡|▲|・|･|\*','',val)
                val4 = re.split(' |（|\(',val3)
                val5 = [s for s in val4 if s != '']
                if val5:
                    word = val5[0].strip()
                    self.logger.debug('ingredient: ' + word)
                ingredients += word + ','
        ingredients = ingredients[:-1]

        # Store Cuisine object
        cuisine = Cuisine(cuisine_name, ingredients)
        return cuisine
