# toi_fa.py : File Access
# v07 : 2019/02/23
import os
import sys
import pickle

class FileAccess:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug(': __init__() called.')


    def write_csv(self, filepath, csvlist):
        self.logger.debug('write_csv() called.')
        if not isinstance(csvlist, list):
            self.logger.error('argument csvlist is not list.')
            sys.exit()
        f = open(filepath, 'w')
        for r_list in csvlist:
            self.logger.debug(r_list)
            row = r_list + '\n'
            f.write(row)
        f.close()

    def read_csv(self, filepath):
        self.logger.debug('read_csv() called.')
        f = open(filepath, 'r')
        lines = f.readlines()
        #lists = [x.strip() for x in lines]
        lists = []
        for row in lines:
            if row[0] != '#' and '\n' :
                lists.append(row.strip())
        f.close()
        return lists

    def make_nested_list(self, f):
        self.logger.debug('make_nested_list() called.')
        f_list = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.replace('\n','')
            line = line.split(',')
            f_list.append(line)
        return f_list

    def save_dense(self, filepath, dense_all):
        self.logger.debug('save_dense() called.')

        # store corpus (text matrix)
        f = open(filepath, 'w')
        for r_list in dense_all:
            row = str(r_list) + '\n'
            f.write(row)
        f.close()

        # store corpus (binary)
        f_fb = open(filepath, 'wb')
        pickle.dump(dense_all, f_fb)
        f_fb.close()

    def load_dense(self, filepath):
        self.logger.debug('load_dense() called.')
        f = open(filepath, 'rb')
        return pickle.load(f)

    def save_vec(self, filepath, vec):
        self.logger.debug('save_vec() called.')
        f_fb = open(filepath, 'wb')
        pickle.dump(vec, f_fb)
        f_fb.close()

    def load_pkl(self, filepath):
        self.logger.debug('load_pkl() called.')
        f = open(filepath, 'rb')
        return pickle.load(f)

    def show_file(self, filepath, comment):
        self.logger.debug('show_file() called.')
        f = open(filepath, 'r')
        for line in f.readlines():
            print(comment)
            print(line.strip())
