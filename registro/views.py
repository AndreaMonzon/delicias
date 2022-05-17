from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from registro.forms import SignUpForm
from registro.models import DatosAdicionales


def registro(request):
    data ={
        'form':SignUpForm()
    }
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            nombre_usuario = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            telefono = form.cleaned_data.get('telefono')
            user = authenticate(username=nombre_usuario, password=raw_password)
            login(request, user)
            dato_usuario = User.objects.get(username= nombre_usuario)
            registrar_tel = DatosAdicionales(
                user=dato_usuario,
                telefono=telefono,)
            registrar_tel.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registro/registro.html',data)