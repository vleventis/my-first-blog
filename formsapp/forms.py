from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class CreditForm(forms.Form):
    your_credit = forms.IntegerField(label='Your credit')

class TeleForm(forms.Form):
    your_duration = forms.IntegerField(label='Your call duration')
    your_call = forms.CharField(max_length=12, label='Number you want to call')