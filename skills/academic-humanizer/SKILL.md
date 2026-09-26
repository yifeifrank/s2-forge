---
name: academic-humanizer
description: Revise academic, scholarly, scientific, and technical prose so it reads as deliberate, natural authorial writing while preserving meaning, evidence, citations, terminology, formatting, and causal certainty. Use whenever the user asks to humanize, de-AI, polish, tighten, edit, rewrite, or improve a paper, manuscript, abstract, literature review, methods section, results section, report, thesis, reviewer response, or other scholarly text; asks to remove AI-sounding language, generic transitions, excessive hedging, defensive writing, repetitive structure, or inflated wording; or supplies academic prose for stylistic revision even without naming this skill.
---

# Academic Humanizer

Revise supplied prose into deliberate, natural scholarly writing. Preserve the author's intellectual position and recognizable voice. Make the smallest changes needed to solve the stated problem.

Edit for clarity and authorial quality, not for an AI-detector score or to conceal provenance.

## Establish the Editing Contract

Before revising, infer the passage's function and the user's requested scope. A paragraph may state a finding, motivate a method, interpret evidence, acknowledge a limitation, review literature, or advance an argument. Preserve that function.

Use these defaults unless the user specifies otherwise:

- Preserve meaning, evidence, citations, technical terms, and causal certainty.
- Keep the original organization, section boundaries, and formatting.
- Prefer a light edit over a wholesale rewrite.
- Match any writing sample or surrounding manuscript text the user provides.
- Return only revised text unless the user requests commentary.
- Keep editorial diagnoses, newly inferred limitations, and declarations of weakness out of the revised main text.

If a requested stylistic improvement would require new evidence or a substantive change in interpretation, do not make that change. Preserve the author's original claim and flag the concern outside the article when necessary.

## Non-Negotiable Preservation

Do not invent or silently alter facts, examples, citations, numbers, definitions, results, interpretations, or methodological details.

Preserve exactly unless the user requests a substantive correction:

- Citation keys, citation syntax, and evidence placeholders
- LaTeX commands, labels, cross-references, equations, and table or figure references
- Defined terminology, abbreviations, symbols, and variable names
- The distinction between association, prediction, explanation, and causation
- The original degree of confidence or uncertainty

Define an abbreviation at first use only when the surrounding document does not already define it. Use terms consistently after definition.

## Core Editing Rules

### Lead with substance

Open with the claim, finding, question, or action that matters. Remove throat-clearing such as "In today's rapidly changing world," "It is important to note," "This paper aims to," and similar preambles when they add no content.

Do not strip necessary orientation. Keep context that identifies the problem, population, time period, comparison, or analytical purpose.

### Ground claims in evidence

Retain citations and evidence placeholders next to the claims they support. Replace vague generalizations with concrete information already present in the source. If the source does not support greater specificity, do not fabricate it.

Distinguish observed results from interpretation. Do not present an interpretation as though it were directly measured.

Do not insert a new evidentiary caveat into the article merely because the design appears weaker than the wording. Preserve the author's claim and raise the concern separately for the user.

### Preserve inferential position while calibrating prose

Treat the finding's causal, associational, predictive, or descriptive position as author-controlled. A request to humanize, polish, tighten, or improve style does not authorize changing that position.

Within the author's existing inferential position, make certainty language concise only when the replacement has the same substantive force. Preserve the author's choice among terms such as "show," "suggest," "may," "mixed," and "inconclusive."

Remove a hedge cascade such as "may possibly suggest" only when doing so does not make the claim stronger or weaker. If equivalence is uncertain, retain the original wording and raise the issue outside the article.

### Keep editorial diagnosis outside the article

Do not add limitations, defenses, justifications, disclaimers, declarations of weakness, or reviewer-style criticism to the main text unless the user explicitly asks for them. This includes newly inferred concerns about identification, causal interpretation, robustness, generalizability, measurement, specification choice, or data quality.

If the source already contains a limitation or justification, treat it as authored content and preserve its meaning unless the user asks to remove it. Edit it concisely and plainly. Its presence in the supplied article counts as permission to retain it, but not to expand it with new criticism.

When the source already explains an analytical choice, state its purpose prospectively, such as "to capture," "to distinguish," or "this specification allows us to estimate." Do not invent a defense for the choice or make it sound like an ex post justification.

If an editorial concern materially affects the claim, report it to the user outside the article. For example, if a regression does not appear to support a causal interpretation, do not insert that diagnosis into the revised paragraph or silently weaken the claim. Preserve the requested article text and place the concern in a clearly separated author note.

### Separate the article from its production record

Present the research in its final analytical form. Keep version-control and revision histories, debugging notes, correction logs, case-specific fixes or overrides, implementation quirks, operational version/export dates, file hashes, local paths, packaging/build instructions, and technical limitations of tools or workflows in a separate technical report, outside both the main text and scholarly appendices. Do not add a manuscript citation, link, or aside pointing to that report unless the user or submission requirements request it.

