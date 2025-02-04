from django.shortcuts import render
from users.forms import RegisterForm,LoginForm
from .forms import ContactForm,DailyForm
from django.contrib.auth.hashers import make_password,check_password
from users.models import CustomUser
from .models import Daily
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

def index(request):
    form1 = RegisterForm()
    form2 = LoginForm()
    form3 = ContactForm()
    form4 = DailyForm()
    dailys = Daily.objects.none()
    form11 = RegisterForm()

    if request.method == "POST":
        if "register" in request.POST:
            form1 = RegisterForm(request.POST)
            if form1.is_valid():
                user = form1.save()
                login(request, user)
                print("Kayıt Olundu Ve Giriş Yapıldı")
                return redirect('index')
            else:
                messages.warning(request,form1.errors)

        elif "login" in request.POST:
            form2 = LoginForm(request.POST)
            if form2.is_valid():
                username = form2.cleaned_data.get("username")
                password = form2.cleaned_data.get("password")

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    print("Başarıyla Giriş Yapıldı")
                    return redirect('index')
                else:
                    try:
                        user1 = CustomUser.objects.get(username=username)
                        print(f"Kullanıcı Bulundu: {user1}")
                        print(f"is_active: {user1.is_active}")
                        print(f"Form Data: {form2.cleaned_data}")

                        if check_password(password, user1.password):
                            print("Şifre Doğru!")
                        else:
                            print("Şifre Yanlış!")
                    except CustomUser.DoesNotExist:
                        print(f"Geçersiz giriş: Kullanıcı Adı: {username}, Şifre: {password}")
                        messages.warning(request,'Kullanıcı Bulunamadı')
        
        elif "contact" in request.POST:
            form3 = ContactForm(request.POST)
            if form3.is_valid():
                form3.save()
                print("Form Başarıyla Kaydedildi")
                messages.success(request,"İletişim Formu Başarıyla Gönderildi")
                return redirect('index')
            else:
                messages.warning(request,form3.errors)
                print(form3.errors)

        elif "dailyadd" in request.POST:
            form4 = DailyForm(request.POST)
            if form4.is_valid():
                formsave = form4.save(commit=False)
                formsave.author = request.user
                formsave.save()
                messages.success(request,"Günlük Başarıyla Eklendi.")
                print("Günlük Başarıyla Eklendi")
                return redirect('index')
            else:
                messages.warning(form4.errors)
                print(form4.errors)

        elif "userdetail" in request.POST:
            user = CustomUser.objects.get(username=request.user)
            form11 = RegisterForm(request.POST, instance=user)
            if form11.is_valid():
                updateduser = form11.save()
                login(request, updateduser)
                print("Bilgiler Başarıyla Düzenlendi")
                messages.success(request,"Bilgiler Başarıyla Düzenlendi")
            else:
                print(form11.errors)
                messages.warning(request,form11.errors)
                return redirect('index')
            

    
    elif request.user.is_authenticated:
        dailys = Daily.objects.filter(author=request.user)
        print(dailys)
    else:
        dailys = Daily.objects.none()

    return render(request, "index.html", {"form1": form1, "form2":form2, "form3":form3, "form4":form4, "dailys":dailys, "form11":form11})



def dailydetail(request,pk):
    daily = get_object_or_404(Daily,pk=pk)
    context = {
        "daily":daily
    }
    return render(request,"dailydetail.html",context)