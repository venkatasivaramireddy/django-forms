from .models import StudentModel
from django import forms


# class StudentForm(forms.form):
#     s_reg_no=forms.integerfield(label="register_no")
#     s_name=forms.charfield(label="name")
#     s_email=forms.emailfield(label='email')
#     s_password=forms.charfield(widget=forms.passwordinput,label="password")
#     s_image=forms.imagefield(label="image")
#     s_number=forms.integerfield(label="mobile nunmber")

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields = "__all__"
        widgets = { 'password': forms.PasswordInput }
        # widgets={'gender':forms.ChoiceField()}
        exclude = ['image']