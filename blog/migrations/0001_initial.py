# Generated by Django 4.2.3 on 2023-09-03 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Unique identifying part of the URL', max_length=63, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, help_text='Recommended resolution: 1040px * 585px', null=True, upload_to='blog-posts/', verbose_name='Image')),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1, verbose_name='Status')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('seo', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='SEO Description')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Unique identifying part of the URL', max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=63, verbose_name='Author')),
                ('message', models.TextField(max_length=1023, verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
