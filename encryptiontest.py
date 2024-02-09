from enyoencryption import encrypt, decrypt

test = encrypt("test", "secretkey")
print(test)

test = decrypt("SaSQpN", "secretkey")
print(test)
