import os
print("一元二次方程求解计算器")
print("ax^2+bx+c=0")
print("开发者信息：\n鼎天网络\nDTNETWORK\nGary Chan")
print("感谢使用")
import math
a1 = input("a=")
b1 = input("b=")
c1 = input("c=")
a4 = int(a1)
b4 = int(b1)
c4 = int(c1)
x1 = ( - b4 + ( b4 ** 2 - 4 * a4 * c4 ) ** ( 1/2 ) ) / 2 * a4
x2 = ( - b4 - ( b4 ** 2 - 4 * a4 * c4 ) ** ( 1/2 ) ) / 2 * a4
print( x1 , x2 )
e = "单击任意键退出"
print(e)
os.system("pause")