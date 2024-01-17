from django.shortcuts import render
from newApp.forms import UserForm, UserExtensionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'newApp/index.html', context={})

@login_required()
def user_logout(request):
    logout(request)
    return index(request)

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print(email, password, user)
        if user:
            if user.is_active:
                login(request, user)
                return index(request)
        else:
            print('Someone tried')
            return HttpResponse('Login Failed')
    else:
        return render(request, 'newApp/login_page.html')

def user_page(request):
    registered = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        form_extension = UserExtensionForm(request.POST)
        if form.is_valid() and form_extension.is_valid():
            print(form.cleaned_data['username'])
            user = form.save()
            user.set_password(user.password)
            user.save()

            info = form_extension.save(commit=False)
            info.user = user

            if 'profile_pic' in request.FILES:
                info.profile_pic = request.FILES['profile_pic']
            info.save()
            registered = True
        else:
            print(f"Errors! {form.errors} {form_extension.errors}")

    else:
        form = UserForm()
        form_extension = UserExtensionForm()

    return render(request, 'newApp/user.html', context={'form': form,
                                                        'form_extension': form_extension,
                                                        'registered': registered})
