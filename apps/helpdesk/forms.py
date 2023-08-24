from django import forms
from .models import Ticket
#from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget



class TicketForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Ticket
        fields = "__all__"