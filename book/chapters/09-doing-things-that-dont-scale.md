# Chapter 9 — Doing Things That Don't Scale

Stanley Tang and his cofounders spent an afternoon building a website called
PaloAltoDelivery.com. It had no backend, no driver algorithm, and no real infrastructure
of any kind. It was a single ugly page listing PDF menus they'd copied from local
restaurants, with one phone number at the bottom — their own personal cell phone. They
launched it without expecting much of anything.

Someone called. They wanted Thai food. Tang and his cofounder got in a car, bought the
food, and delivered it themselves to a stranger on Alpine Road, who turned out to be the
author of a book called *Weed the People*. It was, in Tang's own words, the best and
worst delivery they could have asked for. The next day, two more calls came in. Then
five. Then seven, then ten. That ugly, hour-old landing page became DoorDash.

Nothing about that first delivery scaled. There was no algorithm, no dispatch system, no
professional anything. That's exactly the point of this chapter: at the very beginning
of a company, the things that work are frequently the things that could never work at
a million users — and doing them anyway, deliberately and without embarrassment, is one
of the real advantages a small company has that a large one has already lost.

## The Core Idea: A Bridge, Not a Business Model

"Doing things that don't scale" describes a specific, narrow category: growth and
operations strategies that are genuinely unsustainable — they will not carry you to a
million users, and they're not supposed to. Walker Williams, who built Teespring the
same way, defines the category by where it breaks: usually time, sometimes money, always
eventually. The point isn't that these strategies are secretly efficient. The point is
that they're a bridge — the only available way to get from zero customers to enough
customers that a real, scalable strategy becomes possible at all.

Every founder eventually has to build the scalable version. The mistake this chapter is
about isn't failing to plan for scale. It's giving up the unscalable, ugly, personal
version too early — before it's actually stopped being useful — because it starts to feel
embarrassing, or beneath the company you're trying to look like.

## Why It's True: Testing Fast, Recruiting by Hand, and Building the Wrong Codebase on Purpose

### Test the hypothesis before you build anything real

DoorDash's own origin makes the case better than any abstract advice could: before
writing a single line of real infrastructure, Tang and his cofounders wanted to know
whether people would actually pay for restaurant delivery in Palo Alto at all. Rather
than guess, or research it, they built the cheapest possible real test — a landing page
with a phone number — and let actual behavior answer the question. No drivers were
hired in advance. No dispatch software was written. No assumptions were left unchecked
that could be checked in an afternoon instead.

This is worth separating clearly from over-planning. The test wasn't a business plan or
a slide deck estimating a total addressable market. It was a live, working (if barely)
version of the actual transaction, thrown at the smallest possible real audience, fast
enough that the answer came back in days instead of months.

### Hack the operations together with whatever's already on hand

Once real orders started arriving, DoorDash's actual operations ran on tools that were
never built to run a business. Tang and his cofounders were the delivery drivers
themselves, showing up between classes. There was no dispatch software — driver
locations were tracked using Apple's Find My Friends, an app built for keeping tabs on
your friends, not managing a delivery fleet. Orders were logged in a shared Google Doc.
Payments ran through Square, and the volume of small, rapid transactions grew fast
enough that Square's own systems flagged the account for suspected money laundering — a
problem resolved only because one of the cofounders happened to know people at Square
personally.

None of this was a considered strategy. It was whatever actually got food from a phone
call to a customer's door that same day. Tang offers one moment from this period that
captures its texture well: after wrapping up a meeting with a restaurant partner, the
team wanted to try a new ice cream shop that had just opened nearby. A text came in
asking for more drivers on the road immediately. The decision took about ten seconds —
they went to deliver, not to get ice cream — and Tang describes it as exactly the kind
of tradeoff this entire stage of a company runs on: do the unglamorous thing now, on the
promise that scaling far enough eventually buys you the ice cream too.

### There is no silver bullet for your first users

Walker Williams is blunt about a specific fantasy nearly every founder has starting out:
the belief that somewhere out there is a single, high-leverage channel — a viral
mechanic, an ideal partnership, an affiliate deal — that will make the first hundred
users appear with minimal effort. In his experience talking to founders across many
companies, that channel essentially doesn't exist. Even companies that look, from the
outside, like they had an effortless growth curve almost always had a period where the
first users were "impossibly hard to get."

Teespring's own beginning bears this out: in 2012, closing a sale meant days of back and
forth, free custom designs, and multiple rounds of revision, all to sell about fifty
shirts to a single nonprofit for roughly a thousand dollars in total revenue. Williams's
metaphor for this stage is pushing a boulder up a smooth hill: the incline is steepest,
and the effort required per unit of progress is highest, right at the very start. It
gets easier as you go — but only if you push through the beginning instead of waiting
for it to get easier on its own.

