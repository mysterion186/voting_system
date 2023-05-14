# Generated by Django 4.2.1 on 2023-05-14 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_type', models.CharField(max_length=100)),
                ('voting_method', models.CharField(max_length=150)),
                ('voting_delay', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(max_length=150)),
                ('private_key', models.CharField(max_length=150)),
                ('nonce', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weight_arrays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=1.0)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_votes', models.CharField(choices=[('Commit', 'Commit'), ('reveal', 'reveal'), ('Fully encrypted', 'Fully encrypted'), ('fully open', 'fully open')], max_length=100)),
                ('encryption_distribution_method', models.CharField(choices=[('voter_encryption_method', 'voter_encryption_method'), ('Burner anonymous wallet', 'Burner anonymous wallet'), ('Open wallet', 'Open wallet')], max_length=100)),
                ('vote_encryption_method', models.CharField(choices=[('Homomorphism', 'Homomorphism'), ('Public key hashing user(commit and reveal)', 'Public key hashing user(commit and reveal)'), ('Direct reveal', 'Direct reveal')], max_length=100)),
                ('list_of_voters', models.JSONField()),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('notification_per_user', models.IntegerField()),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('weight_arrays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.weight_arrays')),
            ],
        ),
        migrations.CreateModel(
            name='New_voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.wallet')),
            ],
        ),
    ]
