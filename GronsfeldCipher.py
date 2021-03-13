import string
string.digits + string.ascii_letters + string.punctuation + string.digits
alph = string.ascii_uppercase


def algo(text, k, op):
    k *= len(text) // len(k) + 1
    return ''.join(alph[alph.index(j) + int(k[i]) * op] for i, j in enumerate(text))


def encrypt(message, key):
    return algo(message, key, 1)


def decrypt(message, key):
    return algo(message, key, -1)


print(encrypt('ANCIENT', '420'))  #шифрование
print(decrypt('EPCMGNX', '420'))  #расшифровывание
