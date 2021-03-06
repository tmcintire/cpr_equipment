from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponseRedirect, RequestContext
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from models import Equipment, Drivers, Service, Type, Department
from forms import ServiceForm, DriverForm, EquipmentForm, TypeForm, NewServiceForm, DepartmentForm

# Create your views here.


@login_required()
def equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment.html', locals())


@login_required()
def drivers_list(request):
    if request.POST:
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/drivers/')
    else:
        form = DriverForm(request.POST)

    drivers = Drivers.objects.all()

    return render(request, 'drivers.html', locals())


@login_required()
def details(request, equipment_id):
    """display all of the equipment details"""
    equipment = Equipment.objects.get(id=equipment_id)
    total = Service.objects.filter(equipment_id=equipment_id).aggregate(Sum('cost')).values()[0]
    services = Service.objects.filter(equipment_id=equipment_id)

    if request.POST:
        equipments = Equipment.objects.get(id=equipment_id)
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/details/%s' % equipment_id)
    else:
        equipments = Equipment.objects.get(id=equipment_id)
        form = ServiceForm(initial={'equipment_id': equipments})

    return render(request, 'details.html', locals())


@login_required()
def addservice(request, equipment_id):
    if request.POST:
        equipments = Equipment.objects.get(id=equipment_id)
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addservice/')
    else:
        equipments = Equipment.objects.get(id=equipment_id)
        form = ServiceForm(initial={'equipment': equipments})

    equipments = get_object_or_404(Equipment, id=equipment_id)

    return render(request, 'addservice.html', locals())


@login_required()
def newservice(request):
    if request.POST:
        equipments = Equipment.objects.all()
        form = NewServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service Log Added!')
            return HttpResponseRedirect('/addservice/')
    else:
        equipments = Equipment.objects.all()
        form = NewServiceForm()

    return render(request, 'addservice.html', locals())


@login_required()
def servicelog(request):

    total = Service.objects.aggregate(Sum('cost')).values()[0]
    servicelog = Service.objects.all().order_by("service_date")
    equipment = Equipment.objects.all()

    return render(request, 'servicelog.html', locals())


@login_required()
def serviceview(request, service_id):
    service = Service.objects.get(id=service_id)

    return render(request, 'servicedetails.html', locals())


@login_required()
def editservice(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    t = "Edit"

    if request.POST:
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/service/%s' % service_id)

    else:
        form = ServiceForm(instance=service)

    return render_to_response("editservice.html", {
        'form': form,
        't': t,
        'service': service,
    }, context_instance=RequestContext(request))


@login_required()
def deleteservice(request, service_id):
    service = get_object_or_404(Service, pk=service_id).delete()

    messages.success(request, 'Service Removed!')
    return render(request, 'deleted.html', locals())


@login_required()
def addequipment(request):
    if request.POST:
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipment/')
    else:
        form = EquipmentForm()

    return render(request, 'addequipment.html', locals())


@login_required()
def editequipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    t = "Edit"

    if request.POST:
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/equipment/')

    else:
        form = EquipmentForm(instance=equipment)

    return render_to_response("editequipment.html", {
        'form': form,
        't': t,
        'equipment': equipment,
    }, context_instance=RequestContext(request))


def yearreport(request, year):
    costs = {}
    for item in Equipment.objects.all():
        costs[item] = item.service_set.filter(service_date__year=year).aggregate(Sum('cost'))

    total = Service.objects.filter(service_date__year=year).aggregate(Sum('cost')).values()[0]

    return render(request, 'reports.html', locals())


@login_required()
def addtype(request):
    if request.POST:
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addtype/')
    else:
        form = TypeForm()

    types = Type.objects.all()

    return render(request, 'addtypes.html', locals())


@login_required()
def adddriver(request):
    if request.POST:
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/drivers/')
    else:
        form = DriverForm()

    return render(request, 'drivers.html', locals())


@login_required()
def editdriver(request, driver_id):
    drivers = get_object_or_404(Drivers, pk=driver_id)
    vehicles = Equipment.objects.filter(driver_id=driver_id)
    t = "Edit"

    if request.POST:
        form = DriverForm(request.POST, instance=drivers)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/drivers/')

    else:
        form = DriverForm(instance=drivers)

    return render_to_response("editdriver.html", {
        'form': form,
        't': t,
        'drivers': drivers,
        'vehicles': vehicles,
    }, context_instance=RequestContext(request))


@login_required()
def deletedriver(request, driver_id):
    drivers = get_object_or_404(Drivers, pk=driver_id).delete()
    for d in Equipment.objects.filter(driver=drivers):
        d.driver = None
        d.save()

    messages.success(request, 'Driver Removed!')
    return render(request, 'deleted.html', locals())


@login_required()
def adddepartment(request):
    if request.POST:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adddepartment/')
    else:
        form = DepartmentForm()

    department = Department.objects.all()

    return render(request, 'adddepartment.html', locals())


