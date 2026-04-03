# main.py

from models import Patient, Doctor, Appointment, MedicalRecord, Resource
from hospital_system import HospitalSystem

def manage_resources(system):
    ""Sub-menu for managing hospital resources.""
    while True:
        print("\n-- Resource Management --")
        print("1. Add a new Resource")
        print("2. List all Resources")
        print("3. Update Resource Status")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter resource name (e.g., X-Ray Machine): ")
            category = input("Enter category (e.g., Equipment, Room): ")
            new_resource = Resource(system.generate_resource_id(), name, category)
            system.add_resource(new_resource)
        elif choice == '2':
            system.list_all_resources()
        elif choice == '3':
            res_id = input("Enter Resource ID to update: ")
            new_status = input("Enter new status (Available/In Use): ")
            system.update_resource_status(res_id, new_status)
        elif choice == '4':
            break
        else:
            print(" Invalid choice. Please try again.")
        input("\nPress Enter to continue...")

def main():
    """Main function to run the interactive hospital management system."""
    
    system = HospitalSystem()
    print("🏥 Welcome to the Serenity Health Hospital Management System 🏥")
    
    # Pre-populate with some data for easier testing
    doc1 = Doctor(system.generate_doctor_id(), "Emily Carter", "Pediatrics", "MD, FAAP", "Room 301", "Mon-Wed 9am-5pm")
    system.add_doctor(doc1)
    pat1 = Patient(system.generate_patient_id(), "John Smith", "1990-05-20", "555-0101", "BlueCross PPO")
    system.add_patient(pat1)
    res1 = Resource(system.generate_resource_id(), "ECG Machine", "Equipment")
    system.add_resource(res1)
    print("-" * 50)

    while True:
        print("\n======= Main Menu =======")
        print("1. List all Patients")
        print("2. List all Doctors")
        print("3. List all Appointments")
        print("---")
        print("4. Add a new Patient")
        print("5. Add a new Doctor")
        print("6. Schedule an Appointment")
        print("---")
        print("7. Update Patient Information")
        print("8. Add Medical Record for Patient")
        print("9. View Patient Medical History")
        print("---")
        print("10. Cancel Appointment")
        print("11. Complete Appointment")
        print("---")
        print("12. Manage Hospital Resources")
        print("13. Exit")
        
        choice = input("Enter your choice (1-13): ")

        if choice == '1':
            system.list_all_patients()
        
        elif choice == '2':
            system.list_all_doctors()

        elif choice == '3':
            system.list_all_appointments()
            
        elif choice == '4':
            name = input("Enter patient's full name: ")
            dob = input("Enter patient's date of birth (YYYY-MM-DD): ")
            contact = input("Enter patient's contact info: ")
            insurance = input("Enter patient's insurance details: ")
            new_patient = Patient(system.generate_patient_id(), name, dob, contact, insurance)
            system.add_patient(new_patient)

        elif choice == '5':
            name = input("Enter doctor's name: ")
            spec = input("Enter doctor's specialization: ")
            qual = input("Enter doctor's qualifications: ")
            room = input("Enter doctor's consultation room: ")
            avail = input("Enter doctor's availability schedule: ")
            new_doctor = Doctor(system.generate_doctor_id(), name, spec, qual, room, avail)
            system.add_doctor(new_doctor)

        elif choice == '6':
            if not system.patients or not system.doctors:
                print(" Error: Add at least one patient and one doctor before scheduling.")
                continue
            
            pat_id = input(f"Enter Patient ID (e.g., {list(system.patients.keys())[0]}): ")
            doc_id = input(f"Enter Doctor ID (e.g., {list(system.doctors.keys())[0]}): ")
            
            patient = system.find_patient_by_id(pat_id)
            doctor = system.find_doctor_by_id(doc_id)
            
            if not patient or not doctor:
                print(" Error: Invalid Patient or Doctor ID.")
                continue
            
            date_time = input("Enter appointment date and time (e.g., 2025-09-15 10:00): ")
            dept = doctor.specialization
            
            new_appointment = Appointment(system.generate_appointment_id(), patient, doctor, date_time, dept)
            system.schedule_appointment(new_appointment)

        elif choice == '7':
            pat_id = input("Enter Patient ID to update: ")
            contact = input("Enter new contact info: ")
            insurance = input("Enter new insurance details: ")
            system.update_patient_details(pat_id, contact, insurance)

        elif choice == '8':
            pat_id = input("Enter Patient ID to add record for: ")
            date = input("Enter date of record (YYYY-MM-DD): ")
            diag = input("Enter diagnosis: ")
            pres = input("Enter prescription: ")
            tests = input("Enter test results: ")
            new_record = MedicalRecord(system.generate_record_id(), date, diag, pres, tests)
            system.add_medical_record(pat_id, new_record)
            
        elif choice == '9':
            pat_id = input("Enter Patient ID to view history: ")
            system.view_patient_medical_history(pat_id)

        elif choice == '10':
            app_id = input("Enter Appointment ID to cancel: ")
            system.cancel_appointment(app_id)

        elif choice == '11':
            app_id = input("Enter Appointment ID to complete: ")
            system.complete_appointment(app_id)

        elif choice == '12':
            manage_resources(system)

        elif choice == '13':
            print("Thank you for using the system. Goodbye! ")
            break
            
        else:
            print(" Invalid choice. Please enter a number between 1 and 13.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
