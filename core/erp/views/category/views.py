from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from core.erp.forms import CategoryForm
from core.erp.models import Category


def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request, "category/list.html", data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        context['create_url'] = reverse_lazy("category_create")
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy("category_list")
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy("category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy("category_list")
        return context
