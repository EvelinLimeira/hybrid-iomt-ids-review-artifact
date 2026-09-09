# Replication package: hybrid unsupervised–supervised intrusion detection in IoMT

Supplementary data for the systematic literature review *Hybrid Unsupervised-Supervised
Intrusion Detection in IoMT: A Systematic Review of Architectures, Integration Patterns,
and Evaluation Evidence*, currently under review.

The package contains the full screening trail, the quality-assessment scores, the
59-field extraction grid and its three research-question coding sheets, and the raw search
exports, so that the selection of the 34 included studies can be audited and reproduced end
to end.

> **Dataset DOI — withheld during review.**
> This copy is anonymised for double-blind review and asserts no DOI. An archived,
> citable version will be deposited once the review closes. See `ANONYMITY.md`.

## Review at a glance

| | |
|---|---|
| Protocol | PRISMA 2020 and Kitchenham & Charters |
| Search date | 6 July 2026 (single date, all eight sources) |
| Sources | IEEE Xplore, Scopus, SpringerLink, ACM DL, ScienceDirect, arXiv, Semantic Scholar, OpenAlex |
| Records retrieved | 1,441 |
| After deduplication | 1,417 (24 duplicates removed) |
| Excluded at title/abstract | 1,247 |
| Reports sought | 170 (13 not retrievable) |
| Full texts assessed | 157 |
| **Studies included** | **34** (123 excluded at full text) |
| Corpus span | 2022–2026 |
| Quality assessment | 10 items; QA1–QA4 core; core threshold ≥ 2.0; mean 4.96/10, median 5.0, range 2.0–7.0 |
| Screening | Single reviewer, with scripted completeness and cross-count checks and a second full-text reading |

Every figure in this table has been recomputed from `data/01_screening_trail.csv` and
matches Fig. 1 (the PRISMA 2020 flow diagram) and Sect. 3 of the paper.

## Contents

```
data/
  01_screening_trail.csv                1,417 records, phase 1–7 decisions
  02_accepted_studies.csv               the 34 included studies
  03_quality_assessment_scores.csv      QA1–QA10 per study, totals, threshold flag
  04_quality_assessment_questions.csv   the 10 QA questions and scoring rubric
  05_inclusion_exclusion_criteria.csv   IC1–IC6 and EC1–EC10
  06_rq1_architecture.csv               RQ1 coding: topology, components, integration, anomaly role
  07_rq2_design.csv                     RQ2 coding: thresholds, granularity, XAI, deployment, privacy
  08_rq3_gaps.csv                       RQ3 coding: datasets, validation, novelty, reproducibility
docs/
  extraction-grid.md                    the 59 extraction fields, grouped by research question
search/
  queries.md                            canonical query, per-database adaptations, export provenance
  exports/                              raw exports as downloaded, one or more files per source
LICENSE.md                              CC BY 4.0 for the coding; provider terms for the exports
ANONYMITY.md                            what this copy omits, and why
```

## How each file maps to the paper

Table and figure numbers below refer to the **final revised manuscript**, which has six
tables and four figures.

