# Import the required libraries
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class NewsScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("News Headlines Scraper")
        self.root.geometry("600x400")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # URL entry
        ttk.Label(main_frame, text="Website URL:").grid(row=0, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))
        self.url_entry.insert(0, "https://www.livemint.com/news")
        
        # Scrape button
        ttk.Button(main_frame, text="Scrape Headlines", command=self.scrape_headlines).grid(row=1, column=0, columnspan=3, pady=10)
        
        # Headlines display
        ttk.Label(main_frame, text="Latest News Headlines:").grid(row=2, column=0, sticky=tk.W)
        self.headlines_text = scrolledtext.ScrolledText(main_frame, width=60, height=15)
        self.headlines_text.grid(row=3, column=0, columnspan=3, pady=5)
        
        # Save button
        ttk.Button(main_frame, text="Save Headlines", command=self.save_headlines).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def scrape_headlines(self):
        website_url = self.url_entry.get()
        self.headlines_text.delete(1.0, tk.END)
        
        try:
            # Add headers to mimic a browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            webpage = requests.get(website_url, headers=headers)
            
            if webpage.status_code == 200:
                soup = BeautifulSoup(webpage.text, 'html.parser')
                
                # Try different selectors for headlines
                headlines = []
                
                # Try h3 tags
                headlines.extend(soup.find_all('h3'))
                
                # Try h2 tags
                headlines.extend(soup.find_all('h2'))
                
                # Try headlines with specific classes
                headlines.extend(soup.find_all(class_=['headline', 'title', 'news-title']))
                
                if not headlines:
                    # If no headlines found, show the HTML structure for debugging
                    self.headlines_text.insert(tk.END, "No headlines found. Here's the page structure:\n\n")
                    self.headlines_text.insert(tk.END, str(soup.prettify()[:1000]))  # Show first 1000 chars
                    messagebox.showwarning("Warning", "No headlines found. Check the displayed HTML structure.")
                    return
                
                # Display found headlines
                for number, headline in enumerate(headlines[:10], 1):  # Show up to 10 headlines
                    text = headline.get_text().strip()
                    if text:  # Only show non-empty headlines
                        self.headlines_text.insert(tk.END, f"{number}. {text}\n")
                
                if not self.headlines_text.get(1.0, tk.END).strip():
                    self.headlines_text.insert(tk.END, "No headlines found. The website structure might have changed.")
                    messagebox.showwarning("Warning", "No headlines found. The website structure might have changed.")
            else:
                messagebox.showerror("Error", f"Could not connect to the website. Error code: {webpage.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def save_headlines(self):
        headlines = self.headlines_text.get(1.0, tk.END).strip()
        if headlines:
            try:
                with open("news_headlines.txt", "w", encoding="utf-8") as file:
                    file.write(headlines)
                messagebox.showinfo("Success", "Headlines have been saved to 'news_headlines.txt'")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save headlines: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No headlines to save!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsScraperGUI(root)
    root.mainloop()