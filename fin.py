class Bank(object):
    """
        A financial institutions class used to instantiate various fin institutions and to depict the type, 
        name and simple tiered interest calculation on savings by the institution
    """
    def __init__(self, f_type, f_name, offer_islamic_finance):
        self.f_type = f_type
        self.f_name = f_name
        self.offer_islamic_finance = offer_islamic_finance
        self.interest_rate = 0

    """ Get name of Bank """
    def getname(self):
        return self.f_name

    """ Get type of Bank """
    def gettype(self):
        return self.f_type

    """ Calculate loan interest rate of Bank """
    def calculate_interest(self, balance):
        raise NotImplementedError("Subclass must implement abstract method")


class CommercialBank(Bank):
    def __init__(self, f_type, f_name, offer_islamic_finance, sme_loans):
        """ call parent constructor to set f_type, f_name and check if it offers islamic finance """
        Bank.__init__(self, f_type, f_name, offer_islamic_finance)
        self.sme_loans = sme_loans
        
    
    
    def calculate_interest(self, balance):
        interest_rate = 0.04
        return interest_rate * float(balance)
        


class MicroFinance(Bank):
    def __init__(self, f_type, f_name, offer_islamic_finance, wakulima_loans):
        """ call parent constructor to set f_type, f_name and check if it offers islamic finance """
        Bank.__init__(self, f_type, f_name, offer_islamic_finance)
        self.wakulima_loans = wakulima_loans

    
    def calculate_interest(self, balance):
        interest_rate = 0.08
        return interest_rate * float(balance)