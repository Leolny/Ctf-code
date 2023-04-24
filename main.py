from cipher.Caesar import Caesar
from cipher.Fence import Fence
from cipher.Vigen import Vigen
from cipher.Morse import Morse

if __name__ == '__main__':
    print('欢迎使用该脚本程序!')
    choose = ''
    # 创建储存用户输入的字符串
    while choose != 'q':
        print('------------------------------')
        choose = input('请选择模式:1.密码模块 q.退出程序:')
        # 使用while进行死循环,除非用户输入'q',并让用户选择模式

        if choose == '1':
            # 选择模式1.密码模块
            choose_cipher = ''
            # 创建储存用户输入的字符串
            while choose_cipher != 'q':
                print('------------------------------')
                choose_cipher = input(
                    '请选择模式:1.摩斯密码 2.栅栏密码 3.凯撒密码 4.维吉尼亚密码 q.返回上一级:')
                # 使用while进行死循环,除非用户输入'q',并让用户选择模式

                if choose_cipher == '1':
                    Morse()
                    # 选择模式1.摩斯密码，并调用Morse函数

                elif choose_cipher == '2':
                    Fence()
                    # 选择模式2.栅栏密码，并调用Fence函数

                elif choose_cipher == '3':
                    Caesar()
                    # 选择模式3.凯撒密码，并调用Caesar函数

                elif choose_cipher == '4':
                    Vigen()
                    # 选择模式4.维吉尼亚密码，并调用Vigen函数
