from chepy import Chepy
import binascii
import hashlib

def _decode_out(o):
    return o.decode('utf-8', errors='ignore') if isinstance(o, (bytes, bytearray)) else o

def _md5_hex(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()

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

def aes(text: str, key: str, encrypt: bool = True,
        iv_hex: str = '00'*16, mode: str = 'CBC') -> str:
    key_hex = _md5_hex(key)           # 32 hex chars = 16 bytes
    c = Chepy(text)
    if encrypt:
        # → Chepy → to_hex() → .o (bytes) → decode jadi str
        return _decode_out(
            c.aes_encrypt(
                key_hex,
                mode=mode,
                iv=iv_hex,
                key_format='hex',
                iv_format='hex'
            )
            .to_hex(delimiter='')
            .o
        )
    # decrypt: hex→raw→decrypt→.o (bytes)→decode
    return _decode_out(
        c.hex_to_str()
         .aes_decrypt(
            key_hex,
            mode=mode,
            iv=iv_hex,
            key_format='hex',
            iv_format='hex'
         )
         .o
    )

def des(text: str, key: str, encrypt: bool = True,
        iv_hex: str = '00'*8, mode: str = 'CBC') -> str:
    key_hex = _md5_hex(key)[:16]      # 16 hex chars = 8 bytes
    c = Chepy(text)
    if encrypt:
        return _decode_out(
            c.des_encrypt(
                key_hex,
                mode=mode,
                iv=iv_hex,
                key_format='hex',
                iv_format='hex'
            )
            .to_hex(delimiter='')
            .o
        )
    return _decode_out(
        c.hex_to_str()
         .des_decrypt(
            key_hex,
            mode=mode,
            iv=iv_hex,
            key_format='hex',
            iv_format='hex'
         )
         .o
    )