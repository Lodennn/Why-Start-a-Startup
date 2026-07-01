*This is an optional interlude. It covers hardware and connected-device products
specifically — a narrower case than the software-only startups the rest of this book
focuses on. If you're building pure software, you can skip this and go straight to Part
Four. If you're building anything with a physical component — a wearable, a connected
device, anything in the "internet of things" space — this is for you.*

# Interlude — Building Hardware in a Software World

In 2010, the market for wireless speakers was, by Hosain Rahman's own account,
effectively zero percent of the overall speaker market. Bluetooth speakers barely
existed as a category. By Christmas of 2013, three years later, wireless speakers were
78% of the entire speaker market — a category that had existed in roughly its current
form since the 1950s, turned upside down in three years. Rahman's company, Jawbone,
built the product — the Jambox — that helped create that shift.

Here's the detail worth sitting with: if you had asked people in 2010 whether they
wanted a $199 wireless speaker for their phone, when a phone already had a speaker built
in for free, almost nobody would have said yes. That's not a hypothetical — Rahman is
direct that this is exactly what would have happened, and it's the same trap this book
has already named twice. Rahman's own illustration of the right way to ask: don't ask
someone "do you want a digital portable music player," ask "if you could put a thousand
songs in your pocket and take them anywhere, would that be cool?" Emmett Shear's Twitch
interviews
(Chapter 7) don't ask people if they'd use a proposed feature, because the honest-
sounding answer is nearly worthless. Hardware runs into this same problem, just with
higher stakes, because a bad guess costs months of tooling and manufacturing, not a
wasted sprint.

## The Core Idea: Hardware, Software, and Data, as Three Equal Legs

A hardware startup — especially anything connected, sensor-driven, or "smart" in the
now-familiar sense — has to be genuinely excellent at three different disciplines at
once, not one. **Hardware**: a physical object good enough that someone will actually
keep it on or nearby all the time, since a wearable left in a drawer collects no data and
solves no problem. **Software**: an application layer with the same bar for engagement
as a pure software company's product — Rahman's own comparison point is Instagram and
WhatsApp, not other hardware companies. **Data**: the ability to actually do something
useful with everything the hardware is sensing, rather than just displaying numbers back
at the user.

Most companies are naturally strong at one of these and weak at the other two — people
who build great hardware tend to come from a mechanical and electrical engineering
background, with a completely different skill set and completely different production
cycle than people who build great software. Combining the two into one team, Rahman is
candid, creates real internal friction: hardware teams have to learn to move faster than
their instincts want to, and software teams have to learn to think through problems more
completely before shipping, since a hardware bug can't be patched with a Friday-afternoon
deploy.

## Why It's True: The WHYs Framework, and Asking About Behavior Instead of Features

### The WHYs: a single question that governs every product decision

Jawbone's internal process for deciding what to build centers on a question they call
the WHY: what specific user problem does this solve, such that once it's solved, the
user genuinely can't live without it. Every product decision gets tested against this
question repeatedly, at every stage, rather than being decided once at the start and
assumed to hold.

This connects directly to a lesson this book has already covered from a completely
different industry: you cannot get a reliable answer to the WHY question by asking users
directly. The parallel to Chapter 2's "one sentence" test and Chapter 7's "ask about
behavior, not features" is exact, and Rahman states the hardware version of it plainly:
the questions that actually produce insight aren't "would you pay for this," but
questions about existing behavior — how often do you listen to music around other
people, do you use headphones or a speaker, how often do you want a personalized versus
a shared experience. The underlying problem the product solves gets found by
understanding behavior deeply enough to notice the gap yourself; it doesn't get handed
to you by a user filling out a survey about a feature that doesn't exist yet.

### Track, understand, act: turning sensors into a reason to keep wearing something

Jawbone's wearable health products (UP, then UP24) organize around a three-part
framework worth borrowing for any sensor-based product: **track** (the hardware and
sensor layer — batteries, materials, the physical habit of actually keeping the device
on), **understand** (turning raw sensor data into something a person can actually
interpret — a heart rate of 75 means nothing on its own; whether it's good or bad
depends entirely on context), and **act** (turning that understanding into a concrete
behavior change, like a well-timed notification suggesting a workout at the time of day
the data shows it actually helps that specific person sleep better).

Data on its own, without the "understand" and "act" layers built on top of it, isn't a
product. It's a stream of numbers a user will stop looking at within a week. The
discipline this framework enforces is refusing to ship the "track" layer alone and
calling it done.

### Resolving tradeoffs across an entire system, not one team at a time

