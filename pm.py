'''
Executa regras relacionadas à entidade Prefeitura.
'''
import os.path

from contest.rules import *
from contest.engine import DefaultEngine
from contest.reporter import ScreenReporter, ExcelReporter
import glob

from contest.repository import PadRepo

padrepo = PadRepo(path=r'C:\Users\Everton\Desktop\Prefeitura\PAD\v2\current\pickle', entities=['pm'])
# Verifica se tem arquivos em stage e exclui se o usuário quiser
stage_files = glob.glob(os.path.join(padrepo.stage_path, '*.db'))

if len(stage_files) > 0:
    choice = input('Existem arquivos na área de stage. Deseja excluí-los? [S/N] ')
    if choice.lower() == 's':
        print('Excluir os arquivos do stage...')
        for file in stage_files:
            os.remove(file)
    elif choice.lower() == 'n':
        print('Manter os arquivos do stage...')
    else:
        print('Você precisa escolher uma opção válida! Preste atenção da próxima vez...')
        exit()

reporters = [ScreenReporter(), ExcelReporter(r'report.xlsx')]


check_rules = (
    fechamento_natureza_patrimonial,
    fechamento_natureza_orcamentario,
    fechamento_natureza_controle,
    anulacao_dotacao,
    suprimento_de_fundos_a_apropriar,
    parcerias_a_apropriar,
    precatorios_cp_a_pagar,
    contribuicao_previdenciaria_rpps_a_pagar,
    contribuicao_previdenciaria_inss_a_pagar,
    fgts_a_pagar,
    passivo_rpp_a_pagar,
    rpp_a_pagar,
    pasep_a_pagar,
    previsao_inicial_receita_bruta,
    previsao_inicial_deducao_fundeb,
    previsao_inicial_deducao_exceto_fundeb,
    reestimativa_receita,
    dotacao_inicial,
    credito_suplementar_aberto,
    credito_especial_aberto,
    credito_extraordinario_aberto,
    cancelamento_dotacao,
    emissao_empenhos,
    rpnp_inscritos_ultimo_ano,
    rpnp_inscritos_anos_anteriores,
    rpnp_inscritos_inscricao,
    rpnp_inscritos_inscricao_saldo_inicial,
    rpp_inscritos_ultimo_ano,
    rpp_inscritos_anos_anteriores,
    rpp_inscritos_inscricao,
    rpp_inscritos_inscricao_saldo_inicial,
    receita_a_realizar,
    receita_bruta_realizada,
    deducao_receita_fundeb,
    deducao_renuncia_receita,
    deducao_outras,
    credito_empenhado_a_liquidar,
    empenhos_a_liquidar,
    credito_liquidado_a_pagar,
    empenho_liquidado_a_pagar,
    credito_pago,
    empenho_pago,
    rpnp_a_liquidar,
    rpnp_a_pagar,
    rpnp_pagos,
    rpnp_cancelados,
    rpp_pagos,
    rpp_cancelados,
    fechamento_orcamentario_11,
    fechamento_orcamentario_12,
    fechamento_orcamentario_21,
    fechamento_orcamentario_221,
    fechamento_orcamentario_222,
    fechamento_orcamentario_223,
    fechamento_orcamentario_229,
    fechamento_orcamentario_31,
    fechamento_orcamentario_32,
    fechamento_controle_111101,
    fechamento_controle_111102,
    fechamento_controle_111103,
    fechamento_controle_111104,
    fechamento_controle_111201,
    fechamento_controle_111202,
    fechamento_controle_111203,
    fechamento_controle_111204,
    fechamento_controle_111301,
    fechamento_controle_111302,
    fechamento_controle_111303,
    fechamento_controle_111304,
    fechamento_controle_111401,
    fechamento_controle_111402,
    fechamento_controle_111403,
    fechamento_controle_111404,
    fechamento_controle_111501,
    fechamento_controle_111502,
    fechamento_controle_111503,
    fechamento_controle_111504,
)

engine = DefaultEngine(repositories=[padrepo], reporters=reporters, rules=check_rules)
engine.run_tests()