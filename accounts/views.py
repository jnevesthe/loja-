from django.shortcuts import render, redirect
from .forms import Register, EditProfile
from  django.views.generic import TemplateView  
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required

class Home(TemplateView):

    template_name="accounts/home.html"
    
    
def signin(request):
    
    if request.method=='POST':
        form=Register(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=Register()    
    return render(request, 'accounts/signin.html', {'form': form})       
    
def login_view(request):
        
    if request.method=='POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password') 
            
            
        user=authenticate(username=username, password=password)
        if(user):
            login(request, user)
            return redirect('profile')
        else:
                error="Usuario ou Senha erradas"
    else:
        error="Preencha Tudo"                
    return render(request, 'accounts/login.html', {'error':error})                
                
def logout_view(request):
    logout(request)    
    return redirect('login')     

@login_required                                
def profile(request):
    return render(request, 'accounts/profile.html')   
    

    
def edit(request):

    if request.method=='POST':
        
        form=EditProfile(request.POST, request.FILES, request.user) 
        
        if form.is_valid():
            form.save()
            return redirect('profile')    
                                                                           
    else:
        form=EditProfile(instance=request.user)                                                 
                
    return render(request, 'accounts/edit.html', {'form':form})                    
                        
                                
    
    
    
    
                                                                     
                                                            
                                                                                                                                                 
                                                