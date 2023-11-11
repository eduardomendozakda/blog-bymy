from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bymy.views import HomePage, SettingsUser, WallpaperCreate, WallpaperDelete, WallpaperDetail, WallpaperUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', SettingsUser.as_view(), name='profile'),
    path('create/', WallpaperCreate.as_view(), name='create'),
    path('detail/<int:pk>', WallpaperDetail.as_view(), name='detail'),
    path('update/<int:pk>', WallpaperDelete.as_view(), name='delete'),
    path('delete/<int:pk>', WallpaperUpdate.as_view(), name='update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)