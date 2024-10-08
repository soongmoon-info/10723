# 전체 학생 list: [이름, 학번, 수학점수, 국어점수, 정보점수]
student = [['강호명','10100',36.6,67.1,55.4],  
          ['이규래','10400',96.1,75.2,87.3],
          ['이준동','10700',87.4,45.6,97.9]]



# 추가 입력하려는 학생의 이름, 학번, 수학 점수, 국어 점수, 정보 점수를 입력하는 함수
def inputStu():
  new_student=[input('학생 이름 입력:'),input('학생 학번 입력:'),float(input('수학 점수 입력:')),float(input('국어 점수 입력:')),float(input('정보 점수 입력:'))]
  student.append(new_student)
  # !!코드 입력 필요!!



# 학생 한 명씩 출력하는 함수
def printStu(s):
  for stu in s:
    print(stu)
  
  # !!코드 입력 필요!!



# 학생들의 성적의 총합, 평균, 등급을 연산하는 함수
def calcStu(setList: list):
    for getStu in setList:
        if len(getStu) < 8:  # 이미 계산된 경우를 방지
            total = getStu[2] + getStu[3] + getStu[4]  # 총합 계산
            avg = total / 3  # 평균 계산
            getStu.append(total)  # 총합 추가
            getStu.append(avg)  # 평균 추가

            # 등급 결정
            if getStu[2] < 30 or getStu[3] < 30 or getStu[4] < 30:
                grade = 'F'
            elif avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            else:
                grade = 'C'
            getStu.insert(2, grade)  # 등급 삽입
    return setList
  
#(매개변수:자료형)이런 형식으로 매개변수의 자료형을 미리 알려줄 수 있다.
  
  
  
 
  # !!코드 입력 필요!!



# main: 프로그램의 실행 시작.
print('<학생 성적처리 프로그램 v0.1.0>')
print('-'*50)
calcStu(student)
# !!코드 입력 필요!!: list에 입력된 학생들의 성적을 calcStu함수를 통해 연산
print('DB에 입력된 학생의 성적 처리가 완료되었습니다.')

while True:
  answer = input('학생을 추가 입력 하시겠습니까? (Y/N):')
  if answer == 'Y' or answer == 'y':
    inputStu()
    calcStu(student)
    # !!코드 입력 필요!!: inputStu함수에서 반환받은 리스트를 student리스트에 추가
    # !!코드 입력 필요!!: 새로 추가한 리스트의 총합, 평균, 등급을 calcStu함수를 통해 연산
    continue
  elif answer == 'N' or answer == 'n':
    printStu(student)
    # !!코드 입력 필요!!: 전체 학생을 printStu를 통해 출력
    break
  else:
    print('잘못된 입력입니다.')
