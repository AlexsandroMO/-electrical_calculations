# Generated by Django 3.0.1 on 2020-01-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disjuntor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dj', models.CharField(max_length=4, verbose_name='Mini DJ Schneider')),
            ],
        ),
        migrations.CreateModel(
            name='TabelaCondutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secao', models.CharField(max_length=5, verbose_name='Seção Transversão')),
                ('capacidade_conducao', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Capacidade de Condução')),
                ('queda_tesao', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Queda de Tensão')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCircuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ckt', models.CharField(max_length=50, verbose_name='Tipo de Circuito')),
            ],
        ),
        migrations.CreateModel(
            name='ResidencDimens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=50, verbose_name='Local da Instalação')),
                ('tensa_va', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Tensão (VA)')),
                ('quant', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Quantidade')),
                ('potencia_va', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Potência (VA)')),
                ('total_va', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Total (VA)')),
                ('corrente_a', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Corrente (A)')),
                ('comprimento', models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Comprimento do Circuito (m)')),
                ('queda_tensao_ckt', models.DecimalField(blank=True, decimal_places=2, max_digits=2, verbose_name='Queda de Tensão do Circuito (%)')),
                ('queda_tensao_perm', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Queda de Tensão Permitida (%)')),
                ('queda_tensao_test', models.CharField(blank=True, max_length=3, verbose_name='Queda de Tensão')),
                ('capacidade_corrente', models.CharField(blank=True, max_length=3, verbose_name='Capacidade de Corrente')),
                ('numero_polos', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Número de Polos')),
                ('verifica_dj', models.CharField(blank=True, max_length=3, verbose_name='Verifica Disjuntor')),
                ('corrente_nominal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cable.Disjuntor', verbose_name='Corrente Nominal')),
                ('sessao_condutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cable.TabelaCondutor', verbose_name='Sessão Transversal do Condutor (mm²)')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cable.TipoCircuito', verbose_name='Tipo de Instalação')),
            ],
        ),
    ]
