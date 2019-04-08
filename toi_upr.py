# toi_upr.py : Utility for Collect Data & Predict
# v08 : 2019/04/06
import sys
from sklearn.externals import joblib
from toi_en import EnvDef
from toi_fa import FileAccess
from toi_sc import Scraper
from toi_lm import Lemmatizer
from toi_cp import Corpus
from toi_cl import Classifier

def main():
    if len(sys.argv) != 2:
        errmsg = 'Usage: ' + __file__ + ' pagenumber'
        sys.exit(1)

    # initialize
    en = EnvDef()
    en.logger.info('========== ' + __file__ + ' start ==========')
    scraper = Scraper(en.logger)
    url = en.d_url['cp'] + sys.argv[1]
    en.logger.debug('url: ' + url)

    # scraping
    html = scraper.get_html(url)
    cuisine = scraper.get_ingredients(html)
    ingredients_list = [cuisine.ingredients]
    en.logger.info('cuisine: ' + cuisine.name)
    en.logger.info('ingredients: ' + cuisine.ingredients)

    prefix = 'upr'
    filepath = en.d_data + prefix + en.f_work1_suffix
    fa = FileAccess(en.logger)
    fa.write_csv(filepath, ingredients_list)
    #fa.show_file(filepath, '--original--')

    lm = Lemmatizer(en, fa)
    filepath2 = en.d_data + prefix + en.f_work2_suffix
    lm.remove_stop_words(filepath, filepath2)
    #fa.show_file(filepath2, '--remove_stop_words--')

    filepath3 = en.d_data + prefix + en.f_work3_suffix
    lm.lemmatize(filepath2, filepath3)
    fa.show_file(filepath3, '--lemmatize--')

    if en.l_eng == True:
        filepath4 = en.d_data + prefix + en.f_feature_suffix
        lm.translate(filepath3, filepath4)
        fa.show_file(filepath4, '--translate--')

    ans = input('Do you want to continue? (y/n) >> ')
    if ans == 'n':
        print('Stopped.')
        sys.exit(1)

    # vectorize
    en.logger.info('---- vectorize ----')
    if en.l_eng == True:
        f_csv = filepath4
    else:
        f_csv = filepath3

    f = open(f_csv, 'r')
    f_list = fa.make_nested_list(f)
    cp = Corpus(en.logger)
    dic = cp.load_corpus(en.f_corpus)
    dense_all = cp.make_dense(f_list, dic)

    # predict
    en.logger.info('---- predict ----')
    cl = Classifier(en.logger)

    scikit_ver = joblib.__version__
    filepath = en.f_model_prefix + '{ver}.pkl'.format(ver=scikit_ver)
    en.logger.info('filepath: ' + filepath)
    #filepath = en.d_data + sys.argv[2]
    y_pred = cl.predict(dense_all, filepath)

    filepath = en.d_def + en.f_country
    f_dic2 = open(filepath, 'r')
    t_dic = dict((line.strip().split(',') for line in f_dic2))
    for key, cid in t_dic.items():
        if cid == str(y_pred[0]):
            print(key)

if __name__ == '__main__':
    main()
