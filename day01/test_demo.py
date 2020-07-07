a = 16
b = 6
print(a + b)

# python 靠缩进识别代码块，一个代码块是一个整体
# 压缩赋值
a = 1,2,3,4,5,6
x = '贡','绪','豪','好','帅'
print(a)
print(x)

# 解包
g,v,h,s = ['贡','绪','豪','帅']
print(g)
print(v)
print(h)
print(s)

j,k,*l = a
print(j)
print(k)
print(l)

g = 98
x = 6
print(g + x)
print(x - g)
print(g % x)
print(g // x)
print(g / x)
print(g**x)

print(g == x and 4 == 4)
print(g == x or 4 == 4)
print(g != x and 4 == 4)
print(g == x and 4 != 4)
print(g != x and 4 != 4)
print(g > x)
print(g != x and 4 == 4)
print (not g != x and 4 != 4)
a = 'sadfdgs'
print('s' in a)
print('s' not in a)
b = 1,2,3,4,5,6
print(4 in b)
c = {'name': '贡绪豪','手机号': '13023248465'}
print('name' in c)

s = 14561234
print(s % 10)
s //= 10
print(s % 10)


s = 156432156
s //= 100
print(s % 10)


f = int(input('请输入成绩'))
if (f >= 0 and f < 60):
    print('不及格')
elif (f >= 60 and f < 70):
    print('及格')
elif (f >= 70 and f < 80):
    print('良好')
elif (f >= 80 and f < 100):
    print('优秀')
