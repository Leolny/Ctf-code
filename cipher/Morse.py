morse_dict1 = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', '?': '..--..', '!': '-.-.--', '(': '-.--.', '@': '.--.-.', ':': '---...', '=': '-...-', '-': '-....-', ')': '-.--.-',
    '+': '.-.-.', ',': '--..--', '\'': '.----.', '_': '..--.-', '$': '...-..-', ';': '-.-.-.', '/': '-..-.', '\"': '.-..-.', '~': '------.',
    '#': '-...--', '%': '-..-.-', '^': '-.----.', '[': '-.--.--', ']': '-.---.-', '\\': '-.---..', '{': '----.--', '}': '-----.-', '|': '-----..', '<': '----..', '>': '-----.',
}
# 创建字典
morse_dict2 = {
    'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111', 'K': '101', 'L': '0100', 'M': '11', 'N': '10',
    'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1', 'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100',
    '1': '01111', '2': '00111', '3': '00011', '4': '00001', '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110', '0': '11111',
    '.': '010101', '?': '001100', '!': '101011', '(': '10110', '@': '011010', ':': '111000', '=': '10001', '-': '100001', ')': '101101',
    '+': '01010', ',': '110011', '\'': '011110', '_': '001101', '$': '0001001', ';': '101010', '/': '10010', '\"': '010010', '~': '1111110',
    '#': '100011', '%': '100101', '^': '1011110', '[': '1011011', ']': '1011101', '\\': '1011100', '{': '1111011', '}': '1111101', '|': '1111100', '<': '111100', '>': '111110',
}
# 创建字典


def Morse_encode(input_1):
    # 定义摩斯加密函数
    plaintext = str(input_1).upper()
    # 将用户输入字符用str规范并使用upper函数将其变为大写字符,储存为明文
    ciphertext_1 = ''
    ciphertext_2 = ''
    # 创建储存密文字符串的ciphertexe_1和ciphertext_2
    for i in plaintext:
        for j in morse_dict1.keys():
            # 使用for循环嵌套,在字典中找寻与明文对应的键
            if j == i:
                ciphertext_1 += morse_dict1[j]
                ciphertext_1 += '/'
                ciphertext_2 += morse_dict2[j]
                ciphertext_2 += '/'
            elif i not in morse_dict1.keys():
                ciphertext_1 += '\033[31m' + i + '\033[0m'
                ciphertext_1 += '/'
                ciphertext_2 += '\033[31m' + i + '\033[0m'
                ciphertext_2 += '/'
                break
            # 使用if和else,判断字典的键是否和明文值相等,相等则在储存区加入对应的值,若字典无键与他相等储存区加入原先的值并标红
    return ciphertext_1[:-1], ciphertext_2[:-1]
    # 函数返回删除最后一个字符后的储存密文字符串的ciphertexe_1和ciphertext_2


def Morse_decode_ms(input_1):
    # 定义摩斯向字符串的解密函数
    ciphertext = str(input_1)
    # 将用户输入字符用str规范,储存为密文
    plaintext = ''
    # 创建储存明文字符串的plaintext
    if '/' in ciphertext:
        ciphertext_list = ciphertext.split('/')
    elif ' ' in ciphertext:
        ciphertext_list = ciphertext.split(' ')
    # 判断密文分隔符是'/'还是' ',删除分隔符储存为密文列表
    for i in ciphertext_list:
        for j in morse_dict1.keys():
            # 使用for循环嵌套,在字典中找寻与明文对应的值
            if morse_dict1[j] == i:
                plaintext += j
            elif i not in morse_dict1.values():
                plaintext += '/'
                plaintext += '\033[31m' + i + '\033[0m'
                plaintext += '/'
                break
            # 使用if和else,判断字典的值是否和明文值相等,相等则在储存区加入对应的键,若字典无值与他相等储存区加入原先的值并标红
    return plaintext
    # 函数返回储存明文的字符串plaintext


def Morse_decode_22(input_1):
    # 定义二进制摩斯向字符串的解密函数
    ciphertext = str(input_1)
    # 将用户输入字符用str规范,储存为密文
    plaintext = ''
    # 创建储存明文字符串的plaintext
    if '/' in ciphertext:
        ciphertext_list = ciphertext.split('/')
    elif ' ' in ciphertext:
        ciphertext_list = ciphertext.split(' ')
    # 判断密文分隔符是'/'还是' ',删除分隔符储存为密文列表
    for i in ciphertext_list:
        for j in morse_dict2.keys():
            # 使用for循环嵌套,在字典中找寻与明文对应的值
            if morse_dict2[j] == i:
                plaintext += j
            elif i not in morse_dict2.values():
                plaintext += '/'
                plaintext += '\033[31m' + i + '\033[0m'
                plaintext += '/'
                break
            # 使用if和else,判断字典的值是否和明文值相等,相等则在储存区加入对应的键,若字典无值与他相等储存区加入原先的值并标红
    return plaintext
    # 函数返回储存明文的字符串plaintext


def Morse():
    # 定义该模块主函数
    choose = ''
    # 创建储存用户输入的字符串
    while choose != 'q':
        print('------------------------------')
        choose = input('请选择模式:1.加密 2.摩斯解密 3.二进制解密 q.返回上一级:')
        # 使用while进行死循环,除非用户输入'q',并让用户选择模式

        if choose == '1':
            # 选择模式1.加密
            print('------------------------------')
            plaintext = input('请输入明文:')
            # 根据提示输入明文
            try:
                print('------------------------------')
                ciphertext_1, ciphertexte_2 = Morse_encode(plaintext)
                print('摩斯加密为:', ciphertext_1)
                print('二进制加密为:', ciphertexte_2)
                # 调用函数Morse_encode生成密文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '2':
            # 选择模式2.摩斯解密
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            try:
                print('------------------------------')
                plaintext = Morse_decode_ms(ciphertext)
                print('转换为大写字符串为:', plaintext)
                print('转换为小写字符串为:', plaintext.lower())
                # 调用函数Morse_decode_ms生成明文,并输出其大小写
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '3':
            # 选择模式3.二进制解密
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            try:
                print('------------------------------')
                plaintext = Morse_decode_22(ciphertext)
                print('转换为大写字符串为:', plaintext)
                print('转换为小写字符串为:', plaintext.lower())
                # 调用函数Morse_decode_22生成明文,并输出其大小写
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')


# 摩斯密码详细解释:https://baike.baidu.com/item/%E6%91%A9%E5%B0%94%E6%96%AF%E7%94%B5%E7%A0%81/1527853
# 我在这个脚本中加入了摩斯没有的如: '{' '}' 这些符号编码及解码(根据在线网站的编码解码整理得来)
