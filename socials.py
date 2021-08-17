#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Socials
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📱
# @raycast.packageName Utilities

# Documentation:
# @raycast.description Displays all my social media usernames and links
# @raycast.author Jack Parsons
# @raycast.authorURL https://github.com/jackparsonss


def display_social(company, profile_link, username=None):
    print("Social: " + company)
    print("Profile: " + profile_link)
    if username:
        print("Username: " + username)
    print("\n---\n")


display_social("🎨 Portfolio", "https://jackparsonss.github.io/")

display_social("✍️ Blog", "https://jackparsonss.hashnode.dev/")

display_social("🗣 Linkedin", "https://www.linkedin.com/in/jack-parsonss/")

display_social("😸 Github", "https://github.com/jackparsonss", "@jackparsonss")

display_social("🕊 Twitter", "https://twitter.com/jackparsonss", "@jackparsonss")
