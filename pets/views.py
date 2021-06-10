from django.views.generic import ListView
from .models import Pet


class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
