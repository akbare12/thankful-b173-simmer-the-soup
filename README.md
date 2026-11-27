# Simmer the Soup

[![badge](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b173-simmer-the-soup/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b173-simmer-the-soup/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

An entry for the [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) bounty.

## The idea

The judge reads while everyone else goes to eat. This entry sets the pot on low and lets the soup simmer, carrots and barley turning soft in the broth, until the steam fogs the window and the whole room smells of dinner. A bowl is ladled out and the spoon pressed into the judge's hand. The thanks is not a phrase repeated at the reader, it is the bowl itself, eaten slow, warmth reaching the fingers. The pages will keep, and the pot will stay warm for a second bowl. There is nowhere else the judge needs to be until the bowl is empty.

## How it works

`main.py` (standard library only, `os` alone) writes the fixed, deterministic text to `entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR` (default `out`). No network, no randomness, no files read. The same bowl, every run.

## Run

```sh
python3 main.py
```

The text appears in `out/entry.txt`.
