import requests

def get_reddit_story():
    print("Kapcsolódás a Reddithez...")
    
    # Sokkal "emberibb" fejléc, ami egy valódi Chrome böngészőt szimulál Mac-en
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    url = 'https://www.reddit.com/r/askhungary/top.json?limit=1&t=day'
    
    try:
        response = requests.get(url, headers=headers)
        
        # Megnézzük, hogy a szerver zöld utat adott-e (200-as kód a siker)
        if response.status_code != 200:
            return f"A Reddit blokkolta a kérést. Állapotkód: {response.status_code}"
            
        data = response.json()
        
        # Az adatok kibányászása
        post = data['data']['children'][0]['data']
        title = post['title']
        text = post.get('selftext', '')
        
        full_story = f"A mai legolvasottabb kérdés a Redditen. {title}. {text}"
        
        return full_story
        
    except Exception as e:
        return f"Rendszerhiba történt: {e}"

if __name__ == "__main__":
    napi_sztori = get_reddit_story()
    print("\nEzt találta a script:")
    print("-" * 40)
    print(napi_sztori)
    