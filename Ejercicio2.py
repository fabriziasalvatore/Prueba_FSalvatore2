#!/usr/bin/env python

# Import the library to interact with the operarating system
import os
# Import the library to do request in HTTP
import requests
# Import the library to analyze, navigate, modify and extract data from the HTML script
from bs4 import BeautifulSoup
# Import the library for the HTTP connection requests
import urllib3
# Import the library to manage and codify the special characters to be suitable in the URL
from urllib.parse import quote
# Import the library to iteract with the browser
from selenium import webdriver
# Import the library for the regular expressions
import re

#--------------------------------------------------------------------------------------------------------------------------------------
# ATTENTION! CHANGE the path to the Chrome WebDriver executable on your pc and the path to the output folder to save the screenshot
webdriver_path = 'C:/WebDriver/chromedriver_win32'
output_path = 'C:/Users/e_fsalva/Documents/PERSONALE/PROVA/Prueba_FSalvatore/.git'
#--------------------------------------------------------------------------------------------------------------------------------------

# Make "automatización" research in Google

# Save "automatización" as query
google_query = "automatización"

# Build the correct url
research_url = f"https://www.google.com/search?q={quote(google_query)}&hl=es"

# Enable the SSL verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Header to use different user agents types to send the HTTP request 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Make the HTTP request to Google with the SSL verification enable
google_research = requests.get(research_url, headers=headers, verify=False)

# Save the response of the server as text
google_result = google_research.text

# Analyze the HTML text and build an object with the structure of the HTML text
google_object = BeautifulSoup(google_result, 'html.parser')


# Find and navigate to wikipedia page

# Find the wikipedia link in the HTML text
wikipedia_link = google_object.find('a', {'href': lambda href: href and 'wikipedia.org' in href})

if wikipedia_link:
    # If the link is found save the url the links point to
    wikipedia_url= wikipedia_link['href']
else:
    print("La búsqueda de automatización no arrojó ningún resultado.")
    
# Make the HTTP request with the SSL verification enable
wikipedia_research = requests.get(wikipedia_url, headers=headers, verify=False)

# Save the response of the server as text
wikipedia_result = wikipedia_research.text

#analyze the HTML text and build an object with the structure of the HTML text
wipedia_object = BeautifulSoup(wikipedia_result, 'html.parser')


# Find information about the year of the first automated process

# Make a research filtering for the strings "primero" and "año"
first_aut = r'\b\w*primero\w*\b.*?\baño\b.*?\b(\d{3,4})\b'
found_year = re.findall(first_aut, wikipedia_result, re.IGNORECASE)

# Verify the first year of automatization process 

for year in found_year:
    # Find a match of the first_aut expression in the text of the wikipedia page
    match = re.search(first_aut, wikipedia_result, re.IGNORECASE)
    
    if match:
        #If there is a match, assign the value of the amtching group found to variable found_sentence
        found_sentence = match.group(0)
        break
 
# Take the screenshot of the page with the information about the year of the first automated process

if found_sentence:
	# Add the driver executable path to the PATH environment variable	
    os.environ['PATH'] += os.pathsep + webdriver_path
    
    # Create an instance of Chrome WebDriver
    driver = webdriver.Chrome()
    
    # Instructs the webdriver to navigate to the wikipedia_url 
    driver.get(wikipedia_url)
    
    # Scroll to the element containing the information about the year (found_sentence)
    sentence = driver.find_element_by_xpath(f"//*[contains(text(), '{found_sentence}')]")  
    driver.execute_script("arguments[0].scrollIntoView();", sentence)
    
    # Take a screenshot of the page with the information about the year of the first automatization process
    driver.save_screenshot(output_path+"/screenshot.png")
    
    print("Screenshot guardado")
    # Close the driver
    driver.quit()
    
else:
    print("Información no encontrada")
