from requests_html import HTMLSession


session = HTMLSession()
url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"


r = session.get(url)

r.html.render(timeout=20, scrolldown=0)

articles = r.html.find("article")

count = 0
for item in articles:
    count += 1
    if count == 2 or count == 3 or count == 4:
        pass
    elif count == 5:
        count = 1
        newsitem = item.find('h4', first=True)
        title = newsitem.text
        
        print(title)
    else:
        newsitem = item.find('h4', first=True)
        title = newsitem.text
        print(title)