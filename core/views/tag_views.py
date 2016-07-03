from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.models import Tag

class TagList(ListView):
    model = Tag
    
class TagCreate(CreateView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    fields = ['tag_name',]

class TagUpdate(UpdateView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    fields = ['tag_name',]

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
