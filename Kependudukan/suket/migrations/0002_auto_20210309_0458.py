# Generated by Django 2.2 on 2021-03-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borang',
            name='jenis_surat',
            field=models.CharField(choices=[('1', 'Keluhan'), ('2', 'Pendafataran KTP'), ('3', 'Legalisir'), ('4', 'Keterangan Tidak Mampu')], default=1, max_length=40),
        ),
    ]