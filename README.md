 <div align="center">

```text
███████╗██╗     ██╗     ██╗ ██████╗ ████████╗
██╔════╝██║     ██║     ██║██╔═══██╗╚══██╔══╝
█████╗  ██║     ██║     ██║██║   ██║   ██║
██╔══╝  ██║     ██║     ██║██║   ██║   ██║
███████╗███████╗███████╗██║╚██████╔╝   ██║
╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝    ╚═╝

       H I D D E N   U R L   F I N D E R
             E L L I O T  |  v1.0
             A U T H O R :  N U R
```

# 🕵️ Hidden URL Finder

**Discover hidden directories, files, and unlinked URLs on a website.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-black?style=flat-square&logo=linux)](https://www.kali.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

---

> ⚠️ **LEGAL NOTICE**
>
> This tool is intended for authorized penetration testing, bug bounty reconnaissance, and educational purposes only. Unauthorized scanning may violate applicable laws. You are responsible for ensuring you have permission to test the target.

## 🎯 Features

| Feature | Description |
|---|---|
| 🕷️ **Recursive Crawler** | Extracts links from `<a>`, `<script>`, `<img>`, and `<form>` tags |
| 🤖 **robots.txt Parser** | Discovers paths listed in `Disallow` and `Allow` directives |
| 🗺️ **Sitemap Detection** | Checks for `sitemap.xml` |
| 📖 **Dictionary-Based Discovery** | Includes 100+ common paths |
| 🎨 **Matrix CLI Output** | Colorized, timestamped terminal output |
| 📊 **JSON Export** | Exports results using `--json` |
| 🛡️ **Rate Limiting** | Supports request delays and browser-style headers |
| 🎯 **Smart Status Handling** | Identifies HTTP 200 and 403 responses |

## 🚀 Quick Start (Kali Linux)

### 1. Clone the Repository

```bash
git clone https://github.com/mr-elliot-dev/hidden-url-finder.git
```

### 2. Navigate to the Project

```bash
cd hidden-url-finder
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 5. Install Requirements

```bash
pip install -r requirements.txt
```

### 6. Run the Tool

```bash
python3 hidden_url_finder.py -u https://example.com
```

## 💻 Usage

### Basic Scan

```bash
python3 hidden_url_finder.py -u https://example.com
```

### Custom Wordlist and JSON Output

```bash
python3 hidden_url_finder.py -u https://example.com \
    -w /usr/share/wordlists/dirb/common.txt \
    -o results.json
```

### Rate-Limited Scan

```bash
python3 hidden_url_finder.py -u https://example.com -d 1.0
```

### Deep Crawl

```bash
python3 hidden_url_finder.py -u https://example.com --depth 3
```

*Only scan websites you own or have explicit permission to test.*

## 📸 Sample Output

```text
[14:22:01] [*] Phase 1/3 → Scanning robots.txt & sitemap.xml
[14:22:01] [+] Found robots.txt
[14:22:01] [★] robots.txt → https://example.com/admin/

[14:22:02] [*] Phase 2/3 → Checking common paths
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
```

*Example output for documentation; actual results will vary.*

## 🧠 How It Works

```text
          ┌──────────────────┐
          │   Target URL     │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ robots.txt probe │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Sitemap detection│
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Path discovery   │
          │ Wordlist-based   │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ HTML crawler     │
          │ Depth-limited    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Unique Results   │
          │ JSON Export      │
          └──────────────────┘
```

## 📂 Project Structure

```text
hidden-url-finder/
│
├── hidden_url_finder.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 🛠️ Requirements

- Python 3.8+
- Kali Linux / Linux
- Internet connection
- Required Python packages from `requirements.txt`

## ⚖️ Disclaimer

This project is developed for educational purposes and authorized security testing.

- Always obtain permission before scanning a website.
- Do not access or download sensitive information.
- Respect website policies and applicable laws.
- The author is not responsible for misuse of this tool.

## 👨‍💻 Author

**NUR**

Project: **ELLIOT – Hidden URL Finder**

Version: **1.0**

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

---

<div align="center">

**ELLIOT | Hidden URL Finder**

*Developed by NUR*

</div>
