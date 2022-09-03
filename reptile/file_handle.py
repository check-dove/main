import os
from os import linesep

filename = 'file_IO.txt'
path = 'C:\\Users\\shuai\\Documents\\temp'
path2 = 'D:\\liushuai\\9、project\\pythonProject\\storage'


class data_storage(object):
    def __init__(self):
         if not os.path.exists("{}".format(path2)):
             fp = open('{1}\\{0}'.format(filename, path2), 'w+')
             fp.close()

    def file_output(self, meta):
        f = open('{1}\\{0}'.format(filename, path2), 'a+')
        f.write(meta+linesep)
        f.close()


if __name__ == '__main__':
    kil = "asdjfjhkalsdjf"
    kl = data_storage()
    kl.file_output(kil)