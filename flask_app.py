from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
@app.route('/')
def mostra_inicio():
    return render_template('inicio.html')


@app.route('/login')
def mostra_login():
    return render_template('login.html')


## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

'''
Boa noite alunos,

A atividade 4 vai consistir em criar uma aplicação Flask no Heroku com duas telas como mostrado nas imagens anexas. As rotas a implementar vão ser /inicio e /login (como mostrado no vídeo anexo). Criar um repositorio de nome AC04 no GitHub e enviar o link junto com o link da aplicação rodando no Heroku. A atividade pode ser feita de forma individual ou em duplas. Os criterios de avaliação são:

- Uso do Bootstrap e Flexbox
- Uso de templates
- Responsividade das páginas (como mostrado no vídeo).
- Aplicação rodando no Heroku
- Uso do pipenv (arquivos Pipfile e Pipfile.lock)
- Código no GitHub

Podem usar os arquivos das aulas 09 e 07. Qualquer dúvida fico à disposição.
'''