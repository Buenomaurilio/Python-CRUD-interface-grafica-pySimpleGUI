import cx_Oracle

# Função de resposta conectando ao banco a cada chamada.

def responder():
    conn = cx_Oracle.connect('schema', 'senha', 'string de conexão:porta/ORCL')

    cur = conn.cursor()
    cur.execute('''INSTRUÇÃO SQL''')
    
    res = cur.fetchall()
    dados = []
    for dado in res:
        test = dado[0], dado[1], dado[2], dado[3]
        dados.append(test)
    if len(dados) == 0:
        return 'sem dados'
    else:
        return dados
    conn.close()