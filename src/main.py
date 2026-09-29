import time
from leitura_entrada import ler_entrada


def permutation(points):
    if len(points) <= 1:
        return [points]

    # records guarda as permutações
    records = []

    # As permutações são feitas com base na quantidade de lugares de entrega
    for i in range(len(points)):

        # Fatia o vetor points de modo a simular a fixação do elemento atual
        current_element = points[i]
        remaining_elements = points[:i] + points[i+1:]

        # A recursão faz a permutação entre os valores restantes
        for j in permutation(remaining_elements):
            records.append([current_element] + j)

    return records


def distance_calculator(permutation, data):
    coords = dict(data)
    best_route = None
    best_total = float('inf')

    # Para todas as permutações possíveis acrescente origem e retorno ('R')
    for order in permutation:
        route = ['R'] + list(order) + ['R']
        total = 0

        # Para cada dois pontos da matriz, a diferença entre as coords de um ponto e outro representa sua distância
        for i in range(len(route) - 1):
            x1, y1 = coords[route[i]]
            x2, y2 = coords[route[i + 1]]
            total += abs(x1 - x2) + abs(y1 - y2)
            
        # Verifica-se as melhores rotas e suas respectivas distâncias guardando e substituindo resultados anteriores menos eficientes
        if total < best_total:
            best_total = total
            best_route = order

    return best_route, best_total


def main(caminho_arquivo):
    inicio = time.time()
    locais, chaves = ler_entrada(caminho_arquivo)

    if locais is None:
        return

    rotas = permutation(chaves)
    melhor_rota, distancia = distance_calculator(rotas, locais)

    fim = time.time()
    tempo_ms = (fim - inicio) * 1000

    trajeto = " ".join(melhor_rota)

    resultado = (
        f"Melhor trajeto: {trajeto}\n"
        f"Distância total: {distancia}\n"
        f"Tempo percorrido: {tempo_ms:.4f} ms"
    )

    print(resultado)

if __name__ == "__main__":
    main("FlyFood/entradas/matriz1.txt")
