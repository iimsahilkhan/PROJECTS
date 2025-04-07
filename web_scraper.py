import requests
from bs4 import BeautifulSoup

# URL to scrape (example: BBC News)
url = "https://www.bbc.com/news"    #we can take input when we khonw link
                                     # url = input("Enter Website: ")

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all headline elements (adjust selector based on site structure)
    headlines = soup.find_all('h2')  # BBC uses h2 for some headlines, may vary
    
    # Print the headlines
    print("Latest Headlines:")
    for i, headline in enumerate(headlines[:5], 1):  # Limit to 5 for brevity
        print(f"{i}. {headline.get_text().strip()}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Optional: Save to a file
'''with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines[:5]:
        file.write(f"{headline.get_text().strip()}\n")'''