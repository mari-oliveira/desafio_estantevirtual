import sqlite3

conn = sqlite3.connect('formula-1.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT c.temporada_ano, p.nome, e.nome, min(tp.duracao)
    FROM equipe e, resultado r, piloto p, tempo_por_parada tp, corrida c
    WHERE r.equipe_id = e.id
    AND r.piloto_id = p.id
    AND p.id=tp.piloto_id
    AND c.id=tp.corrida_id
    GROUP BY c.temporada_ano
    ORDER BY c.temporada_ano
""")
    
for i in cursor.fetchall():
        print(i);
    

conn.close()
