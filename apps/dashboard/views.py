from django.shortcuts import render

from django.http.response import HttpResponse

def Index(request):

    return render( request, 'dashboard/index.html')


def CreateSubject(request):

    return render( request, 'dashboard/create_subject.html')
