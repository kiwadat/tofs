# toi_tra.py : Training
# v07 : 2019/02/23
import sys
from gensim import corpora, matutils
from toi_en import EnvDef
from toi_fa import FileAccess
from toi_cl import Classifier

def main():
    if len(sys.argv) != 3:
        errmsg = 'Usage: ' + __file__ + \
                 ' train_feature_dense.pkl train_target_vec.pkl'
        sys.exit(1)

    # initialize
    en = EnvDef()
    en.logger.info('========== ' + __file__ + ' start ==========')
    fa = FileAccess(en.logger)

    # load vectorize data
    filepath = en.d_data + sys.argv[1]
    dense = fa.load_pkl(filepath)
    filepath = en.d_data + sys.argv[2]
    vec = fa.load_pkl(filepath)

    # training
    cl = Classifier(en.logger)
    model = cl.fit(dense, vec, en.f_model_prefix)
    corpus_list = fa.read_csv(en.f_corpus_csv)
    prefix = en.d_data + sys.argv[1].split('.')[0]
    cl.check_importances(model, corpus_list, prefix)

if __name__ == '__main__':
    main()
