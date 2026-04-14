function pedirGenero (){
let pedirGenero;
    while (true){ 
        if (pedirGenero === null){ // se o usuário cancelar
            alert("Preenchimento Cancelado.");
            return null; 
            
        }
        Genero = pedirGenerotexto.trim()
        if (pedirGenero === ""){
            alert ("Este campo não pode ficar vazio");
            continue;
        }

        if (Genero!== "masculino" && genero ! == "feminino" && genero !== "outro")
            alert("Digite apenas: masculino, feminino, outro.");
        continue;
     }

     return;
    
}
        document.getElementById("resultado").innerHTML = "<h2>Resultado</h2><p><strong>Genero:</strong> " + genero + "</p>";



function pedirTelefone (){
    let telefoneNumero
     while (true){ 
        if (telefoneNumero === null){ // se o usuário cancelar
            alert("Preenchimento Cancelado.");
            return null;
        }
        telefoneNumero = telefoneNumero.trim(); // se o usúario não digitar nada
        if(telefoneNumero === ""){
            alert("Este campo não pode ficar vazio.");
            continue; // volta para o while
    }
    return telefoneNumero;
}
}

function pedirEstadoCivil (){
    let pedirEstadoCivil
    while (true){
        if (pedirEstadoCivil === null){
            alert ("Preenchimento cancelado.");
            return null;

        }
        pedirEstadoCivil = pedirEstadoCivil.trim()
        if (pedirEstadoCivil === ""){
            alert ("Este campo não pode ficar vazio");
            continue;
        }

        if (pedirEstadoCivil!== "Casado(a)" && pedirEstadoCivil ! == "Solteiro(a)" && pedirEstadoCivil !== "Viúvo(a)")
            alert("Digite apenas: casado(a), solteiro(a), viúvo(a).");
        continue;    
    }
    return pedirEstadoCivil;

}


