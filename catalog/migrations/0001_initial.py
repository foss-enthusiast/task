# Generated by Django 5.0 on 2023-12-10 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('menu_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.node')),
            ],
            bases=('catalog.node',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.node')),
                ('parent_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_items', to='catalog.node')),
            ],
            bases=('catalog.node',),
        ),
    ]
