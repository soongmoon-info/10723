score = float(input('수학점수를 입력하시오:'))
score = float(input('정보점수를 입력하시오:'))+score
score = float(input('국어점수를 입력하시오:'))+score
print('총합:',score)
print('평균:',score//3)
average = score/3
if average >= 90:
  print('등급 : A')
elif average >= 80:
  print('등급 : B') 
else:
  print('등급 : C')