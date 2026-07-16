# Advanced Book Scraping System

A Python-based web scraping project that extracts book information from the **Books to Scrape** website and provides data analysis, visualization, search, export, and database features.

---

## Overview

This project scrapes book data from the Books to Scrape website and performs data cleaning, analysis, visualization, searching, and exporting using Python.

---

## Features

- Scrapes 1000 books from multiple pages
- Extracts:
  - Book Title
  - Price
  - Rating
  - Availability
  - Product URL
- Search books by title
- Filter books by rating
- Sort books by price
- Perform data analysis using Pandas
- Generate charts using Matplotlib
- Export data to:
  - CSV
  - Excel
  - JSON
- Store data in SQLite Database
- Simple GUI built with Tkinter

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- Matplotlib
- SQLite3
- Tkinter
- OpenPyXL

---

## Project Structure

```
Advanced-Book-Scraping-System/
│
├── scraper.py
├── analysis.py
├── search.py
├── export_data.py
├── database.py
├── gui.py
├── requirements.txt
├── README.md
├── books.csv
├── books.xlsx
├── books.json
├── books.db
└── charts/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/zainabbukhari817-spec/Advanced-Book-Scraping-System-.git
```

Navigate to the project directory:

```bash
cd Advanced-Book-Scraping-System-
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the scraper:

```bash
python scraper.py
```

Run data analysis:

```bash
python analysis.py
```

Search books:

```bash
python search.py
```

Export data:

```bash
python export_data.py
```

Create the SQLite database:

```bash
python database.py
```

Launch the GUI:

```bash
python gui.py
```

---

## Outputs

The project generates:

- books.csv
- books.xlsx
- books.json
- books.db
- Price Distribution Chart
- Rating Distribution Chart
- Top Expensive Books Chart

---

## Learning Outcomes

This project demonstrates practical experience in:

- Web Scraping
- Data Cleaning
- Data Analysis
- Data Visualization
- File Handling
- SQLite Database
- GUI Development
- Python Programming

---

## Author

**Syeda Zainab Bukhari**

BS Telecommunication Engineering

University of Engineering & Technology (UET) Taxila

---

## License

This project is developed for educational and learning purposes.
