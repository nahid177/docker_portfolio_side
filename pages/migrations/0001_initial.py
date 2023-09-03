# Generated by Django 4.2.3 on 2023-09-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.TextField(default='Lorem ipsum dolor sit amet, consectetur', max_length=2047)),
                ('image', models.ImageField(help_text='Recommended resolution: 1:1 - Example: 500px * 500px', upload_to='')),
                ('resume', models.FileField(blank=True, help_text='Optionally, recommended format: PDF', null=True, upload_to='resume/')),
                ('skills', models.CharField(default='Python Javascript CSS SQL', help_text='Listing separated by spaces', max_length=511)),
                ('tools', models.CharField(default='Figma Docker Git Ngnix', help_text='Listing separated by spaces', max_length=511)),
                ('interessts', models.CharField(default='Music Linux Open-Source Pixel-Art', help_text='Listing separated by spaces', max_length=511)),
                ('markdown_content', models.TextField(blank=True, help_text='Main About-Content. Markdown supported', max_length=4095, null=True)),
                ('seo', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='SEO Description')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='IndexSiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='Welcome...', max_length=255)),
                ('intro_text', models.TextField(default='Lorem ipsum dolor sit amet, consectetur', max_length=2047)),
                ('seo', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='SEO Description')),
            ],
            options={
                'verbose_name': 'Home',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31, unique=True)),
                ('slug', models.CharField(max_length=31, unique=True)),
                ('content', models.TextField(help_text='Markdown supported.', max_length=4095)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('seo', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='SEO Description')),
            ],
            options={
                'verbose_name': 'Page-Footer',
                'verbose_name_plural': 'Pages-Footer',
                'ordering': ['-updated'],
            },
        ),
    ]
