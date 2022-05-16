from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class GetAnswersForm(forms.Form):
    field = forms.CharField()
    value = forms.CharField()
