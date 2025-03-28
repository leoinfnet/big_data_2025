import csv
import random

# Listando alguns times europeus
times_europeus = [
    "Real Madrid", "Barcelona", "Bayern Munich", "Borussia Dortmund", "Paris Saint-Germain", 
    "Lyon", "Manchester City", "Liverpool", "Chelsea", "Arsenal", "Juventus", "AC Milan", 
    "Atlético de Madrid", "Sevilla", "Tottenham Hotspur", "Manchester United", "Inter Milan", 
    "Napoli", "RB Leipzig", "Benfica"
]

# Função para gerar uma partida aleatória
def gerar_partida():
    time_casa = random.choice(times_europeus)
    time_visitante = random.choice(times_europeus)
    
    # Garantir que o time da casa não seja o mesmo que o visitante
    while time_casa == time_visitante:
        time_visitante = random.choice(times_europeus)
    
    # Gerando gols aleatórios (de 0 a 5)
    gols_casa = random.randint(0, 5)
    gols_visitante = random.randint(0, 5)
    
    return (time_casa, time_visitante, gols_casa, gols_visitante)

# Definindo o nome do arquivo CSV
arquivo_csv = "partidas_europeias_10000.csv"

# Abrindo o arquivo para escrita
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escrevendo o cabeçalho do CSV
    writer.writerow(["Time da Casa", "Time Visitante", "Gols da Casa", "Gols Visitante"])
    
    # Gerando e escrevendo 10.000 partidas
    for _ in range(10000):
        partida = gerar_partida()
        writer.writerow(partida)

print(f"Arquivo {arquivo_csv} criado com 10.000 partidas!")
