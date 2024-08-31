# 변수의 type 변환

a = 123
print(a, type(a)) # 정수

a = "Python"
print(a, type(a)) # 문자열

a = [1, 2, 3]
print(a, type(a)) # 리스트

a = (1, 2, 3)
print(a, type(a)) # 튜플

a = set([1, 2, 3]) # set type 만들기 (값이 중복되지 않도록 함) / set은 인덱스가 없다 = 순서가 없다 = 인덱싱 불가
                   # a = list(a) => set type를 list type로 변환하여 인덱싱 할 수 있음
print(a, type(a))

a = (1 == 2) # bool
print(a, type(a)) # 다른 방법 : print(bool(1 == 2), type(a))

a = {
  "firstName" : 'John',
  "lastName" : "Doe"
}                      # dict(딕셔네리)

# 위(a)의 type

# <class 'int'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'bool'>
# <class 'dict'>