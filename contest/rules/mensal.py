'''
Conjunto de regras de teste.

Cada regra é uma função que deve retornar uma tupla com

- Nome do teste;
- Lista com o valor esquerdo;
- Lista com o valor esquerdo;

As listas de valores esquerdo e direito são um conjunto de tuplas com a seguinte estrutura:

- Tabela: o nome da tabela onde estão os dados;
- Campo de soma: o campo a ser somado;
- Filtro: um filtro adequado à cláusula WHERE (SQL);
- Inverter: um booleano indicando se o valor deve ser invertido (True) ou não (False|None)

'''

def fechamento_natureza_patrimonial():
    name = 'Fechamento dos lançamentos de natureza patrimonial'
    left_value = [
        ('tce_4111', 'valor', 'conta_contabil like "1%" and tipo_lancamento like "D"', False),
        ('tce_4111', 'valor', 'conta_contabil like "2%" and tipo_lancamento like "D"', False),
        ('tce_4111', 'valor', 'conta_contabil like "3%" and tipo_lancamento like "D"', False),
        ('tce_4111', 'valor', 'conta_contabil like "4%" and tipo_lancamento like "D"', False)
    ]
    right_value = [
        ('tce_4111', 'valor', 'conta_contabil like "1%" and tipo_lancamento like "C"', False),
        ('tce_4111', 'valor', 'conta_contabil like "2%" and tipo_lancamento like "C"', False),
        ('tce_4111', 'valor', 'conta_contabil like "3%" and tipo_lancamento like "C"', False),
        ('tce_4111', 'valor', 'conta_contabil like "4%" and tipo_lancamento like "C"', False)
    ]
    return name, left_value, right_value

def fechamento_natureza_orcamentario():
    name = 'Fechamento dos lançamentos de natureza orçamentária'
    left_value = [
        ('tce_4111', 'valor', 'conta_contabil like "5%" and tipo_lancamento like "D"', False),
        ('tce_4111', 'valor', 'conta_contabil like "6%" and tipo_lancamento like "D"', False),
    ]
    right_value = [
        ('tce_4111', 'valor', 'conta_contabil like "5%" and tipo_lancamento like "C"', False),
        ('tce_4111', 'valor', 'conta_contabil like "6%" and tipo_lancamento like "C"', False),
    ]
    return name, left_value, right_value

def fechamento_natureza_controle():
    name = 'Fechamento dos lançamentos de natureza de controle'
    left_value = [
        ('tce_4111', 'valor', 'conta_contabil like "7%" and tipo_lancamento like "D"', False),
        ('tce_4111', 'valor', 'conta_contabil like "8%" and tipo_lancamento like "D"', False),
    ]
    right_value = [
        ('tce_4111', 'valor', 'conta_contabil like "7%" and tipo_lancamento like "C"', False),
        ('tce_4111', 'valor', 'conta_contabil like "8%" and tipo_lancamento like "C"', False),
    ]
    return name, left_value, right_value

def suprimento_de_fundos_a_apropriar():
    name = 'Suprimento de fundos a apropriar'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1131102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1131102%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1131199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1131199%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8912101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8912101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def parcerias_a_apropriar():
    name = 'Parcerias a apropriar'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1198101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1198101%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "812210102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "812210102%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "812210103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "812210103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def precatorios_cp_a_pagar():
    name = 'Precatórios de curto prazo a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2111105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "2111105%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2131108%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "2131108%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8129101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8129101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def contribuicao_previdenciaria_rpps_a_pagar():
    name = 'Contribuição previdenciária ao RPPS a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "211420102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "211420102%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'liquidado_a_pagar', 'elemento like "319113%"', False),
    ]
    return name, left_value, right_value

def contribuicao_previdenciaria_inss_a_pagar():
    name = 'Contribuição previdenciária ao INSS a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2114301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "2114301%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('LIQUIDAC', 'valor_liquidacao', 'rubrica like "31901302%"', False),
        ('PAGAMENT', 'valor_pagamento', 'rubrica like "31901302%"', True),
        ('LIQUIDAC', 'valor_liquidacao', 'rubrica like "33904720%"', False),
        ('PAGAMENT', 'valor_pagamento', 'rubrica like "33904720%"', True),
    ]
    return name, left_value, right_value

