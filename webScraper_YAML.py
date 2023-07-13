# Importing modules request and bs4 to scrap the info from the web
from requests import get
from bs4 import BeautifulSoup as Bs
#importing yaml and re modules to be able to
import yaml
import re

#navigate to the web page to do the scrap
response = get("https://www.w3schools.io/file/yaml-sample-example/")

# using the Beautiful Soup to map the content from the HTML
tags = Bs(response.text, "html5lib") #The HTML content is passed to BeautifulSoup object for parsing.

#find the tag Code and the class language-Yaml
yaml_example = tags.find_all("code", attrs={"language-Yaml"})

comments = [code.text for code in yaml_example]
# The commented line comments = [code.text for code in yaml_example] suggests an alternative approach where the special
# characters and newline characters are not removed. However, it is recommended to use the line with re.sub() and
# replace() as it provides a cleaner output without unwanted characters.

# acces the code part to get the text from it without the special characters
comments2 = [re.sub(r'[^\w\s]+', '',code.text).replace('\n','') for code in yaml_example]

#yaml has a dict type so lets convert the comments into a dict
data = {'comments' : comments2}

#dumping the content of data into a yaml file
with open ('output.yaml', 'w') as file:
    yaml.dump(data, file)




