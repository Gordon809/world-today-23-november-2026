[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Gordon809/world-today-23-november-2026/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Gordon809/world-today-23-november-2026/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World Today — 23 November 2026

One image that sums up Monday 23 November 2026, built for the
[make.fun](https://make.fun/bounty/news-image-20261123) bounty
"Sum up 23 November's world news in one image".

## What's on the page

- **Lead — COP31 collapses in Antalya:** two weeks of UN climate talks end
  with no deal after the EU and island states reject a text that never
  mentions fossil fuels, the first COP breakdown since 2009.
- **Ukraine:** a 7-year-old boy is pulled alive from rubble after Russian
  drones hit a home near Kyiv; nine people are killed.
- **United States:** Democrats take their largest House majority since 1992
  after flipping a North Carolina seat.
- **Health:** the NHS launches the world's largest AI breast-cancer screening
  trial, with 700,000 women taking part.
- **Pacific:** a magnitude 6.5 earthquake strikes the Vanuatu region.
- **Markets:** Asian shares reel as the AI sell-off spreads — the KOSPI falls
  5% and Taiwan's market swings 1,578 points in a day.
- **Footer:** Manchester arena evacuated after a suspected tear-gas release;
  the Mets sign Skubal in a record $450m deal; FIFA to confirm the UK as
  2035 Women's World Cup host; India v New Zealand Test reaches a Day 5
  decider.

## How it is made

`draw.py` (Python 3, Pillow only, no network) draws the page and writes
`entry.png` (1024x1024). Running it twice produces byte-identical output.
`main.ts` copies `entry.png` into `$MAKEFUN_OUTPUT_DIR`.

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=/tmp/out node main.ts
```

## Referral

Built with [make.fun](https://make.fun/r/5g7k5t7n) — referral code `5g7k5t7n`.
