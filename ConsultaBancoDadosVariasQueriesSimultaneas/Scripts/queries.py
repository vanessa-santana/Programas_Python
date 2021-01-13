class Queries():
	@staticmethod
	
	def query1(Particao, DataInicial, DataFinal):
		Query = """
		SELECT
			<colunas>,
			FROM
				schema.tabela PARTITION ("""+ Particao +""") a
			INNER JOIN
				schema.tabela b ON a. =b.
			INNER JOIN
				schema.tabela c ON c. =b.
			WHERE
				a.colunaData BETWEEN '"""+ DataInicial +"""' AND '"""+ DataFinal +"""' 
			GROUP BY
				colunas
		"""
		return Query

	def query2(Particao, DataInicial, DataFinal):
		Query = """
			<colunas>,
			FROM
				schema.tabela PARTITION ("""+ Particao +""") a
			INNER JOIN
				schema.tabela b ON a. =b.
			INNER JOIN
				schema.tabela c ON c. =b.
			WHERE
				a.colunaData BETWEEN '"""+ DataInicial +"""' AND '"""+ DataFinal +"""' 
			GROUP BY
				colunas
		"""
		return Query

