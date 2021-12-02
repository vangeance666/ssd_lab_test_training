
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

from wtforms.validators import DataRequired, Length

# from wtforms import validators as 

# class wtforms.validators.ValidationError(message='', *args, **kwargs)[source]
# class wtforms.validators.StopValidation(message='', *args, **kwargs)[source]
# class wtforms.validators.DataRequired(message=None)[source]
# class wtforms.validators.Email(message=None, granular_message=False, check_deliverability=False, 
# class wtforms.validators.EqualTo(fieldname, message=None)[source]
# class wtforms.validators.InputRequired(message=None)[source]
# class wtforms.validators.IPAddress(ipv4=True, ipv6=False, message=None)[source]
# class wtforms.validators.Length(min=- 1, max=- 1, message=None)[source]
# class wtforms.validators.MacAddress(message=None)[source]
# class wtforms.validators.NumberRange(min=None, max=None, message=None)[source]
# class wtforms.validators.Optional(strip_whitespace=True)[source]
# class wtforms.validators.Regexp(regex, flags=0, message=None)[source]
# class wtforms.validators.URL(require_tld=True, message=None)[source]
# class wtforms.validators.UUID(message=None)[source]
# class wtforms.validators.AnyOf(values, message=None, values_formatter=None)[source]
# class wtforms.validators.NoneOf(values, message=None, values_formatter=None)[source]

class SearchForm(FlaskForm):
	search_text = StringField('search', validators=[DataRequired()])
	submit = SubmitField('SearchSubmit')

	# username = StringField('username'
	# 	, validators=[DataRequired(), Length(max=16)])

	# password = PasswordField('password'
	# 	, validators=[DataRequired()])




# login
# appointment
# otp

# payee:contact form
# support: contact form

# updateprofile: 

