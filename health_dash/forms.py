from django import forms
FIELD_CHOICES = [
    ('#', 'Select Field'),
    ('dummy_total_pop', 'Population'),

   
]

OPERATOR_CHOICES = [
    ('=', '='),
    ('<', '<'),
    ('>', '>'),
]

class QueryForm(forms.Form):
    field  = forms.CharField(widget = forms.Select(choices=FIELD_CHOICES,attrs={'class': 'form-control ajax_change'}) )
    operator= forms.CharField(label='Select Operator', widget=forms.Select(choices=OPERATOR_CHOICES,attrs={'class': 'form-control'}))
    value = forms.CharField(label='Enter Value',widget=forms.NumberInput(attrs={'class': 'form-control'}))
