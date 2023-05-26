import numpy as np

def cruzamento_uniforme(pai1, pai2):
    indices = np.random.choice([0, 1], size=pai1.shape[0])
    filho = np.where(indices, pai1, pai2)
    return filho

def mutação(indivíduo, taxa_de_mutação):
    if np.random.rand() < taxa_de_mutação:
        indivíduo += np.random.normal(0, 0.1, size=indivíduo.shape)
    return indivíduo

def gerar_nova_população(elite_pesos, taxa_de_mutação, tamanho_da_população):
    elite_pesos = np.vstack(elite_pesos)
    novos_pesos = []

    for _ in range(tamanho_da_população):
        pai1, pai2 = np.random.choice(len(elite_pesos), 2, replace=False)
        novo_indivíduo = cruzamento_uniforme(elite_pesos[pai1], elite_pesos[pai2])
        novo_indivíduo = mutação(novo_indivíduo, taxa_de_mutação)
        novos_pesos.append(novo_indivíduo)

    # Adicionando os pais à lista de novos pesos
    novos_pesos = np.vstack([elite_pesos] + novos_pesos)
    
    return novos_pesos[:tamanho_da_população]