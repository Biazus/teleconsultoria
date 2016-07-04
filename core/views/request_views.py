from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.models import Request

class RequestList(ListView):
    model = Request
    
    def get_queryset(self):
        queryset = Request.objects.all()
        if self.request.GET.get('q'):
            #search for tags based on the given value (ignores case)
            queryset = queryset.filter(tags__tag_name__iexact=self.request.GET.get('q')) 
        return queryset

class RequestCreate(CreateView):
    model = Request
    success_url = reverse_lazy('request_list')
    fields = ['request_id','requester','request_description', 'tags']

class RequestUpdate(UpdateView):
    model = Request
    success_url = reverse_lazy('request_list')
    fields = ['request_id','requester','request_description', 'tags']
    
class RequestDelete(DeleteView):
    model = Request
    success_url = reverse_lazy('request_list')
    
    def delete(self, request, *args, **kwargs):
        query = get_object_or_404(Request, request_id=kwargs.get('pk'))
        query.delete()
        messages.info(request, 'Deletado com sucesso.')
        return HttpResponseRedirect(self.success_url)
