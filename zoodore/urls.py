from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', ),
    path('admin/', admin.site.urls),
    path('profile/', include('account.urls'))
]
