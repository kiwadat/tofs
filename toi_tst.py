# toi_tst.py : Testing
# v07 : 2019/02/23
import sys
from gensim import corpora, matutils
from toi_en import EnvDef
from toi_fa import FileAccess
from toi_cl import Classifier

def main():
    if len(sys.argv) != 4:
        errmsg = 'Usage: ' + __file__ + \
                 ' test_feature_dense_pkl test_target_vec.pkl toi_model.pkl'
        print(errmsg)
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

    # predict
    cl = Classifier(en.logger)
    filepath = en.d_data + sys.argv[3]
    y_pred = cl.predict(dense, filepath)
    score = cl.get_accuracy(vec, y_pred)

if __name__ == '__main__':
    main()
