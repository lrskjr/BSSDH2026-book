# Sequence plan — Workshop 2: Analysis and Visualization with Orange Data Mining

*BSSDH2026. Student material: [Orange](../workshops/orange.md). Duration: 2 × 90 min (no break).*

---

## Overview

| Day | Time | Focus |
|-----|------|-------|
| **Part A** — 4 August (Tuesday) | 14.00–15.30 | Intro, add-ons, and three workflows with bibliographic metadata |
| **Part B** — 5 August (Wednesday) | 9.30–11.00 | Geodata, corpus/text mining, image classification, and closing |

---

# Part A — 4 August, 14.00–15.30

*Bibliographic metadata: import, merge, filtering, and visualisation.*

| Time | Activity |
|------|----------|
| 14.00–14.15 | Intro — Orange, widgets, add-ons |
| 14.15–14.35 | Workflow 1 — language landscape |
| 14.35–14.55 | Workflow 2 — merge and UDC distribution |
| 14.55–15.30 | Workflow 3 — Select Rows, Edit Domain, authors |

---

## 14.00–14.15 — Intro: Orange and add-ons (15 min)

### Why Orange? (10 min)

*Short presentation. Reference: [When would I use Orange?](../workshops/orange.md#when-would-i-use-orange) and [Documentation](../workshops/orange.md#documentation)*

- Orange after OpenRefine: cleaned dataset ready for analysis and visualisation
- Widgets, channels, and workflows — no coding required
- Interactivity: select data in one widget and send it on (demo from [Interactivity](../workshops/orange.md#interactivity))
- Point to documentation and the YouTube channel

### Install add-ons (5 min)

*Reference: [Add-ons](../workshops/orange.md#add-ons)*

- Options -> Add-ons -> check Geo, Image Analytics, and Text
- Wait for installation; restart Orange
- Brief tour of widget groups (Data, Transform, Visualize)
- *Geo, Text, and Image Analytics are used in part B tomorrow*

---

## 14.15–14.35 — Workflow 1: Language landscape (20 min)

*Reference: [Import CSV files and build a workflow to analyse the landscape of language](../workshops/orange.md#import-csv-files-and-build-a-workflow-to-analyse-the-landscape-of-language)*

### Demo (10 min)

- CSV File Import: load cleaned metadata from the OpenRefine workshop
- Group by: count records by language (set aggregation correctly)
- Data Table + Bar Plot: show language distribution
- Show the workflow image: ![1 language landscape.svg](../_static/images/1 language landscape.svg)

### Task (10 min)

- Participants build the workflow step-by-step
- Goal: Bar Plot matching the reference image ![Pasted image 20260708191601.png](../_static/images/Pasted image 20260708191601.png)
- Instructor circulates; typical mistakes: wrong column in Group by

---

## 14.35–14.55 — Workflow 2: Merge and data distribution (20 min)

*Reference: [Merge two datasets and analyse data distribution](../workshops/orange.md#merge-two-datasets-and-analyse-data-distribution)*

### Demo (8 min)

- Merge Data: join metadata with UDC labels via a shared control-number column
- Show workflow: ![2 udc_labels.svg](../_static/images/2 udc_labels.svg)
- Brief intro to Column Statistics, Distributions, and Box Plot

### Task (12 min)

- Participants build the merge workflow
- Answer the questions on the workflow image (distribution, outliers, comparison)
- Instructor: check that the merge key matches in both files

---

## 14.55–15.30 — Workflow 3: Authors (35 min)

*Reference: [Select Rows and Edit Domain and analyse how authors write](../workshops/orange.md#select-rows-and-edit-domain-and-analyse-how-authors-write)*

### Demo (10 min)

- Select Rows: filter *author role* = *aut*
- Edit Domain: set *author* to categorical (not string)
- Explain nominal categorical data — count, do not compute with names
- Show workflow: ![3 authors 3.svg](../_static/images/3 authors 3.svg)

### Task (20 min)

- Participants filter and change domain
- Bar Plot or similar visualisation of author frequency
- Instructor circulates; typical mistake: Bar Plot fails because *author* is still a string

### Wrap-up part A (5 min)

- What did we learn? (import, merge, filtering, Edit Domain)
- Save workflows (.ows) — you continue tomorrow with geodata, corpus, and images
- Preview of part B: Geo, Text, and Image Analytics add-ons

---

# Part B — 5 August, 9.30–11.00

*Geographical data, corpus linguistics, and image analysis.*

| Time | Activity |
|------|----------|
| 9.30–9.40 | Brief recap and reopen workflows from yesterday |
| 9.40–10.00 | Geodata — Geocoding and Choropleth Map |
| 10.00–10.35 | Corpus and text mining on titles |
| 10.35–10.55 | Image classification |
| 10.55–11.00 | Closing |

---

## 9.30–9.40 — Recap (10 min)

- Reopen saved workflows from Tuesday
- Brief repetition: widgets, channels, Edit Domain
- Check that Geo, Text, and Image Analytics add-ons are still installed

---

## 9.40–10.00 — Geodata (20 min)

*Reference: [Geocoding of geographical data in the metadata](../workshops/orange.md#geocoding-of-geographical-data-in-the-metadata)*

### Demo (10 min)

- Geocoding -> Geo Map / Choropleth Map
- Show workflow: ![4 geodata.svg](../_static/images/4 geodata.svg)

### Task (10 min)

- Participants build the geodata workflow
- Goal: map like ![Geodata from Metadata in Choropleth Map.svg](../_static/images/Geodata from Metadata in Choropleth Map.svg)
- Instructor: help with choice of geographic column and map type

---

## 10.00–10.35 — Corpus and text mining (35 min)

*Reference: [Corpus linguistic methods on titles and sub titles](../workshops/orange.md#corpus-linguistic-methods-on-titles-and-sub-titles)*

### Demo (15 min)

- Merge metadata + UDC labels (reuse from part A)
- Select Rows: choose a UDC label, language code *lav*, author not empty
- Corpus widget: choose *titles* and *sub_titles*
- Show workflow: ![5 corpus linguistic tools on latvian titles.svg](../_static/images/5 corpus linguistic tools on latvian titles.svg)
- Brief intro to text mining widgets (Word Cloud, Bag of Words, etc.)

### Task (20 min)

- Participants build the corpus workflow with their own choice of UDC label
- Experiment with at least one text mining widget
- Instructor circulates; this is the most extensive workflow

---

## 10.35–10.55 — Image classification (20 min)

*Reference: [And now to something different - Image classification](../workshops/orange.md#and-now-to-something-different-image-classification)*

### Demo (10 min)

- Import Images: folder *daells warehouse categories*
- Hierarchical Clustering -> Image Viewer
- Show workflow: ![6 Images classification.svg](../_static/images/6 Images classification.svg)
- Explain: a different dataset from metadata — same Orange principles

### Task (10 min)

- Participants import the image folder and run clustering
- Click a group and send selected images to Image Viewer
- Brief comparison: metadata vs. images as data types

---

## 10.55–11.00 — Closing (5 min)

- Orange can visualise, filter, merge, and mine text — it does not replace OpenRefine for cleaning
- Resources: [Documentation](../workshops/orange.md#documentation)
- Export all workflows (.ows)
- Point to self-study / hackathon for further exploration

---

## Instructor notes

### Preparation

- [ ] Orange installed with Geo, Image Analytics, and Text add-ons *(preferably before part A)*
- [ ] Cleaned CSV from the OpenRefine workshop ready for part A
- [ ] UDC label file ready for Merge Data
- [ ] *daells warehouse categories* folder ready for part B
- [ ] Workflow images (.svg) and [Orange](../workshops/orange.md) available to participants

### Typical problems

| Problem | Solution |
|---------|----------|
| Bar Plot shows nothing / error | Check Edit Domain — column must be categorical |
| Merge yields empty table | Check that key column has the same name and data type in both files |
| Add-ons missing | Reinstall via Options -> Add-ons; restart Orange |
| Geocoding fails | Check column format; try a different geocoding method in the widget |
| Corpus empty after Select Rows | Check filter combination (UDC + *lav* + author) |

### Timing buffer

**Part A:** If you are behind after workflow 2, shorten the UDC task (guided group walkthrough).

**Part B:** If corpus takes too long, shorten the image task to demo-only. If you are ahead, let participants explore more text mining widgets.

### Learning outcomes (after both parts)

Participants can:

- load a CSV dataset and build Orange workflows with widgets and channels
- group, merge, and visualise bibliographic metadata
- filter rows and change column type (Edit Domain)
- visualise geographical data with the Geo add-on
- build a simple corpus and use text mining widgets
- group images with Hierarchical Clustering
