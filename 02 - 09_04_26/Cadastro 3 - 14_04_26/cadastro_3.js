function  pedirIdade (){
    let idadeTexto;
    while (true){ 
        if (idadeTexto === null){ // se o usuário cancelar
            alert("Cadastro Cancelado.");
            return null;
        }
        idadeTexto = idadeTexto.trim(); // se o usúario não digitar nada
        if(idadeTexto === ""){
            alert("A idade não pode ficar vazia.");
            continue; // volta para o while
        }
        let idade = Number (idadeTexto); // aqui o número em extenso será convertido em número
        if(isNaN(idade)) || idade < 0 // o usuário não poderá digitar um número negativo
        || !Number.IsInteger(idade)) { // isinterger impede números decimais
            alert("Digite uma idade válida usando apenas números inteiros.") // vai barrar o número decimal
            continue;
        }
        return idade;
    }
}
 function digitesuaIdade(){
    let idade = pedirIdade();
    if(idade === null){
        document.getElementById("resultado").innerHTML = "<h2>Cadastro Cancelado</h2> <p>O usuario cancelou o preenchimento</P>";
        return;
        }
        document.getElementById("resultado").innerHTML = "<h2>Resultado</h2> <p><strong>Idade</strong> " + idade + anos "</p>";
        return;

    }
 