from django import forms


class ApplicationForm(forms.Form):
    menu_name = forms.CharField(max_length=80)
    menu_cat = forms.CharField(max_length=80)
    description = forms.TextInput(max_length=80)
    order_date = forms.DateField()
    price = forms.IntegerField(max_length=5)
