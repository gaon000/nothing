#성적표 파일 생성
import random

a = open('score.txt', 'w')
for i in range(80):
    a.write("%d \n"%random.randint(0,100))
a.close()