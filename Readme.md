# Twitter Trends Scraper

This project scrapes the top 5 trending topics from Twitter (X.com) using Selenium and stores the data in a MongoDB database. A Flask API is used to trigger the scraper and fetch the latest results, while a simple frontend displays the trends.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Security Warning](#security-warning)
- [Troubleshooting](#troubleshooting)


## Features
- Automates login to Twitter (X.com) using Selenium.
- Scrapes the top 5 trending topics.
- Stores the results in MongoDB with timestamps and IP addresses.
- Simple Flask API to trigger scraping and retrieve the latest trends.
- Basic frontend to display the results.

## Prerequisites
- Python 3.10+
- MongoDB (running locally at `localhost:27017`)
- Chrome browser and [ChromeDriver](https://sites.google.com/chromium.org/driver/)

### Python Packages
- Flask
- Flask-CORS
- pymongo
- selenium

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/selenophile1805/RSIT_Assignment.git
   cd twitter-trends-scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   Ensure MongoDB is running locally on port 27017.

5. Download ChromeDriver and ensure it matches your Chrome version. Place it in your system's PATH.

## Usage
### Run the API
```bash
python api.py
```

### Access the Frontend
Open `index.html` in your browser or serve it using a simple HTTP server.
```bash
python -m http.server
```

Click the button to trigger the script and display the latest Twitter trends.

## File Structure
```
/
|-- api.py              # Flask API to trigger the scraper and fetch results
|-- scrapper.py         # Selenium script to scrape Twitter trends
|-- index.html          # Frontend to display the results
|-- README.md           # Project documentation
```

## Security Warning
- **DO NOT** hard-code sensitive information (e.g., Twitter username/password) directly in the code. Use environment variables or secure vaults.
- This project uses Selenium to automate login, which can violate Twitter's terms of service. Use at your own risk.

## Troubleshooting
- **ChromeDriver Version Mismatch**: Ensure you download the ChromeDriver that matches your installed Chrome version.
- **MongoDB Connection Issues**: Verify MongoDB is running and accessible at `localhost:27017`.
- **Element Not Found**: Twitter's DOM may change, causing element locators to break. Update the XPaths or selectors in `scrapper.py`.



