#조건물
a = 10
if a < 50:
  print('조건이 T일 경우 출력')

#키를 입력받아 루저를 출력하라
height = float(input('키를 입력하시오:'))
if height <= 140 :
  print('루저~')
else:
  print('루저 아님')
  
# battery = int(input('배터리 잔량:'))
# if battery > 10:
#   print('기기를 작동합니다')
# elif battery > 0:
#   print('충전이 필요합니다!')
# else:
#   print('전원이 꺼집니다!')
battery = int(input('배터리 잔량'))
if battery <= 0:
  print('종료')
elif battery <= 10:
  print('충전을 해주세요')
elif battery <= 20:
  print('저전력 모드')
else:
  print('정상작동중')
  
# 논리 연산자
# 티어가 브론즈이면서 채피언이 야스오면 과학자 출력
tier = '브론즈'
Champ = '야스오'
if tier == '브론즈' and Champ == '야스오':
  print('과학자')

#포함연산자
call = input('-없이 전화번호 입력:')
if '-' in call :
  print('-를 제외하고 입력해주세요.')

