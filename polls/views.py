from django.shortcuts import redirect, render

from polls.models import Data

# Create your views here.
def index(request):
    if request.method == 'POST':
        names = request.POST.getlist('addmore[]')
        
        for name in names:
            data = Data(name=name)
            data.save()
        
        return redirect('/')  # Redirect to a success page
        
    return render(request,'index.html')