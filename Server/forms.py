from django import forms


class MenuForm(forms.Form):
    meat_count = forms.IntegerField(min_value=1)
    veggie_count = forms.IntegerField(min_value=1)