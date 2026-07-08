# Analysis and Visualization with Orange Data Mining

![screenshot](../_static/images/uden-titel-1.jpg)


## Where do I find Orange?

Download Orange from [https://orangedatamining.com/download/](https://orangedatamining.com/download/). Different versions are available for Windows and Mac.

## When would I use Orange?

I use [Orange](https://orangedatamining.com/) when I have well-ordered, structured datasets that I want to analyse and explore — for example through visualisations — and as a pedagogical tool when I want to learn about algorithms used in machine learning, AI, and text and data mining.

The program is relatively easy to get started with because you do not need to code. Everything happens visually: you place widgets — small programs — on a canvas and connect them with channels that send data from one widget to the next in a workflow. Even though it is easy to get started, the data processing and calculations inside the widgets can be very complex if you want to understand them in depth. The advantage is that you can use the program to gain a broad overview of the steps that typically form part of computer-based data analysis.

## Documentation

Orange is very [well documented](https://orangedatamining.com/docs/) with text, images, and short tutorial videos on [YouTube](https://www.youtube.com/channel/UClKKWBe2SCAEyv7ZNGhIe4g), so the hurdle of learning a new program is genuinely manageable.

## Interactivity

A great feature is that Orange's developers have built interactivity into the widgets, so you can select data in one widget and send the selection to another. For example, you can select rows in a Data Table widget and send them to a Bar Plot widget — as in the workflow image below.

![screenshot](../_static/images/pasted-image-20260708184522.png)

## Add-ons

Orange's widgets are grouped into categories — for example Data, Transform, Visualize, and so on.

![screenshot](../_static/images/pasted-image-20260708190200.png)

You add more widget groups by installing optional add-ons. That opens up further possibilities. Later in this text there are examples of workflows that use widgets beyond those installed by default.

Install add-ons by clicking Options -> Add-ons...

![screenshot](../_static/images/pasted-image-20260708190710.png)

A new window opens. Select add-ons by checking the corresponding box. Check Geo, Image Analytics, and Text. Click OK and wait while the new add-ons install. Restart the program when prompted.

## Import CSV files and build a workflow to analyse the landscape of language

Let us learn more about Orange and data analysis — starting from the metadata dataset we worked with in OpenRefine.

Use [CSV File Import](https://orangedatamining.com/widget-catalog/data/csvfileimport/) to load the dataset. Then send data through [Group by](https://orangedatamining.com/widget-catalog/transform/groupby/), [Data Table](https://orangedatamining.com/widget-catalog/data/datatable/), and [Bar Plot](https://orangedatamining.com/widget-catalog/visualize/barplot/) as in the workflow image. Spend some time getting the settings right in Group by.

![screenshot](../_static/images/1-language-landscape.svg)

Can you produce this Bar Plot showing the languages in which the publications were written?

![screenshot](../_static/images/pasted-image-20260708191601.png)

## Merge two datasets and analyse data distribution

![screenshot](../_static/images/2-udc-labels.svg)

When you want to add extra data to your dataset, you can use [Merge Data](https://orangedatamining.com/widget-catalog/transform/mergedata/). This requires a column with values that both datasets share. In this case there is a column of unique control numbers that can be used to combine the two datasets into one. Try building the workflow shown in the image and work through the questions on the image as well. Besides [Merge Data](https://orangedatamining.com/widget-catalog/transform/mergedata/), you will use [Group by](https://orangedatamining.com/widget-catalog/transform/groupby/), [Column Statistics](https://orangedatamining.com/widget-catalog/data/featurestatistics/), [Distributions](https://orangedatamining.com/widget-catalog/visualize/distributions/), and [Box Plot](https://orangedatamining.com/widget-catalog/visualize/boxplot/).

## Select Rows and Edit Domain and analyse how authors write

The next workflow introduces two new widgets: [Select Rows](https://orangedatamining.com/widget-catalog/transform/selectrows/) and [Edit Domain](https://orangedatamining.com/widget-catalog/data/editdomain/).

Use Select Rows to filter the dataset. Try filtering so that only rows with the value *aut* are passed on — the values are in the *author role* column.

In Edit Domain, reinterpret the data in the *author* column as categorical data. By default they are treated as strings, but to create the Bar Plot visualisation further along the workflow, *author* must be changed to categorical data. Categorical data is the opposite of numeric data. You cannot, for example, add two author names together, but you can count how often each name appears in relation to a publication.

![screenshot](../_static/images/3-authors-3.svg)

## Geocoding of geographical data in the metadata

The Geo add-on we installed offers good options for visualising geographical data from the bibliographic metadata. In the workflow below, [Geocoding](https://orangedatamining.com/widget-catalog/geo/geocoding/), [Geo Map](https://orangedatamining.com/widget-catalog/geo/geomap/), and [Choropleth Map](https://orangedatamining.com/widget-catalog/geo/choroplethmap/) are used.

![screenshot](../_static/images/4-geodata.svg)

Can you produce a map like this?

![screenshot](../_static/images/geodata-from-metadata-in-choropleth-map.svg)

## Corpus linguistic methods on titles and sub titles

The following workflow is extensive. Start by merging metadata and UDC labels. In Select Rows, choose three things: 1. a UDC label of your choice. 2. the language code *lav*. 3. rows where the author field is not empty. Then send data to Corpus, where you choose to use *titles* and *sub_titles*. Once data has passed through the Corpus widget, you can use all the text mining widgets.

![screenshot](../_static/images/5-corpus-linguistic-tools-on-latvian-titles.svg)

## And now to something different — Image classification

One last thing worth mentioning is [Image Analytics widgets](https://orangedatamining.com/widget-catalog/image-analytics/importimages/), which can group images that share visual features. For this I use a small new dataset of pages from historical department store catalogues. The images are in the folder *daells warehouse categories*. Import the folder with Import Images and send it through a workflow like the one below. In Hierarchical Clustering the images are grouped, and when you click a group, the images in that group are sent on to Image Viewer.

![screenshot](../_static/images/6-images-classification.svg)
