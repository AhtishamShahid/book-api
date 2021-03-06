# Generated by Django 2.2.5 on 2019-09-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('numberOfPages', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('released', models.DateField()),
                ('authors', models.ManyToManyField(to='books_api.Author')),
            ],
        ),
    ]
