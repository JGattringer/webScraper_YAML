# Importing modules
from requests import get
from bs4 import BeautifulSoup as Bs
import yaml
import re

#navigate to the web page to do the scrap
response = get("https://www.w3schools.io/file/yaml-sample-example/")

# using the Beautiful Soup to map the content from the HTML
tags = Bs(response.text, "html5lib")

#find the tag Code and the class language-Yaml
yaml_example = tags.find_all("code", attrs={"language-Yaml"})

# acces the code part to get the text from it without the special characters
comments2 = [re.sub(r'[^\w\s]+', '',code.text).replace('\n','') for code in yaml_example]

#convert the comments into a dict
data = {'comments' : comments2}

#dumping the content of data into a yaml file
with open ('output.yaml', 'w') as file:
    yaml.dump(data, file)




