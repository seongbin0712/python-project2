# 만약에 입력값을 여러개 받을 때

# 1.  문자열을 여러개 받을 때

# 2. int, float값을 여러개 입력 받을 때
# user_input = input("문자열을 3개 입력하세요. : ")
# my_list = user_input.split(" ")
# print(my_list, type(my_list))

# 리스트의 언팩킹을 사용
# red, blue, yellow = my_list

# print(red)
# print(blue)
# print(yellow)
# 
# 리스트의 인덱싱을 사용
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

#

# 2. int, float값을 여러개 입력 받을 때
user_input = input("정수를 3개 입력하세요. : ")
my_list = user_input.split(" ")
print(my_list, type(my_list))

# 리스트의 언팩킹을 사용
red, blue, yellow = my_list
 
print(int(red))
print(int(blue))
print(int(yellow))
 
# 리스트의 인덱싱을 사용
print(int(my_list[0]))
print(int(my_list[1]))
print(int(my_list[2]))

# 3. 정수와 문자열을 동시에 입력 받을 때 : 각 값을 필요에 따라서 필요애 따라 형변환을 해준다.

user_input = input("금화와 동화를 입력하세요. : ")
my_list = user_input.split(" ")

달러, 통화 = my_list

달러 = int(달러)
통화 = int(통화)