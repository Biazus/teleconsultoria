from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.models import Consultant

class ConsultantList(ListView):
    model = Consultant

class ConsultantCreate(CreateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantUpdate(UpdateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM', 'consultant_graduation_date']

class ConsultantDelete(DeleteView):
    model = Consultant
    success_url = reverse_lazy('consultant_list', 'consultant_graduation_date')
    
    def delete(self, request, *args, **kwargs):
        query = get_object_or_404(Consultant, consultant_id=kwargs.get('pk'))
        query.delete()
        messages.info(request, 'Deletado com sucesso.')
        return HttpResponseRedirect(self.success_url)
