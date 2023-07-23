from urllib.parse import urljoin, urlparse
import requests
import re


def download_page(url):
    try:
        return requests.get(url).text
    except:
        print(f"error in the url, {url}")
    
def extract_link(page):
    if not page:
        return []
    
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return [urljoin(page, link) for link in link_regex.findall(page)]

def get_links(page_url):
    host = urlparse(page_url)[1]
    page = download_page(page_url)
    links = extract_link(page)
    
    return [link for link in links if urlparse(link)[1] == host]

def depth_fist_search(start_url):
    from collections import deque
    visited = set()
    queue = deque()
    queue.append(start_url)
    while queue:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        for link in get_links(url):
            queue.appendleft(link)
        print(url)
        
def breadth_first_search(start_url):
    from collections import deque
    
    visited = set()
    queue = deque()
    queue.append(start_url)
    while queue:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        queue.extend(get_links(url))
        print(url)
        
if __name__ == '__main__':
    
    url = "https://www.sainsburys.co.uk/gol-ui/groceries/meat-and-fish/c:1020388"
    
    depth_fist_search(url)
    
    
    

