from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from core.models import Requester, Request

class RequesterList(ListView):
    model = Requester

class RequesterCreate(CreateView):
    model = Requester
    success_url = reverse_lazy('requester_list')
    fields = ['requester_name', 'requester_email', 'requester_phone', 'requester_CPF']

class RequesterUpdate(UpdateView):
    model = Requester
    success_url = reverse_lazy('requester_list')
    fields = ['requester_name', 'requester_email', 'requester_phone', 'requester_CPF']

class RequesterDelete(DeleteView):
    model = Requester
    success_url = reverse_lazy('requester_list')
    fields = ['requester_name', 'requester_email', 'requester_phone']
    
    def delete(self, request, *args, **kwargs):
        has_requests = Request.objects.filter(requester_id=kwargs.get('pk'))
        if not has_requests:
            requester = Requester.objects.get(requester_id=kwargs.get('pk'))
            requester.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            #Informar que nao é possível deletar usuário com solicitações pendentes
            return HttpResponseRedirect(self.success_url)
            
