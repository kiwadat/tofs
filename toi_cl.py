# toi_cl.py : Classifier
# v07 : 2019/02/23
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from gensim import corpora, matutils
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

class Classifier:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug('__init__() called.')

    def fit(self, x_train, y_train, prefix):
        self.logger.debug('fit() called.')

        # initialize
        estimator = RandomForestClassifier(random_state=0)

        # training
        model = estimator.fit(x_train, y_train)
        self.logger.info('--model--')
        self.logger.info(model)

        # save model
        scikit_ver = joblib.__version__
        filepath = prefix + '{ver}.pkl'.format(ver=scikit_ver)
        filepath_bk = prefix + '{ver}.pkl.bk'.format(ver=scikit_ver)
        if os.path.exists(filepath):
            shutil.move(filepath, filepath_bk)
        joblib.dump(model, filepath)

        return model

    def check_importances(self, model, corpus_list, prefix):
        self.logger.debug('check_importances() called.')

        # get importances
        importances = model.feature_importances_
        self.logger.debug('--importances--')
        self.logger.debug(importances)

        # sort
        indices = np.argsort(importances)[::-1]
        self.logger.debug('--indices--')
        self.logger.debug(indices)

        # save log and data
        indlist = [corpus_list[i] for i in indices]
        for i, row in enumerate(indlist):
            clm = row.split(',')
            log = '{a:03d}: {b} (id={c}, frq={d}, imp={e:.5f})'.format( \
                    a=i+1, b=clm[1], c=clm[0], \
                    d=clm[2], e=importances[indices[i]])
            self.logger.debug(log)
        self.logger.info('--importances (top 20)--')
        for i, row in enumerate(indlist[0:20]):
            clm = row.split(',')
            log = '{a:03d}: {b} (id={c}, frq={d}, imp={e:.5f})'.format( \
                    a=i+1, b=clm[1], c=clm[0], \
                    d=clm[2], e=importances[indices[i]])
            self.logger.info(log)

        # for bar graph
        plt.figure(figsize=(15,9), dpi=80)
        plt.title('Feature Importance', fontsize=20)
        plt.xlabel('ingredient', fontsize=15)
        plt.ylabel('importance', fontsize=15)
        plt.tick_params(labelsize=14)
        plt.grid(True)
        left = [i for i in range(20)]
        labels = [i.split(',')[1] for i in list(reversed(indlist[0:20]))]
        height = np.array(importances[list(reversed(indices[0:20]))])
        plt.barh(left, height, color='yellowgreen', \
                edgecolor='forestgreen', linewidth=1, \
                align='edge', tick_label=labels)
        pngfile = prefix + '.png'
        plt.savefig(pngfile)
        plt.show()

    def predict(self, x_test, filepath):
        self.logger.debug('predict() called.')
        model = joblib.load(open(filepath, 'rb'))
        self.logger.info('--model--')
        self.logger.info(model)

        y_pred = model.predict(x_test)
        self.logger.info('--y_pred--')
        self.logger.info(y_pred)
        return y_pred

    def get_accuracy(self, y_true, y_pred):
        self.logger.debug('get_accuracy() called.')

        score = accuracy_score(y_true, y_pred)
        self.logger.info('accuracy: {0:.2%}'.format(score))
        return score
