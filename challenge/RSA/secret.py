import random

# 生成明文m，格式为flag{...}
flag_content = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=20))
flag = f"flag{{{flag_content}}}"

