from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("polls/", include("polls.urls")),#any route starting with (have polls included in routes must be directed to that (polls) app)
    path("admin/", admin.site.urls),#global admin (default admin)
    path("api/portfolio/", include("portfolio.urls")),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)