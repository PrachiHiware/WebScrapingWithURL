# WebScrapingWithURL

This code performs the following steps:__ __

1 Imports the necessary libraries: urllib.request for making HTTP requests and BeautifulSoup for parsing HTML. <br />
2 Uses urllib.request.urlretrieve() to download the content of a webpage from the specified URL and save it to a local file named text_file.txt.<br />
3 Opens the text_file.txt in read mode to read its contents.<br />
4 Creates a BeautifulSoup object named soup to parse the HTML content of the downloaded file.<br />
5 Opens a new text file named test1.txt in write mode.<br />
6 Iterates through all paragraph elements found in the soup.<br />
7 For each paragraph element, extracts the text content using data.get_text() and writes it to the new text file using f.writelines().<br />
8 Closes the new text file.<br /><br />

Overall, this code snippet downloads a web page, extracts the text content from its paragraph elements, and saves the extracted text into a new text file.
