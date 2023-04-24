from . import Caesar
# 维吉尼亚为凯撒的嵌套,可以调用凯撒密码的函数


def Key_offset(input_1):
    # 定义函数生成密钥偏移量列表
    key = str(input_1)
    # 使用str函数规范用户输入的字符,定义为密钥
    key_list = []
    # 创建密钥对应偏移量的列表
    for i in key:
        # 使用for循环求得密钥中各字母对应偏移量
        key_num = ord(i) - 97
        # 计算该字母偏移量
        key_list.append(key_num)
        # 将偏移量加入列表
    return key_list
    # 函数返回密钥列表


def not_count(input_1):
    # 定义统计字符串中的大写字母,小写字母以及非字母个数
    total = str(input_1)
    # 使用str规范用户输入的字符
    big_num = 0
    small_num = 0
    not_num = 0
    # 创建储存大写字母,小写字母,非字母的变量
    for i in total:
        # 使用for循环历遍该字符串
        if i.isupper():
            big_num += 1
        # 判断是否为大写字母,是则big_num数量加一
        elif i.islower():
            small_num += 1
        # 判断是否为小写字母,是则small_num数量加一
        else:
            not_num += 1
        # 判断是否为非字母,是则not_num数量加一
    return big_num, small_num, not_num
    # 函数返回大写字母,小写字母以及非字母个数


def Delete(input_1):
    # 定义函数删除维吉尼亚求密钥产生的重复值
    key_staging = str(input_1)
    # 使用str规范用户输入的字符，定义为暂存密钥
    key_num = len(key_staging)
    # 统计暂存密钥的长度
    key = ''
    # 创建储存密钥的字符串
    offset_num = 0
    # 密钥长度计算值
    try:
        for i in range(key_num):
            # 使用for循环通过底标历遍暂存的密钥
            if key_staging[i] not in key:
                # 判断暂存密钥是否在储存密钥的字符串里
                key += key_staging[i]
                offset_num += 1
                # 上述判断为不在时将其对应值加入储存密钥的字符串里并对密钥长度加一
            else:
                # 上述判断为在时进入下一层判断
                if key_staging[i] != key_staging[i - offset_num]:
                    # 判断该值是否与密钥的第一个值相等
                    key += key_staging[i]
                    offset_num += 1
                    # 上述判断为不相等时将其对应值加入储存密钥的字符串里并对密钥长度加一
                else:
                    # 上述判断为相等时进入下一层判断
                    decide = offset_num
                    # 判断值
                    for j in range(offset_num):
                        # 使用for循环判断密钥存储的一系列值是否与密钥长度相等的暂存密钥的一系列值相等
                        if key[j] == key_staging[i + j]:
                            decide -= 1
                            # 如果每次相等，判断值则加一
                        else:
                            pass
                            # 不相等则不做反应
                    if decide == 0:
                        # 判断判断值是否改变
                        return key
                        # 如果改变，函数则跳出程序返回密钥值
                    else:
                        key += key_staging[i]
                        offset_num += 1
                        # 如果未改变则将其对应值加入储存密钥的字符串里并对密钥长度加一
    except:
        # 使用try和except避免整个程序意外终止
        print('未知错误!')


def Vigen_encode(input_1, input_2):
    # 定义维吉尼亚的加密函数
    plaintext = str(input_1)
    key = str(input_2).lower()
    # 使用str函数规范用户输入的字符,定义为明文和密钥,且密钥不区分大小写
    key_list = Key_offset(key)
    # 调用函数key_offset生成密钥偏移量列表
    plaintext_num = len(plaintext)
    key_num = len(key_list)
    # 分别求得明文和密钥的总长度
    ciphertext = ''
    # 创建储存密文的字符串ciphertext
    for i in range(plaintext_num):
        # 使用for循环历遍明文底标进行加密
        big_num, small_num, not_num = not_count(ciphertext)
        # 调用not_count函数统计储存密文的字符串有多少大写字母,小写字母以及非字母个数
        offset = (i - not_num) % key_num
        # 计算该明文对应的密钥
        ciphertext_staging = Caesar.Caesar_encode(
            plaintext[i], key_list[offset])
        ciphertext += ciphertext_staging
        # 调用Caesar模块的Caesar_encode函数求得该明文加密后的密文,将其加入储存密文的字符串
    print('大写字母个数为:', big_num)
    print('小写字母个数为:', small_num)
    print('非字母个数为:', not_num)
    return ciphertext
    # 函数输出大写字母,小写字母以及非字母个数并返回储存密文的字符串


def Vigen_decode(input_1, input_2):
    # 定义维吉尼亚的解密函数
    ciphertexe = str(input_1)
    key = str(input_2).lower()
    # 使用str函数规范用户输入的字符,定义为密文和密钥,且密钥不区分大小写
    key_list = Key_offset(key)
    # 调用函数key_offset生成密钥偏移量列表
    ciphertext_num = len(ciphertexe)
    key_num = len(key_list)
    # 分别求得密文和密钥的总长度
    plaintext = ''
    # 创建储存明文的字符串plaintext
    for i in range(ciphertext_num):
        # 使用for循环历遍明文底标进行解密
        big_num, small_num, not_num = not_count(plaintext)
        # 调用not_count函数统计储存明文的字符串有多少大写字母,小写字母以及非字母个数
        offset = (i - not_num) % key_num
        # 计算该密文对应的密钥
        plaintexe_staging = Caesar.Caesar_decode(
            ciphertexe[i], key_list[offset])
        plaintext += plaintexe_staging
        # 调用Caesar模块的Caesar_decode函数求得该密文解密后的明文,将其加入储存明文的字符串
    print('大写字母个数为:', big_num)
    print('小写字母个数为:', small_num)
    print('非字母个数为:', not_num)
    return plaintext
    # 函数输出大写字母,小写字母以及非字母个数并返回储存明文的字符串


