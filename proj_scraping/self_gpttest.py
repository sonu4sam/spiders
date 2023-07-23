# extract the title of the webpage. need to write a Python function that uses Beautiful Soup to parse the HTML and extract the required information. The function should take the HTML as a string as its input and return the extracted information. 

from bs4 import BeautifulSoup


def extract_title(html):
    soup = BeautifulSoup(html, 'lxml')
    tille = soup.title.string
    return tille

def extract_meta_description(html):
    soup = BeautifulSoup(html, 'lxml')
    meta_description = soup.find('meta', {'name': 'description'})
    return meta_description['content'] if meta_description else None

def extract_author(html):
    soup = BeautifulSoup(html, 'lxml')
    author_name = soup.find('meta', {'name': 'author'})
    return author_name['content'] if author_name else None

# Extract the text of all paragraphs in the "Document and Website Structure" section.

def extract_document_structure(html):
    soup = BeautifulSoup(html, 'lxml')
    document_structure_text = soup.find('h2')
    paragraphs = []
    if document_structure_text.name == 'p':
        paragraphs.append(document_structure_text)
        
    return paragraphs


def extract_navigation_items(html):
    soup = BeautifulSoup(html, 'lxml')
    nav_items = soup.find_all('a', href=True)
    return [item.text for item in nav_items]
        

        
if __name__ == '__main__':
    with open('proj_scraping\example.html') as file:
        html_file = file.read() # is being read once and store into the variable. 
        
        print(f"The title of the page is: {extract_title(html_file)}")
        print(f"The meta description of the page is: {extract_meta_description(html_file)}")
        print(f"The author of the page is : {extract_author(html_file)}")
        print(f"The navigation items are: {extract_navigation_items(html_file)}")
        print(f"The documents struct are: {extract_document_structure(html_file)}")

        
        



    