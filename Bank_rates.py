import  random
class Bank():
    '''
    This class contain the rates of different bank
    '''
    def __init__(self):
        self.name = "Bank Rates"
    
    def get_SBI(self):  #method about SBI rates 
       return random.randint(2,10)

    def get_BOB(self):
         return random.randint(2,10)


    def get_PNB(self):
        return  random.randint(2,10)
        
if __name__ =='__main__':
    bank_obj = Bank()
    bank_obj.get_BOB(),
    bank_obj.get_PNB(),
    bank_obj.get_SBI()