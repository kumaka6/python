# multiple inheritance

class bank:
    def trasnaction(self):
        print("total transcation value")

    def account_opening(self):
        print("this will show you your account open status")

    def deposite(self):
        print("this will show your deposited amount")

    def test(self  ):
        print("this is test method from bank class")

class HDFC_bank():
    def hdfc_to_icici(self):
        print("this will show you all the transaction to icici through hdfc")

    def test(self):
        print("this is a test method from hdfc bank")


class ineuron_bank:
    def account_status_icici(self):
        print(" print a account status from icici ")

class icici(HDFC_bank, bank, ineuron_bank):
    pass

i = icici()

i.account_opening()
i.hdfc_to_icici()
i.deposite()
i.trasnaction()
i.account_status_icici()


# when two method name is same and perform multiple inheritance, (conflict in name) by default will be from first class
i.test()
