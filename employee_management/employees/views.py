from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home')
        else:
            return render(request, 'add_employee.html', {'form': form})
    else:
        form = EmployeeForm()
        return render(request, 'add_employee.html', {'form': form})

def update_delete(request):
    employees = Employee.objects.all()
    return render(request, 'update_delete.html', {'employees': employees})

def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        if request.method == "POST":
            form = EmployeeForm(request.POST, instance=employee)
            if(form.is_valid()):
               form.save()
               return redirect('home')
            else:
                return render(request, 'update_employee.html', {'form': form, 'employee': employee})
        
        form = EmployeeForm(instance=employee)
        return render(request, 'update_employee.html', {'form': form, 'employee': employee})
    
    except Employee.DoesNotExist:
        return HttpResponse("Data is Empty..!")

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        if request.method == 'POST':
            employee.delete()
            return redirect('home')
        return render(request, 'delete_employee.html', {'employee': employee})

    except Employee.DoesNotExist:
        return HttpResponse("Empty")

