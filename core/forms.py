from django import forms
from core.models import Requester, Request, Tag, Consultant

my_default_errors = {
    'required': 'Campo obrigatório',
    'unique': 'Já existe um registro com esse valor',
    'invalid': 'Por favor digite apenas dígitos'
}
date_errors = {
    'required': 'Campo obrigatório',
    'invalid': 'Por favor informe uma data do tipo dd/mm/aaaa (exemplo: 31/12/2015)'
}

class RequesterForm(forms.ModelForm):
    requester_CPF = forms.IntegerField(error_messages=my_default_errors, label="CPF")
    requester_name = forms.CharField(error_messages=my_default_errors, label="Nome")
    
    class Meta:
        model = Requester
        fields = ['requester_name', 'requester_email', 'requester_phone', 'requester_CPF']

class RequestForm(forms.ModelForm):
    requester = forms.ModelChoiceField(queryset=Requester.objects.all(), error_messages=my_default_errors, label="Solicitante")
    request_description = forms.CharField(widget=forms.Textarea, error_messages=my_default_errors, label="Descrição")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), error_messages=my_default_errors, required=False)
    
    class Meta:
        model = Request
        fields = ['request_id','requester','request_description', 'tags']
    
class TagForm(forms.ModelForm):
    tag_name = forms.CharField(error_messages=my_default_errors, label="Nome da Tag")
    
    class Meta:
        model = Tag
        fields = ['tag_name',]
        
class ConsultantForm(forms.ModelForm):
    consultant_name = forms.CharField(error_messages=my_default_errors, label="Nome")
    consultant_CRM = forms.IntegerField(error_messages=my_default_errors, label="CRM")
    consultant_graduation_date = forms.DateField(error_messages=date_errors, label="Data de formatura", input_formats=['%d-%m-%Y', '%d-%m-%y', '%d/%m/%Y','%d/%m/%y'])
    
    class Meta:
        model = Consultant
        fields = ['consultant_name', 'consultant_CRM', 'consultant_graduation_date']
