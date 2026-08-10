from pathlib import Path
import shutil


CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(file_extension):
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("❌ Invalid folder path.")
        return

    moved_files = 0

    for file in folder.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.suffix)

        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        if destination.exists():
            print(f"⚠️ Skipped: {file.name}")
            continue

        try:
            shutil.move(str(file), str(destination))
            print(f"✅ {file.name} → {category}/")
            moved_files += 1

        except OSError as error:
            print(f"❌ Could not move {file.name}: {error}")

    print("\n" + "=" * 40)
    print(f"📂 Files organized: {moved_files}")
    print("=" * 40)


def main():
    print("=" * 40)
    print("       📁 FILE ORGANIZER")
    print("=" * 40)

    folder_path = input("Enter folder path: ").strip()

    organize_folder(folder_path)


if __name__ == "__main__":
    main()
