'''
Executa regras relacionadas à entidade FPSM.
'''
import os.path

from contest.rules.mensal import *
from contest.engine import DefaultEngine
from contest.reporter import ScreenReporter, ExcelReporter
import glob

from contest.repository import PadRepo

ano = input('Informe o ano desejado [AAAA]: ')
mes = input('Informe o mês desejado [MM]: ').zfill(2)


padrepo = PadRepo(path=os.path.join(r'C:\Users\Everton\OneDrive - independencia.rs.gov.br\Prefeitura\PAD', f'{ano}-{mes}', 'parquet'), entities=['fpsm'])
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

reporters = [ScreenReporter(), ExcelReporter(r'report-fpsm.xlsx')]


check_rules = (
    fechamento_natureza_patrimonial,
    fechamento_natureza_orcamentario,
    fechamento_natureza_controle,
    suprimento_de_fundos_a_apropriar,
    contribuicao_previdenciaria_rpps_a_pagar,
    passivo_rpp_a_pagar,
    rpp_a_pagar,
    pasep_a_pagar,
    previsao_inicial_receita_bruta,
    # previsao_inicial_deducao_exceto_fundeb,
    previsao_inicial_deducao_renuncia,
    previsao_inicial_deducao_outras,
    reestimativa_receita,
    dotacao_inicial,
    credito_suplementar_aberto,
    credito_especial_aberto,
    credito_extraordinario_aberto,
    anulacao_dotacao,
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
    deducao_renuncia_receita,
    deducao_outras,
    credito_disponivel,
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
    fechamento_controle_112101,
    fechamento_controle_112102,
    fechamento_controle_112199,
    fechamento_controle_113101,
    fechamento_controle_113102,
    fechamento_controle_113103,
    fechamento_controle_113104,
    fechamento_controle_113105,
    fechamento_controle_113108,
    fechamento_controle_113112,
    fechamento_controle_113113,
    fechamento_controle_113199,
    fechamento_controle_1141,
    fechamento_controle_1142,
    fechamento_controle_1143,
    fechamento_controle_1144,
    fechamento_controle_1145,
    fechamento_controle_119101,
    fechamento_controle_119102,
    fechamento_controle_119103,
    fechamento_controle_119104,
    fechamento_controle_119105,
    fechamento_controle_121101,
    fechamento_controle_121102,
    fechamento_controle_121103,
    fechamento_controle_121104,
    fechamento_controle_121201,
    fechamento_controle_121202,
    fechamento_controle_121203,
    fechamento_controle_121204,
    fechamento_controle_121301,
    fechamento_controle_121302,
    fechamento_controle_121303,
    fechamento_controle_121304,
    fechamento_controle_121401,
    fechamento_controle_121402,
    fechamento_controle_121403,
    fechamento_controle_121404,
    fechamento_controle_121501,
    fechamento_controle_121502,
    fechamento_controle_121503,
    fechamento_controle_121504,
    fechamento_controle_122101,
    fechamento_controle_122102,
    fechamento_controle_122199,
    fechamento_controle_123101,
    fechamento_controle_123102,
    fechamento_controle_123103,
    fechamento_controle_123104,
    fechamento_controle_123105,
    fechamento_controle_123106,
    fechamento_controle_123107,
    fechamento_controle_123108,
    fechamento_controle_123109,
    fechamento_controle_123110,
    fechamento_controle_123111,
    fechamento_controle_123112,
    fechamento_controle_123113,
    fechamento_controle_123199,
    fechamento_controle_1241,
    fechamento_controle_1242,
    fechamento_controle_1243,
    fechamento_controle_1244,
    fechamento_controle_1245,
    fechamento_controle_129101,
    fechamento_controle_129102,
    fechamento_controle_1292,
    fechamento_controle_1293,
    fechamento_controle_21,
    fechamento_controle_22,
    fechamento_controle_23,
    fechamento_controle_24,
    fechamento_controle_31,
    fechamento_controle_32,
    fechamento_controle_4111,
    fechamento_controle_4112,
    fechamento_controle_4113,
    fechamento_controle_4114,
    fechamento_controle_4115,
    fechamento_controle_4119,
    fechamento_controle_4211,
    fechamento_controle_4212,
    fechamento_controle_4213,
    fechamento_controle_4214,
    fechamento_controle_52,
    fechamento_controle_531,
    fechamento_controle_532,
    fechamento_controle_533,
    fechamento_controle_534,
    fechamento_controle_535,
    fechamento_controle_536,
    fechamento_controle_537,
    fechamento_controle_611,
    fechamento_controle_612,
    fechamento_controle_613,
    fechamento_controle_619,
    fechamento_controle_62,
    fechamento_controle_631,
    fechamento_controle_632,
    fechamento_controle_633,
    fechamento_controle_8,
    fechamento_controle_9111,
    fechamento_controle_9112,
    fechamento_controle_9113,
    fechamento_controle_9114,
    fechamento_controle_9115,
    fechamento_controle_9119,
    fechamento_controle_9121,
    fechamento_controle_9122,
    fechamento_controle_9124,
    fechamento_controle_9125,
    fechamento_controle_912901,
    fechamento_controle_925,
    fechamento_controle_926,
    fechamento_controle_929,
    fechamento_controle_9991,
    fechamento_controle_9992,
    fechamento_controle_9993,
    fechamento_controle_9994,
    fechamento_controle_9995,
    disponibilidades,
    resultado_financeiro,
    resultado_periodo,
    situacao_financeira_orcamentaria,
    ddr_disponivel,
    ddr_comprometida_empenho,
    ddr_comprometida_liquidacao,
    # ddr_utilizada, Desativado porque não estou conseguindo pegar a movimentação extra-orçamentária de forma correta pelos dados do PAD.
)

engine = DefaultEngine(repositories=[padrepo], reporters=reporters, rules=check_rules)
engine.run_tests()