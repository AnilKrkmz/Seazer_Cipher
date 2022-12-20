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

def ceaser_decrypt(text, number):
  final_result = ""
  for c in text:
    if c.isupper():
      final_result += chr((ord(c) - number - 65) % 26 + 65)
    else:
      final_result += chr((ord(c) - number - 97) % 26 + 97)
  return final_result

print(ceaser_decrypt(console1,console2))
