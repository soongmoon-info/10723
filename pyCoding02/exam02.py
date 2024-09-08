math = float(input('수학 점수:'))
language = float(input('국어 점수:'))
info = float(input('정보 점수'))
print('총합:', math+language+info)
print('평균 점수',(math+language+info)/3)
average = math+language+info/3
if math < 30 or language < 30 or info < 30:
  print('등급 : F')
elif  average >= 90:
  print('등급 : A')
elif average >= 80:
  print('등급 : B') 
else:
  print('등급 : C')