from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Wallpaper
from .forms import FormCreationWallpaper

class HomePage(View):
    def get(self, request,*args, **kwargs):
        context = {
            'objects': Wallpaper.objects.all()
        }
        return render(request, 'index.html', context)

@method_decorator(login_required, name='dispatch')
class SettingsUser(View):
    def get(self, request,*args, **kwargs):
        context = {
            'objects': Wallpaper.objects.filter(author=request.user)
        }
        return render(request, 'settings_user.html', context)
    
@method_decorator(login_required, name='dispatch')   
class WallpaperCreate(View):
    def get(self, request,*args, **kwargs):
        form = FormCreationWallpaper()

        context = {
            'form': form
        }
        return render(request, 'create_wallpaper.html', context)
    
    def post(self, request,*args, **kwargs):
        form = FormCreationWallpaper()

        if request.method == 'POST':
            form = FormCreationWallpaper(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()

                return redirect('home')
            
        context = {
            'form': form
        }
            
        return render(request, 'create_wallpaper.html', context)
    
@method_decorator(login_required, name='dispatch')   
class WallpaperUpdate(View):
    def get(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Wallpaper, pk=pk)

        form = FormCreationWallpaper(object)

        context = {
            'form': form
        }
        return render(request, 'create_wallpaper.html', context)
    
    def post(self, request,*args, **kwargs):
        form = FormCreationWallpaper()

        if request.method == 'POST':
            print(request.POST)
            
        context = {
            'form': form
        }
            
        return render(request, 'create_wallpaper.html', context)
    
@method_decorator(login_required, name='dispatch')
class WallpaperDelete(View):
    def get(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Wallpaper, pk=pk)

        if not request.user == object.author:
            return redirect('home')
      
        context = {
            'object': object
        }

        return render(request, 'delete.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Wallpaper, pk=pk)

        if request.method == 'POST':
            if request.user == object.author:
                Wallpaper.delete(object)
                return redirect('home')

        context = {
        }

        return render(request, 'delete.html', context)
    
class WallpaperDetail(View):
    def get(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Wallpaper, pk=pk)

        context = {
            'object': object
        }
        return render(request, 'detail.html', context)

# Create your views here.
