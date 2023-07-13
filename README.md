# YAML Code Scraper

This script is designed to scrape YAML code snippets from a web page and store them in a YAML file. It utilizes the `requests` and `bs4` libraries to fetch and parse HTML content, and the `yaml` and `re` libraries for data processing.

## Installation

Before running the code, make sure you have the necessary libraries installed. You can install them using pip:
Check the requeriments to know what modules you will need to execute the code

## Usage

1. Import the required modules at the beginning of your Python script:

from requests import get
from bs4 import BeautifulSoup as Bs
import yaml
import re

2. Navigate to your desirable page
response = get("https://www.w3schools.io/file/yaml-sample-example/")

3. Parse the HTML content using Beautiful Soup:
tags = Bs(response.text, "html5lib")

4. Find the YAML code snippets in the HTML:
yaml_example = tags.find_all("code", attrs={"language-Yaml"})

5. Extract the comments from the code snippets:
comments = [re.sub(r'[^\w\s]+', '', code.text).replace('\n', '') for code in yaml_example]

6. Convert the comments into a dictionary:
data = {'comments': comments}

7. Dump the dictionary into a YAML file:
with open('output.yaml', 'w') as file:
    yaml.dump(data, file)
   
Make sure to customize the web page URL and the output file name according to your requirements.

Feel free to modify and use this code for your own purposes. Contributions and suggestions are always welcome!






