from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","tpTxf&25"))
index = input("digite 1 ou 0:\n")
index  = int(index)

def add_console(tx, nome, geracao):
    tx.run("create(aa:Console{nome:$nome, geracao:$geracao})", nome = nome, geracao = geracao)
    print "adicionado"
def add_aresta(tx, var, ):
    while(index!=0):
        nome = raw_input("nome do console:\n")
        geracao = raw_input("geracao do console:\n")
        nome = str(nome)
        geracao = str(geracao)
        with driver.session() as session:
            session.write_transaction(add_console, nome, geracao)
        index = int(input("continuar? 1 - sim, 0 - nao:\n"))    


print "FIM\n"