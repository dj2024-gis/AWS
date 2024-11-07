from django.urls import path
from .views import (
    DepartmentList, DepartmentDetail,
    EmployeeList, EmployeeDetail,
    ProjectList, ProjectDetail,
    ProjectAddMember, ProjectBudget,
    HighestSalary, SecondHighestSalary, TotalSalaryByDepartment,
    ProjectsByStatus, EmployeeDepartmentDetail
)

urlpatterns = [
    path('departments/', DepartmentList.as_view(), name='department-list'),
    path('departments/<int:id>/', DepartmentDetail.as_view(), name='department-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:id>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:id>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:id>/add-member/', ProjectAddMember.as_view(), name='project-add-member'),
    path('projects/<int:id>/budget/', ProjectBudget.as_view(), name='project-budget'),
    path('highest-salary/', HighestSalary.as_view(), name='highest-salary'),
    path('second-highest-salary/', SecondHighestSalary.as_view(), name='second-highest-salary'),
    path('total-salary-by-department/', TotalSalaryByDepartment.as_view(), name='total-salary-by-department'),
    path('projects/status/<str:status>/', ProjectsByStatus.as_view(), name='projects-by-status'),
    path('employees/<int:employee_id>/department/', EmployeeDepartmentDetail.as_view(), name='employee-department-detail'),
]
