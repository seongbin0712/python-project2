# 행맨 : 무작위의 특정 단어의 알파밧엘 맞추는 게임
# 매번 임의 알파벳을 입력하고, 단어에 해당 알파벳이 있으면 표시해준다.


import random

#  등록 단어
eng_words = ["puppy", "kitten", "happy"]

# 컴퓨터가 단어를 선택
answer = random.choice(eng_words)
# 정답 단어의 글자수를 '_'로 화면에 표시
guess_letter = list("_" * len(answer))

life = 3
play = True

while play:
  print(f"남은 기회 : {life}번")

  # 통상적으로 알파벳은 소문자로 비교한다. => lower() 함수 사용
  user_guess = input("한 글자씩 추측을 해보세요  : ").lower()

  # 입력한 문자의 길이가 1 이거나, 또는 알파벳이면 =>
  if len(user_guess) == 1 and user_guess.isalpha():
    # 정답 단어에서 사용자가 입력한 문자가 있으면, 문자로 채운다.
    for i in range(len(answer)):
      if answer[i] == user_guess:
        guess_letter[i] = user_guess
    print(guess_letter)

    # 정답을 판별 : guess_letter에 "_"가 없으면, 정답이다.
    if "_" not in guess_letter:
      play = False
      print("성공입니다.")

    if user_guess not in answer:
      life -= 1
      if life == 0:
        play = False
        print(f"실패입니다. 정답은 {answer}입니다.")
  else:
    print("영문 알파벳을 한자씩 입력하세요.")