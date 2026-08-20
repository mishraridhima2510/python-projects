import socket


def get_network_info(host):
    print("\n🌐 NETWORK INFORMATION")
    print("=" * 45)

    try:
        ip_address = socket.gethostbyname(host)

        print(f"Hostname    : {host}")
        print(f"IP Address  : {ip_address}")

    except socket.gaierror:
        print("❌ Could not resolve hostname.")
        return

    try:
        canonical_name, aliases, addresses = socket.gethostbyname_ex(host)

        print(f"Canonical   : {canonical_name}")

        if aliases:
            print(f"Aliases     : {', '.join(aliases)}")

        if len(addresses) > 1:
            print("IP Addresses:")

            for address in addresses:
                print(f"  • {address}")

    except socket.gaierror:
        print("⚠️ Additional DNS information unavailable.")


def main():
    print("=" * 45)
    print("       🌐 NETWORK INFO TOOL")
    print("=" * 45)

    host = input("Enter hostname or domain: ").strip()

    if not host:
        print("❌ Hostname cannot be empty.")
        return

    get_network_info(host)


if __name__ == "__main__":
    main()
