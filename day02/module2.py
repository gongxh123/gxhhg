# from day02 import module1
# from day02.module1 import a as module1_a,name as module1_name,Test as module1_Test
# from day02.module1 import a,name,Test
# print(module1.a)
# print(module1.name())
# print(module1.Test.name)



a = '我是模块变量2中的a变量'



def name():
    print('我是模块2中的name方法')


class Test:
    name = '我是模块2中的Test类'
if __name__ == '__main__':
    name()
    print(Test.name)
# print(module1_a)
# module1_name()
# print(module1_Test.name)