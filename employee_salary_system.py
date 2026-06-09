# This class is to embed all the methods used for the employee salary system
class employeeSystem:
  def __init__(self): #constructor
    self.__employees = [] #list for all the employees and their information

  def addEmployees(self, employee_name, employee_position, employee_salary):
    employee = {"employee name": employee_name, "employee position": employee_position, "employee salary": employee_salary}

    self.__employees.append(employee)
    print(f"{employee_name}, has been added to the system.")

  def displayEmployees(self):
    if len(self.__employees) == 0:
      print("Employee has been found in the system.")

    else:
      print("\nEmployee Salary System")
      print("---------------")

      for employee in self.__employees:
        print(f"Employee Name: {employee["employee name"]}")
        print(f"Employee Position: {employee["employee position"]}")
        print(f"Employee Salary: {employee["employee salary"]}")

        print("---------------")

  def searchEmployee(self, employee_name):
    for employee in self.__employees:
      if employee["employee name"].lower() == employee_name.lower():
        print("\nEmployee found in the system.")
        print(f"Employee Name: {employee["employee name"]}")
        print(f"Employee Position: {employee["employee position"]}")
        print(f"Employee Salary: {employee["employee salary"]}")

        return
      
      print("Employee not found in the system.")

  def increaseSalary(self, employee_name, employee_salary):
    pass

  def countEmployees(self):
    return len(self.__employees)
  
employeeinfo = employeeSystem()

number_of_employees = int(input("Enter a valid number of employees that you would like to add: "))

for i in range(number_of_employees):
  print(f"\nEnter employee {i + 1}")

  employee_name = input("Enter employee's name: ")
  employee_position = input("Enter employee's position: ")
  employee_salary = float(input("Enter employee's salary: "))

  employeeinfo.addEmployees(employee_name, employee_position, employee_salary)
  
employeeinfo.displayEmployees()

search_employee_name = input("\n Search for employee information in system: ")
employeeinfo.searchEmployee(search_employee_name)

print(f"\n Total employees: {employeeinfo.countEmployees()}") 