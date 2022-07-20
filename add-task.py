#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Add Task
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ✅
# @raycast.argument1 { "type": "text", "placeholder": "Task", "optional": false, "percentEncoded": true}

# Documentation:
# @raycast.description Add task to obsidian
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss
from datetime import date
import sys

task = " ".join(sys.argv[1].split("%20"))

with open(f"/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/Daily Notes/{date.today()}.md", 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('#### 🎯 Todays Tasks'):
            lines[i] = lines[i].strip() + f'\n- [ ] #task #daily {task} 📅 {date.today()} \n'
    f.seek(0)
    for line in lines:
        f.write(line)
print("Wrote Task!")
