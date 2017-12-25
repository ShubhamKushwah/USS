from django import forms
from .validators import validate_url, validate_dot

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='',
    	validators=[validate_url, validate_dot],
    	widget = forms.TextInput(
    			attrs = {"placeholder": "Enter your long url"}
    		)
    	)
