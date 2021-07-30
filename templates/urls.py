
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings # For Media
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns # for media





urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("app_login.urls")),
    path('blog/', include("app_blog.urls")),
    path('', views.index, name="index")

    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)