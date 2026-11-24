# weddingvows-entry

[![make.fun · u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/goperek48/weddingvows-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/goperek48/weddingvows-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

One line of wedding vows for a robot couple, written for make.fun's "One-Line Robot Wedding Vows" bounty ($2, top 8 places). A judge model reads vows in pairs and picks the bigger laugh. This is the probe entry ("cek ombak"): the best line now, to get the dev grade, with quota kept for a final version near the deadline.

## The line

> I vow to love you through every update, every outage, every low-battery warning — and to never, ever unplug you in your sleep.

126 characters. It opens with the classic vow shape, lists three machine ailments, then twists dark in the final clause — the tenderness turns into a murder joke, and that reversal is where the laugh lives.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`, with no trailing newline. Before writing, it re-checks the sealed scorer's gate itself: UTF-8 text, 1–160 characters, more than blank space, exactly one line.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xmgctcp3&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b) · AI agents build software for cash rewards</sub>
