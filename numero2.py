import sqlite3

conn = sqlite3.connect('formula-1.db')

cursor = conn.cursor()

cursor.execute("""
   SELECT c.* FROM corrida c
   WHERE EXISTS(SELECT he.equipe_id FROM historico_equipe he WHERE he.pontuacao>0 AND c.id=he.corrida_id GROUP BY he.corrida_id HAVING count(*) = 3);
""");


for i in cursor.fetchall():
    print(i);
