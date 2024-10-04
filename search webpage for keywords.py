#this will search for HOT WORDS on a WEBPAGE :) 

import requests
from bs4 import BeautifulSoup

# Function to search a webpage for specific keywords
def search_keywords_in_webpage(url, keywords):
    try:
        # Fetch webpage content
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        webpage_text = soup.get_text()

        # Search for keywords in the webpage text
        found_keywords = [keyword for keyword in keywords if keyword.lower() in webpage_text.lower()]
        
        if found_keywords:
            print(f"The following keywords were found on the webpage {url}: {', '.join(found_keywords)}")
        else:
            print(f"No keywords were found on the webpage {url}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage {url}: {e}")

# Example usage
urls = [
    "https://en.wikipedia.org/wiki/Lawrence_Martin-Bittman",
    "https://en.wikipedia.org/wiki/The_KGB_and_Soviet_Disinformation",
    "https://archive.org/stream/1985-09-07-kgb-2955/1985-09-07-KGB-2955_djvu.txt",
    "https://archive.org/stream/1985-07-10-joint-am/1985-07-10-joint-am_djvu.txt"
]
keywords = ["russia", "kgb", "подготовка", "1985", "potato"]

for url in urls:
    search_keywords_in_webpage(url, keywords)
