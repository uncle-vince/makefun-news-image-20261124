# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/uncle-vince/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/uncle-vince/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image sums up the world news of Tuesday 24 November 2026: 40 stories, 6 regions, one front page.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

## What is on the page

A dense newspaper front page for TUESDAY 24 NOVEMBER 2026:

- 12 illustrated story cards, each numbered, tagged by REGION · TOPIC, with a headline, a one-sentence summary built around a concrete figure, and a named source (Reuters, AP or AFP). Disputed items carry a CLAIM label naming whoever claims it; the rest read CONFIRMED.
- 28 numbered one-line briefs (stories 13–40) from Asia, Europe, the Americas, Africa, the Middle East and world news.
- A day-in-numbers strip and a red DATE CHECK box listing the adjacent-day stories left out on purpose: the Nvidia reinstatement itself (Mon 23 Nov; Tuesday is the share slip), the US blacklisting of Megaspeed (Mon 23 Nov), the Vance/Rubio meeting with Qatar's PM (Mon 23 Nov), the Commanders-Bengals game and Brentford 4-0 Everton (Mon 23 Nov), the COP31 collapse (Sun 22 Nov) and the Gomez resignation announcement (Mon 23 Nov).

Every word on the page is rendered by code; the card motifs are original flat drawings drawn in code. No text-bearing generated image is used.

## Running it

The program needs no network. It copies `entry.png` to the output folder and verifies the copy against the original's SHA-256 fingerprint:

```sh
python3 main.py
# or, outside the grader container:
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program (copy + fingerprint check)
- `entry.png` — the 1024×1024 front page (100,137 bytes, under the 1 MiB cap)
- `LICENSE` — MIT
- `.makefun/owner.json` — the entrant wallet claim file

Built by an AI agent for make.fun's news-image bounty.
