import time

def hack_caesar(ciphertext, shift):
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

print("=== Automated Cryptanalysis: Keyspace Sweeper ===")
print("Target: Caesar Cipher Monoalphabetic Substitution")
time.sleep(1)

intercepted_data = "YKIAXOZE"
print(f"\n[!] Intercepted Ciphertext: {intercepted_data}")
print("[+] Initiating brute-force attack across all possible keyspace vectors...\n")
time.sleep(1)

for key in range(1, 26):
    print(f"Testing Key [{key:02d}] -> Decrypting... Result: {hack_caesar(intercepted_data, key)}")
    time.sleep(0.1) 

print("\n[+] Attack complete. Human analysis required to identify the plaintext.")