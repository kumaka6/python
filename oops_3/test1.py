# multilevel inheritance

class bank:
    def trasnaction(self):
        print("total transcation value")

    def account_opening(self):
        print("this will show you your account open status")

    def deposite(self):
        print("this will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction to icici through hdfc")

class icici(HDFC_bank):
    pass


i = icici()

i.hdfc_to_icici()
i.deposite()
i.trasnaction()
i.account_opening()