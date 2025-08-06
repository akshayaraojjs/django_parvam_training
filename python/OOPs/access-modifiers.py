class BankAccount:
    def __init__(self):
        # Syntax:
        # data - Public Data member
        # _data - Protected Data member
        # __data - Private Data member
        self.__acNo = 1234 # private data: (__acNo)
        self.name = "Unknown"
        self.bank = "ABC Bank"
        self.branch = "Chikkabanavara" 
        self._balance = 0 # protected data: (_balance)
        print("Constructor has been invoked")
        
    def setAccountDetails(self, pName, pBank, pBranch):
        self.name = pName
        self.branch = pBranch
        self.bank = pBank
        print(f"Name of the Account Holder: {self.name}, Branch Location: {self.branch}, Bank: {self.bank}")
        
    def setAdditionalDetails(self, pAcNo, pBalance):
        self.__acNo = pAcNo
        self._balance = pBalance
        print("********************Secret Details****************")
        print(f"Account Number: {self.__acNo}, Account Balance: Rs.{self._balance}")
        
A1 = BankAccount()

A1.setAccountDetails("Akshay", "Canara Bank", "Chikkabanavara")

A1.setAdditionalDetails(12345, 50000)