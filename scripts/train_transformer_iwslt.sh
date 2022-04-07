!# /usr/bin/bash

# 레포 위치 설정
REPO_ROOT=$1
# 샌드박스명 설정
SANDBOX_NAME=${1-common}
TRANSLATION_ROOT=$REPO_ROOT/examples/translation
SANDBOX_ROOT=$REPO_ROOT/sandbox/$SANDBOX_NAME

TEXT_ROOT=$SANDBOX_ROOT/text
TEXT=$TEXT_ROOT/iwslt14.tokenized.de-en

DATABIN_ROOT=$SANDBOX_ROOT/data-bin
DATABIN=$DATABIN_ROOT/iwslt14.tokenized.de-en
CHECKPOINT=$SANDBOX_ROOT/checkpoints

export PYTHONPATH=$PYTHONPATH:$REPO_ROOT

pushd $REPO_ROOT
    pip install --editable .
popd

mkdir -p $TEXT_ROOT

pushd $TEXT_ROOT
    $TRANSLATION_ROOT/prepare-iwslt14.sh
popd

# 기존 디렉토리 제거
rm -rf $DATABIN_ROOT

# preprocessing
[ ! -d $DATABIN_ROOT ] && fairseq-preprocess --source-lang de --target-lang en \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir $DATABIN

mkdir -p $CHECKPOINT

fairseq-train $DATABIN \
    --arch transformer --save-dir $CHECKPOINT \
    --max-epoch 10 --max-tokens 3584 --optimizer adam