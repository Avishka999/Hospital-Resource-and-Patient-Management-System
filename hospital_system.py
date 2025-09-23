from models import Patient, Doctor, Appointment, MedicalRecord, Resource

class HospitalSystem:
   
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HospitalSystem, cls).__new__(cls)
            # Initialize dictionaries for quick lookups by ID
            cls._instance.patients = {}
            cls._instance.doctors = {}
            cls._instance.appointments = {}
            cls._instance.resources = {}
            # Counters to generate unique IDs
            cls._instance.next_patient_id = 1
            cls._instance.next_doctor_id = 101
            cls._instance.next_appointment_id = 1001
            cls._instance.next_record_id = 5001
            cls._instance.next_resource_id = 8001
        return cls._instance

    #ID Generation 
    def generate_patient_id(self):
        pid = f"P{self.next_patient_id:03}"
        self.next_patient_id += 1
        return pid

    def generate_doctor_id(self):
        did = f"D{self.next_doctor_id}"
        self.next_doctor_id += 1
        return did
        
    def generate_appointment_id(self):
        aid = f"A{self.next_appointment_id}"
        self.next_appointment_id += 1
        return aid

    def generate_record_id(self):
        rid = f"MR{self.next_record_id}"
        self.next_record_id += 1
        return rid

    def generate_resource_id(self):
        rs_id = f"R{self.next_resource_id}"
        self.next_resource_id += 1
        return rs_id
        
    # --- Patient Management Methods ---
    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient
        print(f" Patient {patient.full_name} (ID: {patient.patient_id}) added.")

    def find_patient_by_id(self, patient_id):
        return self.patients.get(patient_id)

    def list_all_patients(self):
        print("\n--- All Patients ---")
        if not self.patients:
            print("No patients in the system.")
            return
        for patient in self.patients.values():
            patient.display_details()

    def update_patient_details(self, patient_id, new_contact, new_insurance):
        patient = self.find_patient_by_id(patient_id)
        if patient:
            patient.contact = new_contact
            patient.insurance_details = new_insurance
            print(f" Patient {patient_id} details updated.")
        else:
            print(f" Error: Patient with ID {patient_id} not found.")

    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f" Patient {patient_id} removed from the system.")
        else:
            print(f" Error: Patient with ID {patient_id} not found.")

    # --- Doctor Management Methods ---
    def add_doctor(self, doctor):
        self.doctors[doctor.staff_id] = doctor
        print(f" Dr. {doctor.name} (ID: {doctor.staff_id}) added.")

    def find_doctor_by_id(self, doctor_id):
        return self.doctors.get(doctor_id)
        
    def list_all_doctors(self):
        print("\n--- All Doctors ---")
        if not self.doctors:
            print("No doctors in the system.")
            return
        for doctor in self.doctors.values():
            doctor.display_details()
    
    # --- Appointment Management Methods ---
    def schedule_appointment(self, appointment):
        self.appointments[appointment.appointment_id] = appointment
        print(f" Appointment {appointment.appointment_id} scheduled successfully.")

    def list_all_appointments(self):
        print("\n--- All Appointments ---")
        if not self.appointments:
            print("No appointments scheduled.")
            return
        for appointment in self.appointments.values():
            appointment.display_details()
    
    def cancel_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.cancel()
        else:
            print(f" Error: Appointment with ID {appointment_id} not found.")
            
    def complete_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.complete()
        else:
            print(f" Error: Appointment with ID {appointment_id} not found.")

    # --- Medical Record Methods ---
    def add_medical_record(self, patient_id, record):
        patient = self.find_patient_by_id(patient_id)
        if patient:
            patient.add_medical_record(record)
            print(f" Medical record added for patient {patient_id}.")
        else:
            print(f" Error: Patient with ID {patient_id} not found.")
            
    def view_patient_medical_history(self, patient_id):
        patient = self.find_patient_by_id(patient_id)
        if patient:
            print(f"\n--- Medical History for {patient.full_name} (ID: {patient_id}) ---")
            if not patient.medical_history:
                print("No medical records found for this patient.")
                return
            for record in patient.medical_history:
                record.display_details()
        else:
            print(f" Error: Patient with ID {patient_id} not found.")
            
    # --- Resource Management Methods ---
    def add_resource(self, resource):
        self.resources[resource.resource_id] = resource
        print(f" Resource '{resource.name}' (ID: {resource.resource_id}) added.")

    def list_all_resources(self):
        print("\n--- All Hospital Resources ---")
        if not self.resources:
            print("No resources in the system.")
            return
        for resource in self.resources.values():
            resource.display_details()
            
    def update_resource_status(self, resource_id, new_status):
        resource = self.resources.get(resource_id)
        if resource:
            if new_status in ["Available", "In Use"]:
                resource.status = new_status
                print(f" Status for resource {resource_id} updated to '{new_status}'.")
            else:
                print(" Error: Invalid status. Use 'Available' or 'In Use'.")
        else:
            print(f" Error: Resource with ID {resource_id} not found.")
