# 1번
def sum(a, b):
    return a+b
s=sum(2, 3)
print(s)

# 2번
def sub(a,b):
    return a-b
s= sub(3,2)
print(s)

# 3번
def mul(a,b):
    return a*b
s= mul(2,4)
print(s)

# 4번
def div(a,b):
    return a/b
s=div(4,2)
print(s)

# 5번
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
s=distance(1,2,4,6)
print(s)

# 6번
def title(): 
    lylics = "Switch sides and I'm beside you."
    lylics = lylics[21:-1]
    return lylics
print(title())

# 7번
def reverseStr(string):
    return string [::-1]
s = reverseStr("string")
print(s)

# 8번
def introduce():
    intro = "제 이름은 %s입니다. 취미는 %s입니다. 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다." 
    intro = intro %(a,b,c,d,e)
    return intro
a = input("이름을 입력하세요 : ")
b = input("취미를 입력하세요 : ")
c = input("재학 중인 학교를 입력하세요 : ")
k = input("생일을 입력하세요 : ")
d = k[2:4]
e = k[-2:]
print(introduce())

# 9번
def calc():
    c = "두 수의 합 : %d \n두 수의 차 : %d \n두 수의 곱 : %d \n두 수의 몫 : %d"
    c = c %(a+b, a-b, a*b, a%b)
    return c
a_str = input('첫 번째 수를 입력하세요 : ') 
b_str = input('두 번째 수를 입력하세요 : ') 
a = int(a_str)
b = int(b_str)
print(calc())