def bacon_binary_convert(text, mode='encode'):
    """
    二进制培根密码转换器

    参数:
        text: 输入文本（明文或二进制密文）
        mode: 'encode' 或 'decode'

    返回:
        转换后的字符串
    """

    # 标准培根密码映射表（26字母版本）
    bacon_cipher = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
        'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
        'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
        'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
        'Z': 'BBAAB'
    }

    # 创建反向映射
    reverse_bacon = {v: k for k, v in bacon_cipher.items()}

    if mode == 'encode':
        return encode_bacon(text, bacon_cipher)
    elif mode == 'decode':
        return decode_bacon(text, reverse_bacon)
    else:
        return "错误：模式必须是 'encode' 或 'decode'"


def encode_bacon(text, cipher_map):
    """将文本编码为二进制培根"""
    result = []
    text = text.upper().replace(' ', '')  # 转为大写并移除空格

    for char in text:
        if char in cipher_map:
            # 将A替换为0，B替换为1
            binary_bacon = cipher_map[char].replace('A', '0').replace('B', '1')
            result.append(binary_bacon)
        else:
            result.append(f"[无法编码: {char}]")

    return ' '.join(result)


def decode_bacon(binary_text, reverse_map):
    """将二进制培根解码为文本"""
    result = []

    # 清理输入：移除多余空格，按5位分组
    binary_text = binary_text.replace(' ', '')
    if len(binary_text) % 5 != 0:
        return "错误：二进制长度必须是5的倍数"

    # 每5位一组处理
    for i in range(0, len(binary_text), 5):
        group = binary_text[i:i + 5]

        # 将0替换为A，1替换为B
        bacon_code = group.replace('0', 'A').replace('1', 'B')

        if bacon_code in reverse_map:
            result.append(reverse_map[bacon_code])
        else:
            result.append('?')  # 无法解码的组

    return ''.join(result)


# 测试示例
if __name__ == "__main__":
    print("=== 二进制培根密码转换器 ===\n")

    # 示例1：编码
    plaintext = "HELLO"
    encoded = bacon_binary_convert(plaintext, 'encode')
    print(f"编码测试:")
    print(f"原文: {plaintext}")
    print(f"二进制培根: {encoded}")

    # 示例2：解码
    binary_cipher = "00100 01001 01011 01011 01100"
    decoded = bacon_binary_convert(binary_cipher, 'decode')
    print(f"\n解码测试:")
    print(f"二进制密文: {binary_cipher}")
    print(f"解码结果: {decoded}")

    # 示例3：CTF题目模拟
    print(f"\n=== CTF题目模拟 ===")
    ctf_cipher = "01001 00010 00100 01001 00010 00100 01100 10000"
    ctf_solution = bacon_binary_convert(ctf_cipher, 'decode')
    print(f"CTF密文: {ctf_cipher}")
    print(f"Flag: CTF{{{ctf_solution}}}")

    # 交互模式
    print(f"\n=== 交互模式 ===")
    while True:
        print("\n选择操作:")
        print("1. 文本 -> 二进制培根")
        print("2. 二进制培根 -> 文本")
        print("3. 退出")

        choice = input("请输入选择 (1/2/3): ").strip()

        if choice == '1':
            text = input("请输入要编码的文本: ")
            result = bacon_binary_convert(text, 'encode')
            print(f"编码结果: {result}")

        elif choice == '2':
            binary_text = input("请输入二进制培根密文: ")
            result = bacon_binary_convert(binary_text, 'decode')
            print(f"解码结果: {result}")

        elif choice == '3':
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")