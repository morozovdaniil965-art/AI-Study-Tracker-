from django.shortcuts import render, redirect
from .forms import FieldOfStudyForm

def Index(request):

    return render( request, 'dashboard/index.html')


def CreateSubject(request):

    return render( request, 'dashboard/create_subject.html')


def CreateFieldOfStudy(request):

    if request.method == 'POST':

        form = FieldOfStudyForm(request.POST)

        if form.is_valid():

            object = form.save(commit=False)

            object.user = request.user

            object.save()

            return redirect('dashboard:index')


    else:
        form = FieldOfStudyForm()

    return render(request,'dashboard/create_subject.html',{'form':form})