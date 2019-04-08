#!/bin/bash
D_DATA=./data
D_PRV=${D_DATA}/previous
D_DEF=./def

if [ $# -ne 1 ]; then
    echo "Usage: $0 r1/r2"
    exit 1
fi
cmd="cp ./toi_en_$1.py ./toi_en.py"
echo "-- $cmd --"
$cmd

if [ ! -e ${D_PRV} ]; then
    mkdir ${D_PRV}
fi
cmd2="mv ${D_DATA}/test* ${D_DATA}/toi* ${D_DATA}/train* ${D_PRV}/"
echo "-- $cmd2 --"
$cmd2
cmd3="cp -p ${D_DEF}/toi_work1_$1.csv ${D_DATA}/toi_work1.csv"
echo "-- $cmd3 --"
$cmd3
cmd4="cp -p ${D_DEF}/toi_target.csv ${D_DATA}/"
echo "-- $cmd4 --"
$cmd4

echo "======= ToFS Pipeline ======="
echo "== Data Collecting and Cleansing =="
echo "-- python3 toi_ccd.py toi_page_140_$1.csv 101 -l --"
python3 toi_ccd.py toi_page_140_$1.csv 101 -l

echo "== Tokenize and Vectorize =="
echo "-- python3 toi_bcp.py toi_feature.csv --"
python3 toi_bcp.py toi_feature.csv

echo "-- python3 toi_vec.py train_feature.csv train_target.csv --"
python3 toi_vec.py train_feature.csv train_target.csv

echo "-- python3 toi_vec.py test_feature.csv test_target.csv --"
python3 toi_vec.py test_feature.csv test_target.csv

echo "== Training =="
echo "-- python3 toi_tra.py train_feature_dense.pkl train_target_vec.pkl --"
python3 toi_tra.py train_feature_dense.pkl train_target_vec.pkl
# view graph ( $ open train_feature_dense.png )

echo "== Testing =="
echo "-- python3 toi_tst.py test_feature_dense.pkl test_target_vec.pkl toi_model_0.10.3.pkl --"
python3 toi_tst.py test_feature_dense.pkl test_target_vec.pkl toi_model_0.10.3.pkl

