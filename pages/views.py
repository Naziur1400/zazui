from django.shortcuts import render


# Create your views here.

def about_us(request):
	return render(request,'pages/about.html')

def contact_us(request):
	# msg=''
	# if request.method=='POST':
	# 	form=forms.ContactForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		msg='Data has been saved'
	# form=forms.ContactForm()
	return render(request, 'pages/contact.html')
	# {'form':form,'msg':msg}


