import requests
import os
print("Website Template downloader, made by Elderny")
ask = input("Please Type the name of the Website you want to hack, like get data of: ")
website = requests.get(ask)
data = website.text

with open("website_template.html", "w") as f:
    f.write(data)

location = os.getcwd()
print("Done, downloading. Location of download is:- ", location)