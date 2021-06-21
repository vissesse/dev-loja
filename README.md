Loja_tranzações, Django

Esta aplicação tem como finalidade mostrar as tranzações de um grupos de lojas
Ela carrega os dados apartir de um arquivo carredado no formulario da pagina 
inicial, apartir dele mostra as informações importada por loja informações essas:
valor, de uma tranzaçao feita, seja de entrada ou saida, data de tranzacao, hora
cartão pelo qual se fez a tranzação e od depois dados associado a tranzação

## Aplicações necessarias
Tem de ter as plicações pré-instalado
```
posgresSQL
python3
python3-psycopg2
    
```


Criar um banco de dados com nome `loja_tranzacao` 


## Para Instalar

Para instalar as dependências do projeto, executar:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations
`

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate"
```

## Para Executar

Para executar o Servidor de testes do Django, execute:

```bash
python manage.py runserver
```

