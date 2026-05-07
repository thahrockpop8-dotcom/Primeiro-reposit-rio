/*Dia 30/04/2026*/

// ===== MOSTRAR/OCULTAR TERMOS =====
const termos = document.querySelectorAll("dt");

termos.forEach(dt => {
    dt.addEventListener("click", () => {
        let next = dt.nextElementSibling;

        while (next && next.tagName !== "DT") {
            next.classList.toggle("ativo");
            next = next.nextElementSibling;
        }
    });
});


// ===== BUSCA =====
const form = document.querySelector("form");
const input = document.getElementById("busca");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    const termo = input.value.toLowerCase();
    let encontrado = false;

    termos.forEach(dt => {
        if (dt.textContent.toLowerCase().includes(termo)) {
            dt.scrollIntoView({ behavior: "smooth", block: "center" });

            let next = dt.nextElementSibling;
            while (next && next.tagName !== "DT") {
                next.classList.add("ativo");
                next = next.nextElementSibling;
            }

            encontrado = true;
        }
    });

    if (!encontrado) {
        alert("Esse termo não existe no glossário.");
    }
});


// ===== BOTÃO VOLTAR AO TOPO =====
const btnTopo = document.createElement("button");
btnTopo.id = "topoBtn";
btnTopo.innerHTML = "↑";
document.body.appendChild(btnTopo);

window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
        btnTopo.style.display = "block";
    } else {
        btnTopo.style.display = "none";
    }
});

btnTopo.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});