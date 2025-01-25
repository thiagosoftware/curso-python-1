# 6 - Escreva um programa em Python que permita ao usuário digitar um estado do Campeonato Brasileiro de Futebol e informe quais os times desse estado.


# Estados que possuem times na Série A
al = "CRB"
ba = "Bahia"
ce = "Ceará e Fortaleza"
go = "Goiás"
mg = " Atlético Mineiro e Cruzeiro"
pr = "Athletico Paranaense e Coritiba"
pe = "Sport"
rj = "Flamengo, Vasco, Fluminense e Botafogo"
rs = "Grêmio, Internacional"
sc = "Grêmio, Internacional"
sp = "São Paulo, Palmeiras, Corinthians e Santos"


# Estados que NÃO possuem  nenhum times na Série A
ac = ap = am = es = ma = mt = ms = pa = pb = pi = rn = ro = rr = se = to = "Não há times na Série A"

uf = input("Digite a sigla (UF) do Estado que você deseja conferir:\n")
uf = uf.lower()

if uf == "al":
    print(al)
elif uf == "ba":
    print(ba)
elif uf == "ce":
    print(ce)
elif uf == "go":
    print(go)
elif uf == "mg":
    print(mg)
elif uf == "pr":
    print(pr)
elif uf == "rj":
    print(rj)
elif uf == "rs":
    print(rs)
elif uf == "sc":
    print(sc)
elif uf == "sp":
    print(sp)
elif uf == "ac" or uf == "am" or uf == "es" or uf == "ma" or uf == "mt" or uf == "ms" or uf == "pa" or uf == "pb" or uf == "pi" or uf == "rn" or uf == "ro" or uf == "rr" or uf == "se" or uf == "to":
    print(ac)  
else: 
    print("Estado inexistente, tente novamente.")