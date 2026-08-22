import re


def analyze_password(password):
    checks = {
        "Length >= 12": len(password) >= 12,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    score = sum(checks.values())

    print("\n🔐 PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    for name, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"{status} {name}")

    print("-" * 45)

    if score == 5:
        strength = "STRONG 🟢"
    elif score >= 3:
        strength = "MEDIUM 🟡"
    else:
        strength = "WEAK 🔴"

    print(f"Strength: {strength}")

    print("\n💡 Suggestions")

    if len(password) < 12:
        print("• Use at least 12 characters.")

    if not re.search(r"[A-Z]", password):
        print("• Add uppercase letters.")

    if not re.search(r"[a-z]", password):
        print("• Add lowercase letters.")

    if not re.search(r"\d", password):
        print("• Add numbers.")

    if not re.search(r"[^A-Za-z0-9]", password):
        print("• Add special characters.")


def main():
    print("=" * 45)
    print("       🔐 PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    password = input("Enter a password to analyze: ")

    if not password:
        print("❌ Password cannot be empty.")
        return

    analyze_password(password)


if __name__ == "__main__":
    main()