One specific trap to avoid at this stage, despite how tempting it looks: don't give the
product away for free to manufacture early traction. Free users behave differently from
paying ones in ways that create a false sense of security — a founder can convince
themselves that a free user will convert later, without ever testing whether that's
true. Early users need real, personal effort from the founder — cold emails, phone calls,
personal networks — not a price cut standing in for that effort.

### Turn early users into champions, and treat every failure as an opportunity to prove it

Getting a user is only half the job. The other half is turning them into someone who
actively tells other people about you — what Williams calls a champion. The most
reliable, if unglamorous, way to create champions is talking to users constantly and
personally. Williams, even once Teespring had scaled well past its earliest days,
continued to personally answer ten to twenty customer support tickets a day and read
through the company's entire social media mentions every night — not because it scaled,
but because it was the only way to actually understand what was breaking for real
customers.

There are three specific channels for this kind of contact worth naming: running support
yourself in the early days (Williams and his cofounder handled all of Teespring's
support personally until the company was doing well over $100,000 a month in revenue),
proactively reaching out to customers who've already left rather than only focusing on
new ones, and actively monitoring social media and online communities for both praise
and complaints. The asymmetry between the last two matters: a single, visibly unresolved
complaint can undo the goodwill of ten genuine champions, simply because a detractor is
louder and more memorable than nine quiet, satisfied customers.

The instinct when something goes wrong — a botched order, a mistake affecting a large
share of a month's revenue — is to minimize it, or explain it away as only partially
wrong. Teespring's own experience was the opposite lesson: customers who started out the
most frustrated by a real mistake, once that mistake was made right without excuses,
frequently became the company's longest-term and most vocal champions. Making a real
mistake fully right, rather than defending it, is one of the more reliable ways to create
a champion out of someone who had every reason to become a detractor instead.

### The product you launch with is not the product that scales

Once early demand is real, a second kind of "doesn't scale" work becomes necessary: the
product itself, as built, usually cannot survive contact with real growth, and the
engineering instinct to build it properly the first time can actively slow a company
down. Teespring's own example: a handful of larger nonprofit customers wanted enterprise
features the core product didn't have. Building those features the "right" way — cleanly
integrated into the existing platform — was estimated at about a month of engineering
time, which in a fast-moving startup is close to a year in ordinary time. Instead, the
company's CTO duplicated the entire codebase and database, built a separate, disposable
version of the product specifically for those customers, and shipped it in three to four
days. The features that turned out to matter were folded back into the core product
later, once real usage had shown which ones were actually worth keeping.

The underlying discipline here: worry only about the next order of magnitude, not the
final one. A company with ten users shouldn't be designing for a million; it should be
figuring out how to serve a hundred. Teespring went through real stretches where the site
crashed every single night, and the team slept with their phones on loud specifically so
they could wake up and restart the server — a genuinely painful, unsustainable practice,
and also, in Williams's own accounting, worth it, because it bought speed at a stage
where speed mattered more than stability.

The closing point Williams makes is the one this whole chapter is really about: there is
no natural milestone — not a funding round, not a revenue number — at which "doing things
that don't scale" is supposed to end on its own. The unscalable, personal version of
doing business is a genuine competitive advantage for as long as a company can keep doing
it, precisely because a smaller, hungrier competitor can still do it even after you've
grown past it. Williams's own framing: you shouldn't give it up voluntarily. It should
have to be taken from you, by growth that's outpaced your ability to keep doing it by
hand — not surrendered early because it started to feel beneath the company you're trying
to look like.

## Common Mistakes

- **Waiting for the perfect growth channel instead of manually finding the first
  customers yourself.** Williams's experience across many companies: that channel
  essentially never exists for the first users, no matter how it looks from the outside
  later.
- **Giving the product away for free to manufacture early traction.** This creates a
  false sense of momentum and doesn't test whether anyone would actually pay.
- **Explaining away or minimizing a real mistake instead of making it fully right.**
  Teespring's most frustrated early customers, once treated well, became some of its
  strongest champions — the opposite would likely have happened had the mistake been
  downplayed.
- **Building the "correct," fully scalable version of a feature before you know it's
  worth building at all.** Teespring's duplicated-codebase shortcut shipped in days what
  a proper integration would have taken a month to build, for a feature whose long-term
  value wasn't even confirmed yet.
- **Designing for the size you hope to be, instead of the size you actually are.**
  Optimize for the next order of magnitude, not the final one.
- **Abandoning manual, personal, unscalable work once it starts to feel embarrassing**,
  rather than continuing it until growth genuinely makes it impossible to keep doing.

## Tradeoffs and Edge Cases

