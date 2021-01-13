from pymysql import connect, cursors
import pandas as pd

#Definição para conexão no banco de dados
conexao = connect(host='',
	user='',
	password='',
	db='',
	cursorclass=cursors.DictCursor)

#Definindo o periodo de consulta
dtini = '2019-11-01'
dtfim = '2019-12-31'

ano_mes = dtini[:7]
ano_mes = ano_mes.replace('-','')
partition = 'p' + ano_mes

Query = """
SELECT
	<colunas>
	FROM
	schema.tabela PARTITION("""+partition+""") a
	WHERE
	a. BETWEEN '"""+dtini+""" 00:00:00' AND '"""+dtfim+""" 23:59:59'
GROUP BY 	
"""

#Abrindo banco e execuntando a query
recordset = conexao.cursor()
recordset.execute(Query)

#Resultado recebera todo o resultado da query
resultado = recordset.fetchall()

#Encerrando a conexão
conexao.close()

#Para ver a impressão
for row in resultado:
	print(row)

#Cria arquivo que recebera o resultado da query
#ArquivoTxt = open('C:\\Users\\...\\.txt', 'w')

ArquivoCsv = 'C:\\Users\\...\\'

df = pd.DataFrame(resultado)
df.to_csv(ArquivoCsv + dtfim + '.csv',index=False)

print('Queries executadas')
