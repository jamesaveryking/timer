from django import forms

PRAYER_CATEGORIES = (
    ('Thanksgiving', 'Thanksgiving'),
    ('Healing', 'Healing'),
    ('Intervention', 'Intervention'),
    ('Salvation', 'Salvation'),
)

class TimerForm(forms.Form):
    timerLabel = forms.CharField(label='Timer Label', required=True)
    start_time = forms.DateTimeField(label='Start Time', disabled=True)
    end_time = forms.DateTimeField(label='End Time', disabled=True)
    total_time = forms.DateTimeField(label='Total Time', disabled=True)
    start_switch = forms.BooleanField(label='Start Switch')
    end_switch = forms.BooleanField(label='End Switch')
    start_primer = forms.BooleanField(label='Start Primer')
    end_primer = forms.BooleanField(label='End Primer')

class UserForm(forms.Form):
    user_id = forms.CharField(label='Username', max_length=35, required = True)
    first_name = forms.CharField(label = 'First Name', max_length=70, required = True)
    last_name = forms.CharField(label = 'Last Name', max_length=70, required = True)
    email_address = forms.EmailField(label = 'Email', max_length=70, required = True)
    password = forms.CharField(label = 'Password', max_length=49, required = True)
    security_question = forms.CharField(label = 'Security Question', max_length=70, required = True)
    security_answer = forms.CharField(label = 'Security Question Answer', max_length=70, required = True)
