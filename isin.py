import requests
from bs4 import BeautifulSoup

# Hardcoded ISIN-to-Company Mapping with their corresponding NSE tickers
isin_to_company = {
    'INE002A01018': ('Reliance Industries', 'RELIANCE'),
    'INE123A01016': ('Tata Consultancy Services', 'TCS'),
    'INE062A01020': ('Infosys', 'INFY'),
    'INE105A01010': ('HDFC Bank', 'HDFCBANK'),
    'INE258A01026': ('Larsen & Toubro', 'LT'),
    'INE446A01022': ('Bajaj Finance', 'BAJFINANCE'),
    'INE040A01034': ('ICICI Bank', 'ICICIBANK'),
    'INE467A01023': ('Hindustan Unilever', 'HINDUNILVR'),
    'INE318A01028': ('Maruti Suzuki', 'MARUTI'),
    'INE274A01024': ('State Bank of India', 'SBIN')
}

# Scrape stock data from Screener.in using company ticker symbol
def scrape_stock_data(company_name, ticker):
    url = f"https://www.screener.in/company/{ticker}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    print(f"Fetching data from: {url}")  # Debugging line to print the URL
    
    if response.status_code != 200:
        print(f"Failed to retrieve data from Screener.in for {company_name}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape key metrics
    metrics = {}
    ratios = soup.find_all('div', class_='company-ratios')
    for ratio_div in ratios:
        items = ratio_div.find_all('li')
        for item in items:
            key_span = item.find('span', class_='name')
            value_span = item.find('span', class_='number')
            if key_span and value_span:
                key = key_span.text.strip()
                value = value_span.text.strip()
                metrics[key] = value

    # Scrape Pros and Cons
    pros = []
    cons = []

    # Extract the pros and cons sections
    analysis_section = soup.find("section", id="analysis")
    if analysis_section:
        flex_div = analysis_section.find("div", class_="flex flex-column-mobile flex-gap-32")
        if flex_div:
            # Extracting pros
            pros_div = flex_div.find("div", class_="pros")
            if pros_div:
                pros_content = pros_div.get_text(separator="\n", strip=True)
                pros = pros_content.split('\n')

            # Extracting cons
            cons_div = flex_div.find("div", class_="cons")
            if cons_div:
                cons_content = cons_div.get_text(separator="\n", strip=True)
                cons = cons_content.split('\n')
        else:
            print("No flex div found")
    else:
        print("No analysis section found")

    return {
        "metrics": metrics,
        "pros": pros,
        "cons": cons
    }

# Main function to ask for ISIN and fetch data
def main():
    # Ask for ISIN code
    isin = input("Enter ISIN code: ").strip().upper()

    # Lookup company and ticker from hardcoded ISIN mapping
    company_data = isin_to_company.get(isin)

    if not company_data:
        print(f"Company for ISIN {isin} not found.")
        return

    company_name, ticker = company_data

    print(f"\nFound company: {company_name}")
    
    # Scrape stock data from Screener.in
    data = scrape_stock_data(company_name, ticker)
    if not data:
        print("Failed to scrape stock data.")
        return

    # Display results
    print("\nKey Metrics:")
    for k, v in data['metrics'].items():
        print(f"{k}: {v}")

    print("\nPros:")
    for p in data['pros']:
        print(f"- {p}")

    print("\nCons:")
    for c in data['cons']:
        print(f"- {c}")

if __name__ == "__main__":
    main()
