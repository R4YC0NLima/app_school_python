# Notas de Provas acadêmicas

<p style="text-align: justify">
    O objetivo desse projeto é desenvolver uma Rest Api de Alunos aprovados em provas acadêmicas.
</p>

<p>Requisitos obrigatórios:</p>
<ul>
    <li>Cadastrar gabaritos de cada prova</li>
    <li>Cadastrar as resposta de cada aluno para cada prova</li>
    <li>Verificar a nota final de cada aluno</li>
    <li>Listar os alunos aprovados</li>
</ul>

 <table style="width:100%">
    <thead>
      <tr>
        <th></th>
        <th>Ambiente de trabalho</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Docker</td>
        <td><a target="_blank" href="https://www.docker.com/">https://www.docker.com/</a></td>
      </tr>   
      <tr>
        <td>DJango</td>
        <td><a target="_blank" href="https://docs.djangoproject.com/en/3.1/">https://docs.djangoproject.com/en/3.1//</a></td>
      </tr>   
      <tr>
        <td>Insomnia</td>
        <td><a target="_blank" href="https://insomnia.rest/">https://insomnia.rest/</a></td>
      </tr>    
    </tbody>
</table>


### Development

- Página principal
    - http://localhost

- Página admin
    - http://localhost/admin


## Comandos de execução

O primeiro build do projeto, execute:
```
$ docker-compose up -d --build
```

Em comum, execute
```
$ docker-compose up -d
```

Para derrubar os container, execute:
```
$ docker-compose down
```

Para entrar no container do python e fazer instalações de dependências:
```
$ docker exec -it python-school sh
```

### Commands Python dentro do container de python: python-school

criação de app django
```
$ python ./manage.py startapp {app_label}
```

create models from existing database
```
$ python ./manage.py inspectdb > {path/to/models.py}
```

execute migration
```
$ python ./manage.py migrate
```

create a migration file
```
$ python ./manage.py makemigrations
```

create dump fixture files
```
$ python ./manage.py dumpdata {app_label.model} --indent 2 > {path/to/fuxture.json}
```

load data from fixture files
```
$ python ./manage.py loaddata --verbosity 2 > {path/to/fuxture.json}
```

create an admin account
```
$ python ./manage.py createsuperuser
```

