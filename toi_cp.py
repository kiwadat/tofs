# toi_cp.py : Corpus
# v07 : 2019/02/23
import subprocess
from gensim import corpora, matutils

class Corpus:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug('__init__() called.')

    def create_corpus(self, f_list):
        self.logger.debug('create_corpus() called.')
        dic = corpora.Dictionary(f_list)
        self.logger.debug(dic)
        self.logger.debug(dic.token2id)  # {'しめじ':0, '豚肉':1, ...}

        # filter out tokens (less than 2)
        dic.filter_extremes(no_below=2)
        self.logger.debug(dic)
        self.logger.debug(dic.token2id)
        return dic

    def save_corpus(self, dic, filepath):
        self.logger.debug('save_corpus() called.')
        # store dictionary : for predict (create dense_all from testdata)
        dic.save_as_text(filepath)

    def save_corpus_csv(self, txtfile, csvfile):
        self.logger.debug('save_corpus_csv() called.')
        cmd = "sed -e '1d' ./" + txtfile \
                + " | sort --numeric-sort | tr '\t' ',' > " + csvfile
        self.logger.debug('--cmd--')
        self.logger.debug(cmd)
        res = subprocess.call(cmd, shell=True)
        self.logger.debug('--res--')
        self.logger.debug(res)

    def load_corpus(self, filepath):
        self.logger.debug('load_corpus() called.')
        dic = corpora.Dictionary.load_from_text(filepath)
        return dic

    def make_dense(self, f_list, dic):
        self.logger.debug('make_dense() called.')
        dense_all = []
        for i, r_data in enumerate(f_list):
            ctr = '{:04d}'.format(i+1)
            self.logger.info('=== ' + ctr + ': ingredients ===')
            self.logger.info(r_data)

            # corpus: [(id,freq),(id,freq),...]
            corpus = dic.doc2bow(r_data)
            self.logger.debug("--corpus--")
            self.logger.debug(corpus)

            # convert corpus into a dense numpy 2D array,
            #    with documents as columns
            # cf.) https://radimrehurek.com/gensim/matutils.html
            dense = list(matutils.corpus2dense([corpus], \
                            num_terms=len(dic)).T[0])
            self.logger.info("--dense matrix (1-recipe) --")
            self.logger.info(dense)
            dense_all.append(dense)
        return dense_all
