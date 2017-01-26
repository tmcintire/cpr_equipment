from models import Service

def navbar(request):
    years = Service.objects.all().dates('service_date', 'year')

    return locals()
