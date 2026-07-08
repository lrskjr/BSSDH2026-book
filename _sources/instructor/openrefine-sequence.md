# Sequence plan — Workshop 1: Data cleaning with OpenRefine

*BSSDH2026. Student material: [OpenRefine](../workshops/openrefine.md). Duration: 9.30–13.00 (incl. break).*

---

## Overview

| Time | Activity |
|------|----------|
| 9.30–11.00 | Workshop 1, part A — import and column operations |
| 11.00–11.30 | Coffee break |
| 11.30–13.00 | Workshop 1, part B — Transform/GREL, facets and clustering, export |

---

## Part A: Import and column operations (9.30–11.00)

### 9.30–9.45 — Why OpenRefine? (15 min)

*Short presentation. Reference: [When would I use OpenRefine?](../workshops/openrefine.md#when-would-i-use-openrefine)*

- What is a dataset in rows and columns (CSV/Excel)?
- Inconsistencies in bibliographic data (names entered differently)
- Cells with several pieces of data in one cell — need to split
- Workshop goal: cleaning before analysis in Orange, pandas, etc.

### 9.45–9.55 — How the program runs (10 min)

*Reference: [When would I use OpenRefine?](../workshops/openrefine.md#when-would-i-use-openrefine) (section on local server)*

- Browser vs. local program: address bar `http://127.0.0.1:3333`
- Console window must stay open
- Project ≠ original file (changes are saved in the project)

### 9.55–10.15 — Import dataset (20 min)

*Reference: [How do I get data into the program?](../workshops/openrefine.md#how-do-i-get-data-into-the-program)*

- Participants import the workshop file (choose files -> next)
- Check *Trim leading & trailing whitespace from strings*
- Create project
- Brief tour of the interface: column arrows, the *All* column

### 10.15–10.35 — Demo: split, trim, rename, join (20 min)

*Reference: [Split into several columns](../workshops/openrefine.md#split-into-several-columns) through [Join columns](../workshops/openrefine.md#join-columns)*

Joint demo on the *author* column:

1. Edit column -> Split into several columns (separator: comma, max 2 columns)
2. Edit cells -> Trim leading and trailing whitespace
3. Edit column -> Rename column
4. Edit columns -> Join columns (separator: `, `, delete joined columns)

Participants follow step-by-step.

### 10.35–10.50 — Task: split *host_info* (15 min)

*Reference: [Task: Split host_info into three columns](../workshops/openrefine.md#task-split-host_info-into-three-columns)*

- Participants split *host_info* into three columns (individual task)
- Walk around and help with separator and number of columns
- Typical mistakes: too many/few columns, forgot to trim

### 10.50–11.00 — Wrap-up part A (10 min)

- What did we learn? (split, trim, rename, join)
- The project is a copy — the original file is unchanged
- Preview of part B: Transform, GREL, clustering

---

## Break (11.00–11.30)

Coffee break.

*Tip for instructor: check that console windows are still running; participants do not need to close OpenRefine.*

---

## Part B: Transform, GREL, clustering and export (11.30–13.00)

### 11.30–11.45 — Transform and `.replace()` (15 min)

*Reference: [Transform and GREL](../workshops/openrefine.md#transform-and-grel)*

- Edit cells -> Transform
- GREL: `value` and `.replace()`
- Demo: remove the prefix *host_title: * in host columns

### 11.45–12.05 — Task: clean and rename *host_name* 1–3 (20 min)

*Reference: [Task: Clean and rename host_name 1–3](../workshops/openrefine.md#task-clean-and-rename-host_name-1-3)*

- Participants use Transform + Rename column
- Instructor circulates; group walkthrough of one solution if many are stuck

### 12.05–12.20 — RegEx: remove trailing comma (15 min)

*Reference: [Transform and advanced GREL solutions](../workshops/openrefine.md#transform-and-advanced-grel-solutions)*

- Problem in *subject_person*: two commas, only the last one should go
- Why `value.replace(',', '')` does not work
- Solution: `value.replace(/,$/, '')`
- Brief explanation: `/,$/` and that `$` in regex means end of string

### 12.20–12.40 — Text facets and clustering (20 min)

*Reference: [Text facets and clusters](../workshops/openrefine.md#text-facets-and-clusters)*

- Facet -> Text facet (demo on names/subjects)
- Cluster button: merge variants of the same value
- Short demo of Merge selected & re-cluster
- Point to documentation if time allows: https://openrefine.org/docs/technical-reference/clustering-in-depth

### 12.40–12.55 — Task: clean *author* and *topic* (15 min)

*Reference: [Task: Clean the author and topic columns with clustering](../workshops/openrefine.md#task-clean-the-author-and-topic-columns-with-clustering)*

- Participants cluster and merge in *author*
- Then *topic* (or whatever column name the dataset uses)
- Instructor: help participants choose merge targets deliberately (not just the first suggestion)

### 12.55–13.00 — Export and closing (5 min)

*Reference: [How do I export the project to a new file?](../workshops/openrefine.md#how-do-i-export-the-project-to-a-new-file)*

- Export -> CSV -> new filename (e.g. with suffix *_cleaned*)
- Short summary: what OpenRefine can and cannot do
- Resources: [Resource](../workshops/openrefine.md#resource)

---

## Instructor notes

### Preparation before the workshop

- [ ] OpenRefine installed and tested on teaching PCs
- [ ] Workshop CSV ready and shared (USB, link, or learning platform)
- [ ] Participants have read a short intro or received the file in advance
- [ ] [OpenRefine](../workshops/openrefine.md) available to participants

### Typical problems

| Problem | Solution |
|---------|----------|
| Browser shows an error | Check that the console window is running; restart OpenRefine |
| Wrong separator when splitting | Undo (History); try again |
| Clustering merge too aggressive | Undo; choose a different algorithm |
| UTF-8/characters look wrong | Check encoding on import |

### Timing buffer

If you are behind after part A: shorten the *host_info* task (guided group solution).

If you are behind after part B: shorten the RegEx demo; prioritise the clustering task.

If you are ahead: let participants export and open the cleaned CSV in Excel/Orange for comparison.

### Learning outcomes (after the workshop)

Participants can:

- import a CSV dataset and create an OpenRefine project
- split, trim, rename, and join columns
- use Transform with simple GREL and RegEx
- find and merge inconsistent values with clustering
- export a cleaned dataset for further analysis
