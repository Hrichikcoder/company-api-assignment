from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Handles GET (List all) and POST (Create new)
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Handles GET (Retrieve one), PUT (Update), and DELETE (Remove)
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'