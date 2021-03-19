from django.shortcuts import redirect, render
from .models import Borang
from .forms import Borang_form

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string

from weasyprint import HTML
import pdfkit
import datetime


def borang_isian(request):
    form = Borang_form()
    return render(request, 'borang.html', { 'form': form })
    

def daftar_borang(request):
    data = Borang.objects.all()
    return render(request, 'daftar_borang_masuk.html', { 'data': data })

def hapus_borang(request, id):
    Borang.objects.get(id=id).delete()
    return redirect('/suket/daftar')

def html_to_pdf(request, id):
    data = Borang.objects.get(id=id)
    #Belum berhasil langsung konvert ke pdf

    #url = str(request.build_absolute_uri())
    #print(url)
    #pdfkit.from_url(url, 'doc.pdf')
    return render(request, 'pdf.html', { 'data': data })

    """
    data = Borang.objects.get(id=id)
    html_string = render_to_string('pdf.html', { 'data': data, 'date': datetime.date.today(), 'month': datetime.date.today().strftime("%B") })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/document.pdf')    

    fs = FileSystemStorage('/tmp')
    with fs.open('document.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="document.pdf"'
        return response
    """
    


def konfirmasi_borang(request):
    if request.POST:
        form = Borang_form(request.POST)
        if form.is_valid():
            form.save()
        else :
            #dibuat jangan sampai harus isi lagi
            return redirect('/suket/borang')
        return render(request, 'konfirmasi.html', {'form': form.instance, 'date': datetime.date.today(), 'month': datetime.date.today().strftime("%B")})
        # ini kalau front end nya langsung oleh django, jika menggunakan frontend lain (e.g vue.js)
        # yang diberikan harus data json, bukan instance dari model
    return redirect('/suket/borang')