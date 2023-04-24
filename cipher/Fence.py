def factor(input_1):
    # 定义获取一个数除去1和本身的所有因数
    factor_list = []
    # 创建储存因素的列表
    factor_num = int(input_1)
    # 使用int将输入的字节转换为整型,定义为整数
    for i in range(2, factor_num):
        # 使用for循环历遍从2到输入的数找寻所有因数
        if factor_num % i == 0:
            factor_list.append(i)
        # 判断该整数能否被除尽,若能则将该除数加入列表
    return factor_list
    # 函数返回储存因素的列表


def Fence_encode(input_1, input_2):
    # 定义栅栏密码的加密算法
    plaintext = str(input_1)
    # 使用str将输入的第一字节转换为字符型,定义为明文
    key = int(input_2)
    # 使用int将输入的第二字节转换为整型,定义为密钥
    plaintext_num = len(plaintext)
    # 统计明文总长数
    group_num = int(plaintext_num // key)
    # 统计分组后每组长度,且用int函数做规范操作
    ciphertext = ''
    # 创建储存密文的字符串
    for i in range(key):
        for j in range(group_num):
            # 使用for循环嵌套,进行栅栏加密的重新排列
            offset = j * key + i
            # 计算加密顺序的底标
            ciphertext += plaintext[offset]
            # 将明文该底标的字符添加进密文字符串中
    return ciphertext
    # 函数返回加密完成后的密文


def Fence_decode(input_1, input_2):
    # 定义栅栏密码的解密算法
    ciphertext = str(input_1)
    # 使用str将输入的第一字节转换为字符型,定义为密文
    key = int(input_2)
    # 使用int将输入的第二字节转换为整型,定义为密钥
    ciphertext_num = len(ciphertext)
    # 统计密文总长度
    group_num = int(ciphertext_num // key)
    # 统计分组后每组长度,且用int函数做规范操作
    plaintext = ''
    # 创建储存明文的字符串
    for i in range(group_num):
        for j in range(key):
            # 使用for循环嵌套,进行栅栏解密的重新排列
            offset = j * group_num + i
            # 计算解密顺序的底标
            plaintext += ciphertext[offset]
            # 将密文该底标的字符添加进明文字符串中
    return plaintext
    # 函数返回加密完成后的明文


def Fence_encode_pro(input_1):
    # 定义栅栏密码的加密算法（升级版）
    plaintext = str(input_1)
    # 使用str将输入的字节转换为字符型,定义为明文
    plaintext_num = len(plaintext)
    # 统计明文总长数
    key = factor(plaintext_num)
    # 调用factor函数求得该明文的可能的密钥
    for i in key:
        # 使用for循环历遍可能的密钥列表
        key_staging = i
        # 将密钥暂存为一个值
        ciphertext_staging = Fence_encode(plaintext, key_staging)
        # 将明文和该值调用函数Fence_encode生成可能的密文
        print('当组数为', key_staging, '时,密文为:', ciphertext_staging)
        # 输出在该密钥条件下生成的密文


def Fence_decode_pro(input_1):
    # 定义栅栏密码的解密算法（升级版）
    ciphertext = str(input_1)
    # 使用str将输入的字节转换为字符型,定义为密文
    ciphertext_num = len(ciphertext)
    # 统计密文总长数
    key = factor(ciphertext_num)
    # 调用factor函数求得该密文的可能的密钥
    for i in key:
        # 使用for循环历遍可能的密钥列表
        key_staging = i
        # 将密钥暂存为一个值
        plaintext_staging = Fence_decode(ciphertext, key_staging)
        # 将密文和该值调用函数Fence_decode生成可能的明文
        print('当组数为', key_staging, '时,明文为:', plaintext_staging)
        # 输出在该密钥条件下生成的明文


def Fence():
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
            plaintext_num = len(plaintext)
            key_num = factor(plaintext_num)
            print('该明文总长度为:', plaintext_num)
            print('可使用的密钥有:', key_num)
            # 分别统计明文总长度和所有可能的密钥,并输出
            print('------------------------------')
            key = input('请输入密钥:')
            # 根据提示输入密钥
            try:
                print('------------------------------')
                ciphertext = Fence_encode(plaintext, key)
                print('密文为:', ciphertext)
                # 调用函数Fence_encode生成密文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '2':
            # 选择模式2.解密
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            print('------------------------------')
            ciphertext_num = len(ciphertext)
            key_num = factor(ciphertext_num)
            print('该密文总长度为:', ciphertext_num)
            print('可使用的密钥有:', key_num)
            # 分别统计密文总长度和所有可能的密钥,并输出
            print('------------------------------')
            key = input('请输入密钥:')
            # 根据提示输入密钥
            try:
                print('------------------------------')
                plaintext = Fence_decode(ciphertext, key)
                print('明文为:', plaintext)
                # 调用函数Fence_decode生成明文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '3':
            # 选择模式3.懒人加密
            print('------------------------------')
            plaintext = input('请输入明文:')
            # 根据提示输入明文
            print('------------------------------')
            plaintext_num = len(plaintext)
            key_num = factor(plaintext_num)
            print('该明文总长度为:', plaintext_num)
            print('可使用的密钥有:', key_num)
            # 分别统计明文总长度和所有可能的密钥,并输出
            try:
                print('------------------------------')
                Fence_encode_pro(plaintext)
                # 调用函数Fence_encode_pro生成密文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')

        elif choose == '4':
            # 选择模式4.暴力破解
            print('------------------------------')
            ciphertext = input('请输入密文:')
            # 根据提示输入密文
            print('------------------------------')
            ciphertext_num = len(ciphertext)
            key_num = factor(ciphertext_num)
            print('该密文总长度为:', ciphertext_num)
            print('可使用的密钥有:', key_num)
            # 分别统计密文总长度和所有可能的密钥,并输出
            try:
                print('------------------------------')
                Fence_decode_pro(ciphertext)
                # 调用函数Fence_decode_pro生成明文,并输出
            except:
                # 使用try和except避免整个程序意外终止
                print('未知错误!')


# 栅栏密码详细解释:https://baike.baidu.com/item/%E6%A0%85%E6%A0%8F%E5%AF%86%E7%A0%81/228209
