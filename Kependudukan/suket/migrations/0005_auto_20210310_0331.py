# Generated by Django 2.2 on 2021-03-10 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suket', '0004_auto_20210309_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borang',
            name='jenis_surat',
            field=models.CharField(choices=[(None, 'Jenis Surat'), ('Keluhan', 'Keluhan'), ('Daftar KTP', 'Pendafataran KTP'), ('Legalisir', 'Legalisir'), ('KTM', 'Keterangan Tidak Mampu')], default=1, max_length=40),
        ),
    ]
