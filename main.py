import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv

def search_wikipedia(company_name):
    """
    Searches Wikipedia for the given company name and returns the founder's name if available.

    Parameters:
    company_name (str): The name of the company to search for.

    Returns:
    str: The name of the founder(s) or an error message if the information cannot be retrieved.
    """
    # Define the Wikipedia API endpoint for searching
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': company_name,  # The search term (company name)
        'utf8': 1
    }

    # Send a GET request to the Wikipedia API
    response = requests.get(search_url, params=params)

    # Check if the API request was successful
    if response.status_code != 200:
        return "Failed to retrieve search results"

    # Parse the JSON response from the Wikipedia API
    search_results = response.json()
    search_hits = search_results.get('query', {}).get('search', [])

    # If there are no search results, return a message indicating this
    if not search_hits:
        return "No search results found"

    # Retrieve the title of the first search result (most relevant result)
    page_title = search_hits[0]['title']
    page_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_title)}"

    # Send a GET request to the Wikipedia page of the company
    response = requests.get(page_url)

    # Check if the page request was successful
    if response.status_code != 200:
        return f"Failed to retrieve the page: {page_url}"

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the infobox on the page (typically contains company details)
    infobox = soup.find('table', {'class': 'infobox'})
    if infobox:
        rows = infobox.find_all('tr')
        founders = []
        for row in rows:
            header = row.find('th')
            # Look for a row that contains 'Founder' in the header
            if header and 'Founder' in header.get_text():
                founder = row.find('td')
                if founder:
                    founders.append(founder.get_text(strip=True))
        # If founders were found, return them as a comma-separated string
        if founders:
            return ', '.join(founders)
    return "Founder information not found"

def process_csv_file(file_path):
    """
    Processes a CSV file containing company names and searches for each company's founder.

    Parameters:
    file_path (str): The path to the CSV file containing company names.
    """
    try:
        # Open the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            # Skip the header row if there is one
            next(csv_reader, None)

            # Process each company name in the CSV file
            for row in csv_reader:
                company_name = row[0].strip()  # Extract the company name from the row
                if company_name:  # Check if the company name is not empty
                    print(f"\nSearching for {company_name}...")
                    founder = search_wikipedia(company_name)
                    print(f"Founder of {company_name}: {founder}")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def main():
    """
    The main function that initiates the script.
    """
    print("Welcome to the Company Founder Finder!")

    # Hardcoded path to the CSV file containing company names
    file_path = "/content/Company_Names_Dataset.csv"

    # Process the CSV file to find the founders
    process_csv_file(file_path)

if __name__ == "__main__":
    main()
