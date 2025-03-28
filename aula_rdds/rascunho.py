from pyspark.sql import SparkSession
import csv
# Inicializando o SparkSession
spark = SparkSession.builder.appName('ExemploRDD').getOrCreate()

# Carregando o arquivo CSV como um RDD
rdd_partidas = spark.sparkContext.textFile('/temp/partidas_europeias_10000.csv')

# Ignorar o cabeçalho
cabecalho = rdd_partidas.first()
rdd_partidas = rdd_partidas.filter(lambda linha: linha != cabecalho)

# Convertendo as linhas do RDD para tuplas com dados relevantes
rdd_partidas_tuplas = rdd_partidas.map(lambda linha: linha.split(","))
rdd_partidas_tuplas = rdd_partidas_tuplas.map(lambda x: (x[0], x[1], int(x[2]), int(x[3])))

# Filtrando as partidas onde o time da casa venceu
rdd_partidas_vencedoras_casa = rdd_partidas_tuplas.filter(lambda x: x[2] > x[3])

# Contando a quantidade de vitórias por time da casa
rdd_vitorias_casa = rdd_partidas_vencedoras_casa.map(lambda x: x[0])  # Time da casa
vitorias_casa_count = rdd_vitorias_casa.countByValue()

# Definindo o nome do arquivo CSV para salvar as vitórias
arquivo_vitorias_csv = "/temp/vitorias_por_time_da_casa.csv"

# Escrevendo as vitórias no arquivo CSV
with open(arquivo_vitorias_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escrevendo o cabeçalho
    writer.writerow(["Time da Casa", "Vitórias"])
    
    # Escrevendo os dados de vitórias por time
    for time, vitorias in vitorias_casa_count.items():
        writer.writerow([time, vitorias])

print(f"Arquivo {arquivo_vitorias_csv} criado com sucesso!")
