from django.urls import include, path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/enviar-email', views.enviar_email, name='enviar_email'),
    path('accounts/', include('allauth.urls')),
]
