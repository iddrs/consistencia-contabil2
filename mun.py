'''
Executa regras relacionadas ao município de forma agregada.
'''
import os.path

from contest.rules.mensal import *
from contest.engine import DefaultEngine
from contest.reporter import ScreenReporter, ExcelReporter
import glob

from contest.repository import PadRepo

ano = input('Informe o ano desejado [AAAA]: ')
mes = input('Informe o mês desejado [MM]: ').zfill(2)


padrepo = PadRepo(path=os.path.join(r'C:\Users\Everton\OneDrive - independencia.rs.gov.br\Prefeitura\PAD', f'{ano}-{mes}', 'parquet'), entities=['cm', 'pm', 'fpsm'])
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

reporters = [ScreenReporter(), ExcelReporter(r'report-mun.xlsx')]


check_rules = (
    receita_despesa_intraorcamentaria,
    movimento_ativo_passivo_intra_ofss,
    movimento_vpa_vpd_intra_ofss,
    contribuicao_previdenciarai_rpps_a_receber,
    suplementacao_reducao_outra_entidade,
    dotacao_adicional_fonte_anulacao,
    credito_especial_reaberto,
    dotacao_adicional_fonte_excesso,
    dotacao_adicional_fonte_reabertura,
    dotacao_adicional_fonte_superavit
)

engine = DefaultEngine(repositories=[padrepo], reporters=reporters, rules=check_rules)
engine.run_tests()