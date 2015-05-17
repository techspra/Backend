from django.shortcuts import render
from forms import QueryForm
# Create your views here.
def getForm(request):
	if request.method == "request.POST" :
		form = QueryForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = QueryForm()
	return render(request,'query.html',{"form":form})
