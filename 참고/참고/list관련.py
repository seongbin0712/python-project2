# 리스트 관련 함수

# 1. 리스트 추가
# append(), insert()

# append(값) : 리스트의 맨 마지막에 값을 추가
# insert(인덱스, 값) : 인덱스 위치에 값을 추가

a = [1, 2, 3, 4]

a.append(5) # a = [1, 2, 3, 4, 5]
a.insert(2, 6) # a = [1, 2, 6, 3, 4, 5]

# 2. 리스트 수정 : 인덱스를 사용

b = [1, 2, 3, 4]

b[1] = 5 # b = [1, 5 ,3, 4]

# 3. 리스트 삭제
# index - del, 값 - remove()

# del : 인덱스를 사용한다.
# remove() : 값을 사용한다.

c = [1, 2, 3, 4]

del c[2] # c = [1, 3, 4]
c.remove(3)   # 지우고자하는 값을 전달한다.
              # c = [1, 2, 4]