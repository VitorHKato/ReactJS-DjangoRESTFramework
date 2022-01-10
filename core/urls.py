from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import EmployeeAPIView

urlpatterns = [
    path('employee/', csrf_exempt(EmployeeAPIView.as_view()), name='employee')
]