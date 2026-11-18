<div align="center">
           ███████╗██╗     ██╗     ██╗ ██████╗ ████████╗
            ██╔════╝██║     ██║     ██║██╔═══██╗╚══██╔══╝
            █████╗  ██║     ██║     ██║██║   ██║   ██║
            ██╔══╝  ██║     ██║     ██║██║   ██║   ██║
            ███████╗███████╗███████╗██║╚██████╔╝   ██║
            ╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝    ╚═╝
               H I D D E N   U R L   F I N D E R
                     E L L I O T  |  v1.0
                     A U T H O R :  N U R



# 🕵️ Hidden URL Finder

**Discover hidden directories, files and unlinked URLs on a website.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-black?style=flat-square&logo=linux)](https://kali.org)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

> ⚠️ **LEGAL NOTICE**  
> This tool is for **authorized penetration testing**, **bug bounty recon**,  
> and **educational use only**. Unauthorized scanning is **illegal**.  
> You are solely responsible for how you use it.

</div>

---

## 🎯 Features

| Feature | Description |
|---|---|
| 🕷️ **Recursive Crawler** | Extracts links from `<a>`, `<script>`, `<img>`, `<form>` tags |
| 🤖 **robots.txt Parser** | Auto-discovers `Disallow`/`Allow` paths |
| 🗺️ **Sitemap Detection** | Flags `sitemap.xml` presence |
| 📖 **Dictionary Brute-Force** | 100+ common hidden paths preloaded |
| 🎨 **Matrix CLI Output** | Colorized, timestamped, hacker-styled terminal |
| 📊 **JSON Export** | `--json out.json` for automated pipelines |
| 🕵️ **Stealth Mode** | Realistic browser headers + rate-limiting |
| 🎯 **Smart Status Handling** | `403 Forbidden` counts as a valid discovery |

---

## 🚀 Quick Start (Kali Linux)

```bash
# 1. Clone
git clone https://github.com/mr-elliot-dev/hidden-url-finder
cd hidden-url-finder

# 2. Setup venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run
python hidden_url_finder.py -u https://example.com

##💻 Usage
# Basic scan
python hidden_url_finder.py -u https://example.com

# Custom wordlist + JSON output
python hidden_url_finder.py -u https://example.com \
    -w /usr/share/wordlists/dirb/common.txt \
    -o results.json

# Stealth mode (slower, safer)
python hidden_url_finder.py -u https://example.com -d 1.0

# Deep crawl
python hidden_url_finder.py -u https://example.com --depth 3

##📸 Sample Output
[14:22:01] [*] Phase 1/3 → Scanning robots.txt & sitemap.xml
[14:22:01] [+] Found robots.txt
[14:22:01] [★] robots.txt → https://example.com/admin/
[14:22:02] [*] Phase 2/3 → Brute-forcing 100 paths
[14:22:03] [  OPEN   ] https://example.com/.env
[14:22:04] [FORBIDDEN] https://example.com/backup.zip
[14:22:05] [★] Link → https://example.com/api/v1/users
[14:22:06] [*] Phase 3/3 → Crawling site structure

═══════════════════════════════════════════════════════
  🎯 SCAN COMPLETE
═══════════════════════════════════════════════════════
  Target  : https://example.com
  Found   : 17 URLs
  Time    : 4.82s
═══════════════════════════════════════════════════════

  ⚡ DISCOVERED URLs
  → https://example.com/.env
  → https://example.com/admin/
  → https://example.com/api/v1/users
  → https://example.com/backup.zip
##🧠 How It Works
┌──────────────────┐
│   Target URL     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────┐
│ robots.txt probe │─────▶│ Pull disallow│
└────────┬─────────┘      └──────────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────┐
│ Brute-force      │─────▶│  HEAD/GET    │
│ 100+ paths       │      │  200/403=HIT │
└────────┬─────────┘      └──────────────┘
         │
         ▼
┌──────────────────┐      ┌──────────────┐
│ HTML Crawler     │─────▶│ Parse tags   │
│ (depth-limited)  │      │ <a> <form>…  │
└────────┬─────────┘      └──────────────┘
         │
         ▼
┌──────────────────┐
│ Unique Results   │
│ + JSON export    │
└──────────────────┘

