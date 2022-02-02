from django.shortcuts import render, redirect
from .models import Empleado #importamos nuesto modelo
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def createView(request):
    return render(request, 'create.html')

    
#creo la funcion Store que almancena los datos del formulario
def store(request):
    emp = Empleado()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_emial = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.emp_address = request.POST.get('emp_address')
    emp.save()
    messages.success(request, "Empleado agregado correctamente")
    return redirect('/gestion_crud/create')

#creo la funion para vizualizar y renderizar las cambios
def index(request):
    emp = Empleado.objects.all()
    return render(request, 'index.html', {'emp':emp})

""" data = serializers.serialize('json', index.objects.all())
    return JsonResponse({'data': data})"""
    
#creo la funcion que encuentra al usuario con su informacion detallada
def detailEmp(request, pk):
    emp = Empleado.objects.get(id=pk)
    return render(request, 'details.html', {'emp':emp})

#creo la funcion para eliminar un registro por ID
def deleteEmp(request, pk):
    emp = Empleado.objects.get(id=pk)
    emp.delete()
    messages.success(request, "empleado elimado")
    return redirect('/gestion_crud/')
#creo la funcion para actualizar datos 'X' regstro de la DB
def updateEmp(resquest, pk):
    emp = Empleado.objects.get(id=pk)
    return render(resquest, 'update.html', {'emp':emp})

def update(request, pk):
    print('in')
    emp = Empleado.objects.get(id=pk)
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_emial = request.POST.get('emp_emial')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.emp_address = request.POST.get('emp_address')
    emp.save()
    messages.success(request, "se actualizo correctamente")
    return redirect('/gestion_crud/')
#funcion para convertir los datos y retornar un Json
def jsondata(request):
    data = list(Empleado.objects.values())
    return JsonResponse(data, safe = False)
    
"""def indexList(request):
    data = serializers.serialize('json', index.objects.all())
    #return JsonResponse({'data': data})
    return HttpResponse(data, content_type='application/json')"""
    
    
    
    
