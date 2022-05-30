# Generated by Django 4.0.4 on 2022-05-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infonoun',
            name='noun_making',
            field=models.CharField(choices=[('morfologik', 'Morfologik usul'), ('sintaktik', 'Sintaktik usul')], default='morfologik', max_length=15, verbose_name="Ot yasalishiga ko'ra turi"),
        ),
        migrations.AlterField(
            model_name='infonoun',
            name='noun_types',
            field=models.CharField(choices=[('shaxs', 'Shaxs otlar'), ('narsa', 'Narsa otlar'), ('orin_joy', "O'rin-joy otlar"), ('faoliyat', 'Faoliyat-otlari')], default='shaxs', max_length=15, verbose_name='Ot turi'),
        ),
        migrations.AlterField(
            model_name='infonoun',
            name='noun_types_structure',
            field=models.CharField(choices=[('sodda', 'Sodda'), ('qoshma', "Qo'shma"), ('juft', 'Juft'), ('takroriy', 'Takroriy')], default='sodda', max_length=15, verbose_name="Tuzilishiga ko'ra turi"),
        ),
    ]