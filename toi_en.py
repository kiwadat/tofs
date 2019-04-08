# toi_en.py : Environment Definition
# v08 : 2019/03/02
import logging.config

class EnvDef:
    # for directory, url
    d_log = './log/'
    d_def = './def/'
    d_data = './data/'
    d_url = {'cp': 'http://xxx/recipe/'}

    # for language
    l_eng = True

    # for def
    f_logfile = d_def + 'toi_logger.conf'
    f_stopwords = d_def + 'toi_stopwords.csv'
    f_lemma = d_def + 'toi_lemma.csv'
    f_dic = d_def + 'toi_dic.csv'
    f_country = 'toi_country.csv'

    # for data
    f_toi_work1 = d_data + 'toi_work1.csv'
    f_toi_work2 = d_data + 'toi_work2.csv'
    f_toi_work3 = d_data + 'toi_work3.csv'
    f_toi_feature = d_data + 'toi_feature.csv'
    f_toi_target = d_data + 'toi_target.csv'

    f_train_work1 = d_data + 'train_work1.csv'
    f_train_work2 = d_data + 'train_work2.csv'
    f_train_work3 = d_data + 'train_work3.csv'
    f_train_feature = d_data + 'train_feature.csv'
    f_train_target = d_data + 'train_target.csv'

    f_test_work1 = d_data + 'test_work1.csv'
    f_test_work2 = d_data + 'test_work2.csv'
    f_test_work3 = d_data + 'test_work3.csv'
    f_test_feature = d_data + 'test_feature.csv'
    f_test_target = d_data + 'test_target.csv'

    f_corpus = d_data + 'toi_corpus.txt'
    f_corpus_csv = d_data + 'toi_corpus.csv'

    f_dense_suffix = '_dense.pkl'
    f_vec_suffix = '_vec.pkl'
    f_model_prefix = d_data + 'toi_model_'

    f_work1_suffix = '_work1.csv'
    f_work2_suffix = '_work2.csv'
    f_work3_suffix = '_work3.csv'
    f_feature_suffix = '_feature.csv'

    def __init__(self):
        logging.config.fileConfig(self.f_logfile)
        self.logger = logging.getLogger()
