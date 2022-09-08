from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render


# Create your views here.
# Model object - Single Student Data

def student_detail(request, pk):

    stu = Student.objects.get(id=pk)
    # print(stu, "\n")
    serializer = StudentSerializer(stu)
    # print(serializer, "\n")
    # print(serializer.data, "\n")
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data, "\n")
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data) #by deafault safe=True


#queryset all student data
def student_list(request):

    stu = Student.objects.all()
    # print(stu, "\n")
    serializer = StudentSerializer(stu, many=True)
    # print(serializer, "\n")
    # print(serializer.data, "\n")
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data, "\n")
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
