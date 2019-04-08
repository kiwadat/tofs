# toi_ccd.py : Collect and Cleansing Data
# v08 : 2019/04/07
import os
import sys
import argparse
import time
import pandas as pd
from toi_en import EnvDef
from toi_sc import Scraper
from toi_fa import FileAccess
from toi_lm import Lemmatizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('page', help='page data csv file')
    parser.add_argument('sline', type=int, \
                        help='starting line of testing data')
    parser.add_argument('-l', '--local', action='store_true', \
                        help='run locally')
    args = parser.parse_args()

    # initialize
    en = EnvDef()
    en.logger.info('========== ' + __file__ + ' start ==========')
    scraper = Scraper(en.logger)
    pfile = en.d_def + args.page
    rdata = pd.read_csv(pfile, comment='#', header=None, dtype='object')
    en.logger.debug(rdata)
    fa = FileAccess(en.logger)

    # get recipe data
    ingredients_list = []
    country_list = []
    if args.local:
        if not os.path.isfile(en.f_toi_work1):
            print('Error: ' + en.f_toi_work1 + ' not found.')
        if not os.path.isfile(en.f_toi_target):
            print('Error: ' + en.f_toi_target + ' not found.')
        ingredients_list = fa.read_csv(en.f_toi_work1)
        country_list = fa.read_csv(en.f_toi_target)
    else:
        en.logger.info('---- get recipe data ----')
        df = pd.DataFrame(rdata)
        en.logger.debug('row: ' + str(df.shape[0]))
        cuisine_list = []  # notice: not used
        for index, row in df.iterrows():
            time.sleep(0.1)
            country = row[2]    # country name (target)
            country_list.append(country)
            num = row[4]        # recipe page number
            en.logger.debug('country=' + country + ', num=' + num)
            url = en.d_url[row[1]] + num
            en.logger.debug('==== url: ' + url + ' ====')
            html = scraper.get_html(url)
            cuisine = scraper.get_ingredients(html)
            cuisine_list.append(cuisine)
            ingredients_list.append(cuisine.ingredients)
            lctr = '{:04d}'.format(index + 1)
            en.logger.debug(lctr + ': ' + cuisine.name)
            en.logger.debug(cuisine.ingredients)

        # --- all data (training data + testing data) ---
        en.logger.info('make all data')
        # store recipe data (features: ingredients, target: country)
        fa.write_csv(en.f_toi_work1, ingredients_list)
        fa.write_csv(en.f_toi_target, country_list)

    # remove stop words
    en.logger.info('- remove stop words')
    cl = Lemmatizer(en, fa)
    cl.remove_stop_words(en.f_toi_work1, en.f_toi_work2)

    if en.l_eng == True:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_toi_work2, en.f_toi_work3)
        # translate
        en.logger.info('- translate')
        cl.translate(en.f_toi_work3, en.f_toi_feature)
    else:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_toi_work2, en.f_toi_feature)

    # --- training data ---
    en.logger.info('make training data')
    # store recipe data (features: ingredients, target: country)
    boundary = args.sline
    lines = boundary - 1
    fa.write_csv(en.f_train_work1, ingredients_list[0:lines])
    fa.write_csv(en.f_train_target, country_list[0:lines])

    # remove stop words
    en.logger.info('- remove stop words')
    cl.remove_stop_words(en.f_train_work1, en.f_train_work2)

    if en.l_eng == True:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_train_work2, en.f_train_work3)
        # translate
        en.logger.info('- translate')
        cl.translate(en.f_train_work3, en.f_train_feature)
    else:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_train_work2, en.f_train_feature)

    # --- testing data ---
    en.logger.info('make testing data')
    # store recipe data (features: ingredients, target: country)
    fa.write_csv(en.f_test_work1, ingredients_list[boundary - 1:])
    fa.write_csv(en.f_test_target, country_list[boundary - 1:])

    # remove stop words
    en.logger.info('- remove stop words')
    cl.remove_stop_words(en.f_test_work1, en.f_test_work2)

    # lemmatize
    if en.l_eng == True:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_test_work2, en.f_test_work3)
        # translate
        en.logger.info('- translate')
        cl.translate(en.f_test_work3, en.f_test_feature)
    else:
        # lemmatize
        en.logger.info('- lemmatize')
        cl.lemmatize(en.f_test_work2, en.f_test_feature)

if __name__ == '__main__':
    main()
