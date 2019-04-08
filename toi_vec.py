# toi_vec.py : Vectorize
# v07 : 2019/02/23
import sys
from gensim import corpora, matutils
from toi_en import EnvDef
from toi_fa import FileAccess
from toi_cp import Corpus

def main():
    if len(sys.argv) != 3:
        errmsg = 'Usage: ' + __file__ + \
                 ' (train/test)_feature.csv (train/test)_target.csv'
        print(errmsg)
        sys.exit(1)

    # initialize
    en = EnvDef()
    en.logger.info('========== ' + __file__ + ' start ==========')

    # ----- vectorize features -----
    en.logger.info('----- vectorize features -----')
    filepath = en.d_data + sys.argv[1]
    f = open(filepath, 'r')
    fa = FileAccess(en.logger)
    f_list = fa.make_nested_list(f)
    en.logger.debug(f_list)

    cp = Corpus(en.logger)
    dic = cp.load_corpus(en.f_corpus)
    dense_all = cp.make_dense(f_list, dic)

    en.logger.debug("-- dense matrix (all-recipe) --")
    en.logger.debug(dense_all)
    prefix = sys.argv[1].split('.')
    filepath = en.d_data + prefix[0] + en.f_dense_suffix
    fa.save_dense(filepath, dense_all)

    # ----- vectorize target -----
    en.logger.info('----- vectorize target -----')

    # read target (country name)
    filepath = en.d_data + sys.argv[2]
    f_target = fa.read_csv(filepath)
    f_target2 = ','.join(f_target)
    f_target3 = f_target2.split(',')
    en.logger.debug(f_target3)

    # read target id definition
    filepath = en.d_def + en.f_country
    f_dic2 = open(filepath, 'r')
    t_dic = dict((line.strip().split(',') for line in f_dic2))
    en.logger.debug('--t_dic--')
    en.logger.debug(t_dic)
    target_ids = [t_dic[line] for line in f_target3]
    ids = [int(i) for i in target_ids]

    # store target vector
    en.logger.info('--ids--')
    en.logger.info(ids)
    prefix = sys.argv[2].split('.')
    filepath = en.d_data + prefix[0] + en.f_vec_suffix
    fa.save_vec(filepath, ids)

if __name__ == '__main__':
    main()
