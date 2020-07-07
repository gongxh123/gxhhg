# sl = [20,35,84,56,96,75,23,48,60,57,82]
# for s in sl:
#     if (s >= 0 and s < 60):
#         print('不及格')
#     elif (s >= 60 and s < 70):
#         print('及格')
#     elif (s >= 70 and s <= 100):
#         print('良好')
#     else:
#         print('请输入正确的成绩')

# f = int(input('请输入成绩'))
# if (f >= 0 and f < 60):
#     print('不及格')
# elif (f >= 60 and f < 70):
#     print('及格')
# elif (f >= 70 and f < 80):
#     print('良好')
# elif (f >= 80 and f < 100):
#     print('优秀')

# a=1
# for c in range(10,0,-1):
#     a *= c
# print(a)

# flag = True
# g = 72
# while flag:
#     b = int(input('请输入数字'))
#     if b < g :
#         print('小')
#     elif b > g :
#         print('大')
#     else:
#         print('恭喜猜对了')
#         flag = False


# for a in range(1,100):
#     if a // 10 == 1:
#         continue
#     print(a)

# for a in range(1,100) :
#     if a % 6 != 0 :
#         continue
#     print(a)

# a = 10
# b = 20
# print(a,'**2','+',b,'**2','+','2','*',a,'*',b)

# def g(a,b) :        # 方法定义
#     print(a % b , a // b)   #a,b 形参
#     # print(a // b)
# g(60 , 30)       #方法调用  60 30实参
# g(60 , 15)

# def g(a , b):
#     if b == 0 :
#         print('请输入正确的参数')
#     else:
#         print('商为:',a % b,'余为:',a // b)
# g(30 , 20)


# def g(a , b):
#     if (b == 0) :
#         return None
#     else:
#         return (a % b , a // b)
# res = g(b = 20 ,a = 30)
# if res is None:
#     print('b不能为空')
# else:
#     print('商是:',res[0],'余是:',res[1])

# def g(a,b,c = 20):
#     return a // b +c
# print(g(40,20))

# def sd(*args): # *args接收动态位置参数  **kwargs接收动态关键字参数
#     s = 0
#     for a in args :
#         s += a
#     return s
# print(sd(456454,54545465,4456465))


# 面向对象
# class calc():
#     g = None
#     x = None
#     jg = None
#     def input(self,g,x):
#         self.g = g
#         self.x = x
#     def jia(self):
#         self.jg = self.g + self.x
#     def chu(self):
#         self.jg = self.g / self.x
#     def get_result(self):
#         print(self.jg)
# h = calc()
# h.input(20,30)
# h.jia()
# h.get_result()
# h.chu()
# h.get_result()


# class calc():
#     jg = None # 类的所有实例共享
#     def __init__ (self,g,x):  # 魔法函数，类实例化的时候调用，又称构造方法
#         self.g = g
#         self.x = x
#     def jia(self):
#         self.jg = self.g + self.x
#     def chu(self):
#         self.jg = self.g / self.x
#     def get_result(self):
#         print(self.jg)
# c = calc(30,13)  #通过对象操作实例变量  类变量通过类名操作
# c.jia()
# c.get_result()


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'x',i,'=',i*j,end='\t')
#     print()

# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(j,'x',i,'=',i*j,end='\t')
#     print()


# l = [123,156,2,156,45647,894,25,45,4123,456,74,564,89,4756,4,56847,65,746,54,89,4894,895,487,489,4]
# length = len(l)
# for i in range(length,1,-1):
#     for j in range(1,i):
#         if(l[j-1] > l[j]):
#             l[j-1],l[j] = l[j],l[j-1]
# print(l)


# l = [123,156,2,156,45647,894,25,45,4123,456,74,564,89,4756,4,56847,65,746,54,89,4894,895,487,489,4]
# length = len(l)
# for i in range(length-1,0,-1):
#     for j in range(i):
#         if(l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)



# def sd(*args): # *args接收动态位置参数  **kwargs接收动态关键字参数
#     s = 0
#     for a in args :
#         s += a
#     return s
# print(sd(456454,54545465,4456465))

# def sd(*args,**kwargs): # *args接收动态位置参数  **kwargs接收动态关键字参数
#     print(args)
#     print(kwargs)
#     return 10
# print(sd(456454,54545465,4456465,'字符串'))

# a = [456,456,489,65,456,4,4,564,564,23,123,489,4897,98,42,132,489,45,12,48,456,1]
# length = len(a)
# print(length)
# for i in range(length-1,0,-1):
#     for j in range(0,i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# a = [456,456,489,65,456,4,4,564,564,23,123,489,4897,98,42,132,489,45,12,48,456,1]
# length = len(a)
# print(length)
# for i in range(length,1,-1):
#     for i in range(1,i):
#         if a[i-1] > a[i]:
#             a[i-1],a[i] = a[i],a[i-1]
# print(a)

# class aaa():
#     money = '公有变量'
#     __lao_pop = '私有变量'
#     _yi_fu = '私有变量2'
#
# print(aaa.money)
# print(aaa._yi_fu)

# class Parent():
#     money = '10000000000'
#     _renti_shousi = '王多鱼'
#     __zu_qiu = '盖了帽了我的老北鼻'
#     def __init__(self,a):
#         self.a = a
#
#     def zican(self):
#         house = 300
#         _zi_can = '300亿'
#         print(house)
#         print(_zi_can)
#
# class Child(Parent):
#     ai_hao = '打游戏'
#     def __int__(self,a,*args,**kwargs):
#         super().__int__(a,*args,**kwargs)
#     def zican(self):
#         super().zican()
#         print('秽土转生')
# c = Child(123)
# print(c.ai_hao)
# print(c.money)
# print(c._renti_shousi)
# print(c.zican())





