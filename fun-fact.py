#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title fun-fact
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description A random fun fact
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import requests

res = requests.get("https://uselessfacts.jsph.pl/random.json")

print(res.json()['text'])


