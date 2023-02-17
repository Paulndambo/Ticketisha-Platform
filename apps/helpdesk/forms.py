from django import forms
from .models import Ticket
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class TicketForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Ticket
        fields = "__all__"