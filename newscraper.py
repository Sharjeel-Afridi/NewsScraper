from requests_html import HTMLSession


session = HTMLSession()
url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"


r = session.get(url)

r.html.render(timeout=20, scrolldown=0)

articles = r.html.find("article")

def scrap():
    newsitem = item.find('h4', first=True)
    title = newsitem.text
    link = item.find('a', first=True).attrs.get('href', None)
    realLink = "https://news.google.com" + link[1:]
    print(title, realLink)

count = 0
for item in articles:
    count += 1
    if count == 2 or count == 3 or count == 4:
        pass
    elif count == 5:
        count = 1
        scrap()
    else:
        scrap()