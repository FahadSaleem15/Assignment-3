class employee:
    def __init__(self, name, ID_number, department, job_title, monthly_salary):
        self._name = name
        self._ID_number = ID_number
        self._department = department
        self._job_title = job_title
        self._monthly_salary = monthly_salary

    def get_name(self):
        return self._name
    
    def get_ID_number(self):
        return self._ID_number
    
    def get_department(self):
        return self._department
    
    def get_job_title(self):
        return self._job_title
    
    def get_monthly_salary(self):
        return self._monthly_salary
