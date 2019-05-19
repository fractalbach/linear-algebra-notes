# Linear Algebra Notes

Collection of Reference Sheets and Notes for Linear Algebra.  Includes definitions and proofs. Available as both Webpages and PDF files.

## Table of Contents

[**All Combined Notes** [PDF]](https://fractalbach.github.io/linear-algebra-notes/pdf/combined.pdf)

1. [**Definitions**](https://fractalbach.github.io/linear-algebra-notes/html/1defs.html)

2. [**Proofs**](https://fractalbach.github.io/linear-algebra-notes/html/2proofs.html)

3. [**Matrices**](https://fractalbach.github.io/linear-algebra-notes/html/3matrix.html)

4. [**Applications**](https://fractalbach.github.io/linear-algebra-notes/html/4apps.html)

5. [**Tips and Tricks**](https://fractalbach.github.io/linear-algebra-notes/html/5tricks.html)

## How It's Made

The "source" is markdown files found in `/md`.  That's where all the content is stored.

The builder file, `build.py`, makes use of Pandoc to create the files. It takes the markdown files as input, and outputs files to `/html` and `/pdf` directories. The web pages are made from templates, found in the `/templates` directory.
