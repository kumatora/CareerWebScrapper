import requests
from bs4 import BeautifulSoup


def parseRequirements(url, keywordSet):

    r = requests.get("http://www.indeed.ca" + str(url))
    soup = BeautifulSoup(r.content, "html.parser")

    for text in soup.find_all("ul"):
        for items in text.find_all("li"):
            if keywordSet.lower() in items.text.lower() and url is not None and soup.title is not None :
                print(soup.title.string)
                print(items.text)
                print("http://www.indeed.ca" + url)
                print("-------------------------------------------------------------------")


keywordSet = str(input("Enter a keyword: "))
jobName = str(input("Enter a job title: "))
regionSearch = str(input("Enter the region (ex: Kitchener, ON must be formatted as City,Province: "))

jobName.replace(" ","+")
regionSearch.replace(",","%C+")
r = requests.get("http://www.indeed.ca/jobs?q=" + jobName + "&l=" + regionSearch)
print("-------------------------------------------------------------------")
soup = BeautifulSoup(r.content, "html.parser")
stra = 'a'

for link in soup.find_all("a", {"class" : "turnstileLink"}):
    stra = link.get("href")
    parseRequirements(stra, keywordSet)


