class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = []
        for employee in self.employees:
            if employee.age == target_age:
                result.append(employee)
        return result

    def search_by_name(self, target_name):
        result = []
        for employee in self.employees:
            if employee.name == target_name:
                result.append(employee)
        return result

    def search_by_salary(self, operator, target_salary):
        result = []
        for employee in self.employees:
            if operator == '>' and employee.salary > target_salary:
                result.append(employee)
            elif operator == '<' and employee.salary < target_salary:
                result.append(employee)
            elif operator == '>=' and employee.salary >= target_salary:
                result.append(employee)
            elif operator == '<=' and employee.salary <= target_salary:
                result.append(employee)
        return result

if _name_ == "_main_":
    db = EmployeeDatabase()

    db.add_employee("161E90", "Raman", 41, 56000)
    db.add_employee("161F91", "Himadri", 38, 67500)
    db.add_employee("161F99", "Jaya", 51, 82100)
    db.add_employee("171E20", "Tejas", 30, 55000)
    db.add_employee("171G30", "Ajay", 45, 44000)

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        target_age = int(input("Enter age to search: "))
        result = db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter name to search: ")
        result = db.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (<, <=, >, >=): ")
        target_salary = int(input("Enter salary to search: "))
        result = db.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")

    if result:
        print("Search results:")
        for employee in result:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No results found.")