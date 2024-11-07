# 이름: 전승현
# 학변: 10723
# 주제: 이진수를 십진수로 바꾸는 함수
def to_Binary(num):             #십진수를 이진수로 바꾸는 함수, num은 입력받은 값을 대입할 매게변수
  Num=""                           #Num은 이진수 값을 저장할 변수
  if num!=0:                       #입력받은 값이 0이 아닐 때
    while num>=1:                  #num이 1이상일때 반복문
      Num=str(num%2)+Num           #숫자를 2로 나눈 후 나머지를 계속 문자열로 바꾼후 더함
      num=num//2
    print(Num)
  else:                             #num이 0일때는 0을 출력
    print(0)
  return(Num)                   #Num을 반환

kiss=int(input('숫자를 입력하시오'))  #입력받을 수를 저장하는 변수 kiss
to_Binary(kiss)                           #함수를 호출




