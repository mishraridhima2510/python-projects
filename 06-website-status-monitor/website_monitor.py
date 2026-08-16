from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from time import perf_counter


def check_website(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    request = Request(
        url,
        headers={"User-Agent": "Python-Website-Monitor/1.0"}
    )

    start_time = perf_counter()

    try:
        with urlopen(request, timeout=10) as response:
            response_time = perf_counter() - start_time

            return {
                "url": url,
                "status": response.status,
                "response_time": response_time,
                "online": True
            }

    except HTTPError as error:
        response_time = perf_counter() - start_time

        return {
            "url": url,
            "status": error.code,
            "response_time": response_time,
            "online": False
        }

    except (URLError, TimeoutError):
        return {
            "url": url,
            "status": None,
            "response_time": None,
            "online": False
        }


def display_result(result):
    if result["online"]:
        print(
            f"🟢 ONLINE  | "
            f"{result['url']} | "
            f"HTTP {result['status']} | "
            f"{result['response_time']:.2f}s"
        )
    else:
        status = result["status"] or "N/A"

        print(
            f"🔴 OFFLINE | "
            f"{result['url']} | "
            f"HTTP {status}"
        )


def main():
    print("=" * 65)
    print("             🌐 WEBSITE STATUS MONITOR")
    print("=" * 65)

    while True:
        print("\n1. Check Website")
        print("2. Check Multiple Websites")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            url = input("Enter website URL: ").strip()

            if url:
                result = check_website(url)
                print()
                display_result(result)
            else:
                print("❌ URL cannot be empty.")

        elif choice == "2":
            websites = input(
                "Enter URLs separated by commas: "
            ).split(",")

            print("\n📊 WEBSITE STATUS")
            print("-" * 65)

            for website in websites:
                website = website.strip()

                if website:
                    result = check_website(website)
                    display_result(result)

            print("-" * 65)

        elif choice == "3":
            print("👋 Monitor closed.")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
