# Chapter 15 — Legal and Financial Mechanics

A Y Combinator company once incorporated as an LLC in Connecticut, on the advice of a
local lawyer, and was told to convert to a Delaware corporation once it joined YC — the
standard structure nearly every venture-backed startup uses. The conversion paperwork,
filed by that same local law firm, contained a small, technical mistake. The company
believed, for roughly two years, that it was a Delaware corporation. It wasn't. The error
surfaced only when the company was raising a large round of financing and its lawyers
started digging through the cap table in detail. Untangling it required four separate
law firms across two states. The bill came to roughly half a million dollars, for a
mistake that would have cost nothing to avoid in the first place, by simply using a
standard, well-tested structure from day one.

This chapter is not the most exciting one in this book. It's arguably the one where a
mistake is most expensive, precisely because these mistakes tend to surface at the worst
possible moment — during a fundraise, an acquisition, or a founder dispute — rather than
quietly, when they'd be cheap to fix. The goal here is not to make you a lawyer or an
accountant. It's to make sure you understand this material well enough to know when
something needs a specialist's attention, and well enough that a specialist can't quietly
take advantage of you by burying a real problem in language you don't understand.

## Before Anything Else: Reading a Business's Financial Vocabulary

Founders in this book's audience are assumed to have zero business background, so before
covering startup-specific mechanics, it's worth building the basic vocabulary that
everything else in this chapter — and the fundraising chapters before it — depends on.

A **profit and loss statement** (P&L, sometimes called an income statement) shows
revenue coming in, expenses going out, and the difference between them over a period of
time — a month, a quarter, a year. A company that's losing money simply has expenses
larger than revenue on this statement; that's normal and expected for most early-stage
startups, not automatically a sign of trouble.

A **balance sheet** is different — it's a snapshot at a single moment, not a period of
time. It shows what a company owns (assets: cash in the bank, equipment, money owed to
it) against what it owes (liabilities: unpaid bills, debt) and what's left over
(equity — the value that belongs to the founders and investors).

A **cash flow statement** tracks actual cash moving in and out of a bank account, which
is a different number from the P&L's "profit," because a P&L counts revenue when it's
earned, not necessarily when the cash actually arrives. A company can show a profit on
paper and still run out of actual cash, if customers are slow to pay.

Two more terms matter more to an early startup than almost anything on the statements
above: **burn rate** is how much cash a company spends, net, every month, beyond what it
brings in. **Runway** is how many months of cash remain at the current burn rate before
the company runs out of money entirely — literally, cash in the bank divided by monthly
burn. Every founder should be able to state their own runway, in months, without having
to go look it up. It's the single number that determines how much time exists to hit the
next milestone before a company is forced into an emergency fundraise, or worse.

## The Core Idea: Keep It Standard, So You Can Stop Thinking About It

Every recommendation in this chapter follows from one underlying principle, stated
plainly by Carolynn Levy and Kirsty Nathoo, who handle exactly this kind of work for
Y Combinator companies: use the most standard, most common structure available at every
decision point, and save your actual attention for the parts of the business that are
genuinely novel. A startup's legal and financial structure is not the place to be
creative. The Connecticut-LLC story above is what happens when a founder treats a
solved, standardized problem as though it needed a custom solution.

## Why It's True: Incorporation, Equity, Fundraising Documents, and the Rules of Being an Employer

### Incorporation: Delaware, for reasons that compound over time

A startup needs to exist as a separate legal entity, mainly to protect its founders from
personal liability if the company is ever sued — the company's assets are at risk, not
the founders' personal bank accounts. Delaware is the default choice for nearly every
venture-backed startup, not because of any special local advantage, but because
Delaware's corporate law is unusually well-tested and predictable, and because investors
are already comfortable with it — every deviation from that default adds friction and
cost to every future financing round, exactly the kind of avoidable cost the opening
story illustrates.

Actually incorporating involves a handful of standard documents: articles of
incorporation (the two-page filing that creates the shell), bylaws, a board of directors,
officer titles (Delaware requires a CEO, President, and Secretary to be named, even at a
two-person company), and IP assignment agreements — paperwork confirming that anything a
founder invents or codes belongs to the company, not to them personally. Services like
Clerky handle this with standard, inexpensive templates; there's rarely a good reason to
pay a law firm to draft custom versions of documents this well-trodden. Whatever gets
signed, keep the signed originals somewhere safe and organized — the moment they matter
most is almost always a high-stress one, like a due-diligence process during a large
fundraise or an acquisition, and "we're not sure where those are" is a genuinely bad
thing to have to say at that moment.

### Equity: split close to equal, and vest everyone including yourself

