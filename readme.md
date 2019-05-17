# Linear Algebra Notes

Collection of Reference Sheets and Notes for Linear Algebra.  Includes definitions and proofs.

## Table of Contents

All pages are available as both a webpage and a PDF file.

1. [Defintions](html/vec.html) ... [[PDF]](pdf/vec.pdf)



## How It's Made

The "source" is markdown files found in `/md`.  That's where all the content is stored.

The builder file, `build.py`, makes use of Pandoc to create the files. It takes the markdown files as input, and outputs files to `/html` and `/pdf` directories. The web pages are made from templates, found in the `/templates` directory.