A hardware product is a system in a more literal sense than most software products are:
a decision in battery design affects sensor performance, which affects signal
reliability, which affects what the software layer can promise a user. Rahman's account
of building a later-generation wearable (UP3) with an entirely new sensing system
involved daily three-hour calls between hardware, sensing, and software engineers, for
months, specifically to negotiate these tradeoffs in the open rather than let one team
make a decision in isolation that quietly broke another team's plan. This is slower and
more painful than most software-only development, and it's not optional — a hardware
product that ships with an unresolved tradeoff between, say, battery life and sensor
accuracy can't be patched the way a software bug can.

## Common Mistakes

- **Asking users directly whether they'd want or pay for a proposed hardware feature.**
  The Jambox itself would have failed this test in 2010 — nobody asks for "a thousand
  songs in your pocket" or "a $199 phone speaker" until they've experienced why it
  matters.
- **Treating hardware, software, and data as separate teams with separate roadmaps**,
  rather than one integrated system where a decision in one area constrains the others.
- **Shipping the sensor ("track") layer of a product without the "understand" and "act"
  layers**, and mistaking a stream of raw data for a finished product.
- **Letting one team resolve a system-wide tradeoff in isolation**, rather than
  negotiating it openly across hardware, software, and data teams before committing to
  it.

## Tradeoffs and Edge Cases

**Should a software-focused founder ever choose the hardware path in the first
place?** This deserves an honest answer, not just enthusiasm for the category. Hardware
development cycles are dramatically slower than software — tooling alone can take
sixteen weeks per iteration, compared to a software team that can ship and learn from a
change within a day. Chapter 17's advice about speed, momentum, and rapid iteration
still applies conceptually, but the unit of iteration is months, not days, which changes
the entire cadence of a company. Chapter 2 already flagged that some categories
genuinely require more capital and a longer runway before they work at all; hardware is
usually one of them. This interlude isn't arguing you should build hardware — it's
covering how to do it well if the idea genuinely requires a physical product, which
some real, valuable ideas do.

**Does the WHYs framework replace the monopoly and market-sizing arguments from earlier
chapters?** No — it operates one level down. Chapters 2 and 3 are about *which* market
and business to build toward. The WHYs framework is about deciding *what specific
product decision* serves that strategy, once the strategic question is already
answered. A hardware company still needs a real answer to "why now" and a plan for
durability, the same as any other startup this book covers.

## Applying the Test

Take a hardware or connected-device idea you're considering. Write down the direct
version of the pitch — "would you pay for X feature" — and then rewrite it the way
Rahman's team would: as a question about existing behavior instead. What do people
already do, physically, around the problem your device addresses? Then check your idea
against the track-understand-act framework: does it just track something (a number with
no context), or does it also help a user understand what that number means and act on
it in a way that changes their behavior? A product stuck at "track" is a sensor, not yet
a reason for anyone to keep wearing it.

## Chapter Summary

- A hardware company needs to be excellent at three disciplines at once — hardware,
  software, and data — not just one, and combining all three on one team creates real,
  manageable friction between different working cultures.
- The WHYs framework tests every product decision against one question: what problem
  does this solve that makes it something a user can't live without.
- You cannot get a reliable answer to that question by asking users directly whether
  they'd want a feature — ask about existing behavior instead, the same lesson Chapters
  2 and 7 already established from completely different industries.
- Track, understand, act: sensor data alone isn't a product. It becomes one once a user
  can understand what the data means and act on it to change their behavior.
- Hardware tradeoffs have to be resolved across the whole system, in the open, because
  one team's decision constrains what every other team can promise.
- Hardware's iteration cycle is measured in months, not days — a real, structural
  difference from the software-only startups this book otherwise focuses on.

## Exercises

1. **Recall:** Explain why asking "would you pay for this hardware feature" produces an
   unreliable answer, using the Jambox's own 2010 launch as your example.
2. **Apply:** Take a hardware or connected-device idea and run it through the
   track-understand-act framework. Which layer does your current concept actually
   reach, and what would the next layer require?
3. **Apply:** Pick a sixteen-week tooling cycle constraint (real or assumed) for a
   hardware idea you're considering, and sketch what you'd need to validate through
   software or a non-manufactured prototype before committing to that cycle — the same
   discipline this interlude argues Rahman applied before shipping the Jambox.
4. **Confront a counterexample:** This interlude argues hardware requires a fundamentally
   slower iteration cycle than software. Are there hardware categories where this isn't
   true — where iteration can happen nearly as fast as software — and what would need to
   be true about the product for that to work?

## Further Reading

- Hosain Rahman's original CS183B lecture covers Jawbone's full development process —
  exploration, validation, concept, and development phases — in more detail than this
  interlude's condensed version.
- Chapter 2 and Chapter 7 cover the "ask about behavior, not features" principle this
  interlude borrows, from a software-only perspective.
