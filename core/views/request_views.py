from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.models import Request

def home(request):
    return render_to_response('/core/requests', {})

class RequestList(ListView):
    model = Request
    fields = ['request_id',]

class RequestCreate(CreateView):
    model = Request
    success_url = reverse_lazy('request_list')
    fields = ['request_id',]

class RequestUpdate(UpdateView):
    model = Request
    success_url = reverse_lazy('request_list')
    fields = ['request_id',]

class RequestDelete(DeleteView):
    model = Request
    success_url = reverse_lazy('request_list')
