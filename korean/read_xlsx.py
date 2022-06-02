import pandas as pd
from os import walk
import os
from pathlib import Path

ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

root_dir = f"{ROOT_DIRECTORY}/data"
filenames = next(walk(root_dir), (None, None, []))[2]

print(filenames)

korean_out = f"{root_dir}/korean.out"
english_out = f"{root_dir}/english.out"

for filename in filenames:
    df = pd.read_excel(f"{root_dir}/{filename}")
    korean = df["원문"]
    english = df["번역문"]
    assert len(korean) == len(english)

    with open(korean_out, "a") as f:
        merged = "\n".join(korean)
        f.write(merged)

    with open(english_out, "a") as f:
        merged = "\n".join(english)
        f.write(merged)