| File | Supports | Where it appears in the paper |
|---|---|---|
| `search/queries.md` | canonical Boolean string, per-interface adaptations, exported and post-deduplication counts | **Table 3** (search results and database-specific adaptations); Sect. 3 "Protocol, Search Strategy" |
| `search/exports/` | provenance of the 1,441 identified records | **Table 3**; Sect. 3 |
| `data/01_screening_trail.csv` | the whole selection process: 1,441 → 1,417 → 1,247 excluded → 170 sought → 13 not retrieved → 157 assessed → 123 excluded → 34 included | **Fig. 1** (PRISMA 2020 flow); Sect. 3 "Eligibility and Screening" |
| `data/05_inclusion_exclusion_criteria.csv` | the operational eligibility rule (IoMT environment, cybersecurity detection task, unsupervised component joined to a supervised classifier in one inference process) | **Table 2** (PICOC scope and operational construct); Sect. 3 |
| `data/02_accepted_studies.csv` | the 34 included studies, their years, venues and DOIs | **Fig. 2** (corpus profile: year, publisher, affiliation country); the reference list, entries [10]–[43] |
| `data/03_quality_assessment_scores.csv` | per-study QA1–QA10 scores, totals, core subtotal | Sect. 3 "Quality Assessment and Data Extraction" (mean 4.96/10, median 5.0, range 2.0–7.0); Sect. 5 "RQ3" (QA distribution) |
| `data/04_quality_assessment_questions.csv` | the ten quality items and the scoring rubric | Sect. 3 "Quality Assessment and Data Extraction" |
| `docs/extraction-grid.md` | the 59 extraction fields and how they group by research question | Sect. 3 "Quality Assessment and Data Extraction" (9 + 11 + 13 + 16 + 10 = 59) |
| `data/06_rq1_architecture.csv` | raw RQ1 codes: architecture type, stages, unsupervised and supervised components, integration mechanism, anomaly role | **Table 4** (non-exclusive architectural and integration attributes); **Fig. 3** (transferred object vs decision influence) |
| `data/07_rq2_design.csv` | raw RQ2 codes: threshold strategy, granularity, explainability, deployment target, federated learning | Sect. 4 "RQ2"; **Table 5** (deployment row) |
| `data/08_rq3_gaps.csv` | raw RQ3 codes: datasets, cross-dataset validation, unknown-attack evaluation, per-device evaluation, code availability, reported metrics | **Fig. 4** (reporting dimensions); **Table 5** (attack coverage, datasets); **Table 6** (representative within-study results) |

The two tables with no data file behind them are **Table 1** (a comparison with five prior
IoMT IDS reviews, drawn from the cited reviews themselves, not from this corpus) and the
narrative rows of **Table 5** that come from the exploratory CTI reading of the 34 full
texts rather than from a coded column.

## Screening trail

`01_screening_trail.csv` carries one row per deduplicated record and follows it through
seven phases:

| Phase | Columns |
|---|---|
| 1 identification | `phase1_identified`, `source_database`, `search_date` |
| 2 deduplication | `phase2_dedup_status` |
| 3 title screening | `phase3_title_decision`, `phase3_title_reason` |
| 4 abstract screening | `phase4_abstract_decision`, `phase4_abstract_reason`, `phase4_ic_met`, `phase4_ec_triggered` |
| 5 full-text screening | `phase5_fulltext_decision`, `phase5_ec_triggered`, `phase5_fulltext_reason`, `phase5_decision_reviewed` |
| 6 quality assessment | `phase6_qa_total_score`, `phase6_qa_meets_threshold` |
| 7 final decision | `phase7_final_decision` |

Bibliographic columns (`record_id`, `title`, `authors`, `year`, `venue`, `doi`, `url`,
`content_type`, `is_preprint`, `abstract_source`) carry the record as retrieved.
`abstract_source` names where the abstract was read from during screening (Springer,
OpenAlex, SemanticScholar, Manual, or blank when the record was decided on title alone);
the abstract text itself is not redistributed.

Records are keyed by `record_id`, which is the join key across every file in `data/`.
Identifiers run from `R0088` to `R1528` and are not contiguous.

### Reading the phase-5 decisions correctly

Full-text screening was done in two passes, and the file records both.

- `phase5_fulltext_decision` is the **first-pass, provisional** decision.
- `phase5_decision_reviewed` is the decision **after the second full-text reading**, and
  is the authoritative one.

Seventeen of the 34 included studies carry `phase5_fulltext_decision = Excluded` and
`phase5_decision_reviewed = Accepted`. These are reinstatements, not contradictions: each
was reversed on the second reading, and `phase5_fulltext_reason` records why in prose
("Included as a borderline primary study", "Included with a scope flag", and so on). The
provisional column is preserved deliberately rather than overwritten, so that the
reversals remain visible and auditable. Filter on `phase7_final_decision` for the final
set, never on `phase5_fulltext_decision`.

Two more conventions in phase 5 are worth knowing before filtering:

