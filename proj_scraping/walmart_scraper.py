from urllib import robotparser
import ssl
import urllib.request

context = ssl._create_unverified_context()
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
urllib.request.install_opener(opener)

robot_parser = robotparser.RobotFileParser()

def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)
    robot_parser.read()
    
def print_rules():
    
    for entry in robot_parser.entries:
        print(f"User-agent: {entry.useragent}")
        for rule in entry.rulelines:
            print(f"{'Allow' if rule.allowance else 'Disallow'}: {rule.path}")
            
if __name__ == '__main__':
    prepare("https://www.walmart.com/robots.txt")
    print_rules()
    
    