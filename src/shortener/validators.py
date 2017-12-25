from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	if "http" in value:
		final_value = value
	else:
		final_value = "http://" + value

	try:
		url_validator(final_value)
	except:
		raise forms.ValidationError("This is an invalid URL")

	return final_value

def validate_dot(value):
	if not '.' in value:
		raise ValidationError("URL must contain a .[dot]")
	return value