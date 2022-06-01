import pandas as pd
from os import walk
from pathlib import Path

root_dir = "/Users/byungwook/Codes/vscode/fairseq/korean/mini_data"
filenames = next(walk(root_dir), (None, None, []))[2]

print(filenames)

korean_out = f"{root_dir}/korean.out"
english_out = f"{root_dir}/english.out"

for filename in filenames:
    df = pd.read_excel(f"{root_dir}/{filename}")
    korean = df["원문"]
    english = df["번역문"]
    assert len(korean) == len(english)

    with open(korean_out, "w+") as f:
        merged = "\n".join(korean)
        f.write(merged)

    with open(english_out, "w+") as f:
        merged = "\n".join(english)
        f.write(merged)
