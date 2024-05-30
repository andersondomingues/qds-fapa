# qds-fapa

<a href="#" target="_blank">
    <img src="badges/tests.svg" alt="Test">
</a>

Este projeto é um exemplo de como utilizar o github de uma forma simples.

# comandos do git (básicos)
- `git clone <url_projeto>`: 'baixa' o projeto no seu computador
- `git add <arquivo>`: adiciona um arquivo no índice (vai para o próximo commit)
- `git commit -m <msg>`: cria uma 'versão' do seu código e coloca a mensagem na descrição
- `git push`: envia os commits ao servidor remoto
- `git pull`: puxa as alterações que existem no servidor

# comandos do git (branches)
- `git checkout -b <nome>`: cria uma nova branch 
- `git checkout <nome>`: ativa uma branch já existente
- `git push --set-upstream origin testes`: cria uma nova branch no servidor remoto no momento do primeiro push
- `git checkout -- .\test_main.py`: retorna o arquivo para a versão que estava no último commit (reseta)
- `git merge <branch>`: junta a branch escolhida à branch atual (cola as duas em uma só)


# comandos do python
- `python -m venv .venv`: cria um ambiente virtual no seu projeto
- `./.venv/Scripts/Activate.ps1`: ativa o ambiente virtual no seu terminal
- `python -m pip install pytest`: instala o pytest no seu ambiente virtual (se você criou E ativou o ambiente virtual)
- `python -m pytest`: testa o projeto

