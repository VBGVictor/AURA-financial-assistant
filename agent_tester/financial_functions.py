import re

# Algoritmo TESTE para verificação do Agente

def calcula_juros_compostos(principal, taxa_anual, anos):
    """
    Calcula o montante final com base em juros compostos.
    """
    if principal <= 0 or taxa_anual < 0 or anos < 0:
        raise ValueError("Principal, taxa e anos devem ser valores positivos.")
    taxa_decimal = taxa_anual / 100
    montante = principal * (1 + taxa_decimal) ** anos
    return montante

def valida_cpf(cpf):
    """
    Valida um CPF brasileiro. Retorna True se válido, False caso contrário.
    Remove pontuação para a validação.
    """
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True