def Vigen_key(input_1, input_2):
    # 定义维吉尼亚求密钥的脚本
    plaintext = str(input_1)
    ciphertext = str(input_2)
    # 使用str规范用户输入的字符，并定义为明文和密文
    plaintext_num = len(plaintext)
    ciphertext_num = len(ciphertext)
    # 分别统计明文和密文的长度
    key_staging = ''
    if plaintext_num != ciphertext_num:
        # 判断明文和密文长度是否相等
        print('明文和密文长度不一致!请仔细核对')
        # 输出报错提示
    else:
        # 上述判断不成立执行以下代码
        for i in range(plaintext_num):
            # 使用for循环使用底标历遍明文与密文
            if 65 <= ord(plaintext[i]) <= 90:
                # 判断是否是大写字母
                if ord(plaintext[i]) > ord(ciphertext[i]):
                    # 上述判断成立后判断明文对应的值是否比密文对应的值大
                    offset_1 = 90 - ord(plaintext[i])
                    offset_2 = ord(ciphertext[i]) - 65
                    key_stag = chr(97 + offset_1 + offset_2 + 1)
                    key_staging += key_stag
                    # 在上述条件成立时，进行一系列的偏移量计算然后计算对应的密钥字符，并加入储存密钥的字符串
                else:
                    key_stag = chr(97 + ord(ciphertext[i]) - ord(plaintext[i]))
                    key_staging += key_stag
                    # 在上述条件不成立时，进行一系列的偏移量计算然后计算对应的密钥字符，并加入储存密钥的字符串
            elif 97 <= ord(plaintext[i]) <= 122:
                # 判断是否是小写字母
                if ord(plaintext[i]) > ord(ciphertext[i]):
                    # 上述判断成立后判断明文对应的值是否比密文对应的值大
                    offset_1 = 122 - ord(plaintext[i])
                    offset_2 = ord(ciphertext[i])-97
                    key_stag = chr(97 + offset_1 + offset_2 + 1)
                    key_staging += key_stag
                    # 在上述条件成立时，进行一系列的偏移量计算然后计算对应的密钥字符，并加入储存密钥的字符串
                else:
                    key_stag = chr(97 + ord(ciphertext[i]) - ord(plaintext[i]))
                    key_staging += key_stag
                    # 在上述条件不成立时，进行一系列的偏移量计算然后计算对应的密钥字符，并加入储存密钥的字符串
            else:
                pass
            # 在都不满足时不做任何反应
    key = Delete(key_staging)
    # 调用Delete函数删除密钥重复值，取唯一值
    return key
    # 函数返回密钥值


def Vigen():
    # 定义该模块主函数
    choose = ''
    # 创建储存用户输入的字符串
    while choose != 'q':
        print('------------------------------')
        choose = input('请选择模式:1.加密 2.解密 3.求密钥 q.返回上一级:')
        # 使用while进行死循环,除非用户输入'q',并让用户选择模式

        if choose == '1':
            # 选择模式1.加密
            print('------------------------------')
            plaintext = input('请输入明文:')
            # 根据提示输入明文
            print('------------------------------')
            key = input('请输入密钥:')
            # 根据提示输入密钥
            try:
                print('------------------------------')
                ciphertext = Vigen_encode(plaintext, key)
                print('------------------------------')
                print('密文为:', ciphertext)
                # 调用Vigen_encode生成密文并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '2':
            # 选择模式2.解密
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            print('------------------------------')
            key = input('请输入密钥:')
            # 根据提示输入密钥
            try:
                print('------------------------------')
                plaintext = Vigen_decode(ciphertext, key)
                print('------------------------------')
                print('明文为:', plaintext)
                # 调用Vigen_decode生成明文并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '3':
            # 选择模式3.求密钥
            print('------------------------------')
            plaintext = input('请输入明文:')
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入明文和密文
            plaintext_num = len(plaintext)
            ciphertext_num = len(ciphertext)
            # 分别统计明文和密文的长度
            print('------------------------------')
            print('明文长度为:', plaintext_num)
            print('密文长度为:', ciphertext_num)
            # 输出明文和密文的长度
            try:
                print('------------------------------')
                key = Vigen_key(plaintext, ciphertext)
                print('密钥为:', key)
                # 调用Vigen_key生成密钥并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')


# 维吉尼亚密码详细解释:https://baike.baidu.com/item/%E7%BB%B4%E5%90%89%E5%B0%BC%E4%BA%9A%E5%AF%86%E7%A0%81/4905472
# ASCII码详细解释:http://c.biancheng.net/c/ascii/
