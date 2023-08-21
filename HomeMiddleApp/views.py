from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View
from django import forms
from .models import *

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class CreatedPage(TemplateView):
    template_name = 'creado.html'

class ClientShowView(View):
    template_name = 'show_client.html'

    def get(self, request, id):
        viewData = {}
        viewData["title"] = "Clients - Online Store"
        viewData["subtitle"] =  "List of clients"
        viewData["client"] = get_object_or_404(Client,pk=id)
        
        return render(request, self.template_name, viewData)


def DeleteClient(request, id):
    cliente = get_object_or_404(Client,pk=id)
    if cliente:
        cliente.delete()
        return redirect('client_index')
    else:
        return redirect('home')

    

class CreateClient(View):
    template_name = 'client_form.html'

    def get(self, request):
        form = ClientForm()
        viewData = {}
        viewData["title"] = "Clients - Online Store"
        viewData["subtitle"] =  "List of clients"
        viewData["form"] = form

        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ClientForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('creado')
        else:
            viewData = {}
            viewData["title"] = "Clients - Online Store"
            viewData["subtitle"] =  "List of clients"
            viewData["form"] = form

            return render(request, self.template_name, viewData)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['password','address','email','credit_card_info','user_name']


class ClientIndexView(TemplateView):
    template_name = 'client_index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Clients - Online Store"
        viewData["subtitle"] =  "List of clients"
        viewData["clients"] = Client.objects.all()

        return render(request, self.template_name, viewData)
    