from django import forms
from models import Service, Drivers, Equipment, Type, Department


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        widgets = {
            'service_date': forms.DateInput(attrs={'class':'datepicker'}),
            'equipment_id': forms.HiddenInput(),
        }
        fields = ('equipment_id', 'service_date', 'summary', 'notes', 'cost')


class NewServiceForm(forms.ModelForm):
    equipment_id = forms.ModelChoiceField(queryset=Equipment.objects.order_by('number'))

    class Meta:
        model = Service
        widgets = {
            'service_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('equipment_id', 'service_date', 'summary', 'notes', 'cost')


class DriverForm(forms.ModelForm):

    class Meta:
        model = Drivers
        ordering = ('first_name',)
        fields = ('first_name', 'last_name')


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        widgets = {
            'in_service': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('number', 'in_service', 'department', 'type', 'name', 'vin', 'tag', 'driver')


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('type',)


class EditEquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('number', 'type', 'name', 'vin', 'tag', 'driver')


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('department',)
