import pandas as pd
import matplotlib.pyplot as plt   #biblioteca para graficos,“baixo nível” Mais flexível
import seaborn as sns  #biblioteca para graficos. “alto nível” já vem com estilos bonitos. Menos flexível 
import plotly.express as px #biblioteca de graficos interativa

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head())          #ler a base
df.info()                 #informação sobre os tipos de dados da base
print(df.describe())      #informações estatisticas
print(df.shape)           #informações sobre o tamanho/dimensao da base

linhas, colunas = df.shape[0], df.shape[1] #definindo variaveis com o tamanho da base
print('Linhas:', linhas)
print('Colunas:', colunas)

print(df.columns)          #mostrar todas as colunas

novos_nomes = {            #Dicionário de renomeação
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=novos_nomes, inplace=True)    # Aplicando renomeação- onde inplace=True substitui os dados antigos de forma definitiva

print(df.head())

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
df['senioridade'].value_counts()

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
df['contrato'].value_counts()

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
df['remoto'].value_counts()

df.head()

print(df.describe(include="object"))  

"""Com isso já conseguimos responder algumas perguntas, como:

Qual o nível de experiência mais comum na base de dados?
Qual é o tipo de contrato mais frequente?
Qual o cargo mais frequente na amostra?
De qual país são a maioria dos profissionais da base?
Qual é o país onde mais empresas da amostra estão sediadas?
Qual o regime de trabalho mais comum?
Qual é o tamanho mais comum das empresas na amostra? """

print(df.isnull)  #indica onde nao tem dado falso

print(df.isnull().sum()) #soma todos os campos sem dados, no caso desse dataframe 10 campos com ausencia da informação ano

print(df["ano"].unique()) #o unique() é aplicado a coluna "ano" varrendo a coluna e retornando uma lista contendo apenas valores unicos.

print(df[df.isnull().any(axis=1)]) #um filtro da base de tudo que é nulo e imprime

df_limpo = df.dropna() 
print(df_limpo.isnull().sum()) #remoção de dados nulos em nova variavel df_limpo para nao alterar o df "original"

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))  #vai ser alterada a coluna ano dessa nova variavel passando de float para o tipo int

print(df_limpo)

df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição de senioridade I")        #sera verificado a frequencia dos valores da coluna "senioridade" escolhendo o parametro "bar" e o titulo que deseja exibir no grafico

plt.show()  #exibe o grafico em nova tela

sns.barplot(data=df_limpo, x='senioridade', y='usd') 

plt.show()  #exibe o grafico em nova tela pela biblioteca seaborn *2*

plt.figure(figsize=(8,5))           #Definindo tamanho da figura
sns.barplot(data=df_limpo, x='senioridade', y='usd')    
plt.title("Salário médio por senioridade III")      #titulo do grafico  
plt.xlabel("Senioridade")                       #nome no eixo X
plt.ylabel("Salário médio anual (USD)")         #nome no eixo Y
plt.show()                                      #print 

df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True) #agrupar a coluna senioridade e usd que contem os valores e verificar no grafico do maior para o menor

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index #coloca em ordem as linhas que estavam sem o index

plt.figure(figsize=(8,5)) #novo grafico com novo parametro order
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem) 
plt.title("Salário médio por senioridade IV")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

plt.figure(figsize=(10,5))  #tamanho do grafico
sns.histplot(df_limpo['usd'], bins = 50, kde=True)  #define a coluna a ser analisada com parametro que define qual intervalo entre as barras que vao ser gerados nesse histograma e parametro que adiciona linha pra facilitar visualização
plt.title("Distribuição dos salários anuais V") #
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd']) #novo grafico com serve para resumir e visualizar a distribuição de um conjunto de dados e identificar possíveis outliers (valores muito fora do padrão)
plt.title("Boxplot Salário VI")
plt.xlabel("Salário em USD")
plt.show()

ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo'] #sera avaliado pelo nivel de experiencia esse novo grafico

plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
plt.title("Boxplot da distribuição por senioridade VII")
plt.xlabel("Salário em USD")
plt.show()

ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title("Boxplot da distribuição por senioridade VIII")
plt.xlabel("Salário em USD")
plt.show()

    #gráfico de média salarial por senioridade em barras usando o plotly
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade IX',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})

fig.show()

    #grafico pizza com as respectivas colunas
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho X'

          )

fig.show()

#novo grafico pizza tipo rosquinha
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho XI',
             hole=0.5
          )

fig.show()

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho XII',
             hole=0.5
          )
fig.update_traces(textinfo='percent+label')
fig.show()
