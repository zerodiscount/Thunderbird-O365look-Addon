# Thunderbird O365look Addon

This repository provides an Outlook/Office 365 inspired UI customization setup for Mozilla Thunderbird (Supernova 115+). 

It utilizes a powerful, recursive WebExtension (`O365-Addon.xpi`) to dynamically inject Outlook styling and new functional buttons directly into Thunderbird's interface, requiring **zero manual file configuration**.

## Features

- **True 1-Click Install:** No messing with `userChrome.css` files or hidden profile directories. The entire CSS theme is seamlessly injected directly into Thunderbird's DOM memory at runtime!
- **Outlook-Inspired Cards View:** Removes heavy rounded borders from the message list cards, substituting them with clean, flat lines and a thin white separator.
- **Enhanced Unread Visibility:** Unread messages are styled with bright blue text and a left-aligned vertical blue bar (similar to modern Outlook), removing the default green dot.
- **Dark Warning Banners:** Replaces the native bright yellow "Remote Content Blocked" banner with a dark grey (`#121212`) background and a muted blue preferences button (`#2b4c6e`), blending seamlessly into the dark system theme.
- **Quick Delete Button:** Injects a sleek, thin-stroke SVG trash icon onto every message card, perfectly aligned with the Star icon, enabling one-click deletions.
- **Quick Junk Button:** Injects an elegant flame icon next to the trash. This triggers Thunderbird's native junk filter, training the spam engine and moving the message to your Spam folder instantly.

## Installation Instructions

1. Download the `O365-Addon.xpi` file from this repository.
2. In Thunderbird, navigate to **Settings > Add-ons and Themes**.
3. Click the Gear icon ⚙️ in the top right corner and select **Install Add-on From File...**
4. Select the `O365-Addon.xpi` file.
5. Click **Add** and restart Thunderbird to apply the theme!

### 💡 Crucial Setup for the Junk Button
To ensure the Junk button actually sweeps messages out of your inbox, you must enable Thunderbird's native auto-move feature:
1. In Thunderbird, go to **Settings > Account Settings**.
2. Click on **Junk Settings** under your email account.
3. Check the box that says **"Move new junk messages to: Junk folder"**.

## Credits, License & Disclaimer
* The CSS theme is a custom compilation inspired by modern design principles.
* **Massive credit** to the open-source developers **abtecgh** and **sim32101** for the original `cards-delete-btn` extension, which provided the foundational JavaScript injection logic for the cards view.
* *Technical Disclaimer: This add-on relies on experimental APIs and deep recursive DOM traversal. It may require updates if Thunderbird makes major internal structural changes in the future.*

### Legal Disclaimer & Trademark Notice
This is an independent, community-driven open-source project. **This add-on is NOT official, NOT endorsed by, and NOT connected in any way to Microsoft Corporation.** 

"Outlook" and "Office 365" are registered trademarks of Microsoft Corporation. This project only seeks to provide a visual layout option for Mozilla Thunderbird users who prefer a similar aesthetic.

### License
This project is licensed under the MIT License - see the `LICENSE` file for details.
