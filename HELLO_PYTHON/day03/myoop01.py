class Animal:
    # 생성자
    def __init__(self):
        self.flagM = True
        print('생성자')
    
    def goToThai(self) :
        self.flagM = not self.flagM
        
    # 소멸자
    def __del__(self):
        print('소멸자')
    

if __name__ == '__main__':
    ani = Animal()
    print('flagM1',ani.flagM)
    ani.goToThai()
    print('goToThai_flagM1',ani.flagM)
    
    # 생성자
    # flagM1 True
    # goToThai_flagM1 False
    # 소멸자
