"""
Q10: Hospital Management System.

Classes: Patient, Doctor, Appointment, Hospital.
Features: add patients, schedule appointments, search records,
display appointment history.

Run with: python main.py
"""

from datetime import datetime


class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

    def __str__(self):
        return f"Patient[{self.patient_id}] {self.name}, Age {self.age}, Ailment: {self.ailment}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"


class Appointment:
    def __init__(self, appointment_id, patient, doctor, appointment_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def __str__(self):
        return (f"Appointment[{self.appointment_id}] {self.patient.name} with {self.doctor} "
                f"at {self.appointment_time.strftime('%d-%m-%Y %H:%M')}")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}
        self.appointments = []
        self._next_appointment_id = 1

    def add_patient(self, patient_id, name, age, ailment):
        self.patients[patient_id] = Patient(patient_id, name, age, ailment)
        return f"Patient '{name}' added"

    def add_doctor(self, doctor_id, name, specialization):
        self.doctors[doctor_id] = Doctor(doctor_id, name, specialization)
        return f"Doctor '{name}' added"

    def schedule_appointment(self, patient_id, doctor_id, appointment_time):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)
        if not patient:
            return "Error: patient not found"
        if not doctor:
            return "Error: doctor not found"

        appointment = Appointment(self._next_appointment_id, patient, doctor, appointment_time)
        self.appointments.append(appointment)
        self._next_appointment_id += 1
        return f"Appointment scheduled: {appointment}"

    def search_patient(self, name):
        return [p for p in self.patients.values() if name.lower() in p.name.lower()]

    def appointment_history(self, patient_id):
        return [a for a in self.appointments if a.patient.patient_id == patient_id]


def main():
    print("Q10: Hospital Management System")
    hospital = Hospital("City General Hospital")

    print(hospital.add_patient("P1", "Rahul Nair", 34, "Fever"))
    print(hospital.add_patient("P2", "Sneha Iyer", 28, "Fracture"))
    print(hospital.add_doctor("D1", "Kapoor", "General Medicine"))
    print(hospital.add_doctor("D2", "Mehta", "Orthopedics"))

    print(hospital.schedule_appointment("P1", "D1", datetime(2026, 8, 2, 10, 0)))
    print(hospital.schedule_appointment("P2", "D2", datetime(2026, 8, 3, 14, 30)))
    print(hospital.schedule_appointment("P1", "D2", datetime(2026, 8, 5, 9, 0)))

    print("\nSearch for patients named 'Rahul':")
    for patient in hospital.search_patient("Rahul"):
        print(patient)

    print("\nAppointment history for P1:")
    for appointment in hospital.appointment_history("P1"):
        print(appointment)


if __name__ == "__main__":
    main()