Chapter 4 already covered the *decision* to split cofounder equity close to equally, and
to make that decision early. This section covers the mechanics that actually implement
that decision.

First, a founder doesn't simply own shares by agreeing to found the company — buying
shares from the company (in exchange for cash, or for assigning IP and past work to it)
is a real, two-way legal transaction, formalized in a stock purchase agreement. Skipping
this step because "we already agreed on the split" is a common and avoidable mistake.

Second, that stock is almost always **restricted stock** — meaning it vests over time,
rather than being fully owned the moment it's purchased. The standard structure in
Silicon Valley is **four years, with a one-year cliff**: nothing vests until the first
anniversary of the grant, at which point 25% vests all at once, and the remaining 75%
vests monthly over the following three years.

**Table: A founder's vesting timeline on a standard 4-year grant with a 1-year cliff**

| Time since grant | Percentage vested | What happens if the founder leaves now |
|---|---|---|
| Before 12 months | 0% | Company repurchases 100% of shares at original price |
| Exactly 12 months (the cliff) | 25% | Founder keeps 25%; company repurchases the remaining 75% |
| 24 months | 50% | Founder keeps 50%; company repurchases the remaining 50% |
| 36 months | 75% | Founder keeps 75%; company repurchases the remaining 25% |
| 48 months | 100% | Founder keeps all of it — nothing left to repurchase |

Vesting exists for a specific reason: without it, a founder who leaves after a few
months walks away with a permanent, full share of a company they no longer work on,
which is both unfair to the founders who stayed and, in practice, close to fatal for
future fundraising — investors will rarely fund a company with a large, inert equity
stake sitting with someone no longer involved. This applies to solo founders too, not
just teams: an unvested solo founder sets the wrong precedent for every future employee
whose own equity will vest, and signals a level of commitment investors will specifically
check for.

One more filing deserves special attention because it can't be fixed later if missed: the
**83(b) election**, a one-page IRS form that must be filed within 30 days of receiving
restricted stock. Filing it locks in a founder's tax basis while the company's value is
still low (often close to zero), rather than owing tax later based on the stock's value
each time a chunk vests, which can turn into a serious, avoidable tax bill as the company
becomes more valuable. Missing this specific 30-day window is one of the few mistakes in
this chapter that genuinely cannot be undone after the fact — send it certified mail, and
keep the proof.

### Fundraising documents: what you're actually signing

Chapters 13 and 14 covered the strategy and the pitch. This section covers what the
paperwork that follows an investor's "yes" actually says.

An **unpriced round** — usually called a seed round — doesn't set an exact valuation for
the company. Instead, an investor signs a **SAFE** (simple agreement for future equity)
or a **convertible note**, handing over cash now in exchange for the right to receive
actual shares later, once a **priced round** (typically a Series A or later) sets a real
valuation for the first time. Until that conversion happens, a SAFE or note holder isn't
a shareholder yet and has no voting rights — they're holding a promise of future shares,
not shares themselves.

The mechanism that rewards an investor for taking on early risk is the **valuation
cap**: an upper limit on the valuation used to calculate how many shares their investment
converts into, regardless of what the company is actually worth by the time a priced
round happens. Here's the mechanic worked through with real numbers:

> An investor puts in $100,000 on a SAFE with a $5 million valuation cap. A year later,
> the company raises a priced Series A at a $20 million valuation. Because the SAFE
> converts at the *lower* of the cap or the actual round price, this investor's $100,000
> converts as though the company were worth $5 million, not $20 million — roughly four
> times more favorable than a new investor coming in at the $20 million price for the
> same dollar amount. That better price is the reward for having taken the risk of
> investing before there was a real valuation to point to.

The dilution this produces is easy to underestimate if you don't run the numbers in
advance. Suppose a company raises $2 million across several SAFEs, all with a $6 million
cap. Under the cap convention this course described — where the cap is treated as a
*pre-money* figure, meaning the money being raised gets added on top of it — the
resulting post-money value at conversion is $6 million plus the $2 million raised,
or $8 million, and the SAFE holders collectively own $2 million ÷ $8 million: roughly
**25%** of the company once those SAFEs convert (not simply $2 million divided by the $6
million cap, which is a different, larger number — the extra step of adding the raise
to the cap first is exactly the calculation a pre-money-style cap requires, and exactly
the calculation the newer post-money SAFE format was designed to make unnecessary). If
the same priced round that triggers this conversion also brings in new investors who
want to own 20% of the company themselves, the founders have now given up close to 45%
of the company in a single round — a number that's easy to miss if you only look at the
priced round's headline terms and forget to add back everything that was already
promised through earlier SAFEs.

