import whois, time, random, os, csv, datetime
from pytrends.request import TrendReq

# 1024D KEYWORDS (same brain as before)
keywords = [
    "ai","gpt","claude","grok","deep","quantum","neuron","robot","drone","defi","nft","dao","vr","ar","xr",
    "tokyo","berlin","dubai","austin","lisbon","miami","seoul","taipei","mexico","london","toronto",
    "green","eco","carbon","solar","hydro","wind","fusion","efuel","hydrogen","tesla","lucid",
    "trump","kamala","rfk","vance","2028","vote","maga","debate","rally","senate",
    "alexa","siri","google","hey","ok","voice","talk","shout","ask","listen","speak"
]
tlds = ["ai","io","com","co","gg","vc","sh","to","fm","kg","green","eco","app","dev","xyz"]

def generate():
    domains = set()
    while len(domains) < 5000:
        a = random.choice(keywords); b = random.choice(keywords)
        name = f"{a}{b}"
        if 6 <= len(name) <= 18:
            for t in tlds:
                domains.add(f"{name}.{t}")
    return list(domains)

def is_available(d):
    try: return whois.whois(d).creation_date is None
    except: return True

domains = generate()
checked = 0
os.makedirs("Winners", exist_ok=True)

print("NUCLEAR SNIPER 24/7 ACTIVATED")

while True:
    checked += 1
    d = domains[checked % len(domains)]
    if is_available(d):
        row = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), d, "AVAILABLE"]
        with open(f"Winners/winners_{datetime.date.today()}.csv", "a", newline="") as f:
            csv.writer(f).writerow(row)
        print(f"WINNER → {d}")
    time.sleep(2.5 + random.uniform(0, 1))
