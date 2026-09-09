# The 59-field extraction grid

The grid was derived from the three research questions and from dimensions that earlier
IoMT IDS reviews report descriptively without connecting them to architecture. Each group
is tied to the question it serves, which is how coded values were consolidated into the
counts reported in the paper.

| Group | Fields | Serves | File | Reported in the paper as |
|---|---:|---|---|---|
| Bibliographic and provenance | 9 | corpus profile | `02_accepted_studies.csv` | Fig. 2 |
| Architecture and integration | 11 | RQ1 | `06_rq1_architecture.csv` | Table 4, Fig. 3 |
| Design and deployment | 13 | RQ2 | `07_rq2_design.csv` | Sect. 4 "RQ2", Table 5 |
| Evaluation and gaps | 16 | RQ3 | `08_rq3_gaps.csv` | Fig. 4, Tables 5 and 6 |
| Quality assessment | 10 | all | `03_quality_assessment_scores.csv` | Sect. 3, Sect. 5 |
| **Total** | **59** | | | |

Table and figure numbers refer to the final revised manuscript, which has six tables and
four figures.

`record_id` and `title` repeat across files as join keys and are counted once, under
bibliographic and provenance. `02_accepted_studies.csv` additionally carries a
`fulltext_files` working column, which names the PDF files read during extraction; it is
not one of the 59 grid fields and the PDFs are not redistributed.

Consolidation ran in two steps, as described in the paper. Free-text fields — chiefly the
reconstructed integration mechanism — were written per study from page-level evidence, then
reduced to the closed codes of Tables 4 and 5, with topology, transferred information and
decision influence coded on separate axes. Coded values were then tallied over the 34
accepted rows and reported as frequencies and percentages of N = 34, with *unreported* and
*not applicable* kept distinct so that an absent value is never counted as a negative
finding. **The three sheets in this package hold the raw field values, the input to that
step, not its output**; the "Raw extraction codes are not the reported counts" section of
`README.md` lists every difference between a raw column here and the corresponding count in
the paper.

## Bibliographic and provenance (9)

`record_id`, `title`, `authors`, `year`, `venue`, `doi`, `source_database`, `preprint`,
`fulltext_available`

## Architecture and integration (11) — RQ1

| Field | Meaning |
|---|---|
| `Year` | publication year as coded during extraction |
| `Architecture Type` | two-stage, multi-stage, cascade, sequential-pipeline, parallel, ensemble, federated, other |
| `Stages` | number of inference stages |
| `Unsupervised Components` | the unsupervised model(s) used |
| `Supervised Components` | the supervised model(s) used |
| `Integration Mechanism` | prose reconstruction of how the stages connect |
| `Anomaly Role` | filter, filter/gate, feature input, additional_feature, ensemble_vote, parallel_mechanism, classification_trigger, standalone, unclear, not reported |
| `Genuine Hybrid` | whether an unsupervised-to-supervised dependency was demonstrated |
| `Zero-day Support` | whether unknown-attack capability is claimed |
| `Output Type` | binary, multiclass, other |
| `Objective` | the study's stated aim |

`Architecture Type` records the vocabulary used during extraction. The paper reports
topology using four categories (sequential/cascade, parallel/ensemble, hierarchical,
distributed); the distributed category also draws on `Federated Learning` and
`Deployment Target` in `07_rq2_design.csv`.

## Design and deployment (13) — RQ2

`Unsupervised Detail`, `Supervised Detail`, `Threshold Strategy`, `Granularity`,
`Feature Type`, `Explainability`, `Deployment Target`, `Latency`, `Memory`, `Energy`,
`FPR`, `Patient Safety`, `Federated Learning`

## Evaluation and gaps (16) — RQ3

`Datasets`, `Dataset Type`, `IoMT Specific`, `# DS`, `Cross-DS Validation`,
`Per-device Eval.`, `Unknown Attack Eval.`, `Operational Metrics`, `FPR Clinical`,
`XAI Present`, `Code Available`, `Baselines Compared`, `Patient Safety`,
`Reported Metrics`, `Best Result`, `Limitations (authors)`

The name `Patient Safety` occurs in both groups and denotes two different fields: in
`07_rq2_design.csv` it records whether the study discusses a patient-safety link, and in
`08_rq3_gaps.csv` whether patient safety enters the evaluation. They are counted as two of
the 59 fields.

## Quality assessment (10)

`QA1`–`QA10`, scored 1, 0.5 or 0. The ten questions and their scoring rubric are in
`04_quality_assessment_questions.csv`, which also marks which items are core.

`QA1`–`QA4` are the core items: architecture, integration, IoMT relevance, and metrics.
A study had to reach a combined score of at least 2.0 on those four to be retained.
`03_quality_assessment_scores.csv` additionally carries `Total`, `Core 1-4`,
`Meets Threshold` and `FT Avail.` as derived columns.
