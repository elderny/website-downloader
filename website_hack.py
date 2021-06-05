import requests
import os
print("Website Template downloader, made by Elderny")
ask = input("Please Type or paste the url of the Website you want to get template of: ")
website = requests.get(ask)
data = website.text

with open("website_template.html", "w") as f:
    f.write(data)

location = os.getcwd()
print("Done, downloading. Location of download is:- ", location)
