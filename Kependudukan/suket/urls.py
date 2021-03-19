from django.urls import path
from . import views

urlpatterns  = [
    path('borang', views.borang_isian),
    path('konfirmasi', views.konfirmasi_borang),
    path('daftar', views.daftar_borang),
    path('hapus/<int:id>', views.hapus_borang),
    path('pdf/<int:id>', views.html_to_pdf),
]