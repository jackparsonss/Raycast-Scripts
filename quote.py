#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Quote
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📜
# @raycast.packageName Inspiration

# Documentation:
# @raycast.description Generates a random quote
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import requests

res = requests.get("https://api.themotivate365.com/stoic-quote")

quote = res.json()["data"]

print('"' + str(quote["quote"]) + '"')

author = quote["author"]

if author == "":
    author = "Unkown"

print("\n\t-" + str(author))
