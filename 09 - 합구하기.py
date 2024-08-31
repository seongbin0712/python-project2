# 1. 숫자의 범위(시작값, 종료값)를 입력하고
# 2. for문과 range함수를 사용해서 그 범위의 수를 모두 합한다.

user_input = input("시작값과 종료값을 입력하세요. : ")
my_list = user_input.split(" ")

start, end = my_list # 언팩킹 ['시작값', '종료값']

start = int(start)
end = int(end)

total = 0

for val in range(start, end + 1):
  total += val

print(f"{start}에서 {end}까지의 합은 {total} 입니다.")