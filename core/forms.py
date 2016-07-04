from django.forms import ModelForm
from myapp.models import Requester


class RequesterForm(ModelForm):
    class Meta:
        model = Requester
        fields = ['requester_name']