Appendix A works through a complete, multi-round version of this same math in detail —
founding through a Series A, with actual share counts — using the cleaner post-money
SAFE convention described in the note below, specifically so the arithmetic at each step
stays checkable rather than compounding into the kind of easy-to-miss error this section
just walked through by hand.

> **A note on how this has evolved:** the mechanics above reflect the standard structure
> at the time this course was taught. Since then, Y Combinator introduced an updated,
> "post-money" version of its standard SAFE template, specifically to make this kind of
> dilution easier for founders to calculate in advance rather than after the fact. The
> underlying tradeoff — a valuation cap rewards early risk, and stacking several rounds
> of SAFEs compounds dilution in ways worth modeling before you sign — hasn't changed.

Investors typically ask for a few standard things beyond the core investment, and it's
worth knowing which requests are normal and which deserve real pushback. A **board seat**
request should usually be declined unless the specific investor will add real, ongoing
strategic value — a board seat isn't a favor to hand out for the size of a check alone.
**Advisor** arrangements should generally come free with an investment, not require
additional equity on top of it; an investor asking for extra shares in exchange for
occasional introductions is, bluntly, asking for a freebie. **Pro-rata rights** — the
right to invest again in future rounds to maintain a fixed ownership percentage — are
common and not inherently a bad request, but they do mean founders bear correspondingly
more dilution over time as investors exercise that right. **Information rights** —
regular updates, typically monthly — are reasonable and often genuinely useful, since
investors who are kept informed can help with introductions and hiring; a request for
weekly reports or granular budget oversight has usually crossed into overreach.

### Running the business: whose money is it, and who's actually an employee

Once money is in the bank, it belongs to the company, not personally to the founders —
a distinction that sounds obvious and is nonetheless violated often enough that Nathoo
and Levy tell a specific cautionary story about it: a founder who used investor money for
a personal trip to Las Vegas is, in their blunt framing, no longer with the company, and
for good reason — that's not a gray-area expense, it's converting investor money to
personal use. The practical test for anything less obviously egregious: if you had to
read an investor a line-by-line list of what you spent their money on, would any single
line embarrass you? If yes, it's probably not a legitimate business expense.

Founders themselves are legal employees of the company they founded, not exempt from
labor law by virtue of being the boss — which means founders must actually be paid, at
least a minimum wage, and the company must handle payroll taxes on that pay correctly.
Skipping this is not a minor technicality: one company that avoided payroll taxes on
founder pay for three years created a serious, expensive legal problem for itself, with
criminal liability a real (if rare) possibility in extreme cases. A related, less obvious
cost of skipping this: if a cofounder relationship later breaks down and one founder is
let go, unpaid wages become real leverage for that departing founder to extract extra
equity or vesting acceleration in exchange for signing a release — a problem this section
of the chapter, alongside Chapter 4's advice to decide vesting and equity early, exists
specifically to prevent. The practical fix is simple: run payroll properly for founders
from day one, the same as for any other employee, and treat the arrangement with the same
seriousness Nathoo and Levy suggest thinking of as a "marital pre-nup" for the
relationship — decided in advance, not renegotiated under stress later.

Hiring anyone else requires knowing whether they're a **contractor** or an **employee**,
a distinction the IRS cares about and penalizes getting wrong. A contractor sets their
own hours and location, uses their own equipment, works toward a defined deliverable, and
receives a 1099 form at year-end with no taxes withheld by the company. An employee has
taxes withheld by the company and receives a W2. Both need to sign IP assignment
agreements; only one of them requires the company to carry workers' compensation
insurance and verify legal work authorization. A payroll service (rather than manually
handling this) is worth paying for from the first hire — the cost of getting this wrong,
as with the three-year payroll-tax story above, is far larger than the cost of the
service itself.

