# Thunderbird Outlook Theme & Unified Customizations

This repository provides a unified UI customization extension for Mozilla Thunderbird (Supernova 115+) to create a cleaner, flatter interface inspired by modern Outlook / Office 365. 

It completely overhauls the message list "Cards View" and the remote content warning banner. This is packaged as a single, easy-to-install `.xpi` extension.

## Features

- **Outlook-Inspired Cards View:** Removes heavy rounded borders from the message list cards, substituting them with clean, flat lines and a thin white separator.
- **Enhanced Unread Visibility:** Unread messages are styled with bright blue text and a left-aligned vertical blue bar (similar to modern Outlook), removing the default green dot.
- **Dark Warning Banners:** Replaces the native bright yellow "Remote Content Blocked" banner with a dark grey (`#121212`) background and a muted blue preferences button (`#2b4c6e`), blending seamlessly into the dark system theme.
- **Muted Folder Icons:** Desaturates the default bright yellow folder icons in the left pane to match a neutral, professional aesthetic.
- **Quick Card Delete:** Automatically injects Thunderbird's native SVG trash icon onto every message card, placed perfectly adjacent to the Star icon. This enables quick one-click deletions without opening the email.

## Installation Instructions

1. In Thunderbird, navigate to **Settings > Add-ons and Themes**.
2. Click the Gear icon ⚙️ in the top right corner and select **Install Add-on From File...**
3. Select the `thunderbird-outlook-theme.xpi` file provided in this repository.
4. Click **Add** and restart Thunderbird if prompted.

*Note: You no longer need to use `userChrome.css` for these features. Everything is bundled into the single `.xpi` extension.*

## Credits & Disclaimer
* The CSS theme is a custom compilation inspired by modern Outlook 365 design principles.
* The delete button injection logic is based on the open-source community add-on `cards-delete-btn` (originally created by abtecgh/sim32101).