**Isn't this the same lesson as Chapter 7's "manual before automated"?** Essentially
yes, and it's worth naming the connection directly rather than treating them as
unrelated: Homejoy's manual cleaner-vetting process (Chapter 7) and DoorDash's
founder-driven deliveries are the same underlying principle — expressed by two different
speakers, in two different lectures, about two completely different businesses. That
repetition across independent sources is itself evidence the principle is real rather
than a one-company anecdote. The angle is slightly different in each case: Chapter 7
frames manual work as a *learning* mechanism (you discover what to automate by doing it
by hand first). This chapter frames it as a *growth and resilience* mechanism (unscalable
effort is a genuine, temporary competitive advantage). Both are true at once, and both
usually apply to the same early-stage decisions.

**When does "doing things that don't scale" actually have to stop?** Not at a specific
funding round or revenue milestone, per Williams — but genuinely, eventually, once
growth outpaces what founders and a small team can keep doing by hand. The signal isn't
a calendar date. It's the same kind of signal Chapter 7 described for automating a
manual process: once you've learned enough, from doing something by hand, to know
exactly what the automated or delegated version should look like, that's the right time
to build it — not before, and not long after either.

**Does this conflict with Chapter 19's emphasis on building systems and dashboards?**
Not really — they apply at different stages, and the difference matters. This chapter is
about a company's earliest days, before there's enough signal to know what a good system
should even look like. Chapter 19 assumes a company has already learned those lessons and
is now building the durable infrastructure — dashboards, delegation, editing rather than
writing — to operate at a much larger scale. Skipping straight to Chapter 19's systems
thinking without first doing the unscalable, hands-on version this chapter describes
tends to produce systems built on guesses instead of real, hard-won evidence.

## Applying the Test

Take an idea you're considering, and design the ugliest, fastest, most personally
labor-intensive version of a real test for it — the way PaloAltoDelivery.com tested
DoorDash's core hypothesis in an afternoon. What's the equivalent of a landing page with
your personal phone number at the bottom? What would you personally have to do, by hand,
for the first ten customers, that a "real" version of the business would never ask a
founder to do forever?

Then ask the harder follow-up question: if that unscalable version actually worked,
would you be tempted to hand it off too early because it felt beneath what you were
building — or would you keep doing it until growth genuinely forced you to stop?

## Chapter Summary

- "Doing things that don't scale" describes deliberately unsustainable early strategies —
  a bridge to real traction, not a permanent operating model.
- Test a hypothesis with the cheapest possible real version of the product, the way
  DoorDash tested restaurant delivery with a landing page and a personal phone number.
- Early operations can run on borrowed consumer tools (Google Docs, Find My Friends,
  Square) — the goal is getting the transaction done today, not building it properly yet.
- There is no silver-bullet acquisition channel for your first users — expect to recruit
  them by hand, and don't give the product away for free to fake early traction.
- Turn early users into champions through constant, personal contact, and by making
  real mistakes fully right rather than minimizing them — a single unresolved complaint
  can undo many champions' worth of goodwill.
- The product you launch with is rarely the product that scales — optimize for speed,
  not clean architecture, until you know which features are actually worth keeping.
- Worry only about the next order of magnitude, not the final one.
- There's no natural milestone at which unscalable work is supposed to end voluntarily —
  it should be taken from you by growth, not given up because it feels beneath the
  company you're trying to look like.

## Exercises

1. **Recall:** Explain why Walker Williams argues there's no natural milestone — no
   funding round, no revenue number — at which a founder should voluntarily stop doing
   things that don't scale.
2. **Apply:** Design the cheapest, fastest, most personally labor-intensive real test you
   could run this week for an idea you're considering — your own version of
   PaloAltoDelivery.com.
3. **Apply:** Describe a real mistake (yours or a company you've used as a customer) that
   was either minimized or fully made right. What was the actual difference in how you,
   as the customer, felt afterward?
4. **Confront a counterexample:** This chapter argues you shouldn't give up unscalable,
   personal work voluntarily. But Chapter 19 will argue that building systems and
   delegating is essential once a company grows. How would you know, in the moment,
   whether you're avoiding a system you genuinely need — or correctly holding onto
   hands-on work you haven't outgrown yet?

## Further Reading

- Paul Graham's essay "Do Things That Don't Scale" is the origin of this chapter's title
  and covers additional examples beyond what Stanley Tang's and Walker Williams's
  lectures had time for.
- Chapter 7 covers the same underlying principle from a product-development angle
  (Homejoy's manual cleaner-vetting process) rather than this chapter's growth-and-
  resilience framing.
- Chapter 19 covers the systems and delegation practices that eventually replace the
  unscalable, hands-on work this chapter describes, once a company has genuinely
  outgrown it.
