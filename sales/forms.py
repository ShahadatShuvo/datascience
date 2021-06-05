from django import forms

CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
)


class SalesSearchForm(forms.Form):
    date_from = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    date_to = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
