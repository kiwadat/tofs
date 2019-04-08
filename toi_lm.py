# toi_lm.py : Lemmatizer
# v07 : 2019/02/23
class Lemmatizer:
    def __init__(self, en, fa):
        self.en = en
        self.logger = en.logger
        self.fa = fa
        self.logger.debug('__init__() called.')

    def remove_stop_words(self, fromfile, tofile):
        self.logger.debug('remove_stop_words() called.')

        # read recipe ingredients data (r_data)
        r_data = self.fa.read_csv(fromfile)
        self.logger.debug('--fromfile--')
        self.logger.debug(r_data)

        # refer to stopwords definition (sw_list)
        with open(self.en.f_stopwords,'r') as f:
            sw_list = [s.strip() for s in f.readlines() \
                        if s[0] != '#' and s[0] != '\n']
            self.logger.debug('-- stop words list --')
            self.logger.debug(sw_list)

        # compare recipe ingredients with stopwords
        r_lines = []
        for r_line in r_data:
            # Loop1: by the recipe
            r_list = r_line.split(',')
            self.logger.debug(r_list)
            for sw in sw_list:
                # Loop2: by the stop word
                for r_ingredient in r_list:
                    # Loop3: by the ingredient in recipe
                    if r_ingredient == sw:
                        self.logger.debug(r_ingredient + ' : stopword')
                        r_list.remove(r_ingredient)
            r_str = ','.join(r_list)
            self.logger.debug('r_str : ' + r_str)
            r_lines.append(r_str)

        self.logger.debug('r_lines : ' + str(r_lines))
        self.fa.write_csv(tofile, r_lines)

    def lemmatize(self, fromfile, tofile):
        self.logger.debug('lemmatize() called.')

        # read recipe ingredients data (r_data)
        r_data = self.fa.read_csv(fromfile)
        self.logger.debug('--fromfile--')
        self.logger.debug(r_data)

        # refer to lemmatize list (lm_table)
        with open(self.en.f_lemma,'r') as f:
            lm_table = [s.strip() for s in f.readlines() \
                        if s[0] != '#' and s[0] != '\n']
            self.logger.debug('-- lemmatize list --')
            self.logger.debug(lm_table)

        # compare recipe ingredients with lemmatize words
        r_lines = []
        for i, r_line in enumerate(r_data):
            # Loop1: by the recipe
            lctr = '{:03d}'.format(i+1)
            self.logger.debug('== Loop1: ' + lctr + ': by the recipe ==')
            r_list = r_line.split(',')
            self.logger.debug('r_list: ' + str(r_list))
            for j, r_ingredient in enumerate(r_list):
                # Loop2: by the ingredient in recipe
                lctr2 = '{:03d}'.format(j+1)
                self.logger.debug('-- Loop2: ' + lctr2 + \
                                  ': by the ingredient --')
                self.logger.debug('r_ingredient: ' + r_ingredient)
                for k, lm_str in enumerate(lm_table):
                    # Loop3: by the lemma
                    lm_list = lm_str.split(',')
                    if r_ingredient in lm_list:
                        # if found, get first column word
                        lm_word = lm_list[0].split(',')[0]
                        self.logger.debug('lemma occured: word=' + lm_word)

                        # replace remmatize words
                        idx = r_list.index(r_ingredient)
                        r_list[idx] = lm_word
                        self.logger.debug('r_list: ' + str(r_list))

            r_str = ','.join(r_list)
            self.logger.debug('r_str : ' + r_str)
            r_lines.append(r_str)

        self.logger.debug('r_lines : ' + str(r_lines))
        self.fa.write_csv(tofile, r_lines)

    def translate(self, fromfile, tofile):
        self.logger.debug('translate() called.')

        # read recipe ingredients data (r_data)
        r_data = self.fa.read_csv(fromfile)
        self.logger.debug('--fromfile--')
        self.logger.debug(r_data)

        # refer to translate list and create dic (je_dic)
        with open(self.en.f_dic,'r') as f:
            dic_table = [s.strip() for s in f.readlines() \
                        if s[0] != '#' and s[0] != '\n']
        self.logger.debug('-- translate list --')
        self.logger.debug(dic_table)
        jpn = []
        eng = []
        for row in dic_table:
            lis = row.split(',')
            jpn.append(lis[1])
            eng.append(lis[2].strip())
        self.logger.debug('-- jpn list --')
        self.logger.debug(jpn)
        self.logger.debug('-- eng list --')
        self.logger.debug(eng)
        je_dic = dict(zip(jpn, eng))

        # compare recipe ingredients with dic words
        r_lines = []
        for i, r_line in enumerate(r_data):
            # Loop1: by the recipe
            lctr = '{:03d}'.format(i+1)
            self.logger.debug('== Loop1: ' + lctr + ': by the recipe ==')
            r_list = r_line.split(',')
            self.logger.debug('r_list: ' + str(r_list))
            r_lists = []
            for j, r_ingredient in enumerate(r_list):
                # Loop2: by the ingredient in recipe
                lctr2 = '{:03d}'.format(j+1)
                self.logger.debug('-- Loop2: ' + lctr2 + \
                                  ': by the ingredient --')
                self.logger.debug('r_ingredient: ' + r_ingredient)
                if r_ingredient in je_dic:
                    r_lists.append(je_dic[r_ingredient])
                else:
                    r_lists.append(r_ingredient)

            r_str = ','.join(r_lists)
            self.logger.debug('r_str : ' + r_str)
            r_lines.append(r_str)

        self.logger.debug('r_lines : ' + str(r_lines))
        self.fa.write_csv(tofile, r_lines)
