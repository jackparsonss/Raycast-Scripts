import os
from datetime import datetime


def add_date(path, date):
    with open(f"{path}", "r+") as fp:
        lines = fp.readlines()
        lines.insert(0, f"Date: [[{date}]]\n")
        fp.seek(0)
        fp.writelines(lines)


def add_created_time(path):
    for file in os.listdir(path):
        if file == ".DS_Store":
            continue
        full_path = path + "/" + file

        created_at = os.stat(full_path).st_birthtime
        date = datetime.fromtimestamp(created_at).strftime("%Y-%m-%d")

        print(f"Adding [[{date}]] to {file}")
        add_date(full_path, date)


def main():
    path_notes = "/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/📝 Notes"
    path_inbox = "/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/📥 Inbox"
    add_created_time(path_notes)


if __name__ == "__main__":
    main()