Retain information needed to interpret or evaluate the research: data coverage, variable definitions, sample selection, model specifications, uncertainty, substantive sensitivity analyses, and scientifically relevant software/model or dataset identifiers. Distinguish these from the chronology of how files and analyses were produced. Describe the method used, not the sequence of fixes that produced it. If a case-specific adjustment changes sample eligibility or measurement, retain its analytical rule where needed while moving the individual debugging narrative to the report.

When moving operational material out, preserve it in the technical report rather than discarding it. Keep unresolved errors and discrepancies explicit there and in author-facing communication; do not imply that relocating a correction note repairs inconsistent data, estimates, or tables. Do not silently alter results or remove necessary methodological qualifications to make the article appear cleaner.

### Match the author's voice

Aim for moderately formal, compact, precise prose unless the supplied text indicates another register. Preserve recognizable wording and natural local flow where they work.

When a writing sample is available, match its sentence length, vocabulary, paragraph openings, punctuation, and transitions. Do not impose generic templates, unnecessary headings, or mechanical signposting.

### Remove formulaic AI patterns

Revise patterns that recur mechanically or add no analytical value:

- Formulaic "rather than" constructions
- Repeated "not X, but Y" contrasts
- "Not only ... but also" scaffolding
- Habitual lists of exactly three
- Repeatedly symmetrical or parallel sentences
- Paragraphs built from the same syntactic template
- Em dashes used as a default connective
- Empty participial endings such as "highlighting," "underscoring," or "demonstrating"

Do not ban these forms mechanically. Keep one when it is the clearest and most natural construction in context.

### Prefer concrete language

Name identifiable actors, actions, mechanisms, measures, and outcomes where the source permits. Scrutinize inflated or vague words such as "crucial," "pivotal," "vital," "robust," "seamless," "landscape," "realm," "leverage," "delve," "underscore," "highlight," "multifaceted," "comprehensive," and "transformative."

Retain a word when it has a precise disciplinary meaning. Replace it when it substitutes emphasis for information.

### Vary rhythm naturally

Use short sentences for direct claims and longer ones for necessary qualification or synthesis. Vary paragraph openings, transitions, and list lengths when the original becomes monotonous.

Do not force variation. Parallel form is useful when the ideas themselves are parallel.

### Remove repetition

Delete sentences that merely announce, preview, or repeat nearby content. Combine overlapping claims when doing so preserves their evidentiary distinctions.

Keep a conclusion only when it adds an implication, limitation, synthesis, or genuine analytical advance.

### Take a clear analytical position

Make the passage's existing judgment or inference legible without changing it. Do not manufacture balance by adding alternatives that do not materially affect the argument. Do not introduce competing explanations unless the author has included or explicitly requested them.

Do not add anecdotes, opinions, or unsupported interpretations to create personality.

### Preserve scholarly discipline

Use a conservative preservation rule: do not shift a finding among causal, associational, predictive, or descriptive positions unless the author explicitly authorizes the specific shift. Do not infer authorization from the evidence, research design, reviewer expectations, or a general request for editing.

Do not upgrade a correlational or descriptive claim into causal language. Do not downgrade an existing causal claim into associational or descriptive language. Do not broaden or narrow the stated population, design, evidentiary scope, or generalizability. Preserve these choices exactly and flag any concern outside the article.

Change an inferential position only after the author explicitly permits the substantive change and agrees to the proposed direction. Treat this as a rare exception. When permission is ambiguous, preserve the original position and ask rather than changing the article.

Keep definitions and labels stable throughout the passage.

Do not change section structure, results, or formal notation merely for stylistic variety.

## Editing Procedure

1. Identify what each paragraph is doing and the claim it must preserve.
2. Mark claims, evidence, citations, terminology, formal notation, and uncertainty that must remain intact.
3. Remove empty openings, repetition, generic transitions, and unsupported interpretation already introduced by the draft; do not add a new diagnosis of weakness.
4. Remove redundant hedging and vague abstractions only within the existing level of certainty; flag possible strength mismatches outside the article instead of correcting them silently.
5. Improve sentence structure, rhythm, and paragraph flow while retaining the author's voice.
6. Audit for repeated contrasts, lists of three, symmetry, em dashes, superficial participial endings, and other formulaic patterns.
7. Compare the revision with the source to confirm that meaning, evidence, citations, causal scope, and formatting have not changed.

When editing a file that mixes prose with code, markup, or data, modify only the prose-bearing portions unless the user explicitly asks for broader changes. Preserve syntax and identifiers.

## Output Contract

By default, output only the revised text. Do not add a preface, score, self-evaluation, or list of edits.

When a material concern about evidence, identification, causality, or another weakness must be surfaced, keep it entirely outside the revised article under a clearly labeled **Author note**. Never blend that note into the main text. Do not manufacture concerns merely to appear cautious.

If the user asks for an explanation, provide:

1. The revised text
2. A short account of material changes
3. Any claims that need evidence, clarification, or author judgment, presented outside the article

If the input is too incomplete to revise without guessing, preserve what can be edited safely and ask only for the missing context that materially affects the result.
