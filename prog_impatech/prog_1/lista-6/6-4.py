def converter_polinomio_para_dicionario(expressao_polinomio: str) -> dict:
    termos_polinomio = {}  
    termo_atual = ""  
    # percorre cada caractere na expressão do polinômio
    for indice in range(len(expressao_polinomio) + 1):
        if indice < len(expressao_polinomio):
            caractere_atual = expressao_polinomio[indice]  
        else:
            caractere_atual = None  
        
        # verifica se um novo termo deve ser iniciado 
        if caractere_atual is None or caractere_atual in '+-':
            if termo_atual:  
                # determina o coeficiente e o expoente do termo atual baseado no modelo dado
                if 'x' not in termo_atual:  # Termo constante (grau 0)
                    coeficiente = int(termo_atual)
                    expoente = 0
                elif '^' not in termo_atual:  # Termo de grau 1 (ex: 3x)
                    parte_coeficiente = termo_atual[:-1]  # Remove o 'x' do final
                    if parte_coeficiente and parte_coeficiente not in ('+', '-'):
                        coeficiente = int(parte_coeficiente)
                    else:
                        coeficiente = int(parte_coeficiente + '1')
                    expoente = 1
                else:  # termo de grau n (ex: 2x^3)
                    parte_coeficiente, parte_expoente = termo_atual.split('x^')
                    if parte_coeficiente and parte_coeficiente not in ('+', '-'):
                        coeficiente = int(parte_coeficiente)
                    else:
                        coeficiente = int(parte_coeficiente + '1')
                    expoente = int(parte_expoente)
                
                # Adiciona o coeficiente ao expoente correspondente no dicionário de termos do polinômio
                termos_polinomio[expoente] = coeficiente
                
            termo_atual = caractere_atual if caractere_atual else ""  # Inicia o novo termo
        else:
            termo_atual += caractere_atual
    
    return termos_polinomio

# Exemplo de uso da função para converter uma expressão de polinômio em um dicionário de termos
dicionario = converter_polinomio_para_dicionario("2x^3-x^2+x+5")
print(dicionario)