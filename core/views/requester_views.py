from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

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
    
    def delete(self, request, *args, **kwargs):
        #get_object_or_404 is preventing long-running tabs server error
        #instead of showing a server error, shows to the user that hes trying to access a non existing resource 
        requester = get_object_or_404(Requester, requester_id=kwargs.get('pk'))
        requests = Request.objects.filter(requester_id=kwargs.get('pk'))
        requests.delete()
        requester.delete()
        messages.info(request, 'Deletado com sucesso.')
        return HttpResponseRedirect(self.success_url)
