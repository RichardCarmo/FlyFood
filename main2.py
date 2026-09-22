import time
from leitura_entrada import ler_entrada

def buscar_menor_rota_otimizada(ponto_atual, pontos_restantes, caminho_atual, distancia_atual, coords, melhor_solucao):
    #Se a distância atual já for maior ou igual à melhor distância encontrada, interrompe o ramo
    if distancia_atual >= melhor_solucao['distancia']:
        return

    #Quando não faltar nenhum ponto, calcula o retorno para a origem 'R'
    if not pontos_restantes:
        x_atual, y_atual = coords[ponto_atual]
        x_r, y_r = coords['R']
        dist_retorno = abs(x_atual - x_r) + abs(y_atual - y_r)
        dist_total = distancia_atual + dist_retorno

        # Se encontrou um caminho menor do que o recorde anterior, atualiza o recorde
        if dist_total < melhor_solucao['distancia']:
            melhor_solucao['distancia'] = dist_total
            melhor_solucao['rota'] = caminho_atual
        return

    #Tenta cada um dos pontos restantes como o próximo destino
    for proximo in pontos_restantes:
        x1, y1 = coords[ponto_atual]
        x2, y2 = coords[proximo]
        dist_trecho = abs(x1 - x2) + abs(y1 - y2)

        novos_restantes = [p for p in pontos_restantes if p != proximo]
        
        buscar_menor_rota_otimizada(
            ponto_atual=proximo,
            pontos_restantes=novos_restantes,
            caminho_atual=caminho_atual + [proximo],
            distancia_atual=distancia_atual + dist_trecho,
            coords=coords,
            melhor_solucao=melhor_solucao
        )


def main(caminho_arquivo):
    inicio_v2 = time.time()

    locais_v2, chaves_v2 = ler_entrada(caminho_arquivo)
    melhor_solucao = {'distancia': float('inf'), 'rota': []}
    
    # Inicia a busca a partir da origem 'R'
    buscar_menor_rota_otimizada(
        ponto_atual='R',
        pontos_restantes=chaves_v2,
        caminho_atual=[],
        distancia_atual=0,
        coords=locais_v2,
        melhor_solucao=melhor_solucao
    )

    fim_v2 = time.time()
    tempo_v2_ms = (fim_v2 - inicio_v2) * 1000  
    trajeto_v2 = "R -> " + " -> ".join(melhor_solucao['rota']) + " -> R"

    print(f"Melhor trajeto: {trajeto_v2}")
    print(f"Distância total: {melhor_solucao['distancia']} dronômetros")
    print(f"Tempo de execução do sistema: {tempo_v2_ms:.4f} ms")

    
if __name__ == "__main__":
    main("FlyFood/entradas/matriz5.txt")