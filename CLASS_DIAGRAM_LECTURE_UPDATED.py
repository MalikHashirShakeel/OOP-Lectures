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

    def add_doctor(self,doctor,dept):
        for department in self.departments:
            if department.name == dept:
                department.add_doctor(doctor)

    def list_all_doctors(self):
        i = 1  # Initialize the counter here, outside of the loops
        for department in self.departments:
            for doctor in department.doctors:
                print(f"Doctor {i} ({department.name}): {doctor.name}")
                i += 1  # Increment the counter within the inner loop


    def add_patients_to_doctor(self,patient,dr):
        for department in self.departments:
            for doctor in department.doctors:
                if doctor.name == dr:
                    doctor.add_patient(patient)

    def list_all_patients(self):
        i = 1
        for department in self.departments:
            for doctor in department.doctors:
                for patient in doctor.patients:
                    print(f"Patient {i} ({department.name}) ({doctor.name}): {patient.name}")
                    i += 1

    def list_all_patients_of_a_doctor(self,doctor_name):
        for department in self.departments:
            for doctor in department.doctors:
                if doctor.name == doctor_name:
                    doctor.get_patients_list()

    def list_all_doctors_of_a_patient(self,patient_name):
        for department in self.departments:
            for doctor in department.doctors:
                for patient in doctor.patients:
                    if patient.name == patient_name:
                        print(doctor.name)


#----------------------------------------------CLIENT CODE-------------------------------------------------------
h1 = Hospital("Paagal Khaana.")
h1.add_department("DT-1","Cardiology")
h1.add_department("DT-2","Orthopadics")
h1.get_departments_list()
dr1 = Doctor("DR-1","Maria-Waqas")
dr2 = Doctor("DR-2","Urooj-Ainuddin")
h1.add_doctor(dr1,"Cardiology")
h1.add_doctor(dr2,"Orthopadics")
h1.list_all_doctors()
p1 = Patient("P-1","Sana")
p2 = Patient("P-2","Hashir")
h1.add_patients_to_doctor(p1,"Maria-Waqas")
h1.add_patients_to_doctor(p1,"Urooj-Ainuddin")
h1.add_patients_to_doctor(p2,"Urooj-Ainuddin")
h1.list_all_patients()
h1.list_all_patients_of_a_doctor("Maria-Waqas")
h1.list_all_patients_of_a_doctor("Urooj-Ainuddin")
h1.list_all_doctors_of_a_patient("Sana")
h1.list_all_doctors_of_a_patient("Hashir")