- The **13 reports that could not be retrieved** carry `phase5_fulltext_decision = Excluded`
  with an empty `phase5_ec_triggered` and an empty `phase5_decision_reviewed`; the criterion
  EC10 is recorded in `phase5_fulltext_reason` instead. One of the thirteen (`R0787`) has
  the reason typed as `EC1O` with a capital letter O, so a literal string filter on `EC10`
  returns twelve. The thirteen are: R0518, R0585, R0634, R0655, R0702, R0787, R0819, R0821,
  R0856, R0866, R0868, R0884, R1526.
- Six records carry `phase5_fulltext_decision = Rejected` rather than `Excluded`. These were
  removed at full text as secondary publications: five book chapters under EC7 and one
  survey moved to the background reading set. They are part of the 123 full-text exclusions.

Reconciling those conventions gives exactly the PRISMA numbers: 170 sought − 13 not
retrieved = 157 assessed; 117 `phase5_decision_reviewed = Excluded` + 6 `Rejected` = 123
excluded; 34 accepted.

### The quality-assessment threshold

The threshold was applied to the **four core items (QA1–QA4)**, which had to reach a
combined score of at least 2.0. `phase6_qa_total_score` (and the `Total` column of
`03_quality_assessment_scores.csv`) is the total across all ten items; `Core 1-4` is the
core subtotal, and `Meets Threshold` is computed on that subtotal.

One included study is an explicit exception. `R0338` scores QA1 = 0.5, QA2 = 0.5,
QA3 = 0, QA4 = 0, giving `Core 1-4` = 1.0 and `Meets Threshold` = No, with a ten-item
`Total` of 2.0. It is the only study in the corpus below the core threshold and the only
one carrying `phase6_qa_meets_threshold = no`; it was retained in the final set
nonetheless, and it is the study that makes the reported quality range start at 2.0. Every
other included study has `Core 1-4` ≥ 2.0. The flag has been left as computed rather than
overwritten, so that the exception is visible.

## Column meanings

### `02_accepted_studies.csv` (34 rows)

`record_id`, `title`, `authors`, `year`, `venue`, `doi`, `source_database`, `preprint`,
`fulltext_available` are the nine bibliographic and provenance fields of the extraction
grid. `fulltext_files` is an additional working column naming the PDF files read during
extraction; those PDFs are not redistributed (see "What is not here"). `source_database`
names the source that first supplied the record, not every source that returned it.

### `03_quality_assessment_scores.csv` (1 label row + 34 study rows)

