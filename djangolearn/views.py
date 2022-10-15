from django.shortcuts import render, redirect
from . import models
from django.views import View


class main(View):
    def get(self, request):
        model_obj = models.sinfdoshlar.objects.all()
        return render(request, 'index.html', {"sinf": model_obj})


class adding(View):
    def post(self, request):
        model = models.sinfdoshlar()
        model.firstname = request.POST['firstname']
        model.lastname = request.POST['lastname']
        model.save()
        return redirect('main')

    def get(self, request):
        return render(request, 'adding.html')


class deleting(View):
    def post(self, request, firstname, lastname):
        model = models.sinfdoshlar.objects.get(firstname=firstname,
                                               lastname=lastname)
        model.delete()
        return redirect('main')

    def get(self, request, firstname, lastname):
        return render(request, 'delete.html')


class editing(View):
    def post(self, request, firstname, lastname):
        model = models.sinfdoshlar.objects.get(firstname=firstname,
                                               lastname=lastname)
        model.firstname = request.POST.get('firstname')
        model.lastname = request.POST.get('lastname')
        model.save()
        return redirect('main')

    def get(self, request, firstname, lastname):
        return render(request, 'edit.html')
