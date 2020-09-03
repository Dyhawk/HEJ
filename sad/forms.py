from django import forms

# start below
class UploadFileForm(forms.Form):
    itemNum = forms.IntegerField()
    weight = forms.FloatField()
    file = forms.FileField()

class AsycudaFileForm(forms.Form):
    xml_file = forms.FileField()

class UploadSalesForm(forms.Form):
    sales_file = forms.FileField()