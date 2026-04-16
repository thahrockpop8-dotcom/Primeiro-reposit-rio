    function solicitarEmail() {
    let email = "";
    while (true){
    email = prompt("Por favor digite o seu e-mail.");
    

    if (email.trim() === "") 
    alert("Você cancelou a operação.");
    break;
        
        }
        if (email.trim() === "")
            alert("O campo não pode estar vazio!");
        continue;

    }

    if(!email.includes("@"))
        alert ("Por favor, insira um e-mail válido (faltou o '@')."); 

    {
        else {
            alert("E-mail cadastrado com sucesso: " + email);
        }
    }
