from datetime import datetime
from zoneinfo import ZoneInfo
import random

now_korea=datetime.now(ZoneInfo("Asia/Seoul"))

hour = now_korea.hour
minute = now_korea.minute


correct_answer = []

def date_question():
    year = now_korea.year
    month = now_korea.month
    day = now_korea.day

    your_month,your_day = map(int, input("오늘은 몇월 몇일인가요?").split())

    if your_month == month and your_day == day:
        print("정답입니다\n") 
        correct_answer.append(1)
    else:
        print("틀렸습니다 오늘은",month,"월",day,"일 입니다\n")
        correct_answer.append(0)


def simple_math_question():
    a_random=(random.randint(1,10))
    b_random=(random.randint(1,10))

    real_math_answer=(a_random+b_random)

    your_math_answer = int((input(f"{a_random}+{b_random}의 답은 무엇입니까?")))

    if real_math_answer == your_math_answer:
        print("당신의 정답은 맞았습니다\n")
        correct_answer.append(1)
    else:
        print("당신의 정답은 틀렸습니다. 정답은",real_math_answer,"입니다\n")
        correct_answer.append(0)
        


def correct_answer_rate():
    if correct_answer[0] == 0 and correct_answer[1] == 0:
        print("당신은 치매치료를 받아야 합니다\n")

    elif correct_answer[0] == 0 or correct_answer[1] == 0:
        print("당신은 치매의 의심이 있습니다\n")
    
    else:
        print("당신의 치매로 부터 건강합니다\n")
            



def medicine_time_check():
    
    global hour,minute
    
    medicine_hour,medicine_minute = map(int,input("약먹을 시간을 입력하세요:").split())
    hour = medicine_hour - hour
    minute = medicine_minute - minute

    if minute < 0:
        minute += 60
        hour -= 1
    if hour < 0:
        hour += 24
    
    if hour==0 and minute<=5:
        print(minute,"분 남았습니다,지금 약을 복용하세요.")
    else:   
        print(hour,"시간",minute,"분 남았습니다.")







date_question()
simple_math_question()
correct_answer_rate()
medicine_time_check()