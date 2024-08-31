# for문

# for문의 기본 형태

# for 변수 in 반복 가능한 값:
#   명령문
#   명령문

#   반복 가능한 값 : list, tuple, string, dict(딕셔너리)

# 리스트 
a = [1, 2, 3, 4]

for val1 in a:
  print(val1)

# 다른 방법

for val2 in [1, 2, 3, 4]:
  print(val2)

# 딕셔너리
person = {
  "firstname" : "John",
  "Secondname" : "Doe",
  "age" : 17
}

# 딕셔너리를 for문으로 그냥 반복하면, 변수에 key값이 주어진다.
for val3 in person:
  print(val3) # key값을 출력
  print(person[val3]) # value값을 출력

# range(시작값, 종료값, step) : 주어진 범위의 값을 생성하는 함수
# 시작값 : 시작값
# 종료값 : 종료값은 포함되지 않음. 종료값 앞까지
# step : 건너 뛰기, 값이면, 뒤에서부터

a1 = range(0, 10)
print(list(a))
print(tuple(a))

for val4 in range(0, 10):
  print(val4)
  print(val4, end=" ")

# 1부터 10까지 홀수만 출력하라.

for val5 in range(0, 11):
  if val5 % 2 == 1:
    print(val5)

for val5 in range(0, 11, 2):
  print(val5)

# 1에서 10까지 짝수만 출력하라.
for val5 in range(2, 11, 2):
  print(val5)

# 다른 예제

b = ["one", "two", "three", "four", "five", "six"]
#len(b) = [0, 1,      2,      3,      4,      5]
for val7 in range(len(b)): # len b 에는 6이 된다.
  if val7 % 2 == 0:
    print(a[val7])