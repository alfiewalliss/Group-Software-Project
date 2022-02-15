from django.http import HttpResponse


def index(request):
    return HttpResponse("Landing Page - Group Software project")