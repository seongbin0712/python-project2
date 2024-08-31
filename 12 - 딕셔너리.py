# 반복 검색이 가능하도록 한다.
# '단어 검색을 종료하시겠습니까? (y),

search = True

dic_eng = {
  "apple" : "사과",
  "peach" : "복숭아",
  "mango" : "망고"
}

while search:

  user_input = input("검색할 영어 단어 입력 : ")

  if user_input in dic_eng:
    print(f"검색 단어 : {user_input}, 뜻 : {dic_eng[user_input]}")
  else:
    print("검색하고자 하는 단어가 없음.")
    
  word_stop = input("단어 검색을 종료하시겠습니까? (y) : ")

  if word_stop == 'y':
    search = False
  else:
    print("검색을 계속 진행합니다.\n")