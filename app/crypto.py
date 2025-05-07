from chepy import Chepy
import binascii

def _decode_out(o):
    return o.decode('utf-8') if isinstance(o, (bytes, bytearray)) else o

def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    c = Chepy(text)
    # hitung pergeseran positif untuk encrypt, negatif untuk decrypt
    op = shift % 26 if encrypt else (-shift) % 26
    return _decode_out(c.rotate(op).o)

def rc4(text: str, key: str, encrypt: bool = True) -> str:
    c = Chepy(text)
    if encrypt:
        # Encrypt → hex → bytes → decode
        return _decode_out(
            binascii.unhexlify(
                c.rc4_encrypt(key, key_format='str').o
            )
        )
    # Decrypt: text → hex → raw → decrypt → decode
    return _decode_out(
        c.to_hex(delimiter='')
         .hex_to_str()
         .rc4_decrypt(key, key_format='str')
         .o
    )

def aes(text: str, key: str, encrypt: bool = True) -> str:
    c = Chepy(text)
    if encrypt:
        # ambil .o dari to_hex → hex string
        return c.aes_encrypt(key, key_format='utf-8') \
                .to_hex(delimiter='') \
                .o
    # decrypt: hex → str → decrypt → decode
    return _decode_out(
        c.hex_to_str()
         .aes_decrypt(key, key_format='utf-8')
         .o
    )

def des(text: str, key: str, encrypt: bool = True) -> str:
    c = Chepy(text)
    if encrypt:
        return c.des_encrypt(key, key_format='utf-8') \
                .to_hex(delimiter='') \
                .o
    return _decode_out(
        c.hex_to_str()
         .des_decrypt(key, key_format='utf-8')
         .o
    )