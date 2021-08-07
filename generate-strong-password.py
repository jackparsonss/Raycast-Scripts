#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Generate Strong Password
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔑
# @raycast.packageName Utilities

# Documentation:
# @raycast.description Generates a strong password
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss

import string, pyperclip, random, sys

try:
    # Retrieve length of desired password
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except:
            print("Please enter a length or leave blank for default length")
    else:
        length = 20

    # Generate password
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    options = letters + numbers + symbols

    if length > len(options):
        raise ValueError("Please give a shorter length")

    password_chars = random.sample(options, length)
    password = "".join(password_chars)

    # Copy password to clipboard
    pyperclip.copy(password)
    print("New Password Copied To Clipboard!")

except Exception as e:
    print(e)
