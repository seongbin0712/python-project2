dic_eng = {
  "apple" : "사과",
  "peach" : "복숭아",
  "mango" : "망고"
}

for i in dic_eng:
  print(i)

for i in dic_eng.values():
  print(i)

# 딕셔너리의 속성 추가

dic_eng["banana" ] = "바나나"

print(dic_eng)

# 딕셔너리의 속성 삭제

del dic_eng["banana"]
print(dic_eng)

# 딕셔너리의 값 수정

dic_eng["apple"] = "큰 사과"
print(dic_eng)

word = 'python'

result = list("_" * len(word))
print(result)

# 어떤 문자가 알파벳인지, 숫자인지 판별 법
# isalpha(), isdigit()
# isalnum() : 알파벳 혹은 숫자 인지를 판별