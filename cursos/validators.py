from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    return all(part.isalpha() for part in nome.split())

def rg_valido(numero_rg):
    return len(numero_rg) == 9 and  numero_rg.isdigit()
