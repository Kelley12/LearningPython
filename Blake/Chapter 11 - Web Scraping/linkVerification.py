#! python3
# linkVerification.py - given the URL of a web page, will attempt to download
# every linked page on the page. The program should flag any pages
# that have a 404 “Not Found” status code and print them out as broken links.

import requests, bs4

res = requests.get(sys.argv[1:])
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

brokenLinks = []

# Find all links on page
linkElems = soup.select('a')
for link in linkElems:
    try:
        linkRes = requests.get(link.get('href'))
        linkRes.raise_for_status()
    except Exception as exc:
        brokenLinks = brokenLinks + [link]

if len(brokenLinks) < 1:
    print("All links successful")
else:
    print("Broken Links:")
    for brokenLink in brokenLinks:
        print(brokenLink)
