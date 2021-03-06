from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from core.forms import TagForm

from core.models import Tag

class TagList(ListView):
    model = Tag
    
class TagCreate(CreateView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    form_class = TagForm
    

class TagUpdate(UpdateView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    form_class = TagForm

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    
    def delete(self, request, *args, **kwargs):
        query = get_object_or_404(Tag, tag_id=kwargs.get('pk'))
        query.delete()
        messages.info(request, 'Deletado com sucesso.')
        return HttpResponseRedirect(self.success_url)
