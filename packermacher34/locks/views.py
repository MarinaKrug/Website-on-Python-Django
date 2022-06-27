from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView

from locks.forms import AddMessageForm
from locks.models import *
from locks.telegram import send_message

menu = [{'title': 'ГЛАВНАЯ', 'url_name': 'home'},
        {'title': 'АКЦИИ', 'url_name': 'show_sale'},
        {'title': 'КОНТАКТЫ', 'url_name': 'show_contacts'},
        {'title': 'УСЛУГИ', 'url_name': 'show_services'},
        {'title': 'ГАЛЕРЕЯ', 'url_name': 'show_gallery'},
        ]


def index(request):
    context = {'menu': menu,
               'title': 'Главная страница'}

    return render(request, 'locks/index.html', context=context)


def contacts(request):

    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid:
            form.save()
            message = 'Заявка: Имя: ' + form.cleaned_data['name'] + '  ' + 'Телефон: ' + form.cleaned_data['phone_number'] + '  ' + 'Сообщение: ' + form.cleaned_data['message']
            send_message(message)
            try:
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка отправки заявки')
    else:
        form = AddMessageForm()
    context = {'menu': menu,
               'form': form,
               'title': 'Контакты'}
    return render(request, 'locks/contacts.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница  НЕ найдена</h1>')


class Sale(ListView):
    model = Sales
    template_name = 'locks/sale.html'
    context_object_name = 'sale'
    extra_context = {'title': "Акции"}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Sale, self).get_context_data(**kwargs)
        context['menu'] = menu
        return context


class Services(ListView):
    model = Price
    template_name = 'locks/services.html'
    context_object_name = 'price'
    extra_context = {'title': "Услуги"}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Services, self).get_context_data(**kwargs)
        context['menu'] = menu
        return context


class Galleries(ListView):
    model = Gallery
    template_name = 'locks/gallery.html'
    context_object_name = 'gallery'
    allow_empty = False

    def get_queryset(self):
        return Gallery.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        context['title'] = "Галерея"
        return context



class Categories(ListView):
    model = Gallery
    cats = Category.objects.all()
    template_name = 'locks/gallery.html'
    context_object_name = 'gallery'
    allow_empty = False
    slug_url_kwarg = 'cat_slug'

    def get_user_context(self, **kwargs):
        context = kwargs

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


    def get_queryset(self):
        print(self.kwargs)
        return Gallery.objects.filter(cat__slug=self.kwargs['cat_slug'])



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['gallery'][0].cat_id
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['gallery'][0].cat)

        return context

