
from django .forms import ModelForm
from .models import *

class gestion(ModelForm):
    class gerer :
        model=Gère
        fields="_all_"
class createkessform(ModelForm):
     class Meta:

        model = kes
        fields ="__all__"         

class modifkessform(ModelForm):
     class Meta:

        model = kes
        fields ="__all__"   

class classmodifkesform(ModelForm):  
     class Meta:

        model = kes
        fields =['nomkes']