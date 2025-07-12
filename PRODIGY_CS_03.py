import re

def check_password_strength(password):
    # Initialize strength points and feedback
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("🔸 Make it at least 8 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add uppercase letters (A-Z).")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add lowercase letters (a-z).")

    # Digit check
    if re.search(r"\d", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add numbers (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*()\-_=+\[\]{}|;:'\",.<>?/]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add special characters (!@#$...).")

    # Determine strength
    if strength_points == 5:
        strength = "🟢 Strong Password"
    elif 3 <= strength_points < 5:
        strength = "🟡 Medium Password"
    else:
        strength = "🔴 Weak Password"

    return strength, feedback

# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, suggestions = check_password_strength(pwd)

    print("\nPassword Strength:", result)
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(tip)
