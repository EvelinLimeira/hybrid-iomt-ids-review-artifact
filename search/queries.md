# Search strategy

All eight sources were queried on **6 July 2026**. A single date was used so that the
exported counts describe one index state and remain mutually comparable. No update search
was run before submission, so studies indexed after that date fall outside the corpus.

## Concept blocks

The strategy combined six blocks with `AND`:

1. IoMT environments
2. IDS functions
3. Hybrid architectures
4. Unsupervised methods
5. Supervised classifiers
6. Device-aware, adaptive, or explainable mechanisms

## Canonical query

Applied in full to IEEE Xplore, Scopus, SpringerLink, ACM Digital Library and OpenAlex:

```
("Internet of Medical Things" OR IoMT OR "medical IoT" OR "healthcare IoT" OR "smart healthcare")
AND
("intrusion detection" OR IDS OR "network intrusion detection" OR NIDS OR "attack detection"
 OR "cyber threat detection")
AND
(hybrid OR "two-stage" OR "multi-stage" OR cascade OR ensemble OR "dual-path" OR "combined model")
AND
("anomaly detection" OR unsupervised OR autoencoder OR "one-class classification" OR clustering
 OR "isolation forest" OR "local outlier factor")
AND
(supervised OR classification OR classifier OR "machine learning" OR "deep learning"
 OR "random forest" OR SVM OR CNN OR LSTM)
AND
("device-specific" OR "device-aware" OR "per-device" OR "device profiling"
 OR "behavioral profiling" OR adaptive OR "concept drift" OR "dynamic threshold"
 OR explainable OR interpretable OR XAI OR SHAP OR LIME)
```

## Per-source adaptations and yields

Three interfaces could not accept the full Boolean string and required shorter forms.
This is a stated search-validity threat in the paper.

The **Exported** column is the number of records contained in the exported files and is the
column that feeds the PRISMA identification count; it is reproduced as Table 3 of the paper.

| Source | Query mode | Exported | After dedup | Raw export file in `exports/` |
|---|---|---:|---:|---|
| SpringerLink | Full Boolean; 2019–2026 | 995 | 987 | `springerlink_export.csv` (995 rows, complete) |
| ScienceDirect | Simplified: `IoMT HYBRID intrusion detection` | 292 | 288 | `sciencedirect_export_01.bib`, `_02`, `_03` (100 + 100 + 92) |
| ACM Digital Library | Full Boolean | 87 | 87 | `acm_export_01.bib`, `acm_export_02.bib` (87 entries each) |
| IEEE Xplore | Full Boolean | 31 | 24 | `ieee_xplore_export.bib` (partial: 1 entry) |
| OpenAlex | Full Boolean | 13 | 12 | none; recorded in the screening trail |
| arXiv | Simplified: `IoMT intrusion detection` | 10 | 10 | none; recorded in the screening trail |
| Scopus | Full Boolean; article and conference filters | 9 | 5 | `scopus_export.bib` (9 entries) |
| Semantic Scholar | Reduced Boolean (three blocks) | 4 | 4 | none; recorded in the screening trail |
| **Total** | | **1,441** | **1,417** | |

Cross-source deduplication removed 24 records, leaving 1,417 unique records for title and
abstract screening. The per-source figures in the "after dedup" column reconcile exactly
with `data/01_screening_trail.csv`, which can be verified with:

```bash
python - <<'PY'
import csv, collections
rows = list(csv.DictReader(open('data/01_screening_trail.csv', encoding='utf-8-sig')))
print(collections.Counter(r['source_database'] for r in rows).most_common(), len(rows))
PY
```

## The authoritative record is the screening trail, not the exports

`data/01_screening_trail.csv` is the complete and authoritative record: it holds all 1,417
deduplicated records with `source_database`, `search_date`, `title`, `authors`, `venue`,
`doi` and `url`, and is the file to use for any reproduction or audit.

The files in `exports/` are the raw downloads retained from the search session. They are
retained for provenance, and three points about their coverage are worth stating plainly:

- **Three interfaces offered no usable bulk export.** arXiv, Semantic Scholar and OpenAlex
  results were transcribed directly into the trail.
- **One export is partial.** The IEEE Xplore file holds a single record rather than the 31
  retrieved. All 31 are complete in the screening trail (24 of them survive deduplication).
- **The SpringerLink export is complete.** `springerlink_export.csv` holds all 995 records
  and covers all 987 SpringerLink records in the screening trail. An earlier version of this
  package shipped a shorter 873-row interface download by mistake; that file was a strict
  subset of this one and has been replaced. See "Export file provenance" below.

The two ACM files are two exports of the same 87 records rather than two halves of a larger
set: they contain identical citation keys and identical DOIs, differing only in record
order. Only 87 unique ACM records entered the corpus. This is the duplicated ACM export
noted and corrected in the paper, and both files are retained here so the correction is
visible.

Every `abstract = {…}` field has been removed from the BibTeX files because abstracts are
the publishers' copyright. No other field was altered, and the entry count of every file is
unchanged by that removal. The SpringerLink CSV export never carried an abstract column,
so it is byte-identical to the download.

## Export file provenance

Files were renamed to a consistent scheme for this deposit. Contents are byte-identical to
the downloads except for the abstract removal described above.

| File in `exports/` | Original download name | Records |
|---|---|---:|
| `springerlink_export.csv` | `springer_raw.csv` (SpringerLink CSV download, 6 Jul 2026) | 995 |
| `sciencedirect_export_01.bib` | `ScienceDirect_citations_1783367361996.bib` | 100 |
| `sciencedirect_export_02.bib` | `ScienceDirect_citations_1783367385925.bib` | 100 |
| `sciencedirect_export_03.bib` | `ScienceDirect_citations_1783367410672.bib` | 92 |
| `acm_export_01.bib` | `acm_part01_06072026.bib` | 87 |
| `acm_export_02.bib` | `acm_part02_06072026bib.bib` | 87 |
| `ieee_xplore_export.bib` | `IEEE Xplore Citation BibTeX Download 2026.7.6.19.54.8.bib` | 1 |
| `scopus_export.bib` | `scopus_export_Jul 6-2026_adf19c3d-5e73-4fee-82d1-64e0894b3709.bib` | 9 |