The first row has an empty `ID` and carries short labels for QA1–QA10 ("Architecture
described", "Genuine hybrid", …); it is a header aid, not a study. Scores are recorded as
`Yes` = 1, `Part.` = 0.5, `No` = 0. `Total` is the ten-item sum, `Core 1-4` the QA1–QA4
subtotal, `Meets Threshold` the core gate, `FT Avail.` whether the full text was obtained.

### `04_quality_assessment_questions.csv` (10 questions + 1 threshold row)

`ID`, `Question`, `Partially means` (what earns 0.5), `Core?`, `Score`. The final row has
`ID = THRESHOLD` and states the gate rather than a question.

### `05_inclusion_exclusion_criteria.csv`

A two-column list in two blocks: six inclusion criteria (IC1–IC6) then ten exclusion
criteria (EC1–EC10), each block preceded by its own `ID` / `Criterion` header row. The file
is a criteria reference, not a per-record table.

### `06_rq1_architecture.csv`, `07_rq2_design.csv`, `08_rq3_gaps.csv` (34 rows each)

`ID` and `Title` are join keys. The remaining 11, 13 and 16 columns are the RQ1, RQ2 and
RQ3 extraction fields; `docs/extraction-grid.md` lists them and defines each one. These
sheets hold **raw field values as extracted**, not the consolidated codes reported in the
paper — see the next section.

## Raw extraction codes are not the reported counts

The paper states that free-text extraction fields were "reduced to the closed codes in
Tables 4 and 5", with topology, transferred information and decision influence coded on
separate axes. `06`–`08` are the input to that step, not its output. Recomputing a paper
figure directly from a single column will therefore not always reproduce it. The
differences are systematic, not errors, and the main ones are listed here so that a reader
can see them at a glance rather than discover them by accident.

| Reported in the paper | Nearest raw column here | Raw value | Why they differ |
|---|---|---|---|
| Explainability mechanisms in 15 studies (44.1%) | `07 Explainability`; `08 XAI Present` | 10 studies with a named mechanism; `XAI Present` = Yes in 8, Partially in 1 | The paper counts any reported explainability or interpretability mechanism, including attention-based and feature-importance evidence read from the full text; the raw columns record only what the extraction sheet named. `R0175` is `Feature importance` in `07` but `No` in `08`. |
| Threshold strategy reported in 15 studies (44.1%); unreported where applicable in 19 | `07 Threshold Strategy` | 11 populated, 23 `not reported` | The paper's denominator is only those architectures where a score actually gates inference, and it counts thresholds evidenced in the full text but left blank in the sheet. The paper's nine "fixed or cross-validated" cut-offs subsume several distinct raw strings (`fixed`, `Fixed/cross-val`, `calibrated`, `dynamic`). |
| Per-device evaluation absent (0 studies); no comparative device-specific validation | `08 Per-device Eval.` | `Yes` in 3 (`R0696`, `R0736`, `R0791`) | Different constructs. The sheet records whether *any* device-level breakdown appears. The paper requires a **comparative** design that validates a device-type model against a pooled baseline, which none of the three provides. |
| Model granularity pooled in 26 (76.5%), local in 8 (23.5%) | `07 Granularity` | `global` 18, `not reported` 7, `per-device` 4, `per-layer` 2, `per-gateway` 1, `per-flow` 1, `per-device-type` 1 | The paper folds `not reported` into the pooled default and treats `per-layer` as an architectural tier rather than a modelling granularity. |
| Cross-dataset validation present in 5 (14.7%), partial in 3 (8.8%), absent in 26 (76.5%) | `08 Cross-DS Validation` | `Yes` 7, `No` 27 | The sheet column is binary; the paper distinguishes full from partial evidence after reading the protocols, and counts eight studies (5 + 3) against the sheet's seven. |
| 30 studies state no held-out novelty protocol | `08 Unknown Attack Eval.` | `No` 28, `Partial` 1, `Yes` 5 | The paper counts `Partial` and one `Yes` whose protocol is not held-out as "no protocol". |
| Dataset mix: mixed 12, IoMT-specific 9, benchmark 8, simulated 3, real 1, NR 1 | `08 Dataset Type` crossed with `08 IoMT Specific` | `public-benchmark` 22, `mixed` 6, `simulated` 2, `not reported` 2, `real-IoMT-traffic` 1, `IoMT-specific` 1 | Table 5 recodes on two axes at once: `Dataset Type` alone does not separate IoMT-specific benchmarks from generic ones; `IoMT Specific` = Yes in 20 studies. |
| Deployment: offline 23 (67.6%), simulation 5, prototype 6 | `07 Deployment Target` | `edge` 10, `not reported` 10, `gateway` 4, `mixed` 3, `cloud` 3, `fog` 3, `edge-cloud` 1 | Different constructs again. `Deployment Target` is the intended tier; the paper's figure is the **evaluation venue** (offline benchmark, simulation, prototype), read from the full texts and not held in any single column. |
| Decision-level influence 15, representation-level 14, unclear 5 | `06 Anomaly Role`, `06 Genuine Hybrid` | `Anomaly Role` uses 13 distinct free strings; `Genuine Hybrid` = Yes 22, Unclear 10, No 2 | Fig. 3 is the two-axis consolidation of `Anomaly Role` into decision-level versus representation-level influence; `Genuine Hybrid` = Unclear is an evidence-quality note, not the same as the paper's five unreconstructable dependencies. |
| Autoencoder-family methods in 22 studies (64.7%) | `06 Unsupervised Components`, `07 Unsupervised Detail` | 20–21 by string match | Two studies name the family only in prose in the integration mechanism field. |
| Federated learning in 6 studies (17.6%) | `07 Federated Learning` | `Yes` 6 | Matches exactly. |

Two further cross-sheet points, so they are not read as contradictions:

- **`Patient Safety` appears in both `07` and `08` and means different things.** In `07` it
  records whether the study discusses a patient-safety link (Yes in 20); in `08` it records
  whether patient safety enters the evaluation (Yes in 14). The 14 are a subset of the 20;
  no study is Yes in `08` and No in `07`.
- **Value vocabularies are not normalised.** The same code appears as `global` and `Global`,
  `none` and `None`, `Yes` and free-text sentences beginning "Unclear — ". Compare
  case-insensitively and expect prose in the judgement columns.

## Reproducing the selection

The included set is recoverable from the screening trail alone:

```bash
python - <<'PY'
import csv
rows = list(csv.DictReader(open('data/01_screening_trail.csv', encoding='utf-8-sig')))
included = [r for r in rows if r['phase7_final_decision'].strip().lower().startswith('accept')]
print(len(rows), 'records ->', len(included), 'included')
PY
```

This prints `1417 records -> 34 included`. The 34 `record_id` values match
`02_accepted_studies.csv` exactly, and every `ID` in `03`, `06`, `07` and `08` is one of
those 34.

## What is not here, and why

**Abstract text has been removed** from `01_screening_trail.csv` and
`02_accepted_studies.csv`, and `abstract = {...}` fields have been stripped from every
BibTeX export. Abstracts are the publishers' copyright and cannot be redistributed. The
screening *decisions* taken on those abstracts are retained in full
(`phase4_abstract_decision`, `phase4_abstract_reason`, `abstract_source`), so the audit
trail stays complete. Every record carries a DOI or URL, so any abstract can be retrieved
from the publisher.

**Full texts of the 34 included studies are not redistributed.** They are identified by
DOI in `02_accepted_studies.csv`; the `fulltext_files` column names the local PDF filenames
used during extraction so that a reader can see how many documents each study contributed.

**No unsupervised or supervised model, code or dataset is included.** This is a review; the
package documents a selection and a coding, not an experiment.

## Corrections applied to this version of the package

- **SpringerLink export replaced.** The package previously shipped an 873-row interface
  download named `Springer_SearchResults.csv`, which was a strict subset of the search
  result and did not match the 995 records reported in Table 3. It has been replaced by the
  complete 995-row export, `springerlink_export.csv`. The 873-row file contained no record
  that the 995-row file lacks, and no screening decision changes.
- **Export files renamed** to a consistent scheme; original download names are recorded in
  `search/queries.md`.
- **Publication year of `R0093` corrected from 2025 to 2024** in `02_accepted_studies.csv`,
  matching Crossref, OpenAlex and reference [10] of the paper. The 2025 value came from the
  ACM Digital Library's own record. `01_screening_trail.csv` and `06_rq1_architecture.csv`
  still carry 2025 for this record, which is the value the ACM export supplied; they have
  been left as the as-collected record.

## Known limitations of this dataset

These are stated in the paper and repeated here so the data is not read as stronger than
it is.

- **Single coder.** Screening and extraction were performed by one reviewer. The data is
  not double-screened and holds no second reviewer's decisions.
- **Web of Science and PubMed were not searched.** Clinical-informatics coverage may be
  incomplete.
- **Three sources used simplified queries.** ScienceDirect, arXiv and Semantic Scholar
  could not accept the full Boolean string; see `search/queries.md` for exactly what was
  run against each.
- **The raw exports do not cover every source.** The IEEE Xplore file holds one of the 31
  records retrieved, and arXiv, Semantic Scholar and OpenAlex offered no usable bulk export
  at all, so their results were transcribed directly into the trail. The screening trail is
  complete for all eight sources; the exports are provenance, not the audit record.
- **The CTI coding is exploratory.** The search was not designed to retrieve the IoMT
  cyber-threat-intelligence literature, so those fields characterise the included corpus
  only.
- **No update search.** All sources were queried on 6 July 2026 and not re-run.

## Licence

The coding, decisions and derived fields in `data/` and `docs/` are released under
**CC BY 4.0**.

Files in `search/exports/` are bibliographic metadata as returned by each database. They
are included unmodified except for the removal of abstract fields, and remain subject to
each provider's terms. See `LICENSE.md`.

## Citation

Cite the paper and this dataset together.

Author, venue and dataset DOI are withheld while the paper is under double-blind review.
A citable archived version with full metadata will be deposited once the review closes.
