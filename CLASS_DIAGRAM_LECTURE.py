#--------------------------------------HOSPITAL MANAGEMENT SYSTEM-------------------------------------------------

class MedicalRecord:

    def __init__(self, doctor_name, diagnosis, medications, date_of_visit):
        self.doctor_name = doctor_name
        self.diagnosis = diagnosis
        self.medications = medications
        self.date_of_visit = date_of_visit

    def print_medical_record(self):
        print(f"Doctor Name: {self.doctor_name}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Medications: {self.medications}")
        print(f"Date of Visit: {self.date_of_visit}")

class Patient:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.medical_records = []

    def add_medical_record(self, doctor_name, diagnosis, medications, date_of_visit):
        medical_record = MedicalRecord(doctor_name, diagnosis, medications, date_of_visit)
        self.medical_records.append(medical_record)

    def get_record_list(self):
        print(f"--------------RECORD OF PATIENT {self.name}-----------------")
        for record in self.medical_records:
            record.print_medical_record()

class Doctor:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patients_list(self):
        i = 1
        for patient in self.patients:
            print(f"Patient no {i}: {patient.name}")
            i += 1

class Department:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_doctors_list(self):
        i = 1
        for doctor in self.doctors:
            print(f"Doctor no {i}: {doctor.name}")
            i += 1

class Hospital:

    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, depart_id, depart_name):
        department = Department(depart_id, depart_name)
        self.departments.append(department)

    def get_departments_list(self):
        for dept in self.departments:
            print(f"Department name: {dept.name}")

p1 = Patient("420","Hashir")
p1.add_medical_record("Gumnaam","Nai Pata","Ye kia hota h","11-11-11")
p1.get_record_list()
d1 = Doctor("421","Gumnaam")
d1.add_patient(p1)
d1.get_patients_list()
d = Department("422","Pscycology")
d.add_doctor(d1)
d.get_doctors_list()
h1 = Hospital("Paagal Khaana")
h1.add_department("423","Yaad nai aaraha")
h1.get_departments_list()