#최종 리스트 내용 [이름, 학번, 등급, 수학점수, 국어점수, 정보점수, 총합, 평균]
student = [['강호명','10100',36.6,67.1,55.4],   # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['이규래','10400',96.1,75.2,87.3],    # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['이준동','10700',87.4,45.6,97.9]]    # [이름, 학번, 수학점수, 국어점수, 정보점수]

for getStu in student:
  getStu.append(getStu[2]+getStu[3]+getStu[4])
  getStu.append(int(getStu[5]/3))
  if getStu[6] >= 90:
    getStu.insert(2,'A')
  elif getStu[6] >= 80:
    getStu.insert(2,'B')
  else:
    getStu.insert(2,'C')
  print(getStu)