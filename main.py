import random

# List of 10 quote tuples: (quote, author)
QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Happiness depends on ourselves.", "Aristotle"),
    ("Act as if what you dmakes a difference. It does.", "William James"),
    ("Keep your face always toward the sunshine-and shadows will fall behind you.", "Walt Whitman"),
    ("What we think, we become.", "Buddha"),
    ("Some people look for a beautiful place. Others make a place beautiful.", "Hazrat Inayat Khan")
    ]

def get_random_quote(quotes_list):
    """Selects and returns a random tuple from the quotes list."""
    return random.choice(quotes_list)

def display_quote():
    """Formats and prints a random quote."""
    quote, author = get_random_quote(QUOTES)
    print("\n" + "=" * 50)
    print(f'"{quote}')
    print(f"  - {author}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    display_quote()