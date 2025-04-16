from pyexpat.errors import messages
from django.shortcuts import redirect, render 
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from.models import *
from .gestion import classmodifkesform, createkessform, gestion, modifkessform
from django.contrib import messages

def home(request):
    return render(request, 'config/dashboard.html')

def main(request):
    administrateurs = Administrateur.objects.all()
    gère = Gère.objects.all()
    t_gère = gère.count()
    c_gère = gère.filter(status='created').count() 
    u_gère = gère.filter(status='updated').count()
    d_gère = gère.filter(status='desactivated').count()  
    context = {'gère' : gère,
               'administrateurs' : administrateurs,
               't_gère' : t_gère,
               'c_gère' : c_gère,
               'u_gère' : u_gère,
               'd_gère' : d_gère}
    return render(request, 'config/main.html', context)


def administrateur(request,pk):
    administrateurs = Administrateur.objects.get(id=pk)
    gère = administrateurs.gère_set.all()
    utilisateurs = Utilisateur.objects.all()
    context = {'administrateurs': administrateurs,
               'gère': gère}
    return render(request, 'config/administrateur.html', context)
    
def utilisateur(request):
   utilisateurs = Utilisateur.objects.all()
   return render(request, 'config/utilisateur.html', {'utilisateur': utilisateurs})

def create (request):
    form : gestion()
    context={ 'form':form }
    return render(request, 'config/ma_gestion.html', context )
   

def createkess(request):
  form = createkessform()

  if request.method == 'POST':
    
    form = createkessform(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request ,  ' Utulisateur Créer Avec Succées')  
 
    return redirect('tablekes')
    {'form':form}
  return render(request , 'config/kescreateform.html',  {'fm':form    } )



def tablekes(request):
  kess= kes.objects.all()

  return render(request,'config/tablekes.html', {'kess':kess})






def delete(request,nkes): 
    order = kes.objects.get(nkes=nkes) 
    if request.method == 'POST':  
        order.delete()
        return redirect('tablekes')

    context = {'order':order}

    return render(request , 'config/delete_form.html', context )



def update(request,nkes): 
    order = kes.objects.get(nkes=nkes)
    form =  classmodifkesform(instance=order) 
    if request.method == 'POST': 
       form =  classmodifkesform(request.POST, instance=order)
       if form.is_valid():
           form.save()
         
           return redirect('tablekes')

    context = {'form':form}

    return render(request , 'config/updatekes.html', context )



 