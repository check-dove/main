import zipfile
import itertools
import rarfile as rarfile

charsw = '1234567890'  # 先创建密码本，把所有的按键敲了一遍


l = 4  # 密码的初始长度为1
while l <= 7:  # 被破解的密码最终长度，先使用迭代创建一个密码本
    for passwords in itertools.product(charsw, repeat=l):
        passwords = ''.join(passwords)
        if passwords > '1722983' or '1700000' <= passwords <= '1701111':
            print(passwords)  # 可以使用pass直接跳过
            f = open('C:\\Users\\shuai\\Desktop\\破解\\passdict.txt', 'a+')
            password = str(passwords) + '\n'
            f.write(password)
            f.close()
    l += 1


def extractFile(rarFile, password):  # 使用rarFile库来破解密码
    try:
        rarFile.extractall(pwd=bytes(password, "utf8"))
        print("rar压缩包密码是" + password)  # 破解成功
    except:
        pass  # 失败，就跳过


def main():
    rarFile = zipfile.ZipFile('D:\\datum and some software\\baiduyunpan\\芉唫RNL\\qian.zip.rar')  # 使用的是绝对路径可以改成rar文件所在地
    PwdLists = open('C:\\Users\\shuai\\Desktop\\破解\\passdict.txt')  # 读入所有密码
    for line in PwdLists.readlines():  # 挨个挨个的写入密码
        Pwd = line.strip('\n')
        extractFile(rarFile, Pwd)


if __name__ == '__main__':
    main()