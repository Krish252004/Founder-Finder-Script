# Company Founder Finder

This Python script allows you to find the founders of companies using their names. The script reads company names from a CSV file, searches Wikipedia for each company, and retrieves the founder's name if available. This tool is useful for quickly gathering founder information from a list of companies.

## Features

- **Automated Search:** Uses Wikipedia's API to search for companies and retrieve founder information.
- **CSV Processing:** Reads company names from a CSV file and processes each one individually.
- **Error Handling:** Includes basic error handling to manage issues such as network errors or missing information.
- **Modular Code:** The script is organized into functions for clarity and reusability.

## Requirements

To run this script, you need to have Python 3 installed on your machine. Additionally, you'll need the following Python packages:

- `requests`
- `beautifulsoup4`

You can install these packages using pip:
pip install requests beautifulsoup4

## Usage
### Clone the Repository:
git clone https://github.com/yourusername/company-founder-finder.git
cd company-founder-finder

### Place your CSV File:
Ensure that CSV file, containing the company names, is placed in the same directory as the script. The file should be named Company_Names_Dataset.csv. The CSV should have one column with no header, listing the company names.

### Run the Script:
You can run the script using Python: main.py
The script will read the company names from the CSV file and output the founder's name for each company.

## Example Output

Welcome to the Company Founder Finder!

- Searching for Google...
- Founder of Google: Larry Page, Sergey Brin

- Searching for Microsoft...
- Founder of Microsoft: Bill Gates, Paul Allen

## Limitations
- The script relies on Wikipedia for data, so the accuracy depends on the quality of the information available on Wikipedia.
- The script currently searches for only the first matching Wikipedia page, which may not always be the correct one.

## Future Improvements
- **Expand Sources**: Incorporate other reliable sources such as Crunchbase or LinkedIn to enhance data accuracy.
- **Machine Learning**: Implement machine learning models to predict founders when direct information is not available.
- **Improve Error Handling**: Enhance the script to handle more complex edge cases and improve robustness.
