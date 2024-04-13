# Teste RevGas
Este é um projeto simples de uma API que consome dados de um banco de dados MYSQL, utilizando Django e Django Rest Framework para criar uma API.

### Passo a Passo 🚀
- Clone o repositório
```
git clone git@github.com:RodrigoEAMarques/test_revgas.git
cd api_revgas
```
- Instale o ambiente virtual e entre no ambiente virtual
```
python3 -m venv venv
```
- Se for ambiente Windows
```
venv\Scripts\activate
```
- Se for ambiente Linux
```
source venv\bin\activate
```
- Instale as dependências
```
pip install - requirements.txt
```
- Execute as migrações do Banco de Dados:
```
python manage.py migrate
```
OBS:. Não esqueça de colocar as suas credenciais do mysql dentro do settings.py
OBS:. NAME é o nome dado ao database, ou seja, então se na sua máquina tiver outro nome
precisará trocar o nome
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dados',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '12345678'
    }
}
```
- Ultima observação
Dentro da pasta api e dentro de models.py, lembre-se também de mudar o nome da tabela
onde está os dados
```
class Meta:
        db_table = 'bancos'
```

- Inicar servidor django
```
python manage.py runserver
```

Ele ficará disponível em http://127.0.0.1:8000/
