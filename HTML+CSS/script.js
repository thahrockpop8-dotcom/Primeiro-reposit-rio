function iniciar(){
    alert ("Bem-Vindo à página do cantor Paul Maccartney!");
    let nome = prompt ("digite o seu nome:");
    console.log ("Nome digitado: " + nome);
    let titulo = document.getElementById("titulo");
    titulo.innerHTML = "Paul Maccartney<br>Olá, " + nome + " ! 🎵";
    

}

function clicou (){
    alert("Você será redirecionado para saber mais sobre o cantor Paul Maccartney");
}

window.onload = iniciar;