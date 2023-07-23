# demonstration of urlparse function for web scraping. 

from urllib.parse import urlparse

url = "https://www.sainsburys.co.uk/gol-ui/groceries/meat-and-fish/meat-and-fish-essentials/c:1020377"

parsed_url = urlparse(url)

print(f"The scheme is: {parsed_url.scheme}")
print(f"The netloc is: {parsed_url.netloc}")
print(f"The urlpath is: {parsed_url.path}")
print(f"The params are: {parsed_url.params}")
print(f"The query is: {parsed_url.query}")
print(f"The fragement is: {parsed_url.fragment}")

