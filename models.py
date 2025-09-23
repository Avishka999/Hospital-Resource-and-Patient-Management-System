# models.py

class Patient:
    """Represents a patient in the hospital system."""
    def __init__(self, patient_id, full_name, dob, contact, insurance_details):
        self.patient_id = patient_id
        self.full_name = full_name
        self.dob = dob
        self.contact = contact
        self.insurance_details = insurance_details
        self.medical_history = []  # List to store MedicalRecord objects

    def display_details(self):
        """Prints the patient's details."""
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.full_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Contact: {self.contact}")
        print(f"Insurance: {self.insurance_details}")
        print("-" * 20)
    
    def add_medical_record(self, record):
        """Adds a medical record to the patient's history."""
        self.medical_history.append(record)

class Doctor:
    """Represents a doctor in the hospital system."""
    def __init__(self, staff_id, name, specialization, qualifications, room, availability):
        self.staff_id = staff_id
        self.name = name
        self.specialization = specialization
        self.qualifications = qualifications
        self.room = room
        self.availability = availability

    def display_details(self):
        """Prints the doctor's details."""
        print(f"Doctor ID: {self.staff_id}")
        print(f"Name: Dr. {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Qualifications: {self.qualifications}")
        print(f"Consultation Room: {self.room}")
        print(f"Availability: {self.availability}")
        print("-" * 20)

class Appointment:
    """Represents an appointment in the hospital system."""
    def __init__(self, appointment_id, patient, doctor, date_time, department):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.department = department
        self.status = "Confirmed"  # Status can be Confirmed, Completed, Cancelled

    def display_details(self):
        """Prints the appointment's details."""
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient: {self.patient.full_name} (ID: {self.patient.patient_id})")
        print(f"Doctor: Dr. {self.doctor.name} (ID: {self.doctor.staff_id})")
        print(f"Date & Time: {self.date_time}")
        print(f"Department: {self.department}")
        print(f"Status: {self.status}")
        print("-" * 20)

    def cancel(self):
        """Changes the appointment status to 'Cancelled'."""
        self.status = "Cancelled"
        print(f"Appointment {self.appointment_id} has been cancelled.")
        
    def complete(self):
        """Changes the appointment status to 'Completed'."""
        self.status = "Completed"
        print(f"Appointment {self.appointment_id} has been marked as completed.")

class MedicalRecord:
    """Represents a single medical record for a patient visit."""
    def __init__(self, record_id, date, diagnosis, prescription, test_results):
        self.record_id = record_id
        self.date = date
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.test_results = test_results

    def display_details(self):
        """Prints the medical record's details."""
        print(f"Record ID: {self.record_id}")
        print(f"Date: {self.date}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Prescription: {self.prescription}")
        print(f"Test Results: {self.test_results}")
        print("-" * 20)

class Resource:
    """Represents a hospital resource like equipment or a room."""
    def __init__(self, resource_id, name, category):
        self.resource_id = resource_id
        self.name = name
        self.category = category  # e.g., "Equipment", "Room", "Pharmacy"
        self.status = "Available" # e.g., "Available", "In Use"

    def display_details(self):
        """Prints the resource's details."""
        print(f"Resource ID: {self.resource_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Status: {self.status}")
        print("-" * 20)