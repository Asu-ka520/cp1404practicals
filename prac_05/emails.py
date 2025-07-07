"""
Email to Name Dictionary
Estimate: 30 minutes
Actual: 30 minutes
"""

def extract_name_from_email(email):
    """
    Extracts a person's name from their email address.
    Rule:
        - Take the part before the @ symbol
        - Replace . and _ with spaces
        - Title-case each word (capitalize the first letter)
        - Example: lindsay.ward@jcu.edu.au -> Lindsay Ward
    """
    if "@" not in email:
        return ""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(parts).title()
    return name

email_to_name = {}

while True:
    email = input("Email: ").strip()
    if not email:
        break
    default_name = extract_name_from_email(email)
    confirm = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
    if confirm in ("", "y", "yes"):
        name = default_name
    else:
        name = input("Name: ").strip().title()
    email_to_name[email] = name

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")