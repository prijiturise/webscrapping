# 📰 News Headlines Scraper

## 1. Project Overview

The News Headlines Scraper is a simple Python application that retrieves the latest news headlines from a news website using the `requests` library and extracts headline text from HTML using `BeautifulSoup`.

The program prints up to five unique headlines in the terminal, numbered from 1 to 5.

## 2. Problem Statement

Write a Python script that opens a news website, fetches its HTML content, extracts the top five headlines, and displays them in the terminal.

The project introduces web scraping fundamentals, HTML inspection, CSS selectors, HTTP requests, and HTML parsing.

## 3. Technologies Used

- **Python** – Programming language
- **Requests** – Fetches webpage content
- **BeautifulSoup4** – Parses HTML and extracts headlines
- **Visual Studio Code** – Development environment

## 4. Project Structure

```text
headlines/
├── venv/
├── headlines.py
└── README.md
```

## 5. Prerequisites

- Python 3.9 or later
- Visual Studio Code or another Python editor
- Internet connection

## 6. Installation and Setup

### Step 1: Create the project folder

Open PowerShell or the VS Code terminal and run:

```powershell
mkdir headlines
cd headlines
```

### Step 2: Create a virtual environment

```powershell
python -m venv venv
```

### Step 3: Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run the following command for the current session and try activation again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Step 4: Install dependencies

```powershell
python -m pip install requests beautifulsoup4
```

## 7. How the Program Works

1. Sends an HTTP GET request to the BBC News website.
2. Includes a User-Agent header to identify the request as coming from a browser-like client.
3. Checks the HTTP response status before processing the webpage.
4. Parses the HTML using BeautifulSoup.
5. Extracts headline elements using CSS selectors.
6. Removes unnecessary whitespace and skips empty or duplicate headlines.
7. Prints up to five unique headlines, numbered from 1 to 5.
8. Handles request errors and cases where fewer than five headlines are available.

**Note:** The HTML structure of news websites may change. Inspect the current webpage and verify the CSS selectors in the browser's Developer Tools. If the headlines are rendered only through JavaScript, consider using an RSS feed, a public API, or Playwright.

## 8. Run the Application

Ensure that your terminal is inside the project folder and run:

```powershell
python headlines.py
```

## 9. Sample Output

The output will vary depending on the latest news available.

```text
1. First news headline
2. Second news headline
3. Third news headline
4. Fourth news headline
5. Fifth news headline
```

If fewer than five unique headlines are found, the program prints the available headlines and displays a message indicating how many were found.

## 10. Error Handling

The program handles the following situations:

- Network connection failures
- Request timeouts
- HTTP errors, such as 404 or 500
- Missing or incorrect HTML selectors
- Empty and duplicate headline entries
- Fewer than five unique headlines

## 11. Learning Outcomes

After completing this project, you will understand:

- How to send HTTP requests using Python
- How to parse HTML using BeautifulSoup
- How to inspect webpage elements using browser Developer Tools
- How to identify and test CSS selectors
- How to filter and display scraped data
- How to handle common web scraping errors

## 12. Future Enhancements

- Allow users to select different news websites.
- Save headlines to a CSV or text file.
- Add publication dates and article URLs.
- Build a Streamlit interface for displaying headlines.
- Use Playwright for JavaScript-rendered webpages.

## 13. Conclusion

This project demonstrates the basic principles of web scraping using Python. It provides practical experience in retrieving webpage content, extracting relevant information, and presenting clean results in the terminal.

**Project:** News Headlines Scraper  
**Language:** Python  
**Libraries:** Requests, BeautifulSoup4  
**Output:** Top five unique news headlines in the terminal
