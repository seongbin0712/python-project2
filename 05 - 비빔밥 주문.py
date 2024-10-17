# 비빔밥 주문하기

# 1. 메뉴를 보여준다.
# 2. 메뉴에는 set가 존재한다. set를 시키면 3000원을 더한다.
# 3. 주메뉴를 주문받고, 추가적으로 set를 주문할 것인지를 묻는다.
# 4. 주문에 따라서, 주문 금액을 계산하여, 사용자에게 출력해 준다.

# 힌트 (비빔밥 가격)
# 불고기 : 12900, 야채 : 8000, 전주 : 10000, set : + 3000원 추가 (밥, 반찬 추가)
# 시작 전 하는 방식 정하기 (문자열 or 숫자) + 효율적인 코드 (simple)

menu = """
-----------------------------------------------------------
                 - 비빔밥 메뉴 -

      불고기 비빔밥 : 12900원 / set : 15900원
      야채 비빔밥   : 8000원  / set : 11000원
      전주 비빔밥   : 10000원 / set : 13000원
-----------------------------------------------------------
"""

print(menu)

order = input("무슨 비빔밥을 주문하시겠습니까? (불고기, 야채, 전주) : ")


