#!/usr/bin/env python3

"""
Pandoc Note Builder

Converts .md files in the current directory to HTML and PDF files.

"""

import subprocess
import re
import os
from datetime import date
from string import Template

MARKDOWN_DIR = 'md'
HTML_DIR     = 'html'
PDF_DIR      = 'pdf'
HTML_TEMPLATE_FILEPATH = "templates/htmlplate.html"
HTML_TEMPLATE = None
TODAY = date.today().isoformat()

def init():
   global HTML_TEMPLATE
   with open(HTML_TEMPLATE_FILEPATH, 'r') as f:
   	HTML_TEMPLATE = Template(f.read())


def main():
    for mdFile in getMarkdownFiles():
        filename = stripFilenameExtention(mdFile)
        makeHTML(filename)
        makePDF(filename)


def stripFilenameExtention(filename):
    return os.path.splitext(filename)[0]


def getMarkdownFiles():
    mdFiles = []
    for filename in os.listdir(MARKDOWN_DIR):
        if filename.endswith('.md'):
            mdFiles.append(filename)
    return mdFiles


def makeHTML(filename):
    output = HTML_DIR + '/' + filename + '.html'
    inputfile = MARKDOWN_DIR + '/' + filename + '.md'
    print("building", output, '...')
    args = [
        'pandoc',
        inputfile,
        '-t',
        'html5',
        '--mathjax',
    ]
    prog = subprocess.run(args, stdout=subprocess.PIPE)
    body = prog.stdout.decode('utf-8')
    fullHTML = HTML_TEMPLATE.substitute({
    	'BODY': body,
        'TODAY': TODAY,
    })
    with open(output, 'w+') as f:
    	f.write(fullHTML)



def makePDF(filename):
    output = PDF_DIR + '/' + filename + '.pdf'
    inputfile = MARKDOWN_DIR + '/' + filename + '.md'
    print("building", output, '...')
    args = [
        'pandoc',
        inputfile,
        '-o',
        output
    ]
    subprocess.call(args)


init()
if __name__ == '__main__':
   main()
