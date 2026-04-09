function pedirNome() {
    let nome;
    let regexNome = /^[A-Za-zÀ-ÿ\s'-]+$/;
    while (true) {
        nome  = prompt("Digite o seu nome completo:") ;
           if (nome === null){
           alert("O nome não pode ficar vazio. ")
           continue;

        }
        if(!regexNome.test(nome)){
         alert("Digite apenas letras e espaços no nome.");
         continue;   
        }
        
    }

}