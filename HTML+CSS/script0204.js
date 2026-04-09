function comecar_historia(){
    alert("Bem-vindo!");
    let nome = prompt ("Qual seu personagem favorito?");
    console.log ("Nome digitado: " + nome);
    let titulo = document.getElementById("titulo");
    alert("Seja Bem-vindo! Ao nightmare " + nome + " Está pronto(a)?")
     
    document.getElementById("resultado").innerHTML = `
        <p> Era uma vez Luce, que despertando de um sono profundo não soube dizer 
            se as pessoas à sua volta eram reais ou fruto de sua imaginação. <br>
            Ela sentiu-se dissociada, um misto de medo, ansiedade e fascinação. <br>
            Mas ao olhar para o lado, seu coração se acalentou um pouco mais, pois ali estava Kiara. <br>
        </p>
    `;
}

