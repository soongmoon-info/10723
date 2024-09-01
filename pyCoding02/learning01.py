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
  
battery = int(input('배터리 잔량:'))
if battery > 10:
  print('기기를 작동합니다')
elif battery > 0:
  print('충전이 필요합니다!')
else:
  print('전원이 꺼집니다!')