def fgts_a_pagar():
    name = 'FGTS a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "211430502%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "211430502%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('LIQUIDAC', 'valor_liquidacao', 'rubrica like "31901301%"', False),
        ('PAGAMENT', 'valor_pagamento', 'rubrica like "31901301%"', True),
    ]
    return name, left_value, right_value

def passivo_rpp_a_pagar():
    name = 'Passivo de Restos a Pagar Processados a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "21311010102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "21311010102%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_final_processados', None, False),
        ('RESTOS_PAGAR', 'liquidado_a_pagar_nao_processados', None, False),
    ]
    return name, left_value, right_value

def rpp_a_pagar():
    name = 'Restos a Pagar Processados a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6321%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6321%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_final_processados', None, False),
    ]
    return name, left_value, right_value

def pasep_a_pagar():
    name = 'PASEP a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "214131102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "214131102%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('LIQUIDAC', 'valor_liquidacao', 'rubrica like "33904712%"', False),
        ('PAGAMENT', 'valor_pagamento', 'rubrica like "33904712%"', True),
    ]
    return name, left_value, right_value

def previsao_inicial_receita_bruta():
    name = 'Previsão inicial da receita bruta'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "52111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "52111%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 0', False),
    ]
    return name, left_value, right_value

def previsao_inicial_deducao_fundeb():
    name = 'Previsão inicial da dedução para o FUNDEB'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "521120101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "521120101%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 105', True),
    ]
    return name, left_value, right_value

def previsao_inicial_deducao_renuncia():
    name = 'Previsão inicial da dedução da receita: renúncia e desconto'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5211202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5211202%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita in(101, 103)', True),
    ]
    return name, left_value, right_value

def previsao_inicial_deducao_outras():
    name = 'Previsão inicial da dedução da receita: outras deduções'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5211299%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5211299%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita in(102, 106, 107, 108, 109)', True),
    ]
    return name, left_value, right_value

# def previsao_inicial_deducao_exceto_fundeb():
#     name = 'Previsão inicial da dedução da receita (exceto FUNDEB)'
#     left_value = [
#         ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5211299%" and escrituracao like "S"', False),
#         ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5211299%" and escrituracao like "S"', True),
#     ]
#     right_value = [
#         ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita not in(0, 105)', True),
#     ]
#     return name, left_value, right_value

def reestimativa_receita():
    name = 'Reestimativa da receita'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5212101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5212101%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'previsao_atualizada', 'tipo_nivel_receita like "A"', False),
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A"', True),
    ]
    return name, left_value, right_value

def dotacao_inicial():
    name = 'Dotação inicial'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221101%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'dotacao_inicial', None, False),
    ]
    return name, left_value, right_value

def credito_suplementar_aberto():
    name = 'Crédito suplementar aberto'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221201%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'credito_suplementar', None, False),
    ]
    return name, left_value, right_value

def credito_especial_aberto():
    name = 'Crédito especial aberto'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221202%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'credito_especial', None, False),
    ]
    return name, left_value, right_value

def credito_extraordinario_aberto():
    name = 'Crédito estraordinario aberto'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221203%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221203%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'credito_extraordinario', None, False),
    ]
    return name, left_value, right_value

def anulacao_dotacao():
    name = 'Cancelamento/Anulação de dotações'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221904%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221904%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('BAL_DESP', 'reducao_dotacao', None, False),
    ]
    return name, left_value, right_value

def emissao_empenhos():
    name = 'Emissão de empenhos'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5229201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5229201%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_empenhado', None, False),
    ]
    return name, left_value, right_value

def rpnp_inscritos_ultimo_ano():
    name = 'Restos a pagar não processados inscritos no último ano'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5311%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5311%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_nao_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def rpnp_inscritos_anos_anteriores():
    name = 'Restos a pagar não processados inscritos nos anos anteriores'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5312%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5312%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_nao_processados_inscritos_anos_anteriores', None, False),
    ]
    return name, left_value, right_value

