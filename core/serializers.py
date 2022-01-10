from rest_framework import serializers

from .models import Employee, Client

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'full_name',
            'date_of_birth',
            'email',
            'creation_date',
            'position',
            'status'
        )

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'full_name',
            'date_of_birth',
            'creation_date',
            'contract_end_date',
            'contract_start_date',
            'status'
        )