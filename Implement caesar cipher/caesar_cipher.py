def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    output = caesar_cipher(text, shift, mode)
    print(f"Result: {output}")
