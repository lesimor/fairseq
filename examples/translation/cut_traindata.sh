set -x

SCRIPT_PATH=$(dirname $0)
TEXT_DIR=${1:-$SCRIPT_PATH/iwslt14.tokenized.de-en}
LINES=${2:-160239}

echo "Cutting training data..."
echo "length of training data: $LINES"

sed -n "1,${LINES}p" $TEXT_DIR/train.de >$TEXT_DIR/train-cut.de
sed -n "1,${LINES}p" $TEXT_DIR/train.en >$TEXT_DIR/train-cut.en

set +x
echo "Done."
