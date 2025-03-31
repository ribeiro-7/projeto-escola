def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11 and numero_cpf.isdigit()

def nome_valido(nome):
    return all(part.isalpha() for part in nome.split())

def rg_valido(numero_rg):
    return len(numero_rg) == 9 and  numero_rg.isdigit()
