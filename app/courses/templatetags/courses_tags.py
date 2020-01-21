from django import template
from app.courses.models import Enrollment
register = template.Library()


@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollment = Enrollment.objects.filter(user=user)
    context = {'enrollment': enrollment}
    return context


@register.simple_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)
