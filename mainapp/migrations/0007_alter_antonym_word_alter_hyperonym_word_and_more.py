# Generated by Django 4.0.4 on 2022-05-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_infoadjective_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antonym',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name="so'z"),
        ),
        migrations.AlterField(
            model_name='hyperonym',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name="so'z"),
        ),
        migrations.AlterField(
            model_name='hyponym',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name="so'z"),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='adjective_level',
            field=models.CharField(choices=[('oddiy', 'Oddiy'), ('orttirma', 'Orttirma'), ('ozaytirma', 'Ozaytirma'), ('qiyosiy', 'Qiyosiy')], default='oddiy', max_length=15, verbose_name='Sifat darajasi'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='adjective_type',
            field=models.CharField(choices=[('xususiyat', 'Xususiyat sifatlari'), ('rang_tus', 'Rang – tus sifatlari'), ('maza_tam', 'Maza – ta’m sifatlari'), ('hajm_olchov', 'Hajm – o’lchov sifatlari'), ('hid', 'Hid sifatlari'), ('makon_zamon', 'Makon-zamon sifatlari')], default='xususiyat', max_length=15, verbose_name='Sifat turi'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='adjective_type_structure',
            field=models.CharField(choices=[('sodda_tub', 'Sodda tub'), ('sodda_yasama', 'Sodda yasama'), ('qoshma', "Qo'shma"), ('juft', 'Juft'), ('takroriy', 'Takroriy')], default='sodda_tub', max_length=15, verbose_name='Tuzilish jihatdan turi'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='adjectives_two',
            field=models.CharField(choices=[('asliy_sifat', 'Asliy sifat'), ('nisbiy_sifat', 'Nisbiy sifat')], default='asliy_sifat', max_length=15, verbose_name='Belgi ifodalashiga ko‘ra turi'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='antonym',
            field=models.ManyToManyField(blank=True, to='mainapp.antonym', verbose_name='Antonim'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='hyperonym',
            field=models.ManyToManyField(blank=True, to='mainapp.hyperonym', verbose_name='Giperonim'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='hyponym',
            field=models.ManyToManyField(blank=True, to='mainapp.hyponym', verbose_name='Giponim'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='review',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='synonym',
            field=models.ManyToManyField(blank=True, related_name='synonyms', to='mainapp.synonym', verbose_name='Sinonim'),
        ),
        migrations.AlterField(
            model_name='infoadjective',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name="So'z"),
        ),
        migrations.AlterField(
            model_name='synonym',
            name='word',
            field=models.CharField(max_length=100, unique=True, verbose_name="so'z"),
        ),
    ]
