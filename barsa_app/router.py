from barsa_app.views import EmployeeViewSet


def register(router):
    router.register('employee', EmployeeViewSet, basename='employee')