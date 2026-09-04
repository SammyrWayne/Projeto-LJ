# Sistema de Lava Jato

Sistema de gerenciamento de clientes desenvolvido em **Python com Streamlit**.

O projeto foi criado com o objetivo de praticar conceitos de programação, manipulação de dados, validação de informações, autenticação e criação de dashboards.

## Sobre o projeto

O sistema permite realizar o cadastro de clientes de um lava jato, armazenar os dados em arquivo CSV, consultar clientes cadastrados e visualizar informações através de um dashboard.

Também possui um sistema de login para restringir o acesso às funcionalidades do sistema.

## Funcionalidades

* Sistema de login
* Cadastro de clientes
* Validação de CPF
* Armazenamento de dados em arquivo CSV
* Consulta de clientes cadastrados
* Busca de clientes pelo nome
* Dashboard com quantidade de clientes
* Gráfico de distribuição das marcas dos veículos
* Exclusão dos dados cadastrados
* Menu lateral para navegação
* Interface personalizada com Streamlit

## Dados cadastrados

O sistema armazena as seguintes informações:

* Nome completo
* CPF
* Endereço
* Data de nascimento
* Tipo de cliente
* Marca do veículo

Os dados são armazenados no arquivo:

`clientes2.csv`

## Tecnologias utilizadas

O projeto utiliza:

* Python
* Streamlit
* Pandas
* Plotly
* CSV
* validate-docbr

## Estrutura do projeto

```text
lava-jato/
│
├── app.py
├── login2.py
├── clientes2.csv
├── requirements.txt
└── README.md
```

O arquivo `app.py` contém as principais funcionalidades do sistema.

O arquivo `login2.py` é responsável pela tela e validação de login.

O arquivo `clientes2.csv` é utilizado para armazenar os clientes cadastrados.

## Dashboard

O dashboard apresenta algumas informações gerais do sistema, como:

* Total de clientes cadastrados
* Status do sistema
* Quantidade de cadastros

Também é apresentado um gráfico em formato de pizza utilizando **Plotly**, mostrando a distribuição das marcas dos veículos dos clientes.

## Cadastro de clientes

Na área de cadastro é possível informar os dados pessoais do cliente e selecionar a marca do veículo.

Antes de salvar um cadastro, o sistema verifica se o CPF informado é válido utilizando a biblioteca `validate-docbr`.

Quando o CPF é válido, ele é formatado automaticamente antes de ser armazenado.

## Consulta de clientes

Na página de clientes é possível visualizar todos os registros armazenados.

Também existe um campo de pesquisa que permite buscar um cliente através do nome.

A pesquisa não diferencia letras maiúsculas e minúsculas.

## Instalação

Para executar o projeto, primeiro clone o repositório:

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DA_PASTA
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## requirements.txt

Um exemplo das principais dependências utilizadas no projeto:

```text
streamlit
pandas
plotly
validate-docbr
```

## Executando o sistema

Execute o projeto com:

```bash
streamlit run app.py
```

Depois disso, o Streamlit abrirá o sistema no navegador.

## Funcionamento dos dados

Os clientes são armazenados utilizando arquivos CSV.

Quando o primeiro cliente é cadastrado, o sistema cria automaticamente o arquivo e adiciona as seguintes colunas:

```text
Nome
CPF
Endereco
Nascimento
Tipo
Marca
```

Os novos clientes são adicionados ao mesmo arquivo.

## Organização do sistema

O sistema possui três áreas principais:

### Dashboard

Apresenta informações gerais e gráficos relacionados aos clientes cadastrados.

### Cadastro

Permite cadastrar novos clientes e validar o CPF informado.

### Clientes

Permite visualizar, pesquisar e excluir os dados armazenados.

## Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Análise e Desenvolvimento de Sistemas**.

Durante o desenvolvimento, foram praticados conceitos como:

* Lógica de programação
* Funções em Python
* Manipulação de arquivos
* Manipulação de dados com Pandas
* Validação de documentos
* Desenvolvimento de interfaces com Streamlit
* Criação de dashboards
* Uso de bibliotecas externas
* Organização de código
* Controle de sessão
* Persistência simples de dados

## Melhorias futuras

Algumas melhorias que podem ser implementadas no projeto:

* Utilização de banco de dados SQLite
* Cadastro de veículos
* Cadastro de serviços
* Controle de pagamentos
* Histórico de lavagens
* Edição de clientes
* Exclusão individual de clientes
* Relatórios financeiros
* Controle de usuários
* Criptografia de senhas
* Melhorias na segurança do login
* Exportação de relatórios
* Dashboard financeiro

## Autor

**Sammyr**

Estudante de Análise e Desenvolvimento de Sistemas.

Projeto desenvolvido para aprendizado e prática de desenvolvimento de software.
