# This class is to embed all the methods used for the employee salary system
class employeeSystem:
  def __init__(self): #constructor
    self.__employees = [] #list for all the employees and their information

  def addEmployee(self, employee_name, employee_position, employee_salary):
    employee = {"employee name": employee_name, "employee position": employee_position, "employee salary": employee_salary}

    self.__employees.append(employee)
    print(f"{employee_name}, has been added to the system.")