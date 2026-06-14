from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import FileResponse, Http404

from .forms import KyrgyzUserCreationForm, KyrgyzAuthenticationForm

from .models import (
    Lecture,
    Laboratory,
    Presentation,
    Material,
    Test,
)


# ================= HOME =================

def home(request):

    context = {
        'lectures_count': Lecture.objects.count(),
        'laboratories_count': Laboratory.objects.count(),
        'presentations_count': Presentation.objects.count(),
        'materials_count': Material.objects.count(),
    }

    return render(
        request,
        'main/home.html',
        context
    )


# ================= LECTURES =================

def lectures(request):

    lectures = Lecture.objects.all().order_by('-created_at')

    return render(
        request,
        'main/lectures.html',
        {
            'lectures': lectures
        }
    )


def lecture_detail(request, lecture_id):

    lecture = get_object_or_404(
        Lecture,
        id=lecture_id
    )

    return render(
        request,
        'main/lecture_detail.html',
        {
            'lecture': lecture
        }
    )


def lecture_file_view(request, lecture_id):

    lecture = get_object_or_404(
        Lecture,
        id=lecture_id
    )

    return render(
        request,
        'main/lecture_file_view.html',
        {
            'lecture': lecture
        }
    )


@xframe_options_exempt
def lecture_pdf_stream(request, lecture_id):

    lecture = get_object_or_404(
        Lecture,
        id=lecture_id
    )

    if not lecture.file:

        raise Http404()

    return FileResponse(
        lecture.file.open('rb'),
        content_type='application/pdf'
    )


# ================= LABORATORIES =================

def laboratories(request):

    laboratories = Laboratory.objects.all()

    return render(
        request,
        'main/laboratories.html',
        {
            'laboratories': laboratories
        }
    )


# ================= TESTS =================

def tests(request):

    tests = Test.objects.all()

    return render(
        request,
        'main/tests.html',
        {
            'tests': tests
        }
    )


def test_detail(request, test_id):

    test = get_object_or_404(
        Test,
        id=test_id
    )

    questions = test.questions.all()

    score = 0

    total = questions.count()

    finished = False


    if request.method == 'POST':

        finished = True

        for question in questions:

            answer = request.POST.get(
                f'question_{question.id}'
            )

            question.user_answer = answer

            if answer == question.correct_answer:

                score += 1

    else:

        for question in questions:

            question.user_answer = None


    percent = 0

    if total > 0:

        percent = int(score / total * 100)


    return render(

        request,

        'main/test_detail.html',

        {

            'test': test,

            'questions': questions,

            'finished': finished,

            'score': score,

            'total': total,

            'percent': percent,

        }

    )


# ================= PRESENTATIONS =================

def presentation(request):

    presentations = Presentation.objects.all()

    return render(
        request,
        'main/presentation.html',
        {
            'presentations': presentations
        }
    )


def presentation_file_view(request, presentation_id):

    presentation = get_object_or_404(
        Presentation,
        id=presentation_id
    )

    return render(
        request,
        'main/presentation_file_view.html',
        {
            'presentation': presentation
        }
    )


@xframe_options_exempt
def presentation_pdf_stream(request, presentation_id):

    presentation = get_object_or_404(
        Presentation,
        id=presentation_id
    )

    if not presentation.file:

        raise Http404()

    return FileResponse(
        presentation.file.open('rb'),
        content_type='application/pdf'
    )


# ================= MATERIALS =================

def materials(request):

    materials = Material.objects.all()

    return render(
        request,
        'main/materials.html',
        {
            'materials': materials
        }
    )


def material_file_view(request, material_id):

    material = get_object_or_404(
        Material,
        id=material_id
    )

    return render(
        request,
        'main/material_file_view.html',
        {
            'material': material
        }
    )


@xframe_options_exempt
def material_file_stream(request, material_id):

    material = get_object_or_404(
        Material,
        id=material_id
    )

    if not material.file:
        raise Http404()

    if material.file_type == 'video':

        return FileResponse(
            material.file.open('rb'),
            content_type='video/mp4'
        )

    elif material.file_type == 'pdf':

        return FileResponse(
            material.file.open('rb'),
            content_type='application/pdf'
        )

    return FileResponse(
        material.file.open('rb')
    )

# ================= PROFILE =================

@login_required(login_url='login')
def profile(request):
    context = {

        'lectures_count': Lecture.objects.count(),

        'laboratories_count': Laboratory.objects.count(),

        'presentations_count': Presentation.objects.count(),

        'materials_count': Material.objects.count(),

        'tests_count': Test.objects.count(),

    }

    return render(
        request,
        'main/admin_panel.html',
        context
    )
    return render(
        request,
        'main/profile.html'
    )


@login_required(login_url='login')
def admin_panel(request):

    context = {

        'lectures_count': Lecture.objects.count(),

        'laboratories_count': Laboratory.objects.count(),

        'presentations_count': Presentation.objects.count(),

        'materials_count': Material.objects.count(),

        'tests_count': Test.objects.count(),

    }

    return render(

        request,

        'main/admin_panel.html',

        context

    )


@login_required(login_url='login')
def teacher_panel(request):

    return render(

        request,

        'main/teacher_panel.html'

    )


# ================= AUTH =================

def register_view(request):

    if request.method == 'POST':

        form = KyrgyzUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = KyrgyzUserCreationForm()

    return render(

        request,

        'main/register.html',

        {

            'form': form

        }

    )


def login_view(request):

    if request.method == 'POST':

        form = KyrgyzAuthenticationForm(

            request,

            data=request.POST

        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if user.is_staff:

                return redirect('admin_panel')

            else:

                return redirect('profile')

    else:

        form = KyrgyzAuthenticationForm()

    return render(

        request,

        'main/login.html',

        {

            'form': form

        }

    )


def logout_view(request):

    logout(request)

    return redirect('home')


@login_required(login_url='login')
def choose_role(request):

    return render(

        request,

        'main/choose_role.html'

    )

def laboratory_file_view(request, laboratory_id):

    laboratory = get_object_or_404(
        Laboratory,
        id=laboratory_id
    )

    return render(
        request,
        'main/laboratory_file_view.html',
        {
            'laboratory': laboratory
        }
    )


@xframe_options_exempt
def laboratory_pdf_stream(request, laboratory_id):

    laboratory = get_object_or_404(
        Laboratory,
        id=laboratory_id
    )

    if not laboratory.file:
        raise Http404()

    return FileResponse(
        laboratory.file.open('rb'),
        content_type='application/pdf'
    )