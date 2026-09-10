# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0005_siteconfig_hero_video_alter_siteconfig_phone_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_hero_bg', models.CharField(blank=True, default='/static/img/hero/hero_bg_3_1.png', max_length=500, verbose_name='Hero — tło/poszerzenie strony głównej')),
                ('home_att8', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.png', max_length=500, verbose_name='Oferta — zdjęcie zakładki Generalne Wykonawstwo')),
                ('home_o_nas_2', models.CharField(blank=True, default='/static/img/mbt/o-nas-2.jpg', max_length=500, verbose_name='Dlaczego MBT — zdjęcie sekcji (o-nas-2)')),
                ('home_o_nas_zespol', models.CharField(blank=True, default='/static/img/mbt/o-nas-zespol.jpg', max_length=500, verbose_name='Sekcja zespołu — tło/grupa (o-nas-zespol)')),
                ('home_realizacja', models.CharField(blank=True, default='/static/img/mbt/realizacja-eurosleeve.jpg', max_length=500, verbose_name='Realizacje na stronie głównej — karta (eurosleeve)')),
                ('home_bg_why', models.CharField(blank=True, default='/static/img/bg/why-bg3-1.png', max_length=500, verbose_name='Tło sekcji Oferta (why-bg3-1)')),
                ('home_bg_cta', models.CharField(blank=True, default='/static/img/bg/cta-bg3-1.png', max_length=500, verbose_name='Tło sekcji CTA „Wyceń projekt" (cta-bg3-1)')),
                ('home_bg_contact', models.CharField(blank=True, default='/static/img/bg/contact-bg3-1.png', max_length=500, verbose_name='Tło sekcji kontakt/aktualności (contact-bg3-1)')),
                ('home_client_group', models.CharField(blank=True, default='/static/img/normal/client_group_1-2.png', max_length=500, verbose_name='Opinie klientów — zdjęcie grupy (client_group_1-2)')),
                ('home_testi_2', models.CharField(blank=True, default='/static/img/testimonial/testi_2_2.png', max_length=500, verbose_name='Opinie klientów — zdjęcie (testi_2_2)')),
                ('work_1', models.CharField(blank=True, default='/static/img/mbt/DJI_0174-scaled-5106e265.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 1')),
                ('work_2', models.CharField(blank=True, default='/static/img/mbt/DJI_0181-1-scaled-b366f7fb.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 2')),
                ('work_3', models.CharField(blank=True, default='/static/img/mbt/DJI_3-03272d0f.jpg', max_length=500, verbose_name='Galeria pracy — zdjęcie 3')),
                ('work_4', models.CharField(blank=True, default='/static/img/mbt/DSC03626-scaled-6f5bda4e.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 4')),
                ('work_5', models.CharField(blank=True, default='/static/img/mbt/DSC03726-scaled-04284a3e.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 5')),
                ('work_6', models.CharField(blank=True, default='/static/img/mbt/DSC03730-scaled-ee7d1094.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 6')),
                ('work_7', models.CharField(blank=True, default='/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 7')),
                ('work_8', models.CharField(blank=True, default='/static/img/mbt/DSC03980-scaled-ea8b4933.jpeg', max_length=500, verbose_name='Galeria pracy — zdjęcie 8')),
                ('about_1', models.CharField(blank=True, default='/static/img/mbt/o-nas-1.jpg', max_length=500, verbose_name='O nas — zdjęcie główne (o-nas-1)')),
                ('service_1', models.CharField(blank=True, default='/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg', max_length=500, verbose_name='Oferta — zdjęcie 1 (Eurosleeve)')),
                ('service_2', models.CharField(blank=True, default='/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg', max_length=500, verbose_name='Oferta — zdjęcie 2 (budowa)')),
                ('gw_hero', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.png', max_length=500, verbose_name='GW — tło hero (ATT-8)')),
                ('gw_1', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-1-scaled-f12dacac.jpg', max_length=500, verbose_name='GW — zdjęcie 1 (ATT-1)')),
                ('gw_2', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg', max_length=500, verbose_name='GW — zdjęcie 2 (ATT-3)')),
                ('gw_3', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-4-scaled-ffc91418.jpg', max_length=500, verbose_name='GW — zdjęcie 3 (ATT-4)')),
                ('gw_4', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg', max_length=500, verbose_name='GW — zdjęcie 4 (ATT-5)')),
                ('gw_5', models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg', max_length=500, verbose_name='GW — zdjęcie 5 (ATT-6)')),
                ('gw_6', models.CharField(blank=True, default='/static/img/mbt/Fronton-1-scaled-42981731.jpg', max_length=500, verbose_name='GW — zdjęcie 6 (Fronton-1)')),
                ('gw_7', models.CharField(blank=True, default='/static/img/mbt/Fronton-2-scaled-de057284.jpg', max_length=500, verbose_name='GW — zdjęcie 7 (Fronton-2)')),
                ('gw_8', models.CharField(blank=True, default='/static/img/mbt/Huber-6-scaled-b00b8b23.jpg', max_length=500, verbose_name='GW — zdjęcie 8 (Huber)')),
                ('gw_9', models.CharField(blank=True, default='/static/img/mbt/3-2-scaled-38947c85.jpg', max_length=500, verbose_name='GW — zdjęcie 9 (3-2)')),
                ('gw_10', models.CharField(blank=True, default='/static/img/mbt/breem-e659b8f2.jpg', max_length=500, verbose_name='GW — zdjęcie 10 (BREEAM)')),
                ('gw_11', models.CharField(blank=True, default='/static/img/mbt/hala-1024x672-eb7144c9.jpg', max_length=500, verbose_name='GW — zdjęcie 11 (hala)')),
                ('gw_12', models.CharField(blank=True, default='/static/img/mbt/stokado-self-storage-krakow/main.jpg', max_length=500, verbose_name='GW — zdjęcie 12 (Stokado)')),
                ('bg_header', models.CharField(blank=True, default='/static/img/bg/header-1-bg.png', max_length=500, verbose_name='Tło nagłówka (header-1-bg)')),
                ('bg_footer', models.CharField(blank=True, default='/static/img/bg/footer-bg1-1.png', max_length=500, verbose_name='Tło stopki (footer-bg1-1)')),
                ('bg_breadcrumb', models.CharField(blank=True, default='/static/img/bg/breadcrumb-bg.png', max_length=500, verbose_name='Tło breadcrumb / podstron (breadcrumb-bg)')),
            ],
            options={
                'verbose_name': 'Zdjęcia strony',
                'verbose_name_plural': 'Zdjęcia strony',
            },
        ),
    ]
