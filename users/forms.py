from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import construct_instance, InlineForeignKeyField


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs=(
        {"class": "focus", "placeholder": "Ваша почта"}
    )))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs=(
        {"class": "focus", "placeholder": "Ваше имя пользователя"}
    )))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs=(
        {"class": "focus", "placeholder": "Пароль"}
    )))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs=(
        {"class": "focus", "placeholder": "Подтвердите пароль"}
    )))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     # Do whatever you want
    #     if error_case:  # Write your own error case.
    #         raise forms.ValidationError(
    #             "Error Message")  # Your own error message that will appear to the user in case the field is not valid
    #     return email  # In case everything is fine just return user's input.

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        return password2

    def _post_clean(self):
        opts = self._meta

        exclude = self._get_validation_exclusions()

        for name, field in self.fields.items():
            if isinstance(field, InlineForeignKeyField):
                exclude.add(name)

        try:
            self.instance = construct_instance(
                self, self.instance, opts.fields, opts.exclude
            )
        except ValidationError as e:
            self._update_errors(e)

        try:
            self.instance.full_clean(exclude=exclude, validate_unique=False)
        except ValidationError as e:
            self._update_errors(e)

        # Validate uniqueness if needed.
        if self._validate_unique:
            self.validate_unique()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user

    # TODO: ADD A RUS VALIDATE MAYBE
    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
