from django.views.generic import CreateView
from django.urls import reverse
from .models import Formulaire

class BlogCreateView(CreateView):
    model = Formulaire
    template_name = "Erdanius.html"
    fields = ['Nom','Email','Entreprise','type_demande','message']
    context_object_name = "form"
    
    def get_success_url(self):
        return reverse("")
