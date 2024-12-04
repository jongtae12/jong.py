import random as rd
def game(): #게임생성
    random_number = rd.randrange(1,11) #1부터 10까지의 랜덤 숫자 생성

    while True:
        try:
            x= int(input("숫자를 입력해주세요:")) # 사용자 값 받기
            if x < 1 or x>10: # 범위 바깥 숫자를 입력할 시
                print("1과 10사이의 숫자를 입력해주세요")
            elif x > random_number: # 사용자 값이 랜덤 숫자보다 클 때
                print("X의 값이 더 작습니다.")
            elif x < random_number: # 사용자 값이 랜덤 숫자보다 작을 때
                print("X의 값이 더 큽니다.")
            else: #사용자 값이 랜덤 숫자와 같을 때
                print("정답입니다.")
                break
        except ValueError: #잘못된 type처리
            print("잘못된 입력입니다.숫자를 입력하세요!")
def main(): 
    while True:
        game()
        while True:  # 잘못된 입력 처리
            restart = input("게임을 재시작 하시겠습니까? [y/n]: ").lower()
            if restart == "y":
                print("게임을 재시작합니다.")
                break  # 내부 while을 종료하고 게임 실행
            elif restart == "n":
                print("게임을 종료합니다.")
                return  # 프로그램 종료
            else:
                print("잘못된 입력입니다. y 또는 n을 입력해주세요!")
main()