# Stock Scraper

This project allows you to fetch stock data from **Screener.in** using **ISIN codes**. However, during the implementation, we faced multiple challenges with **ISIN lookup** and **API limitations**, which led us to a **hard mapping approach** for certain stocks.

## Problem Encountered

1. **ISIN Search Issue**:  
   Initially, I attempted to search for stocks directly by their **ISIN** codes. However, **Screener.in** did not support ISIN-based searches. It only accepts stock tickers, so I was unable to use ISIN codes to fetch data directly from the site.

2. **API Attempts**:
   I explored **external APIs** to convert ISINs into stock tickers. Here's a list of the APIs I attempted:

   - **FinancialModelingPrep API**: I tried using their ISIN search API, but it either didn’t provide results or failed to return the correct ticker data.
   - **Alpha Vantage API**: While attempting to fetch stock data, the API key either didn’t work or the endpoint didn’t support ISIN-based queries.
   - **Other Free APIs**: I also searched for free APIs to convert ISINs to stock tickers but faced issues with access, rate limits, or inaccurate data.

3. **Hard Mapping**:
   After the external API attempts failed, I decided to **manually map the stock names** and **tickers** for a select list of stocks. This allowed me to bypass the ISIN lookup issue by directly searching for stocks via their ticker names on **Screener.in**.

   However, **Screener.in** requires using **NSE ticker symbols** (e.g., `RELIANCE` for **Reliance Industries**) in the URL, not the full stock name (e.g., **Reliance Industries**). So, I created a hard mapping to associate **stock names** with their **NSE ticker symbols**.

---

## Solution

### **Approach I Finally Used:**

- **Hard Mapping of Ticker Symbols**:  
  After failing to find a working API solution, I created a manual mapping of **ISIN codes** to **stock names** and their corresponding **NSE ticker symbols**.
  
  Example:  
  - **Reliance Industries** → **`RELIANCE`**
  - **Tata Consultancy Services** → **`TCS`**
  
  This allowed me to construct the correct **Screener.in** URL for each stock by using the corresponding **NSE ticker symbol** in the URL (`https://www.screener.in/company/<ticker>/`).

- **Fetching Stock Data**:  
  After generating the correct ticker symbols for each stock, I used **Python's BeautifulSoup** to scrape key metrics (like P/E ratio, market cap, etc.) from **Screener.in**.

### **Tools and Libraries Used**:
- **Requests**: For making HTTP requests to **Screener.in** and other APIs.
- **BeautifulSoup**: For scraping stock data from the **Screener.in** web page.
- **Python**: Used for scraping and data extraction logic.

---

## Development and Debugging

During the development of the scraper, I encountered several **syntax and logical errors**. To resolve them, I turned to **ChatGPT** for assistance. Here’s what was fixed:

- **Syntax errors**: I was able to get help fixing missing or mismatched parentheses and other Python syntax issues.
- **Logical errors**: ChatGPT helped me fix issues like handling missing data during the scraping process and correcting the mapping of ISINs to tickers.

---

## How to Use the Scraper

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/your-username/stock-scraper.git
