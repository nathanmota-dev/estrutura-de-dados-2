def gale_shapley(camisetas, voluntarios, preferencias):
    quant_camisetas = camisetas // 6    
    
    estoque = {
        "XXG": quant_camisetas,
        "XG": quant_camisetas,
        "G": quant_camisetas,
        "M": quant_camisetas,
        "P": quant_camisetas,
        "XP": quant_camisetas
    }
    print("Estoque inicial:", estoque)
    
    alocacoes = [None] * voluntarios
    voluntarios_livres = list(range(voluntarios))
    propostas = [0] * voluntarios

    while voluntarios_livres:
        v = voluntarios_livres.pop(0)
        prefer1, prefer2 = preferencias[v]

        if estoque[prefer1] > 0:
            estoque[prefer1] -= 1
            alocacoes[v] = prefer1
        elif estoque[prefer2] > 0:
            estoque[prefer2] -= 1
            alocacoes[v] = prefer2
        else:
            if propostas[v] == 0:
                propostas[v] += 1
                voluntarios_livres.append(v)
            else:
                print("Estoque final:", estoque)
                print("Alocações finais:", alocacoes)
                return "NÃO"
    
    print("Estoque final:", estoque)
    print("Alocações finais:", alocacoes)
    return "SIM"

t = int(input())  

for _ in range(t):
    camisetas, voluntarios = map(int, input().split())  
    preferencias = [input().split() for _ in range(voluntarios)]  
    print(gale_shapley(camisetas, voluntarios, preferencias))
