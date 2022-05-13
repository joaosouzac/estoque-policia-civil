# Estoque-Polícia-Civil API



> Atividade prática utilizando as plataformas de desenvolvimento *Django* e *Django REST Framework* para a segunda fase do processo seletivo da 
> *Polícia Civil do Ceará*

<br>

## 💻 Pré-requisitos

<!---Estes são as tecnologias utilizadas durante o desenvolviemnto da API--->
* A versão mais recente do `Python` instalada na máquina.
* A versão 4.0.4 do `Django` e a versão 3.13.1 do `Django REST Framework` instaladas na máquina.
* A versão 9.1.0 da biblioteca `Pillow` instalada na máquina.

## 🚀 Rodando a API na máquina

Após baixar ou clonar o repósitorio no GitHub, execute o terminal de sua escolha dentro da pasta `estoque-policia-civil`. Então, rode o comando:
```
python manage.py runserver
```

## ☕ Padrões de URL da API

Os padrões de URL para acessar a API seguem abaixo:  
### Raíz da API

```
localhost:8000/estoque/v1
```

### Lista de Objetos, Armas e Munições
Para acessar uma instânica específica da tabela do banco de dados, adicione: `/<id_do_objeto>` no final da URL.

```
localhost:8000/estoque/v1/objetos
```
```
localhost:8000/estoque/v1/armas
```
```
localhost:8000/estoque/v1/municoes
```  

### Interface de Administrador
```
localhost:8000/admin
```

Para logar, utilize as credênciais:  
```
Usuário: admin  
Senha: 1234
```

Se necessário, utilize o comando para criar um *`superuser`*:
```
python manage.py createsuperuser
```

## 📝 Créditos

Esse projeto foi criado por João Augusto de Oliveira Sousa.

[⬆ Voltar ao topo](#estoque-policia-civil)<br>
