from django import forms

class NameForm(forms.Form):
    # inputted_text = forms.CharField(label='inputted_text')
    inputted_text = forms.CharField(widget=forms.Textarea, label='')
