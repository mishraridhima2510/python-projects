import hashlib
from pathlib import Path


def calculate_hash(file_path):
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        print("❌ File not found.")
        return None

    sha256 = hashlib.sha256()

    try:
        with path.open("rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        print(f"❌ Could not read file: {error}")
        return None


def main():
    print("=" * 50)
    print("       🔐 FILE INTEGRITY CHECKER")
    print("=" * 50)

    file_path = input("Enter file path: ").strip()

    file_hash = calculate_hash(file_path)

    if file_hash:
        print("\n🔑 SHA-256 HASH")
        print("-" * 50)
        print(file_hash)
        print("-" * 50)
        print("✅ Hash calculated successfully.")


if __name__ == "__main__":
    main()
