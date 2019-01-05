import sqlite3

conn = sqlite3.connect('formula-1.db')
cursor = conn.cursor()


cursor.execute("""
   SELECT max(hp.pontuacao), p.nome
   FROM historico_piloto hp, piloto p, resultado r
   WHERE p.id=hp.piloto_id AND r.piloto_id=p.id GROUP BY hp.pontuacao HAVING r.rank < 3 ORDER BY hp.pontuacao desc limit 1
   
""");

    
for i in cursor.fetchall():
        print(i);
    

conn.close()
