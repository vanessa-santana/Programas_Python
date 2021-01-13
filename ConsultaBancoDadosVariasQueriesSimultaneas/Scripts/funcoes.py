from pymysql import connect, cursors
from datetime import date, timedelta
from tqdm import tqdm
import variaveis



class Conexao:
	@staticmethod
	
	def conectar():

		cn = connect(host = variaveis.host,
			user = variaveis.user,
			password =variaveis.password,
			#db = variaveis.db,
			charset = variaveis.charset,
			cursorclass = cursors.DictCursor)
		
		return cn


	def executar(Query):

		ObjetoDeConexao = Conexao.conectar()
		rs = ObjetoDeConexao.cursor()
		rs.execute(Query)
		Resultado = rs.fetchall()
		ObjetoDeConexao.close()

		return Resultado




class Tempo:
	@staticmethod
	
	def ontem():
		Intervalo = timedelta(1)
		Ontem = date.today() - Intervalo

		return Ontem
	

	def particao(Valor):
		Partition = 'p' + str(Valor).replace('-', '')[0:6]
		
		return Partition




class SaidaTxt:
	@staticmethod
	
	def escrever_arquivo_txt(NomeArquivo, Resultado, Separador):

		Arquivo = open(NomeArquivo, 'a')
		
		for row in Resultado:

			for k, v in row.items():
				
				if k == list(row.keys())[-1]:
					Arquivo.write(str(v))
				else:
					Arquivo.write(str(v) + Separador)

			Arquivo.write('\n')

		Arquivo.close()




class Processo:
	@staticmethod
	
	def consulta(Mensagem, ListaDataInicial, ListaDataFinal, ListaQueries, NomeArquivo, Separador):
		
		print('\n' + Mensagem + '\n')
		
		BarraProgresso = tqdm(ListaDataInicial)

		y = 0
		for row in BarraProgresso:
			BarraProgresso.set_description('Datas ' + row)

			x = 0
			for row in tqdm(ListaQueries, desc='Queries', leave=False, dynamic_ncols=True):

				Partiti = Tempo.particao(ListaDataInicial[y])

				ResultadoConsulta = Conexao.executar(ListaQueries[x](Partiti, ListaDataInicial[y], ListaDataFinal[y]))
				SaidaTxt.escrever_arquivo_txt(NomeArquivo, ResultadoConsulta, Separador)

				x += 1
			y += 1