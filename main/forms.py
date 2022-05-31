from django import forms
from main.models import Category, Professionnel, Demande_client, UserProfil
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext_lazy as _

#Creez vos formulaire ici>

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProfessionnelForm(forms.ModelForm):
    class Meta:
        model = Professionnel
        fields = '__all__'


class Demande_clientForm(forms.ModelForm):

    class Meta:
        model = Demande_client
        fields = ['demande_sujet', 'demande_description', 'demande_category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['demande_sujet'].label = "Sujet"
        self.fields['demande_description'].label = "Description"
        self.fields['demande_category'].label = "Categorie: "
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-success mt-3"))


class Demande_clientForm1(forms.ModelForm):

    class Meta:
        model = Demande_client
        fields = ['demande_sujet', 'demande_description', 'demande_category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['demande_sujet'].label = "Sujet"
        self.fields['demande_description'].label = "Description"
        self.fields['demande_category'].label = "Categorie: "
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class="btn btn-success mt-3"))


class UserProfilForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = [ 'user_prenom', 'user_nom', 'user_tel', 'user_email', 'user_adresse']
        labels = {
            'user_prenom': _('Prenom'),
            'user_nom': _('Nom'),
            'user_tel': _('Telephone'),
            'user_email': _('Email'),
            'user_adresse': _('Adresse'),
        }
        error_messages = {
            'user_prenom': {
                'max_length': _("Ce prenom est trop long."),
            },
            'user_nom': {
                'max_length': _("Ce Nom est trop long."),
            },
            'user_tel': {
                'errors': _("Ce numero est incorrect ou deja utiliser."),
            },
            'user_email': {
                'errors': _("Cet email est incorrect ou deja utiliser."),
            },
            'user_adresse': {
                'max_length': _("Cette adresse est incorrect."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_prenom'].label = "Prenom"
        self.fields['user_nom'].label = "Nom"
        self.fields['user_tel'].label = "Telephone"
        self.fields['user_email'].label = "Email"
        self.fields['user_adresse'].label = "Adresse"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer', css_class="btn btn-success mt-4"))
