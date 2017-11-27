'''
Created on 02/13/2017

@author: alexisbatistabustavino
'''

from django import forms
from usuarios.models import *
from usuarios.my_user import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar clave', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    cedula = forms.CharField(label='Cedula del usuario', widget=forms.TextInput)
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)
    es_medico = forms.BooleanField(required=False,label='Medico', widget=forms.CheckboxInput)
    es_paciente = forms.BooleanField(required=False,label='Paciente', widget=forms.CheckboxInput)
    is_active = forms.BooleanField(label='Activo', widget=forms.CheckboxInput)
    is_staff = forms.BooleanField(required=False,label='Staff', widget=forms.CheckboxInput)
    is_admin = forms.BooleanField(required=False,label='Admin', widget=forms.CheckboxInput)
    is_superuser = forms.BooleanField(required=False,label='Super usuario', widget=forms.CheckboxInput)

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'cedula', 'first_name','last_name',
                  'es_medico', 'es_paciente', 'is_active', 'is_staff',
                  'is_admin', 'is_superuser',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("La clave no coincide")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'is_active', 'is_admin','cedula',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','first_name','last_name', 'cedula',)

    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'username' )}),
        ('Informacion personal', {'fields': ('first_name', 'last_name', 'cedula')}),
        ('Permisos', {'fields': ('password','is_admin', 'es_medico', 'es_paciente', 'is_active', 'is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'es_paciente')
            }),
        ('Informacion personal', {'fields': ('first_name', 'last_name', 'cedula')}),
        ('Permisos', {'fields': ('is_admin', 'es_medico', 'is_active', 'is_superuser',)}),
    )
    search_fields = ('email','cedula','username',)
    ordering = ('email',)
    filter_horizontal = ()
