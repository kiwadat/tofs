# Step1: Collecting and cleansing data for training and testing

## Common modules
These are imported from other main programs.
- toi_cl.py : Classifier
- toi_cp.py : Corpus
- toi_en.py : Environment Definition
- toi_fa.py : File Access
- toi_lm.py : Lemmatizer
- toi_sc.py : Scraper

## toi_ccd.py
"toi_ccd.py" is a program for collecting and cleansing data.
You need to put this file as follows:

```sh
~/work $ ll
total 136
drwxr-xr-x   8 takashi  staff   272  4  7 18:17 __pycache__/
drwxr-xr-x  26 takashi  staff   884  4  7 18:18 data/
drwxr-xr-x  26 takashi  staff   884  4  7 18:39 def/
drwxr-xr-x  10 takashi  staff   340  4  7 18:36 log/
-rw-r--r--   1 takashi  staff   889  2 24 06:39 toi_bcp.py
-rw-r--r--   1 takashi  staff  4681  4  7 14:23 toi_ccd.py
-rw-r--r--   1 takashi  staff  3465  4  6 21:24 toi_cl.py
-rw-r--r--   1 takashi  staff  2309  2 23 18:13 toi_cp.py
-rwxr-xr-x   1 takashi  staff  1450  4  7 18:16 toi_demo.sh*
-rw-r--r--   1 takashi  staff  1651  4  7 18:17 toi_en.py
-rw-r--r--   1 takashi  staff  1642  3  4 22:23 toi_en_r1.py
-rw-r--r--   1 takashi  staff  1651  4  5 22:02 toi_en_r2.py
-rw-r--r--   1 takashi  staff  2405  3  2 11:43 toi_fa.py
-rw-r--r--   1 takashi  staff  5717  3  3 07:21 toi_lm.py
-rw-r--r--   1 takashi  staff  2597  3 30 10:43 toi_sc.py
-rw-r--r--   1 takashi  staff   936  3  1 21:48 toi_tra.py
-rw-r--r--   1 takashi  staff   888  2 23 17:15 toi_tst.py
-rw-r--r--   1 takashi  staff  2575  4  7 11:29 toi_upr.py
-rw-r--r--   1 takashi  staff  1913  3  2 11:33 toi_vec.py
~/work $
```

## Running
First, check if it works with a small number of data. (2 recipes)

```sh
~/work $ python3 toi_ccd.py toi_page_2.csv 2
[2019/04/07 18:50:33] ========== toi_ccd.py start ==========
[2019/04/07 18:50:33] ---- get recipe data ----
[2019/04/07 18:50:34] make all data
[2019/04/07 18:50:34] - remove stop words
[2019/04/07 18:50:34] - lemmatize
[2019/04/07 18:50:34] - translate
[2019/04/07 18:50:34] make training data
[2019/04/07 18:50:34] - remove stop words
[2019/04/07 18:50:34] - lemmatize
[2019/04/07 18:50:34] - translate
[2019/04/07 18:50:34] make testing data
[2019/04/07 18:50:34] - remove stop words
[2019/04/07 18:50:34] - lemmatize
[2019/04/07 18:50:34] - translate
~/work $
```

## Check
After running this program, several new files are created.

### log file
If it does not work as expected, you need to check this logfile.

```sh
~/work $ cd log
~/work/log $ ll
total 152
-rw-r--r--   1 takashi  staff  77682  4 7 18:50 toi.log
~/work/log $
```

### Cleansing data
If it works correctly, three types of files are created.
- toi_\*.csv : all data (training data + testing data)
- train_\*.csv : training data
- test_\*.csv : testing data

And it is also possible to separate into the five types by another method.

- \*_feature.csv : features for machine learning (translate words)
- \*_target.csv : target labels for supervised learning
- \*_work1.csv : scraping data (origin)
- \*_work2.csv : cleansing data (removing stop words)
- \*_work3.csv : cleansing data (lemmatize words)

The following four files are used for subsequent pipeline process.

- train_feature.csv
- train_target.csv
- test_feature.csv
- test_target.csv

```sh
~/work $ cd data
~/work/data $ ll
total 120
-rw-r--r--   1 takashi  staff   76  4  7 18:50 test_feature.csv
-rw-r--r--   1 takashi  staff    9  4  7 18:50 test_target.csv
-rw-r--r--   1 takashi  staff  115  4  7 18:50 test_work1.csv
-rw-r--r--   1 takashi  staff  105  4  7 18:50 test_work2.csv
-rw-r--r--   1 takashi  staff  102  4  7 18:50 test_work3.csv
-rw-r--r--   1 takashi  staff  163  4  7 18:50 toi_feature.csv
-rw-r--r--   1 takashi  staff   18  4  7 18:50 toi_target.csv
-rw-r--r--   1 takashi  staff  226  4  7 18:50 toi_work1.csv
-rw-r--r--   1 takashi  staff  187  4  7 18:50 toi_work2.csv
-rw-r--r--   1 takashi  staff  193  4  7 18:50 toi_work3.csv
-rw-r--r--   1 takashi  staff   87  4  7 18:50 train_feature.csv
-rw-r--r--   1 takashi  staff    9  4  7 18:50 train_target.csv
-rw-r--r--   1 takashi  staff  111  4  7 18:50 train_work1.csv
-rw-r--r--   1 takashi  staff   82  4  7 18:50 train_work2.csv
-rw-r--r--   1 takashi  staff   91  4  7 18:50 train_work3.csv
~/work $
```
## Next
For the next step, run the same program with the following data and check the output files and log file. It takes about 1-2 minute to run.(43 or 140 recipes. Run time depends on your internet speed.)

```sh
~/work $ python3 toi_ccd.py toi_page_43.csv 41
[2019/04/07 18:53:07] ========== toi_ccd.py start ==========
[2019/04/07 18:53:07] ---- get recipe data ----
[2019/04/07 18:53:27] make all data
[2019/04/07 18:53:27] - remove stop words
[2019/04/07 18:53:27] - lemmatize
[2019/04/07 18:53:28] - translate
[2019/04/07 18:53:28] make training data
[2019/04/07 18:53:28] - remove stop words
[2019/04/07 18:53:28] - lemmatize
[2019/04/07 18:53:28] - translate
[2019/04/07 18:53:28] make testing data
[2019/04/07 18:53:28] - remove stop words
[2019/04/07 18:53:28] - lemmatize
[2019/04/07 18:53:28] - translate
~/work $
~/work $ python3 toi_ccd.py toi_page_140_r1.csv 101
[2019/04/07 18:54:15] ========== toi_ccd.py start ==========
[2019/04/07 18:54:15] ---- get recipe data ----
[2019/04/07 18:55:31] make all data
[2019/04/07 18:55:31] - remove stop words
[2019/04/07 18:55:31] - lemmatize
[2019/04/07 18:55:32] - translate
[2019/04/07 18:55:32] make training data
[2019/04/07 18:55:32] - remove stop words
[2019/04/07 18:55:32] - lemmatize
[2019/04/07 18:55:33] - translate
[2019/04/07 18:55:33] make testing data
[2019/04/07 18:55:33] - remove stop words
[2019/04/07 18:55:33] - lemmatize
[2019/04/07 18:55:33] - translate
```
