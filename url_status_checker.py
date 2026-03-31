import requests
import time

# Safe color support (no crash if colorama not installed)
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except:
    class Dummy:
        def __getattr__(self, name):
            return ""
    Fore = Style = Dummy()


# Check URL
def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()

        status_code = response.status_code
        response_time = round((end - start) * 1000, 2)

        if status_code == 200:
            status = Fore.GREEN + "UP"
        else:
            status = Fore.YELLOW + "ISSUE"

        return url, status, status_code, response_time

    except requests.exceptions.ConnectionError:
        return url, Fore.RED + "DOWN", "-", "-"
    except requests.exceptions.Timeout:
        return url, Fore.YELLOW + "TIMEOUT", "-", "-"
    except:
        return url, Fore.RED + "ERROR", "-", "-"


# Header
def print_header():
    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.CYAN + "        🌐 URL STATUS CHECKER")
    print(Fore.CYAN + "=" * 50)


# Menu
def print_menu():
    print(Fore.MAGENTA + "\n1. Check Single URL")
    print("2. Check Multiple URLs")
    print("3. Exit")


# Print result (single)
def print_result(url, status, code, time_ms):
    print(Fore.BLUE + "\n" + "-" * 50)
    print(f"🔗 URL           : {url}")
    print(f"📡 Status        : {status}")
    print(f"📊 Status Code   : {code}")
    print(f"⚡ Response Time : {time_ms} ms")
    print(Fore.BLUE + "-" * 50)


# Single URL
def check_single():
    url = input(Fore.WHITE + "\nEnter URL: ").strip()

    if not url:
        print(Fore.RED + "❌ URL cannot be empty!")
        return

    if not url.startswith("http"):
        url = "https://" + url

    print(Fore.YELLOW + "\nChecking...\n")

    result = check_url(url)
    print_result(*result)


# Multiple URLs
def check_multiple():
    print(Fore.WHITE + "\nEnter URLs (type 'done' to stop):")

    urls = []
    while True:
        url = input("👉 ").strip()
        if url.lower() == "done":
            break
        if url:
            if not url.startswith("http"):
                url = "https://" + url
            urls.append(url)

    if not urls:
        print(Fore.RED + "❌ No URLs entered!")
        return

    print(Fore.YELLOW + "\nChecking all URLs...\n")

    print(Fore.CYAN + f"{'URL':30} {'STATUS':10} {'CODE':6} {'TIME(ms)'}")
    print(Fore.CYAN + "-" * 60)

    for url in urls:
        u, status, code, t = check_url(url)
        print(f"{u[:30]:30} {status:10} {str(code):6} {str(t)}")


# Main
def main():
    while True:
        print_header()
        print_menu()

        choice = input(Fore.WHITE + "\nEnter choice: ").strip()

        if choice == "1":
            check_single()
        elif choice == "2":
            check_multiple()
        elif choice == "3":
            print(Fore.GREEN + "\n👋 Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice!")


if __name__ == "__main__":
    main()
