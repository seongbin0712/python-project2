# 카페메뉴 관리는 다음과 같은 기능을 구현한다.

# 1. 메뉴를 출력(화면) 기능
# 2. 메뉴를 추가하는 기능
# 3. 메뉴를 삭제하는 기능
# 4. 메뉴 이름 변경 기능
# 5. 종료


# 위 기능이 반복 실행될 수 있도록 한다.
# 사용자에게 메뉴를 보여주고, 사용자가 기능을 선택하여, 실행될 수 있도록 한다.

# 리스트를 사용한다. (추가, 삭제, 수정)

menu = ["1. 사과", "2. 당근", "3. 망고"]
play = True

while play:
  func = """
  ====== 관리자 모드 ======
    1. 메뉴 출력
    2. 신메뉴 추가하기
    3. 메뉴 삭제하기
    4. 메뉴 이름 바꾸기
    5. 관리자 모드 종료하기
  """

  user = int(input("관리 기능 선택 : "))
  print()

  if user == 1:
    for i in menu:
      print(f"{i} 쥬스")

  elif user == 2:
    print(menu)
    new_menu = input("추가할 메뉴 입력 : ")
    menu.append(new_menu)

  elif user == 3:
    print(menu)
    remove_menu = int(input("삭제할 메뉴 선택 : "))
    menu.remove(remove_menu)

  elif user == 4:
    idx = 0
    exist_menu = int(input("수정 할 메뉴 선택 : "))
    for i in menu:
      if i == exist_menu:
        break
      idx += 1
    new_menu = input("새로운 메뉴 입력 : ")
    menu[idx] = new_menu

  elif user == 5:
    play = False

  else:
    print("잘못된 선택입니다.")
    play = False