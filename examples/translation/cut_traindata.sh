SCRIPT_PATH=$(dirname $0)
LINES=${1:-10000}
TEXT_DIR=${2:-$SCRIPT_PATH/iwslt14.tokenized.de-en}

# copy train data
if [ ! -f $TEXT_DIR/train-backup.de ]; then
    cp $TEXT_DIR/train.de $TEXT_DIR/train-backup.de
fi
echo "1,${LINES}p"
sed -n "1,${LINES}p" $TEXT_DIR/train-backup.de >$TEXT_DIR/train.de

if [ ! -f $TEXT_DIR/train-backup.en ]; then
    cp $TEXT_DIR/train.en $TEXT_DIR/train-backup.en
fi
sed -n "1,${LINES}p" $TEXT_DIR/train-backup.en >$TEXT_DIR/train.en
