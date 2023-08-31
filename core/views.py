from django.shortcuts import render, redirect
from django.views import View
from .forms import InscricaoForm, ContactForm
from django.contrib import messages
from .models import *
from django.http import JsonResponse

from telegramProj import settings


def check_unique_email(request):
    email = request.GET.get('email', '')
    is_unique = not Inscricoes.objects.filter(email=email).exists()
    return JsonResponse({'is_unique': is_unique})

def check_unique_phone(request):
    phone = request.GET.get('phone', '')
    is_unique = not Inscricoes.objects.filter(phone=phone).exists()
    return JsonResponse({'is_unique': is_unique})



class HomeView(View):
    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('HomeView')  # Replace 'index' with the appropriate URL name for your index page
        else:
            messages.error(request, 'Erro ao enviar mensagem.\n Tente novamente.')
            return render(request, 'index.html', {'contact_form': contact_form})


    


    def get(self, request):
        contact_form = ContactForm()

    
        context = {
            'key' : settings.STRIPE_PUBLIC_KEY,
            
            'contact_form' : contact_form
        }
        return render(request, 'index.html',context)
    

class FormView(View):
    def post(self, request):
        inscricao_form = InscricaoForm(request.POST)
        if inscricao_form.is_valid():
            inscricao_form.save()
            messages.success(request, 'Inscrição feita com sucesso!')
            return redirect('HomeView')  # Replace 'index' with the appropriate URL name for your index page
        else:
            messages.error(request, 'Erro ao enviar inscrição.\n Verifique os dados e tente novamente.')
            return render(request, 'form.html', {'inscricao_form': inscricao_form})
    
    def get(self,request):

        return render(request,'form.html')
