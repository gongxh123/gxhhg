#
#
# a = 123456132
# b = '56489123'
# print(a+int(b))
# print(str(a)+b)
#
# c = [21,584,8,51,564,8,45,641,3548,4,56,8] # list转列表 tuple转元祖 set转集合 int转整数 str转字符串  字符串能转列表，列表不能强转字符串
# print(list(b))
# print(tuple(c))
# print(set(c))
# print(tuple(set(c)))

# 打开模式：r 读取 w清空写入 a追加写入 b二进制模式
# f = open('gxhhs.txt','w',encoding='utf-8')
# f.write('156715615')
# f.write('贡绪豪好帅')
# f.close()

# f = open('gxhhs.txt','w')  #  open打开文件
# f.write('gxhhs\sadasdsa\dadsadsa\n') #  写入内容至打开文件
# f.writelines(['gxhhs\n','sadasdsa\n','dadsadsa\n'])
# print(f.writable()) # 判断是否可写
# f.close()  # 关闭文件

# f = open('gxhhs.txt','r')
# print(f.read())  #  默认读取全部数据
# print(f.read(10))  #  读取指定大小的数据
# print(f.readline())  #  按行读取，读取一行
# print(f.readlines())  #  按行读取，读取所有行
# f.close()


# a = 'asjdkjahsdlkhgsjdahldkasd'
# print(a[2])
# print(a[-1:0:-1])
# print(a[1:-1:1])
# print(a[1::])
# print(a[:-1:])
# print(a[::])
# print(a[:7:-1])

# f = 'aaaaa.4444'
# f = '  aaaaa , bbbbbbb '
# print(f.strip())
# print(f.lstrip())
# print(f.rsplit())
# print(f.split(","))  #  切片
# f = f.replace(".",",")  #  替换
# print(f)
# print(f.find('.'))   #  查找

# with open('gxhhs.txt','r') as f:
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace('\n',''),end ='\n')

# for i in range(1,10):
#     for j in range(1,i+1):
        # print(j,'x',i,'=',i*j,end='\t')
        # print('%d X %d = %d'%(j,i,i*j), end='\t')
        # print('{} X {} = {}'.format(j,i,i*j), end='\t')
    # print()

# l = [4,4,484,48,15,4,44,45,56,44,45,]
# l[10] = 12
# print(l)
# l[0:-1] = 12,5,3,7,8,9,4,5,6,65
# print(l)

# l = []
# l.append('上海胡歌分哥')
# l.append('重庆吴彦祖分组')
# l.append('多重影分身之术')
# l.extend(('就是我','g','x','h'))
# print(l)


# l = [1,2,3,5,4,5,8,8,4,657,8,45,465,4]
# print(l.pop())
# print(l)
# print(l.pop(5))
# print(l)

# python  True 1  false 0
# l = [1,2,8,6,7,9,3,5,65,2,3,1,6]
# l.remove(2)
# print(l)

# l = [True,0,1,2,4,8,6,7]
# l.remove(1)
# print(l)

# l = []
# print(l)
# l.clear()
# print(l)

# l = [12,5,6,7,874,1,3,8,7,89,4,6]
# l.sort(reverse=True)
# l.sort(reverse=False)
# print(l)

# d = {"name":"小明","age":18,"sex":"男"}
# for key in d:
#     print(d[key])
# for k,v in d.items():
#     print(k,'=',v)
# d.update({'addr':'上海闵行','学历':'博士'})
# print(d)
# print(d.pop('addr'))
# print(d)


# s = {}
# for key in d:
#     if key == 'addr':
#         continue
#     s[key] = d[key]
# print(s)

# try:
#     f = open('aaa.txt','r')
#     print(f.read())
#     f.close()
# except FileNotFoundError as f:
#     print('文件不存在，请重新创建一个为aaa的文件')
#     print(f)


# def div(a ,b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         print(e)
# print(div(2,0))



# def div(a,b):
#     if a/b:
#         print(div)
# div(10,0)
# print(div)

# def div(a ,b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         return
#     else:
#         print('执行else代码')
#     finally:
#         print('执行finally代码')
# div(2,0)

# class CustomException(Exception):
#     def __init__(self,value = '值不能为0'):
#         self.value = value
#
#     def __str__(self):
#         return self.value
# a = 0
# try:
#     if a == 0:
#         print('a = {} 触发异常'.format(a))
#         raise CustomException
#     print('a = {} 未触发异常'.format(a))
# except CustomException as e:
#     print(e)