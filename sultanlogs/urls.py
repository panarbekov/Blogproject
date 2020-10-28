
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [   
    path("", homepage, name="home"),
    path('admin/', admin.site.urls),
    path("test/", test, name="test"),
    path("contacts/", contacts, name="contacts"),
    path("top/", top, name = "top" ),
    path("profile/<int:id>/", profile, name="profile"),
    path("article/", include("core.urls")),
    # path("test2/", another_test, name="test")
    path("test2/", FirstUserDetailView.as_view(), name="test-2-cbv"),
    path("user/<id>", user_fbv )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
