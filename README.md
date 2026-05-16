# Thunderbird O365look Addon & Theme

This repository provides an Outlook/Office 365 inspired UI customization setup for Mozilla Thunderbird (Supernova 115+). 

It utilizes a pure CSS Theme file (`o365Chrome.css`) to style the UI, and a safe Add-on (`O365-Addon.xpi`) to inject functional buttons into the message list.

## Features

- **Outlook-Inspired Cards View:** Removes heavy rounded borders from the message list cards, substituting them with clean, flat lines and a thin white separator.
- **Enhanced Unread Visibility:** Unread messages are styled with bright blue text and a left-aligned vertical blue bar (similar to modern Outlook), removing the default green dot.
- **Dark Warning Banners:** Replaces the native bright yellow "Remote Content Blocked" banner with a dark grey (`#121212`) background and a muted blue preferences button (`#2b4c6e`), blending seamlessly into the dark system theme.
- **Quick Card Delete:** Automatically injects Thunderbird's native SVG trash icon onto every message card, placed perfectly adjacent to the Star icon. This enables quick one-click deletions without opening the email.

## Installation Instructions

We use a safe `@import` strategy to ensure we **never** overwrite your existing Thunderbird customizations!

### Step 1: Install the O365look Theme (CSS)
1. In Thunderbird, go to **Settings > General** and scroll to the bottom. Click **Config Editor...**
2. Search for `toolkit.legacyUserProfileCustomizations.stylesheets` and set it to **true**.
3. Go to **Help > Troubleshooting Information**.
4. Under "Application Basics", find **Profile Folder** and click **Open Folder**.
5. Open the `chrome` directory (create it if it does not exist).
6. Copy `userChrome.css` from this repository and place it in the folder. Rename it to `o365Chrome.css`.
7. If you already have a `userChrome.css` file, open it and paste this line at the absolute top:
`@import url("o365Chrome.css");`
*(If you do not have a `userChrome.css` file, simply create one and paste that exact same line into it!)*

### Step 2: Install the Quick Delete Add-on
1. In Thunderbird, navigate to **Settings > Add-ons and Themes**.
2. Click the Gear icon ⚙️ in the top right corner and select **Install Add-on From File...**
3. Select the `O365-Addon.xpi` file provided in this repository.
4. Click **Add** and restart Thunderbird to apply all changes.

## Credits, License & Disclaimer
* The CSS theme is a custom compilation inspired by modern design principles.
* **Massive credit** to the open-source developers **abtecgh** and **sim32101** for the original `cards-delete-btn` extension, which provided the foundational JavaScript injection logic to get a button onto the cards view!
* *Technical Disclaimer: This add-on relies on experimental APIs and may require updates if Thunderbird makes major internal structural changes in the future.*

### Legal Disclaimer & Trademark Notice
This is an independent, community-driven open-source project. **This add-on is NOT official, NOT endorsed by, and NOT connected in any way to Microsoft Corporation.** 

"Outlook" and "Office 365" are registered trademarks of Microsoft Corporation. This project only seeks to provide a visual layout option for Mozilla Thunderbird users who prefer a similar aesthetic.

### License
This project is licensed under the MIT License - see the `LICENSE` file for details.
