def counting_sort(arr):
    """
    Ordena uma lista de inteiros não-negativos usando o Counting Sort.
    É um algoritmo estável.
    """
    if not arr:
        return []

    # 1. Encontrar o valor máximo (k)
    # Isso define o tamanho do array de contagem.
    max_val = max(arr)
    
    # O array de contagem precisa ser do tamanho (max_val + 1) para incluir o índice 0 até o max_val.
    count = [0] * (max_val + 1)
    
    # Cria o array de saída do mesmo tamanho da lista de entrada
    n = len(arr)
    output = [0] * n

    # --- Passo 1: Contar as Ocorrências ---
    # Percorre a lista de entrada e armazena a frequência de cada elemento
    for num in arr:
        count[num] += 1

    # --- Passo 2: Calcular a Soma Cumulativa (Prefix Sum) ---
    # Modifica o array de contagem para que cada índice contenha a posição real
    # de término do elemento no array de saída ordenado.
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # --- Passo 3: Construir o Array de Saída ---
    # Itera sobre o array de entrada DE TRÁS PARA FRENTE para garantir a ESTABILIDADE.
    for i in range(n - 1, -1, -1):
        num = arr[i]
        
        # A posição correta para o 'num' é count[num] - 1
        posicao_correta = count[num] - 1
        
        # Coloca o elemento no array de saída
        output[posicao_correta] = num
        
        # Decrementa o contador para o próximo elemento com o mesmo valor
        count[num] -= 1
        
    return output

# --- Exemplo de Uso ---
sample_list = [4, 2, 2, 8, 3, 3, 1, 1, 5, 2]
print(f"Lista original: {sample_list}")

sorted_list = counting_sort(sample_list)
print(f"Lista ordenada: {sorted_list}")