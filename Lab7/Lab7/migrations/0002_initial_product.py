from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial_category'),  # Указываем зависимость от предыдущей миграции
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='api.Category', on_delete=models.CASCADE)),
            ],
        ),
    ]
