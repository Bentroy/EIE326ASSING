
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Shift within A-Z or a-z
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Leave non-alphabet characters unchanged
            result += char

    return result

# Example usage
text = input("Enter text to encrypt: ")
shift = int(input("Enter shift amount: "))

encrypted = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted}")