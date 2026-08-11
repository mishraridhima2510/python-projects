import csv
from pathlib import Path


def load_data(file_path):
    path = Path(file_path)

    if not path.exists():
        print("❌ CSV file not found.")
        return []

    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except (OSError, csv.Error) as error:
        print(f"❌ Could not read CSV: {error}")
        return []


def analyze_data(data):
    if not data:
        print("📭 No data available.")
        return

    print("\n📊 CSV DATA ANALYZER")
    print("=" * 40)

    print(f"Records : {len(data)}")
    print(f"Columns : {len(data[0])}")

    print("\n📋 Columns")
    for column in data[0]:
        print(f"• {column}")

    print("\n🔎 Sample Records")
    for row in data[:5]:
        print(row)


def main():
    print("=" * 40)
    print("       📊 CSV DATA ANALYZER")
    print("=" * 40)

    file_path = input("Enter CSV file path: ").strip()

    data = load_data(file_path)
    analyze_data(data)


if __name__ == "__main__":
    main()
