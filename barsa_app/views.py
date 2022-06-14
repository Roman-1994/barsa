from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm, UserForm_2
from .models import Employee
from django.template.response import TemplateResponse


from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from barsa_app.models import Employee
from barsa_app.serializers import EmployeeSerializer


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Employee CRUD methods.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = [AllowAny]


def index(request):
    header = "Персональные данные"  # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]  # массив
    user = {"name": "Максим,", "age": 30}  # словарь
    addr = ("Виноградная", 23, 45)  # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    #return TemplateResponse(request, 'main_list.html')
    return render(request, 'base/second_list.html', context=data)

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        basket = request.POST.get('basket')
        data = request.POST.get('data')
        sity = request.POST.get('sity')
        commy = request.POST.get('commy')
        if basket:
            output = '<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}, Отправлено - {2}, Город - {3}</h3><h3>Комментарий</h3><p>{4}</p>'.format(name, age, data, sity, commy)
        else:
            output = 'Вы ввели свои данные!'
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'base/main_list.html', {'form': userform})

def contact(request):
    userform = UserForm_2()
    if request.method == 'POST':
        userform = UserForm_2(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse("<h2>Имя введено корректно - {0}</h2>".format(name))

    return render(request, 'base/list.html', {'form': userform})

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 5)
    name = request.GET.get("name", 'Максим')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(id, name)
    return HttpResponse(output)

def get_employee(request):
    '''Получение списка сотрудников'''
    employee = Employee.objects.all()
    return render(request, 'base/employee.html', {'employee': employee})

def create_employee(request):
    '''Сохранение нового сотрудника и переход к списку'''
    if request.method == 'POST':
        employee = Employee()
        employee.name = request.POST.get('name')
        employee.phone = request.POST.get('phone')
        employee.age = request.POST.get('age')
        employee.date_birth = request.POST.get('date_birth')
        employee.save()
    return HttpResponseRedirect('/')

def update_employee(request, id):
    '''Изменение данных сотрудника'''
    try:
        employee = Employee.objects.get(id=id)
        if request.method == 'POST':
            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')
            employee.age = request.POST.get('age')
            employee.date_birth = request.POST.get('date_birth')
            employee.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'base/up_employee.html', {'employee': employee})
    except Employee.DoesNotExist:
        return HttpResponseNotFound('<h2>Сотрудник не найден</h2>')

def delete_employee(request, id):
    '''Удаление сотрудника'''
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return HttpResponseRedirect('/')
    except Employee.DoesNotExist:
        return HttpResponseNotFound('<h2>Сотрудник не найден</h2>')