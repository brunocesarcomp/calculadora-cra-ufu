'''
regras de negócio
calcular o cra necessário para obter um cra X ao final do curso
    analisando as horas feitas e o cra obtido
    analisando as horas a fazer e cra desejado ao final do curso
    analisando as horas totais
    informando o cra nas horas a fazer para atingir o cra desejado ao final do curso
'''

def obter_input_numerico(mensagem, tipo=float):
    """Garante que o usuário digite um número válido, evitando a quebra do programa."""
    while True:
        try:
            valor = input(mensagem).replace(',', '.') # Cobre erro comum de digitação
            return tipo(valor)
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")

def calcular_cra_estrategico():
    print("\n==== Calculadora Estratégica de CRA (UFU) ====")
    print("Descubra a nota média necessária nas próximas disciplinas para atingir seu objetivo.\n")

    horas_feitas = obter_input_numerico("Carga horária já concluída: ", int)
    cra_obtido = obter_input_numerico("Seu CRA atual (ex: 85.5): ")
    
    horas_obrigatorias = obter_input_numerico("Carga horária OBRIGATÓRIA restante: ", int)
    horas_optativas = obter_input_numerico("Carga horária OPTATIVA restante: ", int)
    
    cra_desejado = obter_input_numerico("Qual o CRA final desejado? (ex: 90.0): ")

    horas_a_fazer = horas_obrigatorias + horas_optativas

    # Tratamento de erro lógico (Divisão por zero)
    if horas_a_fazer == 0:
        print("\n[RESULTADO] Você não possui horas pendentes. Seu CRA final está consolidado.")
        return # Encerra a função aqui, evitando o erro de escopo

    # O Algoritmo
    soma_total_desejada = cra_desejado * (horas_feitas + horas_a_fazer)
    soma_atual = horas_feitas * cra_obtido
    cra_necessario = (soma_total_desejada - soma_atual) / horas_a_fazer

    # Análise de Viabilidade
    print("\n==== ANÁLISE DE VIABILIDADE ====")
    if cra_necessario > 100:
        print(f"ALERTA: CRA Necessário = {cra_necessario:.2f}.")
        print("Matematicamente impossível. O valor ultrapassa 100 pontos. Escolha um objetivo menor.")
    elif cra_necessario <= 60:
        print(f"CRA Necessário = {cra_necessario:.2f}.")
        print("Cenário Confortável: Apenas aprovação mínima (60) garante seu objetivo.")
    else:
        print(f"O CRA médio necessário nas disciplinas restantes é de: {cra_necessario:.2f} pontos.")

# Execução limpa do programa
if __name__ == "__main__":
    calcular_cra_estrategico()
