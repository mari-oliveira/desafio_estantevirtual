import sqlite3

conn = sqlite3.connect('formula-1.db')
cursor_temporada = conn.cursor()
cursor_pontuacao = conn.cursor()

cursor_temporada.execute('SELECT ano FROM temporada ORDER BY ano DESC LIMIT 10')

for i in cursor_temporada.fetchall():
    ano = i[0]
    cursor_pontuacao.execute("""
    SELECT AVG(pontuacao)
     FROM (
       SELECT hp.pontuacao
         FROM corrida c
         JOIN historico_piloto hp ON (c.id=hp.corrida_id)
         JOIN piloto p ON (p.id=hp.piloto_id)
           WHERE temporada_ano = """+str(ano)+""" ORDER BY hp.pontuacao DESC LIMIT 20)""")
    for j in cursor_pontuacao.fetchall():
        print(j);
    

conn.close()
