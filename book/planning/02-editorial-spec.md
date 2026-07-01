# Editorial Specification - How to Start a Startup: The Book

This is the contract every chapter must satisfy. Nothing gets marked "finalized" unless
it passes every section below.

## 1. Writing Style

Voice: first-person-plural-adjacent mentorship - an experienced founder explaining
things to a sharp engineer over coffee, not a professor lecturing or a consultant
presenting. Model: Paul Graham's essay cadence (short declarative sentences, occasional
dry wit, willingness to say "this is going to sound wrong, but-") crossed with Ben
Horowitz's comfort with hard truths and Andreessen's density-per-sentence.

Rules:

- Prefer short sentences. When a sentence needs a second clause, ask if it should be two
  sentences.
- No throat-clearing. Never open a section with "In today's fast-paced world..." or
  "It's important to note that..."
- Every abstract claim gets a concrete example within 2-3 sentences.
- First person ("I") is used only inside direct quotes/anecdotes attributed to a named
  speaker. The narrating voice is a neutral "we" or unmarked declarative.
- Humor is permitted where the source material has it, never manufactured where the
  source is flat.
- No AI-tell phrases, ever: "it's worth noting," "in the world of X," "at the end of the
  day," "let's dive in," "unpack," "navigate the landscape of," "delve." Banned-phrase
  list checked in the review pass.
- Contractions are fine. This is a book meant to be read, not a memo.

Register: assume the reader is smart, technical, and impatient with fluff, but has never
seen a cap table or a term sheet. Explain finance/business terms the first time they
appear, precisely, once, with an example, and then never re-explain (glossary and
cross-references handle repetition).

## 2. Chapter Template

Every chapter follows this skeleton:

1. Cold open (150-400 words) - a concrete scene, anecdote, or provocative claim from the
   source lectures that hooks the reader before any framework is introduced.
2. The core framework - the chapter's central idea(s), built up from first principles.
   Define every term on first use.
3. Why it's true / why it's counterintuitive - reasoning and evidence, not just
   assertion. Historical + modern examples side by side.
4. Common mistakes - a named list of ways founders get this wrong.
5. Tradeoffs and edge cases - where the framework doesn't apply, or where two pieces of
   advice in the book seem to conflict (reconciled explicitly - see Consistency Rule,
   Section 7).
6. Worked example (required for all of Part Five and any chapter introducing a formula)
   - real numbers, not hand-waving.
7. Chapter summary - 5-8 bullet takeaways, no new information introduced here.
8. Exercises (see Section 6).
9. Further reading - 1-3 pointers into the Bibliography for this chapter's topic.

Target chapter length: per the architecture doc's table. No chapter ships under 4,000
words or over 9,000 without explicit sign-off - if a topic wants to run longer, it gets
split, not stuffed.

## 3. Formatting Rules

- Headings: `##` chapter title, `###` major sections, `####` sparingly for subsections.
- Sidebars (`> **Sidebar: Title**`) used for: (a) "What's Changed Since 2014" notes, (b)
  tangential-but-preservable anecdotes compressed out of the main flow, (c) named
  essays/books referenced inline.
- Pull-quotes: direct quotes from named lecturers set off in blockquote format with
  attribution - load-bearing, not decoration, every one traceable to a specific lecture.
- Diagrams: used only where a relationship is genuinely spatial/structural - org charts,
  retention-curve shape, cap-table dilution waterfall, the idea x product x team x
  execution x luck formula, the sales funnel. Every diagram gets a one-line caption
  stating the takeaway.
- Tables: used for comparative or formulaic content (vesting schedules, SAFE vs. note
  vs. priced round, CAC/LTV formulas) - never for prose that could just be a paragraph.
- Numbers: all dollar figures and dates from the source lectures preserved verbatim and
  flagged with the year they were said, so the reader never mistakes a 2014 number for a
  current one.

## 4. Glossary Rules

- A term enters the glossary the first time it's used anywhere in the book, defined
  inline in the chapter AND given a glossary entry.
- On subsequent use, used freely - but the first occurrence in each new chapter gets a
  light cross-reference (e.g., "your cap table (Ch. 15)") if introduced more than 3
  chapters earlier.
- Glossary entries: one to three sentences, plain language, originating chapter cited.
- No orphan jargon: if a lecture uses a term the target reader won't know (ACRU,
  K-factor, 409A, FF stock) and the book uses it, it must appear in the glossary.

## 5. Diagrams and Visual Aids (Assigned by Chapter)

- Ch. 1: none (narrative chapter)
- Ch. 2: "Idea x Product x Team x Execution x Luck" formula visual; small-market ->
  concentric-expansion diagram
- Ch. 3: X/Y value-capture diagram (Thiel); monopoly-vs-competition spectrum
- Ch. 5: Barrels-and-ammunition diagram (Rabois)
- Ch. 7: MVP storyboard flow; the "honesty curve" (Cheung)
- Ch. 8: Wufoo-style feedback-loop diagram
- Ch. 10: Retention curve (asymptotic vs. decaying to zero) - central diagram of the book
- Ch. 11: Virality loop (payload x conversion x frequency); growth-channel funnel
- Ch. 14: Cap table dilution waterfall (new content)
- Ch. 15: Vesting schedule timeline (new content); SAFE conversion mechanics diagram
  (new content)
- Ch. 16: Sales funnel (prospect -> conversation -> close)
- Ch. 19: Editor's-role diagram (write vs. edit); task-relevant-maturity 2x2 (Rabois/
  Grove)
- Ch. 21: Org-structure-at-25-employees diagram

## 6. Exercises

Each chapter ends with 3-5 exercises in three categories, always in this order:

1. Recall (1 question) - a factual check that the core framework was understood.
2. Apply (2-3 questions) - apply the chapter's framework to a hypothetical or to the
   reader's own idea/company.
3. Confront a counterexample (1 question) - a case where the chapter's advice seems to
   fail, asking the reader to reason about why.

No multiple choice. No answer key - these are meant to be worked through like problem
sets, and manufactured "correct answers" to judgment questions would cheapen it.

## 7. Review Checklist (Every Chapter Must Pass Before "Finalized")

Fact-check pass:
- [ ] Every number, date, name, and quote traced back to a specific source lecture line
- [ ] Every claim about "what happened later" to a company verified against known
  outcomes
- [ ] Every new (non-lecture) example or statistic flagged as such and accurate as of
  the writing date

Consistency pass:
- [ ] No claim in this chapter contradicts a claim in another chapter without explicit
  acknowledgment and reconciliation
- [ ] Terminology matches the glossary exactly
- [ ] Cross-references to other chapters are accurate

Compression-integrity pass:
- [ ] Every fact/anecdote/number marked for compression in the architecture doc is
  verified present somewhere in the final text (main text, sidebar, or appendix) -
  nothing quietly vanished
- [ ] Historical specifics are explicitly time-stamped, not presented as current advice

Style pass:
- [ ] Banned-phrase list checked
- [ ] Chapter template sections all present and in order
- [ ] Reading level appropriate - no unexplained jargon on first use

Pedagogical pass:
- [ ] A reader with zero business background could follow this chapter without external
  lookups
- [ ] Chapter makes the reader "feel smarter" - at least one non-obvious insight beyond
  what a lecture summary would give
- [ ] Exercises actually test the chapter's core claims, not trivia

## 8. Quality Standard

Bar: this should read as if commissioned by O'Reilly or Stripe Press, editable and
shippable with only copyedit-level changes. Every chapter is written, then reviewed
against this spec as a hostile editor, then rewritten, before being marked finalized. No
chapter moves to "finalized" status with an outstanding checklist item.
