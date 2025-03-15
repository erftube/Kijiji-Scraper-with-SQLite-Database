
# Kijiji Scraper with SQLite Database

This repository contains a Python project that scrapes room rental listings from Kijiji and stores the data in a SQLite database. The project includes:

- **Web Scraper:** Uses `requests` and `BeautifulSoup` to extract listing details (title, price, URL) from Kijiji.
- **SQLite Database Handler:** A class that creates an SQLite database, stores items with a unique URL constraint, and gracefully handles duplicate insertions by rolling back transactions.

## Features

- **Scraping:** Extracts room rental listings from a Kijiji search page.
- **Data Storage:** Saves scraped items to a SQLite database with a unique URL column.
- **Error Handling:** Prevents duplicate entries by rolling back on unique constraint violations.

## Requirements

- Python 3.6+
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```

2. **(Optional) Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Either install manually:

   ```bash
   pip install requests beautifulsoup4
   ```

   Or use the provided `requirements.txt` if available:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Scraping Kijiji Listings

1. Update the `search_url` variable in your scraper script (e.g., `scraper.py`) if needed.
2. Run the scraper:

   ```bash
   python scraper.py
   ```

   The script will print the scraped listings to your console.

### Storing Items in SQLite Database

1. The `SQLDatabase` class (in, for example, `database.py`) creates an SQLite database named `items.db` and a table with a unique URL column.
2. Run the script to test inserting items:

   ```bash
   python database.py
   ```

   The script demonstrates inserting items and handles duplicates by rolling back transactions.

## Project Structure

```
.
├── README.md           # This file
├── scraper.py          # Contains the web scraping code
├── database.py         # Contains the SQLite database class and insertion example
└── requirements.txt    # (Optional) List of dependencies
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
