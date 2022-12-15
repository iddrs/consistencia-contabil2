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

def suprimento_de_fundos_a_apropriar():
    name = 'Suprimento de fundos a apropriar'
    left_value = [
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

def previsao_inicial_deducao_exceto_fundeb():
    name = 'Previsão inicial da dedução da receita (exceto FUNDEB)'
    left_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "5211299%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "5211299%" and escrituracao like "S"', True),
    ]
    right_value = [
        ('BAL_REC', 'receita_orcada', 'tipo_nivel_receita like "A" and caracteristica_peculiar_receita not in(0, 105)', True),
    ]
    return name, left_value, right_value

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

def cancelamento_dotacao():
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.1.01'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.1.02'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.1.03'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.1.04'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.2.01'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.2.02'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.2.03'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.2.04'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.3.01'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.3.02'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.3.03'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.3.04'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.4.01'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.4.02'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.4.03'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.4.04'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.5.01'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.5.02'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.5.03'
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
    name = 'Fechamento das contas de controle [7/8]1.1.1.5.04'
    left_value = [
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "7111504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "7111504%" and escrituracao like "S"', True),

    ]
    right_value = [
        ('BAL_VER', 'saldo_atual_credor', 'conta_contabil like "8111504%" and escrituracao like "S"', False),
        ('BAL_VER', 'saldo_atual_devedor', 'conta_contabil like "8111504%" and escrituracao like "S"', True),
    ]
    return name, left_value, right_value