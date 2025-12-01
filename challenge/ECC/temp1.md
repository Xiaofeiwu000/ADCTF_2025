我想出一道CTF ECC使用SSSA的密码学题目(题目应该生成异常曲线#E(Fp) = p)，代码支持在sagemath的在线编程环境（https://sagecell.sagemath.org/）使用，注意参数要尽可能大避免爆破，返回参数（打印）即可，格式flag{...}，内容随机生成,避免使用json

参数：
p = 
a = 
b = 
基点与公钥：

G = 
Q = （已知 Q = d * G）
密文（hex）：


加密细节：

私钥 d 满足 Q=d⋅G

令 K = SHA-256(str(d))（把 d 转为十进制字符串再哈希）。

将明文的每个字节与 K 循环异或，得到密文（在本题中把密文以 hex 提供）。

def kdf_from_d(d: int) -> bytes:
    return hashlib.sha256(str(d).encode()).digest()

def xor_keystream(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("empty key")
    ks = (key * ((len(data) + len(key) - 1) // len(key)))[: len(data)]
    return bytes([a ^ b for a, b in zip(data, ks)])

K = kdf_from_d(d)
ct = xor_keystream(flag.encode(), K)



在sagemath在线环境中，生成#E(Fp) = p

