def counting_sort_by_digit(arr, exp):
    """
    Ordena arr[] usando Counting Sort baseado no dígito representado por 'exp'.
    
    exp é 10^i, onde i é o número do dígito atual (1 para unidade, 10 para dezena, etc.)
    """
    n = len(arr)
    
    # Array de saída que conterá o arr ordenado pelo dígito atual
    output = [0] * n
    
    # Array de contagem para os 10 dígitos (0 a 9)
    count = [0] * 10
    
    # 1. Armazena a contagem de ocorrências de cada dígito
    for i in range(n):
        # A expressão (arr[i] // exp) extrai a porção do número até o dígito atual.
        # O módulo % 10 isola o dígito atual (0-9).
        index = arr[i] // exp
        count[index % 10] += 1
        
    # 2. Modifica o array de contagem para conter a posição real do dígito no output[]
    # Isso é feito somando a contagem anterior.
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # 3. Constrói o array de saída (iterando de trás para frente para garantir estabilidade)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        
        # A posição correta para o elemento é count[dígito] - 1
        output[count[index % 10] - 1] = arr[i]
        
        # Decrementa a contagem para o próximo elemento com o mesmo dígito
        count[index % 10] -= 1
        i -= 1
        
    # 4. Copia os elementos ordenados de volta para o array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Função principal do Radix Sort para ordenar a lista 'arr'.
    """
    if not arr:
        return
        
    # 1. Encontra o número máximo para determinar o número de dígitos (passagens)
    max_val = max(arr)
    
    # 2. Começa com exp = 1 (unidade) e continua enquanto max_val / exp for maior que 0
    exp = 1
    while max_val // exp > 0:
        # Chama a função de ordenação estável para o dígito atual
        counting_sort_by_digit(arr, exp)
        
        # Passa para o próximo dígito (dezena, centena, etc.)
        exp *= 10

# --- Exemplo de Uso ---
data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", data)

radix_sort(data)

print("Lista ordenada:", data)