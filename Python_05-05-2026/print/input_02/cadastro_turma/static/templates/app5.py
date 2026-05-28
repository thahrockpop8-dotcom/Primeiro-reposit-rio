from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista para guardar os cadastros
cadastros = []


# Página principal
@app.route('/')
def home():
    mensagem = "Olá! Este texto veio do Python."
    return render_template('cadastro5.html', texto_dinamico=mensagem)


# Rota de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    dados = request.get_json(silent=True) or request.form or {}

    nome = dados.get('nome', '').strip()
    idade = dados.get('idade', '')
    curso = dados.get('curso', '').strip()

    # Validação do nome
    if not nome:
        return jsonify({
            'sucesso': False,
            'mensagem': 'O nome é obrigatório!'
        })

    # Validação da idade
    try:
        idade = int(idade)

        if idade < 0:
            raise ValueError

    except (ValueError, TypeError):
        return jsonify({
            'sucesso': False,
            'mensagem': 'Idade inválida!'
        })

    # Classificação
    if idade <= 12:
        classificacao = 'Criança'

    elif idade <= 17:
        classificacao = 'Adolescente'

    else:
        classificacao = 'Adulto'

    # Cadastro
    participante = {
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'classificacao': classificacao
    }

    # Guardar na lista
    cadastros.append(participante)

    return jsonify({
        'sucesso': True,
        'mensagem': 'Cadastro realizado com sucesso!',
        'participante': participante,
        'total': len(cadastros)
    })


# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
