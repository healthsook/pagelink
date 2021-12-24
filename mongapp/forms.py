from django import forms
from .models import Record
 
class SearchForm(forms.Form):
    check_values = forms.BooleanField(required=False)

class RecordForm(forms.ModelForm):
    cal = forms.CharField(
        label = "섭취 칼로리",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'cal'
            }
        )
    )
    walk = forms.CharField(
        label = "걸음 수    ",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'walk'
            }
        )
    )
    hour = forms.CharField(
        label = "운동 시간 (시)",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'hour'
            }
        )
    )
    min = forms.CharField(
        label = "운동 시간 (분)",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'min'
            }
        )
    )

    class Meta:
        model = Record
        fields = [
            'cal','walk','hour','min']