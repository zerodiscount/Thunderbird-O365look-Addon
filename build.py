import os
import zipfile
import json

# Read the CSS from the backup file
with open("src/css/o365-theme.css", "r") as f:
    css_content = f.read()

# Escape backticks and dollar signs if any
css_content = css_content.replace('`', '\\`').replace('$', '\\$')

# Write Manifest 1.2.2
with open("src/manifest.json", "r") as f:
    manifest = json.load(f)

manifest["version"] = "1.2.2"

with open("src/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

parent_js_content = f"""\
"use strict";

var {{ ExtensionCommon }} = ChromeUtils.importESModule("resource://gre/modules/ExtensionCommon.sys.mjs");

this.cardsDelete = class extends ExtensionCommon.ExtensionAPI {{
  getAPI(context) {{

    const USER_CHROME_CSS = `{css_content}`;

    const CARDS_CSS = `
      .cards-delete-btn {{
        position: absolute;
        right: 32px;
        bottom: 9px;
        width: 16px;
        height: 16px;
        display: inline-flex;
        background-color: transparent;
        border: none;
        cursor: pointer;
        color: #888;
        opacity: 0.6;
        z-index: 100;
        padding: 0;
        align-items: center;
        justify-content: center;
      }}
      .cards-delete-btn svg {{
        width: 100%;
        height: 100%;
      }}
      .cards-delete-btn:hover {{
        opacity: 1;
        color: #cc3333;
      }}

      .cards-junk-btn {{
        position: absolute;
        right: 52px;
        bottom: 9px;
        width: 16px;
        height: 16px;
        display: inline-flex;
        background-color: transparent;
        border: none;
        cursor: pointer;
        color: #888;
        opacity: 0.6;
        z-index: 100;
        padding: 0;
        align-items: center;
        justify-content: center;
      }}
      .cards-junk-btn svg {{
        width: 100%;
        height: 100%;
      }}
      .cards-junk-btn:hover {{
        opacity: 1;
        color: #ff8c00; /* Bright orange flame */
      }}
    `;

    function deleteMessage(row, innerWin) {{
      const rowIndex = typeof row.index === "number" ? row.index : -1;
      if (rowIndex < 0) return;
      const view = innerWin.gDBView;
      if (!view) return;
      const msgHdr = view.getMsgHdrAt(rowIndex);
      if (!msgHdr) return;
      const topWin = innerWin.browsingContext?.top?.window ?? innerWin;
      const msgWindow = topWin.msgWindow ?? null;
      msgHdr.folder.deleteMessages([msgHdr], msgWindow, false, false, null, true);
    }}

    function markAsJunk(row, innerWin) {{
      try {{
        const rowIndex = typeof row.index === "number" ? row.index : -1;
        if (rowIndex < 0) return;
        const view = innerWin.gDBView;
        if (!view) return;
        
        // Select the specific message row first
        view.selection.select(rowIndex);
        
        // Trigger Thunderbird's native Junk command to properly train the spam filter
        if (typeof innerWin.MsgJunk === "function") {{
            innerWin.MsgJunk();
        }} else if (typeof innerWin.goDoCommand === "function") {{
            innerWin.goDoCommand("cmd_markAsJunk");
        }}
      }} catch (e) {{
          console.error("O365-Addon: Critical failure in markAsJunk", e);
      }}
    }}

    function attachButton(row, innerWin) {{
      if (row._cardsDeleteAttached) return;
      row._cardsDeleteAttached = true;
      const container = row.querySelector(".card-container") ?? row;
      if (innerWin.getComputedStyle(container).position === "static") {{
        container.style.position = "relative";
      }}
      
      const delBtn = innerWin.document.createElement("button");
      delBtn.className = "cards-delete-btn";
      delBtn.title = "Delete Message";
      delBtn.setAttribute("aria-label", "Delete Message");
      delBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/><path d="M10 11v6"/><path d="M14 11v6"/></svg>`;
      delBtn.addEventListener("click", (event) => {{
        event.stopPropagation();
        event.preventDefault();
        deleteMessage(row, innerWin);
      }}, true);
      container.appendChild(delBtn);

      const junkBtn = innerWin.document.createElement("button");
      junkBtn.className = "cards-junk-btn";
      junkBtn.title = "Move to Junk";
      junkBtn.setAttribute("aria-label", "Move to Junk");
      junkBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0011 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 11-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 002.5 2.5z"></path></svg>`;
      junkBtn.addEventListener("click", (event) => {{
        event.stopPropagation();
        event.preventDefault();
        markAsJunk(row, innerWin);
      }}, true);
      container.appendChild(junkBtn);
    }}

    function processCards(innerWin) {{
      innerWin.document
        .querySelectorAll("[is='thread-card']:not([data-cdb-done])")
        .forEach(row => {{
          row.setAttribute("data-cdb-done", "1");
          attachButton(row, innerWin);
        }});
    }}

    function safeInjectCSS(doc, id, cssText) {{
        try {{
          if (!doc.getElementById(id)) {{
            if (doc.head || doc.documentElement) {{
              const style = doc.createElement("style");
              style.id = id;
              style.textContent = cssText;
              (doc.head || doc.documentElement).appendChild(style);
            }}
          }}
        }} catch (err) {{
          console.error("O365-Addon: Failed to inject CSS " + id, err);
        }}
    }}

    function injectInto3Pane(innerWin) {{
      if (!innerWin || innerWin._cardsDeleteInjected) return;
      innerWin._cardsDeleteInjected = true;
      
      safeInjectCSS(innerWin.document, "cards-delete-btn-css", CARDS_CSS);
      
      processCards(innerWin);
      new innerWin.MutationObserver(() => processCards(innerWin))
        .observe(innerWin.document.documentElement, {{ childList: true, subtree: true }});
      let ticks = 0;
      const timer = innerWin.setInterval(() => {{
        processCards(innerWin);
        if (++ticks >= 100) innerWin.clearInterval(timer);
      }}, 600);
    }}

    function injectRecursively(currentDoc) {{
      if (!currentDoc) return;
      
      safeInjectCSS(currentDoc, "o365-global-theme-css", USER_CHROME_CSS);
      
      const href = currentDoc.location?.href || "";
      if (href.startsWith("about:3pane")) {{
          const innerWin = currentDoc.defaultView;
          if (innerWin) injectInto3Pane(innerWin);
      }}
      
      currentDoc.querySelectorAll("browser, iframe").forEach(frame => {{
        try {{
          const cw = frame.contentWindow;
          if (cw && cw.document) {{
              injectRecursively(cw.document);
          }}
        }} catch(e) {{}}
      }});
    }}

    function watchMailWindow(outerWin) {{
      if (!outerWin || outerWin._cardsDeleteWatching) return;
      outerWin._cardsDeleteWatching = true;
      const doc = outerWin.document;

      function tryInject() {{
        injectRecursively(doc);
      }}

      tryInject();
      new outerWin.MutationObserver(tryInject)
        .observe(doc.documentElement, {{ childList: true, subtree: true }});
      doc.getElementById("tabmail")
        ?.addEventListener("select", () => outerWin.setTimeout(tryInject, 300));
      let ticks = 0;
      const timer = outerWin.setInterval(() => {{
        tryInject();
        if (++ticks >= 30) outerWin.clearInterval(timer);
      }}, 500);
    }}

    return {{
      cardsDelete: {{
        async inject() {{
          const {{ ExtensionSupport }} = ChromeUtils.importESModule(
            "resource:///modules/ExtensionSupport.sys.mjs"
          );

          const openWindows = Services.wm.getEnumerator("mail:3pane");
          while (openWindows.hasMoreElements()) {{
            watchMailWindow(openWindows.getNext());
          }}
          
          const messageWindows = Services.wm.getEnumerator("mail:messageWindow");
          while (messageWindows.hasMoreElements()) {{
            watchMailWindow(messageWindows.getNext());
          }}

          ExtensionSupport.registerWindowListener("o365ThemeListener", {{
            onLoadWindow(win) {{
              const winType = win.document?.documentElement?.getAttribute("windowtype");
              if (winType === "mail:3pane" || winType === "mail:messageWindow") {{
                watchMailWindow(win);
              }}
            }},
          }});
          
          context.callOnClose({{
            close() {{
              ExtensionSupport.unregisterWindowListener("o365ThemeListener");
            }},
          }});
        }},
      }},
    }};
  }}
}};
"""

with open("src/api/parent.js", "w") as f:
    f.write(parent_js_content)

with zipfile.ZipFile("O365-Addon.xpi", "w") as zipf:
    for root, dirs, files in os.walk("src"):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, "src")
            zipf.write(file_path, arcname)

print("O365-Addon.xpi version 1.2.2 built successfully.")
