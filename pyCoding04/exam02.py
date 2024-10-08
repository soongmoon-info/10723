#최종 리스트 내용 [이름, 학번, 등급, 수학점수, 국어점수, 정보점수, 총합, 평균]
student = [['강호명','10100',36.6,67.1,55.4],   # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['양정민','10300',100,0,0],             # [이름, 학번, (국어, 정보점수 입력 안됨)]      - 점수 입력 필요
          ['이규래','10400',96.1,75.2,87.3],    # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['김묵병','10500',0,0,0],             # [이름, 학번, (수학, 국어, 정보 점수 입력 안됨)] - 점수 입력 필요
          ['박주근','10600',0,96.7,0],             # [이름, 학번, (수학, 정보점수 입력 안됨)]     - 점수 입력 필요
          ['이준동','10700',87.4,45.6,97.9]]    # [이름, 학번, 수학점수, 국어점수, 정보점수]

for stu in student:
  for i, v in enumerate(stu):
    if v == 0:
      if i == 2:
        score = '수학 점수'
      elif i == 3:
        score = '국어 점수'
      else:
        score = '정보 점수'
      stu[i]=float(input(stu[0]+' 학생 '+score+'를 입력하시오:'))


 
for getStu in student:
  getStu.append(getStu[2]+getStu[3]+getStu[4])
  getStu.append(int(getStu[5]/3))
  if getStu[2] < 30 or getStu[3] < 30 or getStu[4] < 30:
    getStu.insert(2,'F')
  elif getStu[6] >= 90:
    getStu.insert(2,'A')
  elif getStu[6] >= 80:
    getStu.insert(2,'B')
  else:
    getStu.insert(2,'C')
  print(getStu)