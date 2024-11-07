from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Employee, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer

# QUESTION: How can I retrieve all departments or create a new department?
# API for Department List (GET all departments, POST a new department)
class DepartmentList(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# QUESTION: How can I get details of a specific department by ID, update it, or delete it?
# API for Department details (GET, PUT, DELETE by department ID)
class DepartmentDetail(APIView):
    def get(self, request, id):
        try:
            department = Department.objects.get(id=id)
            employees = Employee.objects.filter(department=department)
            department_data = DepartmentSerializer(department).data
            employees_data = EmployeeSerializer(employees, many=True).data
            return Response({
                "department": department_data,
                "employees": employees_data
            })
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            department = Department.objects.get(id=id)
            serializer = DepartmentSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            department = Department.objects.get(id=id)
            employees = Employee.objects.filter(department=department)
            if employees.exists():
                return Response({"error": "Cannot delete department with assigned employees"}, status=status.HTTP_400_BAD_REQUEST)
            department.delete()
            return Response({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I retrieve all employees or create a new employee?
# API for Employee List (GET all employees, POST a new employee)
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# QUESTION: How can I get details of a specific employee by ID, update it, or delete it?
# API for Employee details (GET, PUT, DELETE by employee ID)
class EmployeeDetail(APIView):
    def get(self, request, id):
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I retrieve all projects or create a new project?
# API for Project List (GET all projects, POST a new project)
class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# QUESTION: How can I get details of a specific project by ID, update it, or delete it?
# API for Project details (GET, PUT, DELETE by project ID)
class ProjectDetail(APIView):
    def get(self, request, id):
        try:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            project = Project.objects.get(id=id)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I add a member to a specific project?
# API to add a member to a project (PUT)
class ProjectAddMember(APIView):
    def put(self, request, id):
        try:
            project = Project.objects.get(id=id)
            employee_id = request.data.get('employee_id')
            employee = Employee.objects.get(id=employee_id)
            project.employees.add(employee)
            return Response({"message": "Member added to project"}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I calculate the total budget of a project based on the salaries of its employees?
# API to get project budget based on employee salaries (GET)
class ProjectBudget(APIView):
    def get(self, request, id):
        try:
            project = Project.objects.get(id=id)
            employees = project.employees.all()
            total_budget = sum(employee.salary for employee in employees)
            return Response({"budget": total_budget}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I get the employee with the highest salary?
# API to get the highest salary employee (GET)
class HighestSalary(APIView):
    def get(self, request):
        highest_salary_employee = Employee.objects.order_by('-salary').first()
        if highest_salary_employee:
            serializer = EmployeeSerializer(highest_salary_employee)
            return Response(serializer.data)
        return Response({"message": "No employees found"}, status=status.HTTP_404_NOT_FOUND)

# QUESTION: How can I get the employee with the second-highest salary in each department? (Placeholder)
# API to get the second-highest salary holder grouped by department (GET)
class SecondHighestSalary(APIView):
    def get(self, request):
        pass  # Placeholder for future implementation

# QUESTION: How can I calculate the total salary of employees under each department? (Placeholder)
# API to get the total salary of employees under each department (GET)
class TotalSalaryByDepartment(APIView):
    def get(self, request):
        pass  # Placeholder for future implementation

# QUESTION: How can I get projects based on their status?
# API to get projects by status (GET)
class ProjectsByStatus(APIView):
    def get(self, request, status):
        projects = Project.objects.filter(status=status)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# QUESTION: How can I get the department of a specific employee by employee ID?
# API to get department by employee ID (GET)
class EmployeeDepartmentDetail(APIView):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            department = employee.department
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
