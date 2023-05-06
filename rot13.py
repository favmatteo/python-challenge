def rot13(message):
    final: str = ""
    n: int = 13
    for letter in message:
        first = ord('a' if letter >= 'a' and letter <= 'z' else 'A')
        last = ord('z' if letter >= 'a' and letter <= 'z' else 'Z')
        ascii = ord(letter)
        if letter >= chr(first) and letter <= chr(last):
            final += chr(ascii + n) if (ascii + n) <= last else chr( (ascii + n) % (last) + first-1)
        else:
            final += letter
    return final

normal = ("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")
rot13str = rot13(normal)

normal = normal.split(" ")
rot13str = rot13str.split(" ")

for i in range(len(normal)):
    print(f"{normal[i]} | {rot13str[i]}\n")

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
