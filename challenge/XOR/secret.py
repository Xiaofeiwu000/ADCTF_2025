import random
import string

def generate_random_flag():
    """生成随机flag内容"""
    flag_content = ''.join(random.choices(string.ascii_letters + string.digits, k=18))
    return f"flag{{{flag_content}}}"

def generate_random_key(length=6):
    """生成长度为6的随机密钥"""
    return bytes([random.randint(0, 255) for _ in range(length)])

flag = generate_random_flag()
key = generate_random_key()

if __name__ == "__main__":
    print(f"明文flag: {flag}")
    print(f"密钥(hex): {key.hex()}")
