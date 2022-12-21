import webbrowser
import time

yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

print("This tool was made by Nuri Anıl Korkmaz")
time.sleep(1)
webbrowser.open("https://github.com/AnilKrkmz")

logo = """

\033[91m ███████ ███████  █████  ███████ ███████ ██████   \033[96m    ██████ ██ ██████  ██   ██ ███████ ██████   \033[0m
\033[91m ██      ██      ██   ██    ███  ██      ██   ██  \033[96m   ██      ██ ██   ██ ██   ██ ██      ██   ██  \033[0m 
\033[91m ███████ █████   ███████   ███   █████   ██████   \033[96m   ██      ██ ██████  ███████ █████   ██████   \033[0m 
\033[91m      ██ ██      ██   ██  ███    ██      ██   ██  \033[96m   ██      ██ ██      ██   ██ ██      ██   ██  \033[0m
\033[91m ███████ ███████ ██   ██ ███████ ███████ ██   ██  \033[96m    ██████ ██ ██      ██   ██ ███████ ██   ██  \033[0m

"""

print(logo)


console1 = input("\033[96mEnter the text to decrypt: \033[0m")
console2 = int(input("\033[91mEnter the crypt number: \033[0m"))


def caesar_cipher(text, shift):
    alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    encrypted_text = []
    for char in text:
        if char not in alphabet:
            encrypted_text.append(char)
            continue
        idx = alphabet.index(char)
        idx = (idx + shift) % len(alphabet)
        encrypted_text.append(alphabet[idx])
    return ''.join(encrypted_text)
text = console1
shift = console2

print(caesar_cipher(text, shift))