def rpnp_inscritos_inscricao():
    name = 'Restos a pagar não processados - inscrição no exercício'
    left_value = [
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "5317%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "5317%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_nao_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def rpnp_inscritos_inscricao_saldo_inicial():
    name = 'Restos a pagar não processados - inscrição no exercício - saldo inicial'
    left_value = [
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "63171%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "63171%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_nao_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def rpp_inscritos_ultimo_ano():
    name = 'Restos a pagar processados inscritos no último ano'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5321%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5321%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def rpp_inscritos_anos_anteriores():
    name = 'Restos a pagar processados inscritos nos anos anteriores'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5322%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5322%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_processados_inscritos_anos_anteriores', None, False),
    ]
    return name, left_value, right_value

def rpp_inscritos_inscricao():
    name = 'Restos a pagar processados - inscrição no exercício'
    left_value = [
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "5327%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "5327%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def rpp_inscritos_inscricao_saldo_inicial():
    name = 'Restos a pagar processados - inscrição no exercício - saldo inicial'
    left_value = [
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "6327%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "6327%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'saldo_inicial_processados_inscritos_ultimo_ano', None, False),
    ]
    return name, left_value, right_value

def receita_a_realizar():
    name = 'Receita a realizar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6211%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6211%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'previsao_atualizada', 'tipo_nivel_receita like "A"', False),
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A"', True),
    ]
    return name, left_value, right_value

def receita_bruta_realizada():
    name = 'Receita bruta realizada'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6212%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6212%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 0', False),
    ]
    return name, left_value, right_value

def deducao_receita_fundeb():
    name = 'Dedução da receita para o FUNDEB'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6213101%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6213101%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 105', True),
    ]
    return name, left_value, right_value

def deducao_renuncia_receita():
    name = 'Dedução por renúncia de receitas'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "62132%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "62132%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 101', True),
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita = 103', True),
    ]
    return name, left_value, right_value

def deducao_outras():
    name = 'Outras deduções da receita'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "62139%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "62139%" and escrituracao like "S"', False),
    ]
    right_value = [
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita not in(0, 101, 103, 105)', True),
    ]
    return name, left_value, right_value

def credito_empenhado_a_liquidar():
    name = 'Crédito empenhado a liquidar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221301%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_empenhado', None, False),
        ('BAL_DESP', 'valor_liquidado', None, True),
    ]
    return name, left_value, right_value

def empenhos_a_liquidar():
    name = 'Empenhos a liquidar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "622920101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "622920101%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_empenhado', None, False),
        ('BAL_DESP', 'valor_liquidado', None, True),
    ]
    return name, left_value, right_value

def credito_liquidado_a_pagar():
    name = 'Crédito liquidado a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221303%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_liquidado', None, False),
        ('BAL_DESP', 'valor_pago', None, True),
    ]
    return name, left_value, right_value

def empenho_liquidado_a_pagar():
    name = 'Empenhos liquidados a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221303%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_liquidado', None, False),
        ('BAL_DESP', 'valor_pago', None, True),
    ]
    return name, left_value, right_value

def credito_pago():
    name = 'Crédito pago'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221304%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_pago', None, False),
    ]
    return name, left_value, right_value

def empenho_pago():
    name = 'Empenhos pago'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "622920104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "622920104%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_DESP', 'valor_pago', None, False),
    ]
    return name, left_value, right_value

def rpnp_a_liquidar():
    name = 'Restos a pagar não processados a liquidar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6311%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6311%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'a_liquidar_nao_processados', None, False),
    ]
    return name, left_value, right_value

def rpnp_a_pagar():
    name = 'Restos a pagar não processados a pagar'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6313%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6313%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'liquidado_a_pagar_nao_processados', None, False),
    ]
    return name, left_value, right_value

def rpnp_pagos():
    name = 'Restos a pagar não processados pagos'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6314%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6314%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'pagamento_nao_processados', None, False),
    ]
    return name, left_value, right_value

def rpnp_cancelados():
    name = 'Restos a pagar não processados cancelados'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6319%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6319%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'cancelamento_nao_processados', None, False),
    ]
    return name, left_value, right_value

def rpp_pagos():
    name = 'Restos a pagar processados pagos'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6322%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6322%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'pagamento_processados', None, False),
    ]
    return name, left_value, right_value

