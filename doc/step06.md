# Step6: Predicting
## toi_upr.py
"toi_upr.py" is a program for collecting and cleansing data and predicting.

```sh
~/work $ ll
...
-rw-r--r--   1 takashi  staff  2575  4  7 11:29 toi_upr.py
...
~/work $
```

## Runnning
Run as follows. The argument 'xxxxxxx' is a recipe number.

```sh
~/work $ python3 toi_upr.py xxxxxxx
[2019/04/07 21:20:05] ========== toi_upr.py start ==========
[2019/04/07 21:20:06] cuisine: 肉じゃが
[2019/04/07 21:20:06] ingredients: 牛肉切り落とし,じゃがいも,玉ねぎ,人参,インゲン,日本酒,みりん,濃口醤油
--lemmatize--
牛肉,じゃがいも,玉ねぎ,にんじん,隠元豆,日本酒,みりん,醤油
--translate--
Beef,Potato,Onion,Carrots,Green beans,Sake,Sweet Sake,Soy sauce
Do you want to continue? (y/n) >> y
[2019/04/07 21:20:09] ---- vectorize ----
[2019/04/07 21:20:09] === 0001: ingredients ===
[2019/04/07 21:20:09] ['Beef', 'Potato', 'Onion', 'Carrots', 'Green beans', 'Sake', 'Sweet Sake', 'Soy sauce']
[2019/04/07 21:20:09] --dense matrix (1-recipe) --
[2019/04/07 21:20:09] [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[2019/04/07 21:20:09] ---- predict ----
[2019/04/07 21:20:09] filepath: ./data/toi_model_0.10.3.pkl
[2019/04/07 21:20:09] --model--
[2019/04/07 21:20:09] RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=10, n_jobs=1, oob_score=False, random_state=0,
            verbose=0, warm_start=False)
[2019/04/07 21:20:09] --y_pred--
[2019/04/07 21:20:09] [0]
Japanese
~/work $
```
