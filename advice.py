#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Advice
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 💭
# @raycast.packageName Utilities

# Documentation:
# @raycast.description Generates a random piece of advice
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import requests

res = requests.get("https://api.adviceslip.com/advice")

print(res.json()["slip"]["advice"])