def rpp_cancelados():
    name = 'Restos a pagar processados cancelados'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6329%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6329%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('RESTOS_PAGAR', 'cancelamento_processados', None, False),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_11():
    name = 'Fechamento das contas orçamentárias [5/6].1.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "511%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "511%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "611%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "611%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_12():
    name = 'Fechamento das contas orçamentárias [5/6].1.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "512%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "512%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "612%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "612%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_21():
    name = 'Fechamento das contas orçamentárias [5/6].2.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "521%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "521%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "621%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "621%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_221():
    name = 'Fechamento das contas orçamentárias [5/6].2.2.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_222():
    name = 'Fechamento das contas orçamentárias [5/6].2.2.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5222%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5222%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6222%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6222%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_223():
    name = 'Fechamento das contas orçamentárias [5/6].2.2.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5223%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5223%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6223%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6223%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_229():
    name = 'Fechamento das contas orçamentárias [5/6].2.2.9'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5229%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5229%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6229%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6229%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_31():
    name = 'Fechamento das contas orçamentárias [5/6].3.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "531%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "531%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "631%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "631%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_orcamentario_32():
    name = 'Fechamento das contas orçamentárias [5/6].3.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "532%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "532%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "632%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "632%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111101():
    name = 'Fechamento das contas de controle [7/8].1.1.1.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111102():
    name = 'Fechamento das contas de controle [7/8].1.1.1.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111103():
    name = 'Fechamento das contas de controle [7/8].1.1.1.1.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111103%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111104():
    name = 'Fechamento das contas de controle [7/8].1.1.1.1.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111104%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111104%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111201():
    name = 'Fechamento das contas de controle [7/8].1.1.1.2.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111201%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111201%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111202():
    name = 'Fechamento das contas de controle [7/8].1.1.1.2.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111202%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111202%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111203():
    name = 'Fechamento das contas de controle [7/8].1.1.1.2.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111203%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111203%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111203%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111203%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111204():
    name = 'Fechamento das contas de controle [7/8].1.1.1.2.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111204%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111204%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111204%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111204%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111301():
    name = 'Fechamento das contas de controle [7/8].1.1.1.3.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111301%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111301%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111302():
    name = 'Fechamento das contas de controle [7/8].1.1.1.3.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111302%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111302%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111302%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111302%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111303():
    name = 'Fechamento das contas de controle [7/8].1.1.1.3.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111303%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111303%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111304():
    name = 'Fechamento das contas de controle [7/8].1.1.1.3.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111304%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111304%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111401():
    name = 'Fechamento das contas de controle [7/8].1.1.1.4.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111401%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111401%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111401%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111401%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111402():
    name = 'Fechamento das contas de controle [7/8].1.1.1.4.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111402%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111402%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111402%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111402%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111403():
    name = 'Fechamento das contas de controle [7/8].1.1.1.4.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111403%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111403%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111403%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111403%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111404():
    name = 'Fechamento das contas de controle [7/8].1.1.1.4.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111404%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111404%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111404%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111404%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111501():
    name = 'Fechamento das contas de controle [7/8].1.1.1.5.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111501%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111501%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111501%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111501%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111502():
    name = 'Fechamento das contas de controle [7/8].1.1.1.5.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111502%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111502%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111502%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111502%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111503():
    name = 'Fechamento das contas de controle [7/8].1.1.1.5.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111503%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111503%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111503%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111503%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_111504():
    name = 'Fechamento das contas de controle [7/8].1.1.1.5.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111504%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111504%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_112101():
    name = 'Fechamento das contas de controle [7/8].1.1.2.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7112101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7112101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8112101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8112101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_112102():
    name = 'Fechamento das contas de controle [7/8].1.1.2.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7112102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7112102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8112102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8112102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_112199():
    name = 'Fechamento das contas de controle [7/8].1.1.2.1.99'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7112199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7112199%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8112199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8112199%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113101():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113102():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113103():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113103%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113104():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113104%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113104%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113105():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.05'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113105%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113105%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113108():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.08'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113108%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113108%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113108%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113108%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113112():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.12'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113112%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113112%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113113():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.13'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113113%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113113%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_113199():
    name = 'Fechamento das contas de controle [7/8].1.1.3.1.99'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7113199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7113199%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8113199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8113199%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1141():
    name = 'Fechamento das contas de controle [7/8].1.1.4.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71141%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71141%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81141%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81141%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1142():
    name = 'Fechamento das contas de controle [7/8].1.1.4.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71142%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71142%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81142%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81142%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1143():
    name = 'Fechamento das contas de controle [7/8].1.1.4.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71143%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71143%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81143%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81143%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1144():
    name = 'Fechamento das contas de controle [7/8].1.1.4.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71144%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71144%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81144%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81144%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1145():
    name = 'Fechamento das contas de controle [7/8].1.1.4.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71145%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71145%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81145%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81145%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_119101():
    name = 'Fechamento das contas de controle [7/8].1.1.9.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7119101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7119101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8119101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8119101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_119102():
    name = 'Fechamento das contas de controle [7/8].1.1.9.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7119102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7119102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8119102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8119102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_119103():
    name = 'Fechamento das contas de controle [7/8].1.1.9.1.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7119103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7119103%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8119103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8119103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_119104():
    name = 'Fechamento das contas de controle [7/8].1.1.9.1.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7119104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7119104%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8119104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8119104%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_119105():
    name = 'Fechamento das contas de controle [7/8].1.1.9.1.05'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7119105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7119105%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8119105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8119105%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121101():
    name = 'Fechamento das contas de controle [7/8].1.2.1.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121102():
    name = 'Fechamento das contas de controle [7/8].1.2.1.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121103():
    name = 'Fechamento das contas de controle [7/8].1.2.1.1.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121103%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121104():
    name = 'Fechamento das contas de controle [7/8].1.2.1.1.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121104%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121104%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121201():
    name = 'Fechamento das contas de controle [7/8].1.2.1.2.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121201%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121201%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121202():
    name = 'Fechamento das contas de controle [7/8].1.2.1.2.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121202%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121202%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121203():
    name = 'Fechamento das contas de controle [7/8].1.2.1.2.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121203%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121203%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121203%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121203%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121204():
    name = 'Fechamento das contas de controle [7/8].1.2.1.2.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121204%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121204%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121204%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121204%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121301():
    name = 'Fechamento das contas de controle [7/8].1.2.1.3.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121301%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121301%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121302():
    name = 'Fechamento das contas de controle [7/8].1.2.1.3.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121302%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121302%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121302%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121302%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121303():
    name = 'Fechamento das contas de controle [7/8].1.2.1.3.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121303%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121303%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121304():
    name = 'Fechamento das contas de controle [7/8].1.2.1.3.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121304%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121304%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121401():
    name = 'Fechamento das contas de controle [7/8].1.2.1.4.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121401%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121401%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121401%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121401%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121402():
    name = 'Fechamento das contas de controle [7/8].1.2.1.4.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121402%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121402%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121402%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121402%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121403():
    name = 'Fechamento das contas de controle [7/8].1.2.1.4.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121403%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121403%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121403%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121403%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121404():
    name = 'Fechamento das contas de controle [7/8].1.2.1.4.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121404%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121404%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121404%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121404%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121501():
    name = 'Fechamento das contas de controle [7/8].1.2.1.5.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121501%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121501%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121501%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121501%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121502():
    name = 'Fechamento das contas de controle [7/8].1.2.1.5.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121502%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121502%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121502%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121502%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121503():
    name = 'Fechamento das contas de controle [7/8].1.2.1.5.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121503%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121503%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121503%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121503%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_121504():
    name = 'Fechamento das contas de controle [7/8].1.2.1.5.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7121504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7121504%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8121504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8121504%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_122101():
    name = 'Fechamento das contas de controle [7/8].1.2.2.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7122101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7122101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8122101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8122101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_122102():
    name = 'Fechamento das contas de controle [7/8].1.2.2.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7122102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7122102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8122102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8122102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_122199():
    name = 'Fechamento das contas de controle [7/8].1.2.2.1.99'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7122199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7122199%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8122199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8122199%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123101():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123102():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123103():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.03'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123103%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123103%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123103%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123104():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123104%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123104%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123104%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123105():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.05'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123105%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123105%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123105%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123106():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.06'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123106%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123106%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123106%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123106%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123107():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.07'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123107%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123107%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123107%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123107%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123108():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.08'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123108%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123108%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123108%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123108%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123109():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.09'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123109%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123109%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123109%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123109%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123110():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.10'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123110%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123110%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123110%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123110%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123111():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.11'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123111%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123111%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123112():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.12'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123112%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123112%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123113():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.13'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123113%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123113%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_123199():
    name = 'Fechamento das contas de controle [7/8].1.2.3.1.99'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7123199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7123199%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8123199%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8123199%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1241():
    name = 'Fechamento das contas de controle [7/8].1.2.4.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71241%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71241%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81241%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81241%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1242():
    name = 'Fechamento das contas de controle [7/8].1.2.4.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71242%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71242%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81242%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81242%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1243():
    name = 'Fechamento das contas de controle [7/8].1.2.4.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71243%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71243%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81243%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81243%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1244():
    name = 'Fechamento das contas de controle [7/8].1.2.4.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71244%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71244%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81244%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81244%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1245():
    name = 'Fechamento das contas de controle [7/8].1.2.4.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71245%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71245%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81245%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81245%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_129101():
    name = 'Fechamento das contas de controle [7/8].1.2.9.1.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7129101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7129101%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8129101%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8129101%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_129102():
    name = 'Fechamento das contas de controle [7/8].1.2.9.1.02'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7129102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7129102%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8129102%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8129102%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1292():
    name = 'Fechamento das contas de controle [7/8].1.2.9.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71292%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71292%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81292%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81292%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_1293():
    name = 'Fechamento das contas de controle [7/8].1.2.9.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "71293%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "71293%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "81293%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "81293%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_21():
    name = 'Fechamento das contas de controle [7/8].2.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "721%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "721%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "821%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "821%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_22():
    name = 'Fechamento das contas de controle [7/8].2.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "722%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "722%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "822%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "822%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_23():
    name = 'Fechamento das contas de controle [7/8].2.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "723%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "723%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "823%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "823%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_24():
    name = 'Fechamento das contas de controle [7/8].2.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "724%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "724%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "824%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "824%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_31():
    name = 'Fechamento das contas de controle [7/8].3.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "731%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "731%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "831%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "831%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_32():
    name = 'Fechamento das contas de controle [7/8].3.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "732%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "732%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "832%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "832%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4111():
    name = 'Fechamento das contas de controle [7/8].4.1.1.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74111%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84111%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4112():
    name = 'Fechamento das contas de controle [7/8].4.1.1.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74112%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84112%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4113():
    name = 'Fechamento das contas de controle [7/8].4.1.1.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74113%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84113%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4114():
    name = 'Fechamento das contas de controle [7/8].4.1.1.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74114%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74114%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84114%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84114%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4115():
    name = 'Fechamento das contas de controle [7/8].4.1.1.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74115%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74115%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84115%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84115%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4119():
    name = 'Fechamento das contas de controle [7/8].4.1.1.9'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74119%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74119%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84119%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84119%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4211():
    name = 'Fechamento das contas de controle [7/8].4.2.1.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74211%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74211%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84211%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84211%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4212():
    name = 'Fechamento das contas de controle [7/8].4.2.1.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74212%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74212%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84212%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84212%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4213():
    name = 'Fechamento das contas de controle [7/8].4.2.1.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74213%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74213%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84213%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84213%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_4214():
    name = 'Fechamento das contas de controle [7/8].4.2.1.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "74214%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "74214%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "84214%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "84214%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_52():
    name = 'Fechamento das contas de controle [7/8].5.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "752%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "752%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "852%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "852%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_531():
    name = 'Fechamento das contas de controle [7/8].5.3.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7531%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7531%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8531%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8531%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_532():
    name = 'Fechamento das contas de controle [7/8].5.3.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7532%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7532%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8532%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8532%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_533():
    name = 'Fechamento das contas de controle [7/8].5.3.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7533%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7533%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8533%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8533%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_534():
    name = 'Fechamento das contas de controle [7/8].5.3.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7534%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7534%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8534%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8534%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_535():
    name = 'Fechamento das contas de controle [7/8].5.3.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7535%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7535%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8535%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8535%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_536():
    name = 'Fechamento das contas de controle [7/8].5.3.6'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7536%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7536%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8536%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8536%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_537():
    name = 'Fechamento das contas de controle [7/8].5.3.7'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7537%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7537%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8537%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8537%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_611():
    name = 'Fechamento das contas de controle [7/8].6.1.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7611%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7611%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8611%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8611%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_612():
    name = 'Fechamento das contas de controle [7/8].6.1.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7612%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7612%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8612%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8612%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_613():
    name = 'Fechamento das contas de controle [7/8].6.1.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7613%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7613%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8613%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8613%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_619():
    name = 'Fechamento das contas de controle [7/8].6.1.9'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7619%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7619%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8619%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8619%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_62():
    name = 'Fechamento das contas de controle [7/8].6.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "762%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "762%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "862%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "862%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_631():
    name = 'Fechamento das contas de controle [7/8].6.3.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7631%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7631%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8631%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8631%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_632():
    name = 'Fechamento das contas de controle [7/8].6.3.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7632%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7632%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8632%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8632%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_633():
    name = 'Fechamento das contas de controle [7/8].6.3.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7633%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7633%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8633%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8633%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_8():
    name = 'Fechamento das contas de controle [7/8].8'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "78%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "78%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "88%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "88%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9111():
    name = 'Fechamento das contas de controle [7/8].9.1.1.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79111%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89111%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9112():
    name = 'Fechamento das contas de controle [7/8].9.1.1.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79112%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89112%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9113():
    name = 'Fechamento das contas de controle [7/8].9.1.1.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79113%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89113%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9114():
    name = 'Fechamento das contas de controle [7/8].9.1.1.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79114%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79114%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89114%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89114%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9115():
    name = 'Fechamento das contas de controle [7/8].9.1.1.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79115%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79115%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89115%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89115%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9119():
    name = 'Fechamento das contas de controle [7/8].9.1.1.9'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79119%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79119%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89119%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89119%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9121():
    name = 'Fechamento das contas de controle [7/8].9.1.2.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79121%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79121%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89121%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89121%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9122():
    name = 'Fechamento das contas de controle [7/8].9.1.2.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79122%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79122%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89122%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89122%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9124():
    name = 'Fechamento das contas de controle [7/8].9.1.2.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79124%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79124%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89124%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89124%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9125():
    name = 'Fechamento das contas de controle [7/8].9.1.2.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79125%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79125%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89125%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89125%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_912901():
    name = 'Fechamento das contas de controle [7/8].9.1.2.9.01'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7912901%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7912901%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8912901%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8912901%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_925():
    name = 'Fechamento das contas de controle [7/8].9.2.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7925%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7925%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8925%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8925%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_926():
    name = 'Fechamento das contas de controle [7/8].9.2.6'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7926%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7926%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8926%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8926%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_929():
    name = 'Fechamento das contas de controle [7/8].9.2.9'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7929%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7929%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8929%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8929%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9991():
    name = 'Fechamento das contas de controle [7/8].9.9.9.1'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79991%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79991%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89991%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89991%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9992():
    name = 'Fechamento das contas de controle [7/8].9.9.9.2'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79992%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79992%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89992%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89992%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9993():
    name = 'Fechamento das contas de controle [7/8].9.9.9.3'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79993%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79993%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89993%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89993%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9994():
    name = 'Fechamento das contas de controle [7/8].9.9.9.4'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79994%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79994%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89994%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89994%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def fechamento_controle_9995():
    name = 'Fechamento das contas de controle [7/8].9.9.9.5'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "79995%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "79995%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "89995%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "89995%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def disponibilidades():
    name = 'Disponibilidades'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7211%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7211%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82114%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82114%" and escrituracao like "S"', False),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "111%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "111%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "114%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "114%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
    ]
    return name, left_value, right_value

