from django.shortcuts import render
from django.http import HttpResponse
from .models import Student 

# Create your views here.

# def home(req):
#     first5=Student.objects.all()[0:3]
#     return render(req,'home.html',{'x':first5})


# def home(req):
#     data=Student.objects.all()
#     return render(req,'home.html',{'x':data})

# def home(req):
#     x = Student.objects.get(name="vansh") 
#     print(x)
#     return HttpResponse(x)

# def home(req):
#     x = Student.objects.latest()
#     print(x)
#     return HttpResponse(x)

# def home(req):
#     x = Student.objects.get(name="ragav")
#     print(x)
#     return HttpResponse(x)

# def home(req):
#     data=Student.objects.create(name="vijay",email="vijay@gmail.com",city="jabalpur")

#     return HttpResponse(data)


# def home(req):
#     data=Student.objects.filter(name="shivaji").delete()
#     return HttpResponse(data)

# def home(req):
#     data,create=Student.objects.get_or_create(name="raman",email="raman@gmail.com",city="haryana")

#     print(create)
# return HttpResponse(data)

# def home(req):
#     data,create=Student.objects.update_or_create(id=1,defaults={'name':'kholi','email':'kholi@gmail.com','city':'hydrabad'})
#     print(create)

#     return HttpResponse(data)

def home(req):
    data=Student.objects.bulk_create([Student(name='narendr',email='narender@gmail.com',city='vidisha'),Student(name='vijendr',email='vijender@gmail.com',city='indore'),Student(name='ram',email='ram@gmail.com',city='jhashi')])
    

    return HttpResponse(data)