class payroll_deduction:
    def __init__(self, Description, Date, Charge, EmployeeID):
        self._Description = Description
        self._Date = Date
        self._Charge = Charge
        self._EmployeeID = EmployeeID

    def get_Description(self):
        return self._Description
    
    def get_Date(self):
        return self._Date
    
    def get_Charge(self):
        return self._Charge
    
    def get_EmployeeID(self):
        return self._EmployeeID
    


