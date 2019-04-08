# Step0: Configuring logger, several dictionaries and url pages

## Create directories
You need to create three new directories in current working derectory.
- data
- def
- log

```sh
~/work $ mkdir data def log
~/work $ ll
total 0
drwxr-xr-x  2 takashi  staff  68  3 17 16:46 data/
drwxr-xr-x  2 takashi  staff  68  3 17 16:46 def/
drwxr-xr-x  2 takashi  staff  68  3 17 16:46 log/
~/work $
```

## Put several files
Then, put several files in the ./def directory.

### logging configuration
- toi_logger.conf

### dictionaries
- toi_country.csv : mapping between country name and id
- toi_dic.csv, toi_dic_r2.csv : translating words from Japanese to English
- toi_lemma.csv, toi_lemma_r2.csv : lemmatizing ingredients words
- toi_stopwords.csv, toi_stopwords_r2.csv : filtering out words unprocessed

### url page data
- toi_page_2.csv : 2 recipes data
- toi_page_43.csv : 43 recipes data (40:training, 3:testing)
- toi_page_140_r1.csv : 140 recipes data (100:training, 40:testing)
- toi_page_140_r2.csv : 140 recipes data (100:training, 40:testing)

### features and targets data (for running locally)
- toi_work1_r1.csv : result of 'toi_ccd.py toi_page_140_r1.csv 101' feature data
- toi_work1_r2.csv : result of 'toi_ccd.py toi_page_140_r2.csv 101' feature data
- toi_target.csv : result of target data


```sh
~/work/def $ ll
total 64
-rw-r--r--   1 takashi  staff     44  3  4 20:49 toi_country.csv
-rw-r--r--   1 takashi  staff   4687  3 30 20:29 toi_dic.csv
-rw-r--r--   1 takashi  staff   4948  3 30 20:24 toi_dic_r2.csv
-rw-r--r--   1 takashi  staff   9964  4  7 11:25 toi_lemma.csv
-rw-r--r--   1 takashi  staff  10071  4  7 11:24 toi_lemma_r2.csv
-rw-r--r--   1 takashi  staff    617  3  3 06:39 toi_logger.conf
-rw-r--r--   1 takashi  staff  11841  4  7 18:31 toi_page_140_r1.csv
-rw-r--r--   1 takashi  staff  11841  4  7 18:31 toi_page_140_r2.csv
-rw-r--r--   1 takashi  staff    237  3 17 18:29 toi_page_2.csv
-rw-r--r--   1 takashi  staff   3059  3 21 18:36 toi_page_43.csv
-rw-r--r--   1 takashi  staff   1883  4  6 16:46 toi_stopwords.csv
-rw-r--r--   1 takashi  staff   2021  4  6 16:47 toi_stopwords_r2.csv
-rw-r--r--   1 takashi  staff   1260  4  7 14:52 toi_target.csv
-rw-r--r--   1 takashi  staff  19321  4  7 14:52 toi_work1_r1.csv
-rw-r--r--   1 takashi  staff  19321  4  7 14:54 toi_work1_r2.csv
~/work/def $
```