def resultado_financeiro():
    name = 'Superávit/déficit financeiro'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82111%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82112%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82112%" and escrituracao like "S"', False),
    ]
    return name, left_value, right_value

def resultado_periodo():
    name = 'Resultado do período'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "2%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "4%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "4%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "3%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "3%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def situacao_financeira_orcamentaria():
    name = 'Situação financeira vs Situação orçamentária'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82111%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_anterior_credor', 'conta_contabil like "82112%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_anterior_devedor', 'conta_contabil like "82112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "4511%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "4511%" and escrituracao like "S"', True),
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A"', False),
        ('BAL_DESP', 'valor_empenhado', None, True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "3511%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "3511%" and escrituracao like "S"', False),
        ('RESTOS_PAGAR', 'cancelamento_nao_processados', None, False),
        ('RESTOS_PAGAR', 'cancelamento_processados', None, False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "361710802%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "361710802%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "361719902%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "361719902%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def ddr_disponivel():
    name = 'DDR disponível'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82111%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82111%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "21%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "22%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82112%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82112%" and escrituracao like "S"', False),
    ]
    return name, left_value, right_value

def ddr_comprometida_empenho():
    name = 'DDR comprometida por empenho'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82112%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82112%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221301%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6311%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6311%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def ddr_comprometida_liquidacao():
    name = 'DDR comprometida por liquidacao e entradas compensatórias'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82113%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82113%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221303%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6313%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6313%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6321%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6321%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "113%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "113%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2188%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'saldo_atual_devedor','conta_contabil like "2188%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
    ]
    return name, left_value, right_value

