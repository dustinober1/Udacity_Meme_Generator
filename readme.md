# Meme Generator Project

## Overview
This project is designed to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It demonstrates a profound understanding of Python principles including complex inheritance, abstract classes, class methods, and strategy objects, along with utilizing advanced third-party libraries for image manipulation.

## Table of Contents
- [Setting Up and Running the Program](#setting-up-and-running-the-program)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Running the Program](#running-the-program)
- [Modules Overview](#modules-overview)
  - [1. Quote Engine Module](#1-quote-engine-module)
  - [2. Meme Engine Module](#2-meme-engine-module)
  - [3. Various Ingestors](#3-various-ingestors)
- [Conclusion](#conclusion)

## Setting Up and Running the Program

### Prerequisites
- Python 3.x
- pip (Python’s package installer)

### Installation Steps
1. Clone the repository
   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. Install the required packages
    pip install -r requirements.txt

## Running the Program
   ```sh
   python main.py

# Modules Overview

# Quote Engine Module
Responsibility: Ingests various types of files containing quotes.

Dependencies: None
Usage Example:
from QuoteEngine import Ingestor
quotes = Ingestor.parse('path_to_quote_file')

# Meme Engine Module
Responsibility: Manipulates and draws text onto images.

Dependencies:
Pillow: For loading, resizing, and drawing text on images.
Usage Example:
from MemeEngine import MemeEngine
meme_engine = MemeEngine('output_directory')
meme_engine.make_meme('path_to_image', 'quote text', 'author')

# Various Ingestors
Responsibility: Serve as strategy objects realizing the Ingestor Interface for each file type (csv, docx, pdf, txt).

Dependencies:
pandas: For CSV Ingestor.
python-docx: For DOCX Ingestor.
PyMuPDF: For PDF Ingestor.
Usage Example:
from QuoteEngine import CSVIngestor, DOCXIngestor
csv_quotes = CSVIngestor.parse('path_to_csv_file')
docx_quotes = DOCXIngestor.parse('path_to_docx_file')

# Conclusion
This project provides hands-on experience in designing a system with various components working in unison, implementing object-oriented programming concepts, and utilizing advanced Python libraries for practical application development. It is an exemplar demonstration of building a multimedia application using Python, integrating diverse libraries and maintaining modular, scalable, and robust code.