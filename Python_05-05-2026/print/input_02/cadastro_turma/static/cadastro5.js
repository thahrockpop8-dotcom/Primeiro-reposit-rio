const btnCadastrar = document.getElementById('btnCadastrar');
const btnLimpar = document.getElementById('btnLimpar');
const listaCards = document.getElementById('listaCards');
const contador = document.getElementById('contador');


btnCadastrar.addEventListener('click', async () => {

    const nome = document.getElementById('nome').value;
    const idade = document.getElementById('idade').value;
    const curso = document.getElementById('curso').value;

    const resposta = await fetch('/cadastrar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome,
            idade,
            curso
        })
    });

    const dados = await resposta.json();

    if (!dados.sucesso) {
        alert(dados.mensagem);
        return;
    }

    // Criar card
    const card = document.createElement('div');
    card.classList.add('card');

    card.innerHTML = `
        <h3>${dados.participante.nome}</h3>
        <p><strong>Idade:</strong> ${dados.participante.idade}</p>
        <p><strong>Curso:</strong> ${dados.participante.curso}</p>
        <p><strong>Classificação:</strong> ${dados.participante.classificacao}</p>
    `;

    listaCards.appendChild(card);

    // Atualizar contador
    contador.textContent = dados.total;

    // Limpar formulário
    document.getElementById('nome').value = '';
    document.getElementById('idade').value = '';
    document.getElementById('curso').value = '';
});


btnLimpar.addEventListener('click', async () => {

    const resposta = await fetch('/limpar', {
        method: 'POST'
    });

    const dados = await resposta.json();

    if (dados.sucesso) {
        listaCards.innerHTML = '';
        contador.textContent = '0';
        alert(dados.mensagem);
    }
});
