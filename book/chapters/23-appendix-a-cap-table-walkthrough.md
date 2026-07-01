# Appendix A — A Full Cap Table Walkthrough

Chapter 15 introduced the mechanics of a valuation cap and gave a taste of how dilution
compounds across rounds. This appendix walks through one complete, simplified example
from founding to a Series A, with real numbers at every step, so you can see exactly
where each shareholder's percentage comes from — not just the concept, but the
arithmetic underneath it.

**A caveat worth stating up front**: real cap tables are messier than this. They involve
multiple SAFEs at different terms, seed extensions, warrants, and negotiated
side-letters. This walkthrough uses one clean, illustrative scenario specifically so the
mechanism is visible. Don't treat the specific percentages below as typical — treat the
*method* as transferable.

## Step 1: Founding

Two cofounders incorporate and issue themselves 8,000,000 shares of common stock,
split evenly.

| Shareholder | Shares | Ownership |
|---|---|---|
| Founder A | 4,000,000 | 50% |
| Founder B | 4,000,000 | 50% |
| **Total** | **8,000,000** | **100%** |

Both founders' shares vest over four years with a one-year cliff, per Chapter 15.

## Step 2: The Seed Round (a post-money SAFE)

The company raises $2,000,000 on a SAFE with a **$10,000,000 post-money valuation
cap**. This detail matters: a *post-money* cap (the standard since Y Combinator updated
its template, mentioned in Chapter 15) means the cap already accounts for the SAFE
money itself. That makes the investor's eventual ownership percentage simple to
calculate directly, with no circular math required:

> Investor's locked-in ownership = Investment ÷ Post-money cap = $2,000,000 ÷
> $10,000,000 = **20%**

Nothing converts into actual shares yet — a SAFE holder isn't a shareholder until a
future priced round triggers conversion (Chapter 15). But the 20% figure is now locked
in, and it will get diluted by future rounds exactly the same way the founders'
ownership will.

**The company's ownership picture right after the SAFE closes (on a fully diluted,
as-if-converted basis):**

| Shareholder | Ownership |
|---|---|
| Founder A | 40% |
| Founder B | 40% |
| Seed SAFE investor (locked in, not yet issued shares) | 20% |
| **Total** | **100%** |

## Step 3: The Series A

A year later, the company raises a Series A: $5,000,000 from a new investor, at a
**$20,000,000 pre-money valuation** (meaning $25,000,000 post-money). At the same time,
the board creates a new **15% option pool** for future employees — carved out of the
existing (pre-money) ownership, not out of the new investor's stake, which is the
standard structure.

The new investor's share is simple: $5,000,000 ÷ $25,000,000 = **20% of the
post-Series-A company.**

Everyone who held equity *before* this round — the two founders and the converting seed
SAFE — now splits what's left: 100% − 20% (new investor) − 15% (option pool) = **65%,**
divided among them in the same proportion they held before this round (40% / 40% / 20%).

| Shareholder | Pre-Series-A ownership | Share of the remaining 65% | Final post-Series-A ownership |
|---|---|---|---|
| Founder A | 40% | 40% × 65% | 26% |
| Founder B | 40% | 40% × 65% | 26% |
| Seed SAFE investor (now converted to real shares) | 20% | 20% × 65% | 13% |
| New Series A investor | — | — | 20% |
| Option pool (for future employees) | — | — | 15% |
| **Total** | | | **100%** |

## What Actually Happened, in Plain Terms

The two founders started at 50% each. After one seed round and one Series A — with a
brand-new option pool created along the way — they're each down to 26%, a combined 52%.
That's a completely normal, healthy outcome for a company that's successfully raised two
rounds; it's not a sign anything went wrong. What it illustrates is exactly the point
Chapter 13 raised: think in advance about the ownership level at which you'd personally
start to feel demotivated, because two more rounds after this one (a Series B, a Series
C) will each dilute the founders further using the identical mechanism.

Notice, too, where the dilution actually came from at each step: the seed SAFE diluted
everyone equally once it converted, but the *option pool* at the Series A came
specifically out of the founders' and the seed investor's pre-existing stakes, not out of
the new investor's contribution — which is why option pool size is a real, negotiable
term worth understanding, not an afterthought to accept whatever a term sheet proposes by
default.

## Try It Yourself

Using this same method, model your own company's projected cap table:

1. Start with your actual or planned founder share count and split.
2. Add a seed round: pick a realistic raise amount and post-money cap for your stage
   and market, and calculate the resulting locked-in percentage.
3. Add a Series A: pick a realistic new-money amount and pre-money valuation, decide on
   an option pool size, and work through the same three-step division this appendix
   used.
4. Look at your own final founder percentage. If it's lower than you expected, that's
   worth knowing now — before you sign anything — rather than after.
