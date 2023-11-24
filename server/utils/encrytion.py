from typing import Union
import random


def encrypt_Xbase(string: Union[str, int],
                  encrypt_map: Union[str, list] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                  random_seed=None, transform_ascii=True):
    if random_seed:
        random.seed(random_seed)
        encrypt_map = list(encrypt_map)
        random.shuffle(encrypt_map)
        encrypt_map = "".join(encrypt_map)
    encrypted_text = ""
    if transform_ascii or type(string) != int:
        int_string = int("".join(["%003d" % i for i in bytearray(string.encode())]))
    else:
        int_string = string
    length = len(encrypt_map)
    while int_string > length:
        encrypted_text = encrypt_map[int_string % length] + encrypted_text
        int_string = int_string // length
    encrypted_text = encrypt_map[int_string] + encrypted_text
    return encrypted_text


def decrypt_Xbase(string: Union[str, int],
                  decrypt_map: Union[str, list] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                  random_seed=None, transform_ascii=True):
    cut = lambda obj, sec: [int(obj[i:i + sec]) for i in range(0, len(obj), sec)]
    if random_seed:
        random.seed(random_seed)
        decrypt_map = list(decrypt_map)
        random.shuffle(decrypt_map)
        decrypt_map = "".join(decrypt_map)
    length = len(decrypt_map)
    decrypt_int = sum([decrypt_map.index(i) * length ** k for i, k in zip(string[::-1], range(len(string)))])
    if transform_ascii:
        return bytearray(cut(str(decrypt_int), 3)).decode()
    else:
        return decrypt_int
