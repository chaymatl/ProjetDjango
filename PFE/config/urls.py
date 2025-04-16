    
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home),
    path('utilisateur/',views.utilisateur ,name="utilisateur"),
    #path('administrateur/',views.administrateur), 
    path('administrateur/<str:pk>',views.administrateur, name="administrateur"), 
    path('main/',views.main),  

    
    path('create/',views.create , name="create" ), 

    
    path('createkess/',views.createkess , name="createkess" ),  
    
    
    path('tablekes/',views.tablekes , name="tablekes" ),  
    
    
#path('Numero_order/<int:Numero_order_mission>/', views.updateorder, name="updateorder"),
    
      path('update/<str:nkes>' ,views.update, name="update"),
    
    path('delete/<int:nkes>', views.delete, name="delete"),

  
]
   
