from django.shortcuts import render
from .models import*
# Create your views here.
def index(request):
	if request.method == 'POST':
		n = request.POST['Name']
		e = request.POST['Email']
		s = request.POST['Subject']
		m = request.POST['Message']
		Buyurtmalar.objects.create(name=n, email=e,subject=s,message=m,)
		print('#'*50)
	else:
		print('error'*10)	
	return render(request,'index.html')	