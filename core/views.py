from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Client
from .serializers import EmployeeSerializer, ClientSerializer
from rest_framework import status

class EmployeeAPIView(APIView):
    authentication_classes = []  # disables authentication
    permission_classes = []  # disables permission
    """
        API Para retornar e adicionar Employee's
    """
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)