# toi_bco.py : Building Corpus
# v07 : 2019/02/23
import sys
from gensim import corpora, matutils
from toi_en import EnvDef
from toi_fa import FileAccess
from toi_cp import Corpus

def main():
    if len(sys.argv) != 2:
        errmsg = 'Usage: ' + __file__ + ' toi_feature.csv'
        print(errmsg)
        sys.exit(1)

    # initialize
    en = EnvDef()
    en.logger.info('========== ' + __file__ + ' start ==========')
    filepath = en.d_data + sys.argv[1]
    f = open(filepath, 'r')
    fa = FileAccess(en.logger)
    f_list = fa.make_nested_list(f)
    en.logger.debug(f_list)

    # create/save corpus (mapping between words and their idx)
    cp = Corpus(en.logger)
    dic = cp.create_corpus(f_list)
    cp.save_corpus(dic, en.f_corpus)

    # save corpus for view importance features
    cp.save_corpus_csv(en.f_corpus, en.f_corpus_csv)

if __name__ == '__main__':
    main()
