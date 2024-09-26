# Maya Anderson: 100927762
# Mackenzi Burke : 100918263

students = []
student_number_counter = 1

def newStudent():
    global student_number_counter
    while True:
        print(" ")
        print("=" * 30)
        print("\tNew Student Details")
        print("=" * 30)
        print("Enter the following details: ")
        first_name = input("First name: ")
        middle_name = input("Middle name: ")
        last_name = input("Last name: ")
        dob = input("Date of Birth: ")
        gender = input("Gender: ")
        department = input("Department: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        address = input("Address: ")
        contacts = input("Emergency Contact Details: ")
        courses = input("Course Opted: ")
        schedule = input("Student Detailed Schedule: ")
        fees = input("Information about fees: ")
        aid = input("Awards and Financial Aid: ")
        grades = input("Final Grades: ")

        student = {'First Name': first_name, 'Middle Name': middle_name, 'Last Name': last_name, 'DOB': dob,
                   'Gender': gender, 'Department': department, 'Email': email, 'Phone Number': phone, 'Address': address,
                   'Emergency Contact': contacts, 'Courses Opted': courses, 'Student Detailed Schedule': schedule,
                   'Fees Info': fees, 'Awards and Financial Aid': aid, 'Final Grades': grades}
        students.append(student)

        save_option = input("Do you want to save the entered details? (Yes/No): ").lower()
        if save_option == 'yes':
            student_number_counter += 1
            add_more_option = input("Do you want to add more students? (Yes/No): ").lower()
            if add_more_option != 'yes':
                break
        elif save_option == 'no':
            break
        else:
            print("Invalid option. Please enter 'Yes' or 'No'.")

def displayData(students):
    print(" ")
    print("=" * 30)
    print("\tNew Student Details")
    print("=" * 30)
    for student in students:
        print("=" * 30)
        print(" ")
        print("=" * 30)
        print("\tStudent Details:")
        print("=" * 30)
        for key, value in student.items():
            print(f"{key}: {value}")
    if not students:
        print("No data available.")
        return
    headers = students[0].keys()
    header_line = "|".join(f"{header:<20}" for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print student details
    for student in students:
        values_line = "|".join(f"{value:<20}" for value in student.values())
        print(values_line)
def searchStudent():
    if not students:
        print("No data available. Please add a new student.")
        return

    while True:
        print(" ")
        print("=" * 30)
        print("\tStudent Database")
        print("=" * 30)
        student_number = input("Enter student number to search (1 to return to the main menu): ")

        if student_number == '1':
            break
        elif 1 <= int(student_number) <= len(students):
            student = students[int(student_number) - 1]
            print("\tStudent Details:")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("Student number not found.")

print("=" * 30)
print("\tAdmin Login Page")
print("=" * 30)

username = 'Admin'
password = 'password'

user_input1 = input("Enter username: ")
user_input2 = input("Enter password: ")

while True:
    if user_input1 == username and user_input2 == password:
        print(" ")
        print("=" * 30)
        print("\tStudent Ledger")
        print("=" * 30)
        print("Select an option: ")
        print("[1] Add a student")
        print("[2] Display student database")
        print("[3] Search student details")
        print("[4] Exit")
        option = input("Enter your choice: ")
        if option == '1':
            newStudent()
        elif option == '2':
            displayData(students)
        elif option == '3':
            searchStudent()
        elif option == '4':
            print("Exiting program.")
            break
    else:
        print("Something went wrong. Exiting.")
        break

