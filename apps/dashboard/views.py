from django.shortcuts import render, redirect
from .forms import FieldOfStudyForm
from django.contrib.auth.decorators import login_required
from django.db.models import (
    Case,
    Count,
    ExpressionWrapper,
    F,
    IntegerField,
    Q,
    Value,
    When,
)
from .models import FieldOfStudy

def Index(request):
    ICON_MAP = {
        'python': '🐍',
        'django': 'dj',
        'html': 'HTML',
        'css': 'CSS',
        'javascript': 'JS',
        'analytics': '📊',
        'database': '🗄',
        'programming': '</>',
    }

    if request.user.is_authenticated:
        directions = (
            FieldOfStudy.objects.filter(user=request.user)
            .annotate(
                total_topics=Count('topics'),
                completed_topics=Count(
                    'topics',
                    filter=Q(topics__is_completed=True),
                ),
            )
            .annotate(
                progress_percent=Case(
                    When(total_topics=0, then=Value(0)),
                    default=ExpressionWrapper(
                        F('completed_topics') * 100 / F('total_topics'),
                        output_field=IntegerField(),
                    ),
                    output_field=IntegerField(),
                ),
            )
        )
        for direction in directions:
            direction.display_icon = ICON_MAP.get(direction.image_icon, '')
    else:
        directions = FieldOfStudy.objects.none()

    return render(
        request,
        'dashboard/index.html',
        {'directions': directions }
    )

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
