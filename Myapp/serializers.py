from rest_framework import serializers
from .models import Department, Employee,Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(many=True,queryset=Employee.objects.all())
    team_lead = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all(), required=False)
    project_names = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        project_names = validated_data.pop('project_names', [])
        projects_data = validated_data.pop('projects', [])
        employee = Employee.objects.create(**validated_data)

        for project in projects_data:
            employee.projects.add(project)

        for project_name in project_names:
            project, created = Project.objects.get_or_create(name=project_name)
            employee.projects.add(project)

        return employee
