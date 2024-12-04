class Person: # Person classs 생성
    def __init__(self, name, gender, age): # 매개 변수 생성
        self.name = name
        self.gender = self.validate_gender(gender)
        self.age = self.validate_age(age)

    def validate_age(self, age): # age값에 대한 검증
        if not age.isdigit() or int(age) < 0: # age가 정수가 아니거나 또는 0보다 작을 때
            print("나이는 0 이상의 정수를 입력해주세요.")
            return None
        return int(age) # age가 정상값일 때 그대로 반환

    def validate_gender(self, gender): # gender값에 대한 검증
        if gender.lower() not in ("male", "female"): # 입력값이 male과 female이 아닌 경우
            print("성별은 male과 female 중 입력하세요.")
            return None
        return gender.lower() #gender가 정상값일 때 그대로 반환

    def display(self): # 최종 결과값 출력
        print("이름: {}, 성별: {}\n나이: {}".format(self.name, self.gender, self.age))

    def greet(self): # age의 값에 따라 다른 인사말 출력
        if 0 < int(self.age) < 20:
            print("안녕하세요, {}! 미성년자시군요!".format(self.name))
        else:
            print("안녕하세요, {}! 성인이시군요!".format(self.name))
def main(): # 실행 함수 생성
    name = input("이름: ")
    while True: # 에러 발생 시 반복 실행
        gender = input("성별 (male 또는 female): ")
        age = input("나이 (0 이상의 정수): ")

        p = Person(name, gender, age)

        if p.gender is None:
            continue  # 성별이 유효하지 않으면 반복
        if p.age is None:
            continue  # 나이가 유효하지 않으면 반복

        p.display()
        p.greet()
        break  # 모든 값이 유효하면 루프 종료

main()
