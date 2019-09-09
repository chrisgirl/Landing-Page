from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .form import Form


# Create your views here.
def index(request):
	return render(request, 'index.html')


def form_view(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			new_msg = List(name=form.cleaned_data['name'], email=form.cleaned_data['email'], content=form.cleaned_data['content'])
			new_msg.save()
			messages.success(request, "Message Sent!")
			return redirect('landingpage:index')

		messages.warning(request, "Message not sent!")
	form = Form()
	template = 'form.html'
	return render(request, template_name=template, context={"form": form})