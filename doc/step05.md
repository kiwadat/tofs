# Step5: Testing
## toi_tst.py
"toi_tst.py" is a program for testing.

```sh
~/work $ ll
...
-rw-r--r--   1 takashi  staff   888  2 23 17:15 toi_tst.py
...
~/work $
```

## Runnning
Run as follows. The name specified in the third argument may be different because of scikit-learn version.

```sh
~/work $ python3 toi_tst.py test_feature_dense.pkl test_target_vec.pkl toi_model_0.10.3.pkl
[2019/04/07 21:16:46] ========== toi_tst.py start ==========
[2019/04/07 21:16:46] --model--
[2019/04/07 21:16:46] RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=10, n_jobs=1, oob_score=False, random_state=0,
            verbose=0, warm_start=False)
[2019/04/07 21:16:46] --y_pred--
[2019/04/07 21:16:46] [2 2 0 0 1 0 2 0 0 0 1 0 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 1
 3 3 3]
[2019/04/07 21:16:46] accuracy: 85.00%
~/work $
```
