class Doctor():
    def __init__(self, name, specialization, time):
        self.name = name
        self.specialization = specialization
        self.time = time

class Patient():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wantTime  = ""

class Hospital():
    patientsList = []
    doctorsList = []

    def showPatients(self):
        for index,elem in enumerate(self.patientsList):
            print("Id: ", index,"Nimi: ", elem.name, "Vanus: ", elem.age)

    def showDoctors(self):
        for index,elem in enumerate(self.doctorsList):
            print("Id: ", index,"Nimi: ", elem.name, "Eriala: ", elem.specialization)

    def meeting(self):
        PatsiendiNimi = input("sisesta patsiendi nimi: ")
        ArstiNimi = input("sisesta arsti nimi: ")
        for elem in self.patientsList:
            if elem.name == PatsiendiNimi:
                patientIndex = self.patientsList.index(elem)


        for elem in self.doctorsList:
            if elem.name == ArstiNimi and len(elem.time) > 0:
                self.patientsList[patientIndex].wantTime = elem.time

        for elem in self.patientsList:
            print("Nimi: ", elem.name, "aeg", elem.wantTime)

Patient1 = Patient("Thomas",35)
Patient2 = Patient("Kayle",19)
Doctor1 = Doctor("Ernie", "Silmaarst", ['10:00','11:00','12:00'])
Doctor2 = Doctor("Violet", "Perearst", ['12:00','13:00','14:00'])
hospital = Hospital()
hospital.patientsList.append(Patient1)
hospital.patientsList.append(Patient2)
print("Patients")
hospital.showPatients()
hospital.doctorsList.append(Doctor1)
hospital.doctorsList.append(Doctor2)
print("Doctors")
hospital.showDoctors()

hospital.meeting()