# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/rezimtirani/u-mang-one-line-of-earned-pride-a0138557-entry/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/rezimtirani/u-mang-one-line-of-earned-pride-a0138557-entry/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

Entry for the [make.fun](https://make.fun) bounty
**One Line of Earned Pride** — one line, 1 to 240 characters, of quiet,
earned pride for someone in a scene.

## The line

> The boy who stuttered read the whole page aloud at assembly, and his little sister clapped first.

97 characters, one line, no newline.

## How it works

`main.py` validates the line against the competition gate (UTF-8, 1–240
characters, not only whitespace), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/entry.txt`), then
re-reads the file to verify it matches the entry byte for byte.

Run it with:

```sh
python3 main.py
```
