from django.views import generic
from .models import MenuModel, MEAL_TYPE

#the name of "quesryset" and "template_name" have to be exactly written as such for Django to 
# interpret the data associated with it 

class MenuList(generic.ListView):
    queryset = MenuModel.objects.order_by('date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = MenuModel
    template_name = 'menu_item_detail.html'