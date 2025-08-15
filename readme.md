# Meme Generator

A multimedia application that dynamically generates memes by overlaying quotes on images. This project demonstrates object-oriented programming principles including inheritance, abstract classes, and the strategy pattern.

## Features

- **Web Interface**: Flask-based web application for interactive meme generation
- **Command Line Interface**: Generate memes directly from the terminal
- **Multiple File Format Support**: Ingest quotes from CSV, DOCX, PDF, and TXT files
- **Custom Meme Creation**: Upload images and add custom quotes
- **Random Meme Generation**: Generate memes with random quotes and images

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Udacity_Meme_Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Install the package:
   ```bash
   pip install -e .
   ```

## Usage

### Web Application
Start the Flask web server:
```bash
python app.py
```
Visit `http://localhost:5000` in your browser to use the web interface.

### Command Line Interface
Generate a random meme:
```bash
python meme.py
```

Generate a custom meme:
```bash
python meme.py --path "./path/to/image.jpg" --body "Your quote here" --author "Author Name"
```

## Project Structure

```
Udacity_Meme_Generator/
├── MemeGenerator/          # Meme generation engine
│   ├── __init__.py
│   └── meme_engine.py
├── QuoteEngine/           # Quote ingestion system
│   ├── __init__.py
│   ├── ingestor_interface.py
│   ├── ingestor.py
│   ├── csv_ingestor.py
│   ├── docx_ingestor.py
│   ├── pdf_ingestor.py
│   ├── txt_ingestor.py
│   └── quote_model.py
├── _data/                 # Sample data files
├── templates/             # HTML templates
├── static/                # Static web assets
├── app.py                 # Flask web application
├── meme.py               # Command line interface
└── requirements.txt      # Python dependencies
```

## Modules Overview

### Quote Engine Module
Responsible for ingesting quotes from various file formats using the strategy pattern.

**Key Components:**
- `IngestorInterface`: Abstract base class defining the ingestor contract
- `Ingestor`: Main class that selects appropriate ingestor based on file type
- Individual ingestors for CSV, DOCX, PDF, and TXT files
- `QuoteModel`: Data class representing a quote with body and author

**Usage:**
```python
from QuoteEngine.ingestor import Ingestor
quotes = Ingestor.parse('path/to/quotes.csv')
```

### Meme Engine Module
Handles image manipulation and text overlay for meme generation.

**Features:**
- Image resizing and optimization
- Text overlay with custom fonts
- Automatic text positioning
- Multiple output formats

**Usage:**
```python
from MemeGenerator.meme_engine import MemeEngine
meme_engine = MemeEngine('./output')
path = meme_engine.make_meme('image.jpg', 'Quote text', 'Author')
```

## Dependencies

- **Flask**: Web framework for the web interface
- **Pillow**: Image processing and manipulation
- **requests**: HTTP library for downloading images
- **pandas**: CSV file processing
- **python-docx**: Microsoft Word document processing
- **PyMuPDF**: PDF file processing

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 style guidelines. Run syntax checks:
```bash
python -m py_compile **/*.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is part of the Udacity Intermediate Python Nanodegree program.