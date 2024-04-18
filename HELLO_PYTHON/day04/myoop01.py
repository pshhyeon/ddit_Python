class LeeJY:
    def __init__(self):
        self.money = 100
        
    def yakun(self):
        self.money += 1



class ElonMusk:
    def __init__(self):
        self.skill_gas = 10000

    def getPenalty(self, cnt):
        self.skill_gas -= cnt


class LeeMusk(LeeJY, ElonMusk):
    def __init__(self):
        # super().__init__()
        LeeJY.__init__(self)
        ElonMusk.__init__(self)
        
        
        
if __name__ == '__main__':
    lm = LeeMusk()
    print(lm.money)
    print(lm.skill_gas)
    lm.yakun()
    lm.getPenalty(1000)
    print(lm.money)
    print(lm.skill_gas)
    
    