def ddr_utilizada():
    name = 'DDR utilizada'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "82114%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "82114%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6221304%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6221304%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6314%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6314%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "6322%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "6322%" and escrituracao like "S"', True),
        ('BAL_VER', 'movimento_credor', 'conta_contabil like "113%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'movimento_devedor', 'conta_contabil like "2188%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', False),
        ('BAL_VER', 'movimento_devedor', 'conta_contabil like "218810499%" and escrituracao like "S" and indicador_superavit_financeiro like "F"', True),
        ('BAL_VER', 'saldo_atual_devedor','conta_contabil like "3511%" and escrituracao like "S"', True),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "3511%" and escrituracao like "S"', False),
    ]
    return name, left_value, right_value

def receita_despesa_intraorcamentaria():
    name = 'Receita vs despesa intraorçamentária'
    left_value = [
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and codigo_receita like "7%"', False),
        ('BAL_REC', 'receita_realizada', 'tipo_nivel_receita like "A" and codigo_receita like "8%"', False),
    ]
    right_value = [
        ('BAL_DESP', 'valor_pago', 'elemento like "__91%"', False),
    ]
    return name, left_value, right_value

def movimento_ativo_passivo_intra_ofss():
    name = 'Movimentação intra-OFSS do ativo e passivo'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1___2%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1___2%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "2___2%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "2___2%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def movimento_vpa_vpd_intra_ofss():
    name = 'Movimentação intra-OFSS das VPA e VPD'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "3___2%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "3___2%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "4___2%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "4___2%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value

