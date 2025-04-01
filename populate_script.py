import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from cursos.models import Aluno

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = '{}{}{}{}'.format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))
        data_nascimento = fake.date_of_birth(minimum_age=6, maximum_age=17)
        p = Aluno(nome=nome, email=email, rg=rg, cpf=cpf, data_nascimento=data_nascimento)
        p.save()

criando_pessoas(50)
print('Sucesso!')
