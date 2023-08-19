import urllib.request
from bs4 import BeautifulSoup

# Request the user to provide a URL for scraping
user_url = input("Please enter the URL to scrape: ")

# Download the webpage content using the provided URL
download_path = "text.txt"
urllib.request.urlretrieve(user_url, download_path)

# Read the downloaded content from the text file
with open(download_path, "r") as file:
    downloaded_content = file.read()

# Parse the HTML content using BeautifulSoup
parsed_content = BeautifulSoup(downloaded_content, 'html.parser')

# Create a new text file to store the extracted paragraphs
output_file_path = "test1.txt"
with open(output_file_path, "w") as output_file:
    # Extract and save text from paragraphs (p) elements
    for paragraph in parsed_content.find_all("p"):
        paragraph_text = paragraph.get_text()
        output_file.writelines(paragraph_text)

print("Extraction complete. Paragraphs have been saved in", output_file_path)
