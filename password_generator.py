# password_generator.py
import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not pools:
        raise ValueError("Select at least one character type.")
    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)} to include all selected types.")

    # Ensure at least one character from each chosen pool
    password_chars = [random.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    password_chars += [random.choice(all_chars) for _ in range(length - len(password_chars))]
    random.shuffle(password_chars)
    return "".join(password_chars)

def ask_bool(prompt, default=True):
    ans = input(f"{prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
    if ans == "":
        return default
    return ans.startswith("y")

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        use_lower = ask_bool("Include lowercase letters?", True)
        use_upper = ask_bool("Include uppercase letters?", True)
        use_digits = ask_bool("Include digits?", True)
        use_symbols = ask_bool("Include special symbols?", True)

        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print("\n✅ Generated Password:")
        print(password)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
