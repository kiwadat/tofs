# Step2: building Corpus
## toi_bcp.py
"toi_bcp.py" is a program for building corpus.

```sh
~/work $ ll
...
-rw-r--r--   1 takashi  staff   889  2 24 06:39 toi_bcp.py
...
~/work $
```

## Running
Run as follows:

```sh
~/work $ python3 toi_bcp.py toi_feature.csv
[2019/04/07 20:44:42] ========== toi_bcp.py start ==========
~/work $
```

## Check
After running this program, check the following files.

```sh
~/work/data $ ll
...
-rw-r--r--   1 takashi  staff   1816  4  7 20:44 toi_corpus.csv
-rw-r--r--   1 takashi  staff   1820  4  7 20:44 toi_corpus.txt
...
~/work/data $
~/work/data $ cat toi_corpus.txt
140
95	Anchovy	2
64	Bamboo shoot	4
42	Bean sprouts	18
19	Beef	7
110	Beef bones	2
68	Bell pepper	8
35	Burdock	5
15	Butter	3
16	Cabbage	5
20	Carrots	31
...
~/work/data $
~/work/data $ cat toi_corpus.csv
0,Chicken,21
1,Egg,25
2,Leek,21
3,Noodle soup,8
4,Nori,5
5,Onion,38
6,Sake,26
7,Sesame oil,34
...
~/work/data $
```
