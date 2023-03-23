#1
def sum(a, b):
    return a+b
s=sum(2, 3)
print(s)

#2
def sub(a,b):
    return a-b
s= sub(3,2)
print(s)

#3
def mul(a,b):
    return a*b
s= mul(2,4)
print(s)

#4
def div(a,b):
    return a/b
s=div(4,2)
print(s)

#5
def distance(x1,x2,y1,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
s=distance(1,4,2,6)
print(s)

#6
s = "beside you"
print(s[0:10])

#7
s = "python"
print(s[-1:-7:-1])

#8 
n = input('이름을 입력하세요 : ')
h = input('취미를 입력하세요 : ')
s = input('재학 중인 학교를 입력하세요 : ')
b = str(input('생일을 입력하세요 : '))
print('제 이름은 %s입니다. 취미는 %s입니다. 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다.' %(n, h, s, b[2:4], b[4:]))

#9
a_str = input('첫 번째 수를 입력하세요 : ') 
b_str = input('두 번째 수를 입력하세요 : ') 
a = int(a_str)
b = int(b_str)
print('두 수의 합 : ', a+b)
print('두 수의 차 : ', a-b)
print('두 수의 곱 : ', a*b)
print('두 수의 몫 : ', a%b)