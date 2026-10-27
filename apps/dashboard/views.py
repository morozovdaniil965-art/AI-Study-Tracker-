from django.shortcuts import render, redirect
from .forms import FieldOfStudyForm
from django.contrib.auth.decorators import login_required

def Index(request):

    return render( request, 'dashboard/index.html')


def CreateSubject(request):

    return render( request, 'dashboard/create_subject.html')

@login_required
def CreateFieldOfStudy(request):

    if request.method == 'POST':

        form = FieldOfStudyForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)

            field_of_study = form.save(commit=False)

            field_of_study.user = request.user

            field_of_study.save()

            return redirect('dashboard:index')


    else:
        form = FieldOfStudyForm()

    return render(request,'dashboard/create_subject.html',{'form':form})