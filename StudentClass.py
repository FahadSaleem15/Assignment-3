from datetime import datetime

class student:
    def __init__(self, Student_id, name, Dob, classification):
        self._Student_id = Student_id
        self._name = name
        self._Dob = Dob
        self._classification = classification

    def calc_age(self):
        today = datetime.today()
        dob_datetime = datetime.strptime(self._Dob, '%Y-%m-%d')
        age = today.year - dob_datetime.year - ((today.month, today.day) < (dob_datetime.month, dob_datetime.day))
        return age
    
    def calc_registration_dates(self):
        registration_dates = {
            'Sr': '4/1 thru 4/3',
            'Jr': '4/4 thru 4/6',
            'S': '4/7 thru 4/9',
            'F': '4/10 thru 4/12'
        }
        return registration_dates.get(self._classification)
    
    def get_age(self):
        return self.calc_age()
    
    def get_registration_dates(self):
        return self.calc_registration_dates()
    
    def get_Student_id(self):
        return self._Student_id

    def get_name(self):
        return self._name

    def get_Dob(self):
        return self._Dob
    
    def get_classification(self):
        return self._classification