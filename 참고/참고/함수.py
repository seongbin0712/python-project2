# 함수

# 1. 기본형 : 매개변수가 없고, return 문도 없다.

# def 함수이름():
#   명령문

def print_hello(): # 함수를 선언한다.
  print("Hello")

print_hello() # 함수 호출(실행)

# 2. 매개변수를 가지는 경우

# def 함수이름(매개변수, 매개변수.....):
#   명령문

def add(num1, num2): # num1과 num2 - 매개변수(parameter)
  print(num1 + num2)

add(3, 5) # 3, 5는 매개변수가 아닌 인수(argument)

# 3. 매개변수는 없고, return 문만 있는 경우 : 굉장히 드물다.

# def 함수이름():
#   명령문
#   return 값

def func():
  return "Hello"

result = func()
print(result)

# 4. 매개변수도 있고, return문도 있는 경우

# def 함수이름(매개변수, 매개변수.....):
#   명령문
#   return 값

def calc(x, y):
  result = x * y
  return result

rtn = calc(7, 6)
print(rtn)

# =============================================================================== #

# 매개변수의 수가 정해지지 않을 경우
total2 = 0

def sum(*args):
  # print(args) -> 입력한 인수가 튜플 형태로 나온다
  total = 0
  for i  in args:
    total += i
  return total