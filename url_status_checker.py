import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        code = response.status_code

        print("\nStatus Code:", code)

        if code == 200:
            print("Website is UP")
        elif code == 301 or code == 302:
            print("Website redirected")
        elif code == 403:
            print("Access Forbidden")
        elif code == 404:
            print("Page Not Found")
        elif code == 500:
            print("Internal Server Error")
        elif code == 503:
            print("Service Unavailable (Server Down or Busy)")
        else:
            print("Unknown Status Code")

    except requests.exceptions.Timeout:
        print("Website timed out")
    except requests.exceptions.ConnectionError:
        print("Website is DOWN")
    except requests.exceptions.InvalidURL:
        print("Invalid URL")

def main():
    url = input("Enter website URL (https://example.com): ")
    check_website(url)

if __name__ == "__main__":
    main()
