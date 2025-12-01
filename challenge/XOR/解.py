from typing import Tuple

PRINTABLE_MIN, PRINTABLE_MAX = 32, 126

def rolling_xor_decrypt(
    ciphertext_hex: str,
    known_prefix: str = "flag{",
    known_suffix: str = "}",
    key_length: int = 6,
) -> Tuple[str, bytes]:
    """基于已知前后缀的重复 XOR（俗称“滚动异或”）简单攻击。"""
    ct = bytes.fromhex(ciphertext_hex)
    n = len(ct)

    prefix = known_prefix.encode()
    suffix = known_suffix.encode()

    key = [None] * key_length

    # 用前缀恢复
    for i in range(min(len(prefix), n)):
        key[i % key_length] = ct[i] ^ prefix[i]

    # 用后缀恢复
    for i in range(len(suffix)):
        idx = n - len(suffix) + i
        if 0 <= idx < n:
            key[idx % key_length] = ct[idx] ^ suffix[i]

    # 暴力剩余字节（限定到可打印 ASCII）
    for k_i, k_v in enumerate(key):
        if k_v is not None:
            continue
        positions = [j for j in range(n) if j % key_length == k_i]
        for cand in range(256):
            if all(PRINTABLE_MIN <= (ct[pos] ^ cand) <= PRINTABLE_MAX for pos in positions):
                key[k_i] = cand
                break

    # 未恢复到的字节降级为 0（保守）
    key = bytes((kv if kv is not None else 0) for kv in key)

    # 解密
    pt = bytes(ct[i] ^ key[i % key_length] for i in range(n))
    return pt.decode(errors="replace"), key


if __name__ == "__main__":
    hex_ct = "aa3f78df7abf85295bcf32b4a63755cc78d3fc1040fb7598"
    try:
        plaintext, rec_key = rolling_xor_decrypt(hex_ct)
        print(f"恢复的密钥: {rec_key.hex()}")
        print(f"解密结果: {plaintext}")

    except Exception as e:
        print(f"解密出错: {e}")