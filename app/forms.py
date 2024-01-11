from django import forms
from app.models import *
def validated_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('invalid data')


class DeptForms(forms.Form):
    Deptno=forms.IntegerField()
    Dname=forms.CharField(validators=[validated_a])
    Dloc=forms.CharField()

    

class EmpForms(forms.Form):
    Empno=forms.IntegerField()
    Ename=forms.CharField()
    sal=forms.IntegerField()
    dl=[[d.Deptno,d.Dname] for d in Dept.objects.all() ]
    Deptno=forms.ChoiceField(choices=dl)