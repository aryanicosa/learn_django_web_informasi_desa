# Generated by Django 2.2 on 2021-03-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suket', '0005_auto_20210310_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borang',
            name='jenis_surat',
            field=models.CharField(choices=[(None, 'Jenis Surat'), ('Keluhan', 'Keluhan'), ('Daftar KTP', 'Pendafataran KTP'), ('Legalisir', 'Legalisir'), ('KTM', 'Keterangan Tidak Mampu')], default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='borang',
            name='keterangan_tambahan',
            field=models.TextField(default='Surat ini diajukan untuk keperluan ......... yang membutuhkan surat pengantar dari pihak kelurahan mohon kiranya pengajuan saya dapat diterima.', max_length=150),
        ),
    ]
