from rest_framework import serializers

from barsa_app.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        #fields = ('id', 'name', 'surname', 'patronymic', 'position', 'salary', 'age', 'department', 'photo', )
        fields = '__all__'