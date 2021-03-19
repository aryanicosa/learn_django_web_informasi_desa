from django.db import models

class Borang(models.Model):
    nama = models.CharField(max_length=20)
    nik = models.CharField(max_length=20)
    alamat = models.CharField(max_length=30)
    no_telpon = models.CharField(max_length=13)
    email = models.EmailField(max_length=20)
    jenis_surat = models.CharField(
        max_length=40, choices=[
        (None, "Jenis Surat"),    
        ('Keluhan', "Keluhan"),
        ('Daftar KTP', "Pendafataran KTP"),
        ('Legalisir', "Legalisir"),
        ('KTM', "Keterangan Tidak Mampu"),
    ], default=None)
    keterangan_tambahan = models.TextField(default="Surat ini diajukan untuk keperluan ...... yang membutuhkan surat pengantar dari pihak kelurahan mohon kiranya pengajuan saya dapat diterima.")
