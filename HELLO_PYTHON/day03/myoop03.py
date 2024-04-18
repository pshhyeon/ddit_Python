from day03.myoop01 import Animal
class Human(Animal):
    def __init__(self):
        # __init__를 재정의하려면 부모를 초기화해야 한다.
        # Animal.__init__(self) # 상속 관계가 명시적으로 드러나지만, 만약 상속 관계가 변경되어 다른 클래스를 부모로 사용해야 한다면 모든 해당 부분을 변경해 주어야 하는 불편함이 있다
        super().__init__()
        self.skill_communication = 1
        print('Human 생성자')
    
    def momstouch(self, stroke):
        self.skill_communication += stroke
    
    def __del__(self):
        Animal.__del__(self)
        print('Human 소멸자')
        
if __name__ == '__main__':
    hum = Human()
    print('hum_flagM',hum.flagM)
    print('hum_skill_communication',hum.skill_communication)
    hum.goToThai()
    hum.momstouch(5)
    print('hum_flagM',hum.flagM)
    print('hum_skill_communication',hum.skill_communication)