Firing someone, when it's necessary, should happen quickly rather than being delayed —
Chapter 5 already covered why waiting is usually worse for everyone involved, including
the person being let go. The legal and financial mechanics that go with a firing: pay all
outstanding wages and accrued vacation immediately, since this is a legal requirement in
most places, not a negotiable timeline; cut off physical and digital access right away,
including shared accounts (one company learned this the hard way when a departing founder
held the company's GitHub account password as leverage during a dispute); and repurchase
any vested shares from a departing employee promptly, per the terms already set by their
vesting agreement.

## Common Mistakes

- **Using a non-standard entity structure or state of incorporation to save a small
  amount of money upfront.** The Connecticut LLC story is the clearest illustration of
  how a small shortcut here compounds into an enormous cost later, right when the
  company can least afford the distraction.
- **Treating a founder's cofounder agreement as settled without buying the stock and
  putting vesting in place.** A verbal agreement on equity split isn't the same as an
  actual, documented, vesting stock purchase.
- **Missing the 83(b) election's 30-day window.** This is one of the only mistakes in
  this chapter that cannot be fixed after the fact.
- **Looking only at a single round's headline dilution, without modeling the cumulative
  effect of prior SAFEs or notes converting at the same time.**
- **Spending investor money in a way you'd be embarrassed to itemize for them directly.**
- **Not paying founders a real salary, or not running proper payroll**, which creates
  both a legal liability and, in the event of a founder dispute, real leverage for the
  departing founder.
- **Misclassifying an employee as a contractor (or the reverse)**, which the IRS
  penalizes and which leaves the company without required protections like workers'
  compensation coverage.

## Tradeoffs and Edge Cases

**Is Delaware always the right choice?** For the venture-backed, hyper-growth companies
this book focuses on, yes, close to universally — the benefits of investor familiarity
and legal predictability outweigh any state-specific advantage almost every other state
might offer. A small business not pursuing outside venture capital has more real
flexibility here, since it will never face a Delaware-sophisticated investor's due
diligence process in the first place.

**Do solo founders really need the same vesting discipline as teams?** Yes, for reasons
distinct from the team case. A team needs vesting to protect against one founder leaving
with a large, unearned stake. A solo founder needs it for a different reason: it signals
real commitment to investors, and it sets the correct precedent for every employee who
joins later and will be expected to vest their own equity the same way.

**Are all investor requests for extra rights (board seats, pro-rata, information)
red flags?** No — the point of this chapter isn't that every request should be refused.
It's that each request should be evaluated on whether it reflects real, ongoing value
(a board seat from someone who will genuinely help), a standard and reasonable ask (basic
information rights, pro-rata), or overreach dressed up as a normal request (an advisor
wanting extra equity for occasional introductions). Treating every request identically,
in either direction, misses the actual judgment this section is trying to teach.

## Applying the Test

Using this chapter's dilution table as a template, build your own rough cap table
projection for your actual or hypothetical company across a seed round and a Series A.
Include an employee option pool of 10–15% at the Series A stage. What's your own
realistic ownership percentage after both rounds, and does that number still feel
motivating? If the honest answer is no, that's exactly the signal Chapter 13 warned
about — worth addressing at the term-sheet stage, not after the round has already closed.

## Chapter Summary

- Learn the basic financial vocabulary — P&L, balance sheet, cash flow, burn rate,
  runway — before anything else in this chapter; every founder should know their own
  runway in months without looking it up.
- Use standard, well-tested structures (Delaware incorporation, standard vesting, Clerky-
  style templates) rather than custom solutions — the Connecticut LLC story shows how
  expensive a shortcut here can become.
- Vesting (typically four years with a one-year cliff) protects the company from a
  founder leaving early with a large, unearned stake, and applies to solo founders too.
- File the 83(b) election within 30 days of any restricted stock grant — one of the few
  mistakes in this chapter that can't be corrected after the fact.
- A valuation cap on a SAFE or note rewards early investors with a better effective
  price once a priced round sets a real valuation — model the cumulative dilution across
  multiple rounds before you sign, not just the headline number of the round you're
  currently negotiating.
- Evaluate investor requests (board seats, advisor equity, pro-rata rights, information
  rights) individually, based on real value versus overreach, rather than accepting or
  rejecting all of them uniformly.
- Founders are real employees who must be paid and covered by proper payroll — skipping
  this creates both tax liability and leverage for a departing cofounder later.
- Contractors and employees are legally distinct categories with different tax and
  insurance obligations — get the classification right from the first hire.

## Exercises

1. **Recall:** Explain what a valuation cap actually does, using the worked $100,000-on-
   a-$5-million-cap example from this chapter.
2. **Apply:** Calculate your own company's current runway (or a hypothetical one) in
   months, using the burn-rate definition from this chapter's opening section.
3. **Apply:** Build a simple projected cap table across a seed round and a Series A for
   your own company, including an option pool, using this chapter's worked table as a
   template.
4. **Confront a counterexample:** This chapter argues board seats should usually be
   declined unless an investor adds real ongoing value. Under what specific
   circumstances would giving up a board seat actually be the wrong call, even for an
   investor who isn't especially strategic?

## Further Reading

- Y Combinator's own published library of standard startup legal documents (the same
  templates referenced throughout this chapter) is the most direct, practical next step
  for founders about to incorporate or raise a round.
- Appendix A of this book expands the cap table walkthrough in this chapter into a
  full, multi-round numeric example with an employee option pool included at each stage.
- Appendix B covers how to read an actual term sheet clause by clause, building directly
  on the vocabulary this chapter introduces.
