# BMI 계산
# 1. BMI 산정 기준을 화면에 출력해준다.
# 2. 사용자로 부터 키를 입력 받는다. (Cm)
# 3. 사용자로 부터 몸무게를 입력 받는다. (Kg)
# 4. BMI 지수를 계산해준다. : BMI = 몸무게 / (키의 제곱) * 10000
# 5. 결과 판정 : 계산한 BMI를 가지고, 저체중, 정상, 과체중, 비만 중 결과 출력

# 힌트 :
# bmi, height, weight

info = """
        - Bmi 판정 기준 -

  18.5 미만          : 저체중
  18.5 ~ 22. 9       : 정상
  23 ~ 24.9         :  과체중
  24.9 초과          : 비만
"""

print("+" * 50)
print("Bmi (체질량지수)계산.")
print("+" * 50)

print(info)

# 입력 받기

height = float(input("키를 입력하세요. (Cm) : "))
weight = float(input("몸무게를 입력하세요. (Kg) : "))

Bmi = weight / (height * height) * 10000

print()
result = ""
if Bmi < 18.5:
  result = "저체중"
elif Bmi < 23:
  result = "정상"
elif Bmi < 25:
  result = "과체중"
else:
  result = "비만"

print(f"당신의 Bmi 지수는 {Bmi : .2f}입니다. 따라서, '{result}'입니다.")