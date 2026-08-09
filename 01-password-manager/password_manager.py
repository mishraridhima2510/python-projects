import json
import os
import secrets
import string
import hashlib

VAULT_FILE = "vault.json"


def hash_master_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}

    try:
        with open(VAULT_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_vault(vault):
    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def add_credential(vault):
    website = input("Website: ").strip()
    username = input("Username: ").strip()

    password = input(
        "Password (leave empty to generate): "
    ).strip()

    if not password:
        password = generate_password()

    vault[website] = {
        "username": username,
        "password": password
    }

    save_vault(vault)
    print("✅ Credential saved successfully.")


def view_credentials(vault):
    if not vault:
        print("📭 Vault is empty.")
        return

    print("\n📋 Saved Websites")
    print("-" * 30)

    for website in vault:
        print(f"• {website}")


def search_credential(vault):
    website = input("Enter website to search: ").strip()

    if website in vault:
        credential = vault[website]

        print("\n🔎 Credential Found")
        print("-" * 30)
        print("Website :", website)
        print("Username:", credential["username"])
        print("Password:", credential["password"])
    else:
        print("❌ Website not found.")


def delete_credential(vault):
    website = input("Website to delete: ").strip()

    if website in vault:
        del vault[website]
        save_vault(vault)
        print("🗑️ Credential deleted.")
    else:
        print("❌ Website not found.")


def main():
    print("=" * 40)
    print("        🔐 PASSWORD VAULT")
    print("=" * 40)

    master_password = input("Enter master password: ")

    vault = load_vault()

    if "master_hash" not in vault:
        vault["master_hash"] = hash_master_password(master_password)
        save_vault(vault)
        print("✅ Master password created.")
    elif vault["master_hash"] != hash_master_password(master_password):
        print("❌ Incorrect master password.")
        return

    while True:

        print("\n╔══════════════════════════════╗")
        print("║        🔐 PASSWORD VAULT     ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Add Credential            ║")
        print("║ 2. View Websites             ║")
        print("║ 3. Search Credential         ║")
        print("║ 4. Delete Credential         ║")
        print("║ 5. Generate Password         ║")
        print("║ 6. Exit                      ║")
        print("╚══════════════════════════════╝")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_credential(vault)

        elif choice == "2":
            view_credentials(vault)

        elif choice == "3":
            search_credential(vault)

        elif choice == "4":
            delete_credential(vault)

        elif choice == "5":
            print("\n🔑 Generated Password:")
            print(generate_password())

        elif choice == "6":
            print("👋 Vault locked. Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
