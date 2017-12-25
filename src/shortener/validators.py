from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	value_1_valid = False
	value_2_valid = False
	try:
		url_validator(value)
	except:
		value_1_valid = True
	value_2_url = "http://" + value
	try:
		url_validator(value_2_url)
	except:
		value_2_valid = True
	if value_1_valid == False and value_2_valid == False:
		raise ValidationError("Invalid URL for this field")
	return value

def validate_dot_com(value):
	if not '.com' in value:
		raise ValidationError("URL must contain .com")
	return value