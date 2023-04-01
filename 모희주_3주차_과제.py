# 1번 
def grade (num):
    if 90 <= num <= 100:
        return "A"
    elif 80 <= num < 90:
        return"B"
    elif 70 <= num < 80:
        return"C"
    elif 60 <= num < 70:
        return"D"
    else: 
        return"F"
print(grade(94))
print(grade(64))
print(grade(34))

#2번 
def quadrant(x,y):
    if x>0 and y>0:
        return "제 1사분면"
    elif x<0 and y>0:
        return "제 2사분면"
    elif x<0 and y<0:
        return "제 3사분면"
    else:
        return  "제 4사분면"
print(quadrant(1, 3))
print(quadrant(-1, 3))
print(quadrant(-1, -3))
print(quadrant(1, -3))

# 3번 
def leapyear (year):
    if year % 4 == 0 :
        if year % 400 == 0 or year % 100 != 0:
            return "윤년입니다."   
        else: 
            return "윤년이 아닙니다."
    else: 
        return "윤년이 아닙니다."
print(leapyear(2024))
print(leapyear(1900))
print(leapyear(2000))
print(leapyear(2023))

# 4번
def dice(a, b, c):
    if a == b == c:
        return 10000 + a * 1000
    elif a == b or a == c:
        return 1000 + a * 100
    elif b == c:
        return 1000 + b * 100
    else:
        return max(a, b, c) * 100
print(dice(3,3,6))
print(dice(2,2,2))
print(dice(6,2,5))

# 5번 
def alarm (time):
    time = str(time)
    if time[:-2] == "" and 45 <= int(time[-2:]) <=59:
        return "%d시 %d분" %(00, int(time[-2:])-45)
    elif time[:-2] == "":
        return "%d시 %d분" %(23, int(time[-2:])+15)
    elif 45 <= int(time[-2:]) <= 59:
        return "%d시 %d분" %(int(time[:-2]), int(time[-2:])-45)
    else:
        return "%d시 %d분" %(int(time[:-2])-1, int(time[-2:])+15)
print(alarm(900))
print(alarm(30))
print(alarm(2315))
print(alarm(1050))