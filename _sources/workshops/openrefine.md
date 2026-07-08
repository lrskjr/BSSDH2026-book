# Data cleaning with OpenRefine

﻿![openrefine_logo.svg](../_static/images/openrefine_logo.svg)

## Increasing memory allocation
https://openrefine.org/docs/manual/installing#increasing-memory-allocation


Find openrefine.l4j. On a Windows machine it is here: C:\Program Files (x86)\OpenRefine


## Where do I download OpenRefine?

Download OpenRefine from [https://openrefine.org/download.html](https://openrefine.org/download.html). Versions are available for both Windows and Mac.

## When would I use OpenRefine?
OpenRefine is a smart tool that works best with a dataset organised in rows and columns. Most often this will be a CSV or Excel file. We use it to bring structure and order to the dataset. This is often necessary because, for the vast majority of datasets, there are inconsistencies in the data. These inconsistencies often come from data entry and from the fact that the dataset was originally in one or more other formats before it was brought together in rows and columns.

For example, in a bibliographic dataset you may find inconsistencies like those in the image below. Even before we have looked closely at the dataset, we can say with reasonable confidence that the names are the same but have been entered differently.


![Pasted image 20260706233552.png](../_static/images/Pasted image 20260706233552.png)

These are often small inconsistencies between different text strings, which in many contexts may be insignificant. But if the dataset is to be analysed systematically with a computer, you first need order and consistency. You choose whether to write Ildiko Gāšpāra, Ildikó Gáspár, or Ildiko Gaspar — but it must be exactly the same every time. OpenRefine can help here, because the program has good algorithms that can sort text strings into uniform groups, after which you can merge the different strings in a group into the new string you prefer.

You may also have a dataset where some cells contain several different pieces of data. In these cases it is often ideal to spread the different pieces of data across several columns.
The image below is an example of this. Some data repeats in every record. For example, a host_title, an ISSN number, and an issue — and it can be useful to create order by making three new columns, each with its own piece of data.

![Pasted image 20260707003942.png](../_static/images/Pasted image 20260707003942.png)

OpenRefine is a secure program. It runs locally on your computer and does not need the internet to work. When the program opens, it may look as if you are online, because it opens in a browser window. But if you look carefully at the address bar at the top of the browser — where you enter `https://...` or search — you will see `http://127.0.0.1:3333`. The address 127.0.0.1 means that OpenRefine is hosted by a local server on your computer, and 3333 is the port number the program runs on. You can see the local server in the console window that always opens at the same time as the browser window. The console window must stay open while you use the program; otherwise it will not work.

## How do I get data into the program?
Data enters OpenRefine when you click choose files and locate a file on your computer to import into the program. Once you have found the file, you can click next. A new window opens with a preview of the dataset at the top and some setting options at the bottom. The program is good at recommending the right settings, but to be safe, check "Trim leading & trailing whitespace from strings", so that data is loaded without invisible space characters at the beginning or end of a word. When you are happy with the settings, click "Create project" in the top right corner to create a project. The project is a copy of your dataset, and the changes you make are saved in the project — not in the dataset file you imported. When you have made the changes you want, export the project to a new file and save it under a new filename.

## How do I use the program?
The program has various tools that you can choose from drop-down menus. These appear when you click the small arrows to the left of each column name. The same tools are available in every column. On the far left, however, there is a column called All, which has special tools that apply to all columns. Let us explore some of the tools.

## Split into several columns

Click the arrow to the left of author.

![Pasted image 20260707110449.png](../_static/images/Pasted image 20260707110449.png)

Choose Edit column -> Split into several columns ...


![Pasted image 20260707110708.png](../_static/images/Pasted image 20260707110708.png)

The separator is a comma, and from the first 10 columns we can see immediately, there is a comma in every cell in the column. I enter two in "Split into ... columns at most" to keep track of the number of new columns.

![Pasted image 20260707110610.png](../_static/images/Pasted image 20260707110610.png)

We can inspect the result. It is not obvious, but in front of each name in "author 2" there is a space character left over from the split we just made.

## Trim leading and trailing whitespace
![Pasted image 20260707173503.png](../_static/images/Pasted image 20260707173503.png)

We can handle the space with the "Trim leading and trailing whitespace" function. You find it under Edit cells -> Common transforms -> Trim leading and trailing whitespace.

![Pasted image 20260707174208.png](../_static/images/Pasted image 20260707174208.png)

## Rename column
The new columns are named automatically, but we can change the name with the "Rename column" function. Edit column -> Rename column ...

![Pasted image 20260707181555.png](../_static/images/Pasted image 20260707181555.png)

Give the column a new name.
![Pasted image 20260707181745.png](../_static/images/Pasted image 20260707181745.png)

## Join columns
Now we join the two author columns again.

Edit columns-> Join columns...

![Pasted image 20260707210026.png](../_static/images/Pasted image 20260707210026.png)

Choose the two columns you want to join. In "Separator between ..." enter a comma followed by a space. Give the new column a name (author), check Delete joined columns, and click OK.

![Pasted image 20260707210258.png](../_static/images/Pasted image 20260707210258.png)



## Task: Split host_info into three columns
![Pasted image 20260708125259.png](../_static/images/Pasted image 20260708125259.png)

![Pasted image 20260708125338.png](../_static/images/Pasted image 20260708125338.png)

![Pasted image 20260708125431.png](../_static/images/Pasted image 20260708125431.png)

## Transform and GREL
The Transform function is under Edit cells -> Transform.
![Pasted image 20260708125541.png](../_static/images/Pasted image 20260708125541.png)

A new window opens, and you can use GREL functions. For example, you can use `.replace()`, which lets you replace part of a text string with something else. This allows us to clean the field of 'host_title: '.

![Pasted image 20260708125752.png](../_static/images/Pasted image 20260708125752.png)

## Task: Clean and rename host_name 1–3
Use the functions we have just seen to clean and rename the three columns host_name 1–3.

## Transform and advanced GREL solutions
GREL (General Refine Expression Language) is a scripting language for working with text strings. It can be used to solve all kinds of problems, including ones that are complicated to write. This text does not go into depth on advanced solutions. GREL takes time to learn, because you can use RegEx (Regular Expressions) as a tool for text processing. Let us take a simple example.

In the column 'subject_person' there are two commas. The first comma separates surname and given name, and we want to keep it. The second comma sits at the end of the string after the given name and is essentially just noise.

![Pasted image 20260708145432.png](../_static/images/Pasted image 20260708145432.png)

When we want to remove the final comma, we cannot use `value.replace(',', '')`, because that would delete both commas — including the first one we want to keep. The solution is RegEx, because we can target the comma at the end of the string.

First, open Transform: Edit cells -> Transform.

![Pasted image 20260708150120.png](../_static/images/Pasted image 20260708150120.png)




`value` represents the current text string.

`.replace(..., '')` is the method for replacing part of the text string with an empty string.

`/,$/` is the RegEx pattern that matches the final comma (`$` = end of string)


## Text facets and clusters

You choose text facets under Facet -> Text facet.

![Pasted image 20260708095409.png](../_static/images/Pasted image 20260708095409.png)

The facets appear in a new panel on the left side of the screen.
![Pasted image 20260708113809.png](../_static/images/Pasted image 20260708113809.png)

We can see that identical values are grouped. Ābele, Indra appears once, while Ābele, Inga appears eight times, and so on. The program suggests clicking the Cluster button.

A new window opens. Click Cluster.

![Pasted image 20260708123520.png](../_static/images/Pasted image 20260708123520.png)

A new window opens, and you can now choose between different algorithms that sort similar-looking text strings. Click the Merge? field to the left of the strings if you want to make a correction. When you are done, click Merge selected & re-cluster and try choosing a function.

![Pasted image 20260708124029.png](../_static/images/Pasted image 20260708124029.png)

This text does not explain the different algorithms in depth, but they are well documented in OpenRefine's own documentation. Read more here: https://openrefine.org/docs/technical-reference/clustering-in-depth


## Task: Clean the author and topic columns with clustering

Continue cleaning the author column, then continue with the topic column.

## How do I export the project to a new file?
When you have finished cleaning your dataset, you will probably want to work with it in another program. You can therefore export it. In most cases you will export as a CSV file. The export function is in the top right corner.


## Resource

OpenRefine documentation: [https://openrefine.org/docs/manual/starting](https://openrefine.org/docs/manual/starting)

Library Carpentry: OpenRefine: [https://librarycarpentry.github.io/lc-open-refine/01-introduction.html](https://librarycarpentry.github.io/lc-open-refine/01-introduction.html)

Seth van Hooland, Ruben Verborgh, and Max De Wilde. Cleaning Data with OpenRefine, Programming historian: [https://programminghistorian.org/en/lessons/cleaning-data-with-openrefine](https://programminghistorian.org/en/lessons/cleaning-data-with-openrefine)
