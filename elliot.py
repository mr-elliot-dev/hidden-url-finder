#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
        ███████╗██╗     ██╗     ██╗ ██████╗ ████████╗
        ██╔════╝██║     ██║     ██║██╔═══██╗╚══██╔══╝
        █████╗  ██║     ██║     ██║██║   ██║   ██║
        ██╔══╝  ██║     ██║     ██║██║   ██║   ██║
        ███████╗███████╗███████╗██║╚██████╔╝   ██║
        ╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝    ╚═╝
           H I D D E N   U R L   F I N D E R
                    Elliot   |  v1.0

  Author : Light
  GitHub : https://github.com/YOUR_USERNAME/hidden_url_finder
  License: MIT

  ⚠  FOR AUTHORIZED SECURITY TESTING ONLY ⚠
"""

import argparse
import json
import os
import random
import sys
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] Missing dependencies. Run: pip install -r requirements.txt")
    sys.exit(1)

# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
class C:
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    MAGENTA= '\033[95m'
    BLUE   = '\033[94m'
    GRAY   = '\033[90m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

BANNER = f"""{C.GREEN}{C.BOLD}
            ███████╗██╗     ██╗     ██╗ ██████╗ ████████╗
            ██╔════╝██║     ██║     ██║██╔═══██╗╚══██╔══╝
            █████╗  ██║     ██║     ██║██║   ██║   ██║
            ██╔══╝  ██║     ██║     ██║██║   ██║   ██║
            ███████╗███████╗███████╗██║╚██████╔╝   ██║
            ╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝    ╚═╝
{C.CYAN}        H I D D E N   U R L   F I N D E R
{C.MAGENTA}                 E L L I O T  |  v1.0
{C.GRAY}  ─────────────────────────────────────────────
{C.YELLOW}   [⚠] FOR AUTHORIZED SECURITY TESTING ONLY
{C.GRAY}  ─────────────────────────────────────────────{C.RESET}
"""
# ─────────────────────────────────────────────────────────────
#  DEFAULT WORDLIST
# ─────────────────────────────────────────────────────────────
DEFAULT_WORDLIST = [
    # Admin panels
    "admin", "admin/", "administrator", "login", "wp-admin", "wp-login.php",
    "cpanel", "dashboard", "manager", "console",
    # Sensitive files
    ".env", ".env.backup", ".git/HEAD", ".git/config", ".htaccess",
    ".htpasswd", ".svn/entries", "config.php", "config.yml", "config.json",
    "settings.py", "wp-config.php", "database.yml",
    # Backups
    "backup", "backup.zip", "backup.tar.gz", "backup.sql", "db.sql",
    "database.sql", "dump.sql", "site.zip", "old.zip",
    # Logs & debug
    "debug.log", "error.log", "access.log", "phpinfo.php", "info.php",
    "test.php", "shell.php", "cmd.php",
    # Standard
    "robots.txt", "sitemap.xml", "sitemap_index.xml", "humans.txt",
    "security.txt", ".well-known/security.txt",
    # Directories
    "api", "api/v1", "api/v2", "uploads", "upload", "images", "img",
    "css", "js", "assets", "static", "files", "docs", "dev", "test",
    "staging", "private", "internal", "secret", "hidden", "tmp", "temp",
    # Common CMS
    "wp-content", "wp-includes", "wp-json/wp/v2/users",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# ─────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────
def ts():
    return f"{C.GRAY}[{datetime.now().strftime('%H:%M:%S')}]{C.RESET}"

def info(msg):    print(f"{ts()} {C.CYAN}[*]{C.RESET} {msg}")
def success(msg): print(f"{ts()} {C.GREEN}[+]{C.RESET} {msg}")
def warn(msg):    print(f"{ts()} {C.YELLOW}[!]{C.RESET} {msg}")
def error(msg):   print(f"{ts()} {C.RED}[-]{C.RESET} {msg}")
def hit(msg):     print(f"{ts()} {C.GREEN}{C.BOLD}[★]{C.RESET} {C.GREEN}{msg}{C.RESET}")

def fake_loading(text="Initializing", duration=1.2):
    """A short matrix-ish loading animation."""
    chars = "▁▂▃▄▅▆▇█"
    end = time.time() + duration
    while time.time() < end:
        bar = "".join(random.choice(chars) for _ in range(20))
        sys.stdout.write(f"\r{ts()} {C.CYAN}[*]{C.RESET} {text}... {C.GREEN}{bar}{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

# ─────────────────────────────────────────────────────────────
#  MAIN CLASS
# ─────────────────────────────────────────────────────────────
class HiddenURLFinder:
    def __init__(self, base_url, timeout=5, delay=0.2, max_depth=2):
        self.base_url = base_url.rstrip("/")
        self.domain = urlparse(base_url).netloc
        self.found_urls = set()
        self.visited_pages = set()
        self.results = []          # list of dicts for JSON export
        self.timeout = timeout
        self.delay = delay
        self.max_depth = max_depth
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    # ---------- utils ----------
    def _is_internal(self, url):
        parsed = urlparse(url)
        return parsed.netloc == self.domain or parsed.netloc == ""

    def _normalize(self, url):
        return urljoin(self.base_url, url).split("#")[0]

    def _record(self, url, status, source):
        if url in self.found_urls:
            return
        self.found_urls.add(url)
        self.results.append({
            "url": url,
            "status": status,
            "source": source,
            "timestamp": datetime.now().isoformat(),
        })

    # ---------- phases ----------
    def check_special_files(self):
        info("Phase 1/3 → Scanning robots.txt & sitemap.xml")
        for path in ("/robots.txt", "/sitemap.xml"):
            target = urljoin(self.base_url, path)
            try:
                r = self.session.get(target, timeout=self.timeout)
                if r.status_code == 200:
                    success(f"Found {path}")
                    self._record(target, 200, "special-file")
                    if path == "/robots.txt":
                        for line in r.text.splitlines():
                            low = line.lower()
                            if low.startswith(("disallow:", "allow:")):
                                p = line.split(":", 1)[1].strip()
                                if p and p != "/":
                                    full = self._normalize(p)
                                    hit(f"robots.txt → {full}")
                                    self._record(full, 200, "robots.txt")
            except requests.RequestException:
                pass
            time.sleep(self.delay)

    def brute_force(self, wordlist):
        info(f"Phase 2/3 → Brute-forcing {len(wordlist)} paths")
        for i, path in enumerate(wordlist, 1):
            target = urljoin(self.base_url + "/", path)
            try:
                r = self.session.head(target, timeout=self.timeout, allow_redirects=True)
                if r.status_code in (200, 301, 302, 403):
                    tag = {200: "OPEN", 301: "REDIRECT", 302: "REDIRECT", 403: "FORBIDDEN"}[r.status_code]
                    color = C.GREEN if r.status_code == 200 else C.YELLOW
                    print(f"{ts()} {color}[{tag:^9}]{C.RESET} {target}")
                    self._record(target, r.status_code, "brute-force")
            except requests.RequestException:
                pass
            if i % 25 == 0:
                print(f"{C.GRAY}    ... {i}/{len(wordlist)} checked{C.RESET}")
            time.sleep(self.delay)

    def crawl(self, url, depth=0):
        if depth > self.max_depth or url in self.visited_pages:
            return
        if not self._is_internal(url):
            return
        self.visited_pages.add(url)
        try:
            r = self.session.get(url, timeout=self.timeout)
            if r.status_code != 200:
                return
            if "text/html" not in r.headers.get("Content-Type", ""):
                return
            info(f"Crawling → {url}")
            soup = BeautifulSoup(r.text, "html.parser")
            for tag in soup.find_all(["a", "link", "script", "img", "form"]):
                attr = "href" if tag.name in ("a", "link") else "src"
                if tag.name == "form":
                    attr = "action"
                val = tag.get(attr)
                if not val:
                    continue
                full = self._normalize(val)
                if not self._is_internal(full):
                    continue
                if full not in self.found_urls:
                    hit(f"Link → {full}")
                    self._record(full, 200, "crawler")
                if full not in self.visited_pages and depth < self.max_depth:
                    time.sleep(self.delay)
                    self.crawl(full, depth + 1)
        except requests.RequestException:
            pass

    def run(self, wordlist=None):
        wordlist = wordlist or DEFAULT_WORDLIST
        start = time.time()

        self.check_special_files()
        fake_loading("Brute-forcing", 1.0)
        self.brute_force(wordlist)
        fake_loading("Crawling site", 1.0)
        info("Phase 3/3 → Crawling site structure")
        self.crawl(self.base_url)

        elapsed = time.time() - start
        self._print_summary(elapsed)
        return self.results

    def _print_summary(self, elapsed):
        print(f"\n{C.GRAY}{'═' * 55}{C.RESET}")
        print(f"{C.GREEN}{C.BOLD}  🎯 SCAN COMPLETE{C.RESET}")
        print(f"{C.GRAY}{'═' * 55}{C.RESET}")
        print(f"  {C.CYAN}Target  :{C.RESET} {self.base_url}")
        print(f"  {C.CYAN}Found   :{C.RESET} {C.GREEN}{C.BOLD}{len(self.found_urls)}{C.RESET} URLs")
        print(f"  {C.CYAN}Time    :{C.RESET} {elapsed:.2f}s")
        print(f"{C.GRAY}{'═' * 55}{C.RESET}\n")

        if not self.found_urls:
            warn("No hidden URLs discovered.")
            return

        print(f"{C.YELLOW}{C.BOLD}  ⚡ DISCOVERED URLs{C.RESET}")
        for url in sorted(self.found_urls):
            print(f"  {C.GREEN}→{C.RESET} {url}")
        print()

    def export_json(self, path):
        with open(path, "w") as f:
            json.dump({
                "target": self.base_url,
                "scan_time": datetime.now().isoformat(),
                "total_found": len(self.results),
                "results": self.results,
            }, f, indent=2)
        success(f"JSON exported → {path}")

# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(
        description="Hidden URL Finder — discover hidden dirs/files on a website.",
        epilog="Example: ellio.py -u https://example.com --json out.json"
    )
    p.add_argument("-u", "--url", required=True, help="Target URL (http/https)")
    p.add_argument("-w", "--wordlist", help="Path to custom wordlist file")
    p.add_argument("-o", "--json", help="Export results to JSON file")
    p.add_argument("-t", "--timeout", type=float, default=5.0, help="Request timeout (default 5s)")
    p.add_argument("-d", "--delay", type=float, default=0.2, help="Delay between requests (default 0.2s)")
    p.add_argument("--depth", type=int, default=2, help="Max crawl depth (default 2)")
    return p.parse_args()

def load_wordlist(path):
    if not path:
        return DEFAULT_WORDLIST
    if not os.path.isfile(path):
        error(f"Wordlist not found: {path}")
        sys.exit(1)
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    success(f"Loaded {len(lines)} entries from {path}")
    return lines

def main():
    print(BANNER)
    args = parse_args()

    if not args.url.startswith(("http://", "https://")):
        error("URL must start with http:// or https://")
        sys.exit(1)

    warn("Use only against systems you own or have written permission to test.\n")

    wordlist = load_wordlist(args.wordlist)
    finder = HiddenURLFinder(
        base_url=args.url,
        timeout=args.timeout,
        delay=args.delay,
        max_depth=args.depth,
    )

    results = finder.run(wordlist)

    if args.json and results:
        finder.export_json(args.json)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}[!] Interrupted by user.{C.RESET}")
        sys.exit(0)