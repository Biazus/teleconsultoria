from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.models import Consultant

def home(request):
    return render_to_response('/core/consultants', {})


class ConsultantList(ListView):
    model = Consultant
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantCreate(CreateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantUpdate(UpdateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantDelete(DeleteView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
