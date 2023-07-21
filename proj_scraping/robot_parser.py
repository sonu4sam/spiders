import requests

def parse_robots_txt(url):
    response = requests.get(url)
    lines = response.text.split('\n')
    
    for line in lines:
        if line.startswith('#'):
            continue
        parts = line.split(":")
        
        if len(parts) == 2 and parts[0].strip() == 'Allow':
            print(f"{parts[0].strip()}: {parts[1].strip()}")
            
if __name__ == '__main__':
    parse_robots_txt("https://www.walmart.com/robots.txt")