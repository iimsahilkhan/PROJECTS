# Import the required libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Choose a website to scrape
# We'll use a simple news website
website_url = "https://www.livemint.com/news"

# Step 2: Get the webpage content
# This is like opening a webpage in your browser
webpage = requests.get(website_url)

# Step 3: Check if we successfully got the webpage
if webpage.status_code == 200:
    print("Successfully connected to the website!")
    
    # Step 4: Parse the webpage content
    # BeautifulSoup helps us read the webpage like a book
    soup = BeautifulSoup(webpage.text, 'html.parser')
    
    # Step 5: Find all headlines
    # On BBC News, headlines are in <h3> tags
    headlines = soup.find_all('h3')
    
    # Step 6: Print the headlines
    print("\nHere are the latest news headlines:")
    for number, headline in enumerate(headlines[:5], 1):  # Show only first 5 headlines
        print(f"{number}. {headline.get_text().strip()}")
        
    # Step 7: Save headlines to a file
    with open("news_headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines[:5]:
            file.write(f"{headline.get_text().strip()}\n")
    print("\nHeadlines have been saved to 'news_headlines.txt'")
else:
    print(f"Oops! Could not connect to the website. Error code: {webpage.status_code}")