def contribuicao_previdenciarai_rpps_a_receber():
    name = 'Contribuição previdenciária a receber pelo RPPS'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "1136201%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "1136201%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "21882%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "21882%" and escrituracao like "S"', True),
        ('BAL_DESP', 'liquidado_a_pagar', 'elemento like "319113%"', False)
    ]
    return name, left_value, right_value

def suplementacao_reducao_outra_entidade():
    name = 'Crédito adicional por redução em outra entidade'
    left_value = [
        ('DECRETO', 'valor_credito_adicional', 'origem_recurso = 6', False),
    ]
    right_value = [
        ('DECRETO', 'valor_reducao_dotacoes', 'origem_recurso = 6', False),
    ]
    return name, left_value, right_value

def dotacao_adicional_fonte_anulacao():
    name = 'Dotação adicional por fonte: anulação de dotação'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221303%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221303%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('DECRETO', 'valor_credito_adicional', 'origem_recurso in(5,6)', False),
    ]
    return name, left_value, right_value

def credito_especial_reaberto():
    name = 'Crédito especial reaberto'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "522120202%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "522120202%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('DECRETO', 'valor_reaberto', None, False),
    ]
    return name, left_value, right_value

def dotacao_adicional_fonte_excesso():
    name = 'Dotação adicional por fonte: excesso de arrecadação'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221302%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221302%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('DECRETO', 'valor_credito_adicional', 'origem_recurso = 2', False),
    ]
    return name, left_value, right_value

def dotacao_adicional_fonte_reabertura():
    name = 'Dotação adicional por fonte: reabertura'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221306%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221306%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('DECRETO', 'valor_reaberto', None, False),
    ]
    return name, left_value, right_value

def dotacao_adicional_fonte_superavit():
    name = 'Dotação adicional por fonte: superávit financeiro'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5221301%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5221301%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('DECRETO', 'valor_credito_adicional', 'origem_recurso = 1', False),
    ]
    return name, left_value, right_value