# Notas de Provas acadêmicas

<p style="text-align: justify">
    O objetivo desse projeto é desenvolver uma Rest Api de Alunos aprovados em provas acadêmicas.
</p>

<p>Requisitos obrigaórios:</p>
<ul>
    <li>Cadatrar gabaritos de cada prova</li>
    <li>Cadatrar as resposta de cada aluno para cada prova</li>
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

## Comandos de execução

O primeiro build do projeto, execute:
docker-compose up -d --build

Em comum, execute
docker-compose up -d

Para derrubar os container, execute:
docker-compose down


## Dependence

* [Python](https://www.python.org/) 3.7
* [Django](https://www.djangoproject.com/) 2.1

## Outros suportes

### Development

- Main site
    - http://localhost

- Admin page
    - http://localhost/admin

### Commands
create a django app
```
$ docker exec python ./manage.py startapp {app_label}
```

create models from existing database
```
$ docker exec python ./manage.py inspectdb > {path/to/models.py}
```

execute migration
```
$ docker exec python ./manage.py migrate
```

create a migration file
```
$ docker exec python ./manage.py makemigrations
```

create dump fixture files
```
$ docker exec python ./manage.py dumpdata {app_label.model} --indent 2 > {path/to/fuxture.json}
```

load data from fixture files
```
$ docker exec python ./manage.py loaddata --verbosity 2 > {path/to/fuxture.json}
```

create an admin account
```
$ docker exec -it python ./manage.py createsuperuser
```

