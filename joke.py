#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Joke
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🃏

# Documentation:
# @raycast.description A random joke
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import requests

res = requests.get("https://v2.jokeapi.dev/joke/Any")

print(res.json()['setup'])
print('\n---\n')
print(res.json()['delivery'])


