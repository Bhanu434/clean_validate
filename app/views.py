from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_Dept(request):
    EDFO=DeptForms()
    d={'EDFO':EDFO}
    if request.method=='POST':
        EDDO=DeptForms(request.POST)
        if EDDO.is_valid():
            Dno=EDDO.cleaned_data['Deptno']
            Dna=EDDO.cleaned_data['Dname']
            Dloc=EDDO.cleaned_data['Dloc']
            DO=Dept.objects.get_or_create(Deptno=Dno,Dname=Dna,Dloc=Dloc)[0]
            DO.save()
            return HttpResponse('Data Inserted ')
    return render(request,'insert_Dept.html',d)


def insert_Emp(request):
    EEFO=EmpForms()
    d={'EEFO':EEFO}
    if request.method=='POST':
        EEDO=EmpForms(request.POST)
        if EEDO.is_valid():
            Eno=EEDO.cleaned_data['Empno']
            En=EEDO.cleaned_data['Ename']
            sal=EEDO.cleaned_data['sal']
            Dn=EEDO.cleaned_data['Deptno']
            DO=Dept.objects.get(Deptno=Dn)
            EO=Emp.objects.get_or_create(Empno=Eno,Ename=En,sal=sal,Deptno=DO)[0]
            EO.save()
            return HttpResponse('data inserted in Emp')
    return render(request,'insert_Emp.html',d)