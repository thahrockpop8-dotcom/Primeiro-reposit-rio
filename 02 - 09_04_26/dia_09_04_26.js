function pedirNome() {
    let nome;
    let regexNome = /^[A-Za-zÀ-ÿ\s'-]+$/;
    while (true) {
        nome  = prompt("Digite o seu nome completo:"); //condição
           if (nome === null){
           alert("O nome não pode ficar vazio. ")
           continue;

        }
        if(!regexNome.test(nome)){
         alert("Digite apenas letras e espaços no nome.")
         continue;   
        }

        let partesNome = nome.split(/\s+/);
        if (partesNome.lengt < 2){
            alert ("Digite o nome completo, com nome e sobrenome.") //condição
            continue;
        }
        if (nome.length < 3){
            alert("Digite um nome válido.") //condição
            continue;
        }
        return nome; //se passou por todas as validações, retorna o nome
    }

}

function iniciarCadastro(){
    let nome = pedirNome ();
    if (nome === null){
        document.getElementById("resultado").innerHTML = 
        "<h2>Cadastro cancelado</h2><p>O usuário cancelou o preenchimento</p>"
        return;
    }
    document.getElementById("resultado").innerHTML = 
    "<h2>Resultado</h2>" + 
    "<p><strong>Nome Completo: <strong>" + nome + "</p>"

}