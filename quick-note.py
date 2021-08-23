#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Quick Note
# @raycast.mode compact

# Optional parameters:
# @raycast.icon images/obsidian-logo.png
# @raycast.packageName Obsidian
# @raycast.argument1 { "type": "text", "placeholder": "Note", "optional": false, "percentEncoded": true}

# Documentation:
# @raycast.description Appends the text I give it to my daily note on obsidian
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import sys

path = "/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/📥 Inbox/Quick Notes.md"
with open(path, "a") as note:
    note.write("\n- " + sys.argv[1])

print("Note added to Quick Notes.md")
