from django.shortcuts import render, redirect
from .models import Course, Enrollment
from django.shortcuts import render, get_object_or_404
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {"courses": courses}
    return render(request, template_name, context)


def details(request, slug):  # detalhar o curso buscado na primeira página / detalhe a ser configurado
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context["course"] = course
    context["form"] = form
    template_name = 'courses/details.html'
    return render(request, template_name, context)


@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        enrollment.active()
        messages.success(request, "Inscrição Realizada com Sucesso")
    else:
        messages.info(request, 'Você já está inscrito neste Curso')
    return redirect('dashboard')
