# Iniciando o Python Environment
.\venv\Scripts\activate.ps1

# Escolhendo o perfil de testes
$opt = '&Câmara', '&FPSM', '&Prefeitura', '&Agregado'
$RunR = $Host.UI.PromptForChoice('Executar testes de consistência', 'Escolha um perfil:', $opt, -1)

if ($RunR -eq 0) {
    python cm.py
} elseif ($RunR -eq 1) {
    python fpsm.py
} elseif ($RunR -eq 2) {
    python pm.py
} elseif ($RunR -eq 3) {
    python mun.py
} else {
    Write-Error 'Opção inválida!'
}

Write-Host 'Execução dos testes terminada'

# Desativa o Python Environment
deactivate