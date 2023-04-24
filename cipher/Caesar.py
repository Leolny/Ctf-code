def Caesar_encode(input_1, input_2):
    # 定义凯撒加密函数
    plaintext = str(input_1)
    # 使用str函数规范用户输入的第一字符,定义为明文
    key = int(input_2)
    # 使用int函数规范用户输入的第二字符,定义为密钥
    offset = key % 26
    # 凯撒加密最大偏移量为26
    ciphertext = ''
    # 创建储存密文的字符串ciphertext
    for i in plaintext:
        # 使用for循环历遍明文进行加密
        ciphertext_staging = i
        # 将明文暂储存在该ciphertext_staging变量
        if 65 <= ord(ciphertext_staging) <= 90:
            # 判断是否是大写字母
            offset_staging = 90 - ord(ciphertext_staging)
            # 计算该变量距离'Z'差多少位偏移,储存在offset_staging变量中
            if offset > offset_staging:
                offset_staging = offset - offset_staging
                ciphertext_staging = chr(65 + (offset_staging - 1))
            else:
                ciphertext_staging = chr(ord(ciphertext_staging) + offset)
            ciphertext += ciphertext_staging
            # 进行密钥与该变量的比较,分别在大于和不大于的两种情况下的进行偏移转换,并加入储存密文的字符串中
        elif 97 <= ord(ciphertext_staging) <= 122:
            # 判断是否为小写字母
            offset_staging = 122 - ord(ciphertext_staging)
            # 计算该变量距离'z'差多少位偏移,储存在offset_staging变量中
            if offset > offset_staging:
                offset_staging = offset - offset_staging
                ciphertext_staging = chr(97 + (offset_staging - 1))
            else:
                ciphertext_staging = chr(ord(ciphertext_staging) + offset)
            ciphertext += ciphertext_staging
            # 进行密钥与该变量的比较,分别在大于和不大于的两种情况下的进行偏移转换,并加入储存密文的字符串中
        else:
            ciphertext += ciphertext_staging
            # 若非大小写字母则将原字符加入储存密文的字符串
    return ciphertext
    # 函数返回储存的字符串


def Caesar_decode(input_1, input_2):
    # 定义凯撒解密函数
    ciphertext = str(input_1)
    # 使用str函数规范用户输入的第一字符,定义为密文
    key = int(input_2)
    # 使用int函数规范用户输入的第二字符,定义为密钥
    offset = key % 26
    # 凯撒加密最大偏移量为26
    plaintext = ''
    # 创建储存密文的字符串plaintext
    for i in ciphertext:
        # 使用for循环历遍密文进行解密
        plaintext_staging = i
        # 将密文暂储存在该plaintext_staging变量
        if 65 <= ord(plaintext_staging) <= 90:
            # 判断是否是大写字母
            offset_staging = ord(plaintext_staging) - 65
            # 计算该变量距离'A'差多少位偏移,储存在offset_staging变量中
            if offset > offset_staging:
                offset_staging = offset - offset_staging
                plaintext_staging = chr(90 - (offset_staging - 1))
            else:
                plaintext_staging = chr(ord(plaintext_staging) - offset)
            plaintext += plaintext_staging
            # 进行密钥与该变量的比较,分别在大于和不大于的两种情况下的进行偏移转换,并加入储存明文的字符串中
        elif 97 <= ord(plaintext_staging) <= 122:
            # 判断是否为小写字母
            offset_staging = ord(plaintext_staging) - 97
            # 计算该变量距离'a'差多少位偏移,储存在offset_staging变量中
            if offset > offset_staging:
                offset_staging = offset - offset_staging
                plaintext_staging = chr(122 - (offset_staging-1))
            else:
                plaintext_staging = chr(ord(plaintext_staging) - offset)
            plaintext += plaintext_staging
            # 进行密钥与该变量的比较,分别在大于和不大于的两种情况下的进行偏移转换,并加入储存明文的字符串中
        else:
            plaintext += plaintext_staging
            # 若非大小写字母则将原字符加入储存明文的字符串
    return plaintext
    # 函数返回储存的字符串


def Caesar_encode_pro(input_1):
    # 定义凯撒加密函数(升级版)
    plaintext = str(input_1)
    # 使用str函数规范用户输入的字符,定义为明文
    for i in range(27):
        # 使用for循环历遍从0到26的字节进行偏移加密
        key = i
        # 定义密钥
        ciphertext = Caesar_encode(plaintext, key)
        # 调用函数Caesar_encode加密生成密文
        print('偏移量为', key, '时,密文为:', ciphertext)
        # 输出在不同密钥下的生成的密文


def Caesar_decode_pro(input_1):
    # 定义凯撒解密函数(升级版)
    ciphertext = str(input_1)
    # 使用str函数规范用户输入的字符,定义为密文
    for i in range(27):
        # 使用for循环历遍从0到26的字节进行偏移解密
        key = i
        # 定义密钥
        plaintext = Caesar_decode(ciphertext, key)
        # 调用函数Caesar_decode加密生成明文
        print('偏移量为', key, '时,明文为:', plaintext)
        # 输出在不同密钥下的生成的明文


def Caesar():
    # 定义该模块主函数
    choose = ''
    # 创建储存用户输入的字符串
    while choose != 'q':
        print('------------------------------')
        choose = input('请选择模式:1.加密 2.解密 3.懒人加密 4.暴力破解 q.返回上一级:')
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
                ciphertext = Caesar_encode(plaintext, key)
                print('密文为:', ciphertext)
                # 调用函数Caesar_encode生成密文,并输出
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
                plaintext = Caesar_decode(ciphertext, key)
                print('明文为:', plaintext)
                # 调用函数Caesar_decode生成明文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '3':
            # 选择模式3.懒人加密
            print('------------------------------')
            plaintext = input('请输入明文:')
            # 根据提示输入明文
            try:
                print('------------------------------')
                Caesar_encode_pro(plaintext)
                # 调用函数Caesar_encode_pro生成密文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '4':
            # 选择模式4.暴力破解
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            try:
                print('------------------------------')
                Caesar_decode_pro(ciphertext)
                # 调用函数Caesar_decode_pro生成明文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')


# 凯撒密码详细解释:https://baike.baidu.com/item/%E6%81%BA%E6%92%92%E5%AF%86%E7%A0%81/4905284
# ASCII码详细解释:http://c.biancheng.net/c/ascii/
