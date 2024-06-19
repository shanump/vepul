from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('success/<int:registration_number>/', views.success, name='success'),
    path('userdisplay/', views.userdisplay, name='register_and_display'),
    #path('generate-pdf/<int:registration_number>/', views.generate_pdf, name='generate_pdf'),
    path('hall_ticket_pdf/<int:registration_number>/',views.hall_ticket_pdf, name='hall_ticket_pdf'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)