def bacon_binary(text: str, mode: str = "encode") -> str:
    """
    直接按 0/1 的培根密码（26字母版）编码/解码
    A->00000, B->00001, ..., Z->11001

    mode: "encode" 或 "decode"
    """
    if mode == "encode":
        s = "".join(ch for ch in text.upper() if "A" <= ch <= "Z")
        return " ".join(format(ord(ch) - 65, "05b") for ch in s) or ""
    elif mode == "decode":
        bits = "".join(c for c in text if c in "01")
        if len(bits) % 5 != 0:
            return "错误：二进制长度必须是 5 的倍数"
        out = []
        for i in range(0, len(bits), 5):
            val = int(bits[i:i+5], 2)
            if 0 <= val < 26:
                out.append(chr(val + 65))
            else:
                out.append("?")
        return "".join(out)
    else:
        return "错误：mode 必须是 'encode' 或 'decode'"

# 简单测试
if __name__ == "__main__":
    m = "00101 01011 00000 00110 00011 10100 01101 10010 00111 00000 01101 10010 00111 10100 01110 00011 00100 00011 10100 01000"
    print("解码：", bacon_binary(m, "decode"))

