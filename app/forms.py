from django import forms
from .models import *
class actionForm(forms.ModelForm):
    class Meta:
        model = action
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(actionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
class purchaseForm(forms.ModelForm):
    class Meta:
        model = purchase
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(purchaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
class knowledgeForm(forms.ModelForm):
    class Meta:
        model = knowledge
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(knowledgeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
class tracking_numberForm(forms.ModelForm):
    class Meta:
        model = tracking_number
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(tracking_numberForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
"""
class order_partForm(forms.ModelForm):

    class Meta:
        model = order_part
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(order_partForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class order_callForm(forms.ModelForm):

    class Meta:
        model = order_call
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(order_callForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
"""