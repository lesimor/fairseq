import os
from turtle import pd
import pandas as pd
import numpy as np


ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


with open(
    f"{ROOT_DIRECTORY}/data/korean.out", "r"
) as korean, open(
    f"{ROOT_DIRECTORY}/data/english.out", "r"
) as english:
    korean_lines = korean.readlines()
    english_lines = english.readlines()

data = {
    "korean": [line.replace("\n", "") for line in korean_lines],
    "english": [line.replace("\n", "") for line in english_lines],
}

# Dataframe으로 변환
df = pd.DataFrame(data)

# 랜덤 셔플
shuffled_df = df.sample(frac=1)
print(shuffled_df)

# 전체 데이터 갯수
total_data_count = len(shuffled_df)

# validation set ratio: 5%
validation_set_ratio = 0.05
validation_cnt = int(total_data_count * validation_set_ratio)

# test set ratio: 5%
test_set_ratio = 0.05
test_cnt = int(total_data_count * test_set_ratio)

# dev, test, train set 분할
validation_df = shuffled_df[:validation_cnt]
test_df = shuffled_df[validation_cnt : validation_cnt + test_cnt]
train_df = shuffled_df[validation_cnt + test_cnt :]

text_dir = f"{ROOT_DIRECTORY}/text"

with open(f"{text_dir}/valid.ko", "w") as valid_ko_file, open(
    f"{text_dir}/valid.en", "w"
) as valid_en_file:
    ko_merged = "\n".join(validation_df["korean"])
    valid_ko_file.write(ko_merged)

    en_merged = "\n".join(validation_df["english"])
    valid_en_file.write(en_merged)

with open(f"{text_dir}/test.ko", "w") as test_ko_file, open(
    f"{text_dir}/test.en", "w"
) as test_en_file:
    ko_merged = "\n".join(test_df["korean"])
    test_ko_file.write(ko_merged)

    en_merged = "\n".join(test_df["english"])
    test_en_file.write(en_merged)


with open(f"{text_dir}/train.ko", "w") as train_ko_file, open(
    f"{text_dir}/train.en", "w"
) as train_en_file:
    ko_merged = "\n".join(train_df["korean"])
    train_ko_file.write(ko_merged)

    en_merged = "\n".join(train_df["english"])
    train_en_file.write(en_merged)
