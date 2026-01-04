import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Strip out useless navigation and footer data
        for element in soup(["script", "style", "nav", "footer", "aside"]):
            element.decompose()
            
        return soup.get_text(separator=' ')[:8000] 
    except:
        return ""