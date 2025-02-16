setTimeout(function() {
    document.getElementById ("txt").textContent = "Te manca vai!";
    document.getElementById("camera").style.opacity = 0
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f620.svg"
}, 2000);

setTimeout(function() {
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f60a.svg"
    document.getElementById("camera").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f447.svg"
    document.getElementById("camera").style.opacity = 1
    document.getElementById ("txt").textContent = "To brincando amor, nunca ia te tratar assim, é só clicar no botão abaixo pra voltar pro menu"
    document.getElementById("botao").style.display = "block"
}, 4000);

function amor(){
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f97a.svg"
    document.getElementById("camera").style.opacity = 0
    document.getElementById ("txt").textContent = "Antes q tu vá, só pra eu ter ctz, tu me ama mesmo?"
    document.getElementById("botao").style.display = "none"
    document.getElementById("sim").style.display = "block"
    document.getElementById("nao").style.display = "block"
}

document.addEventListener("DOMContentLoaded", function () {
    const nao = document.getElementById("nao");
    const sim = document.getElementById("sim"); // Seleciona o botão "sim"
    
    nao.addEventListener("click", function () {
        // Gera uma posição aleatória dentro da largura e altura da janela
        const largura = window.innerWidth - nao.offsetWidth;  // Ajusta para não ultrapassar a tela
        const altura = window.innerHeight - nao.offsetHeight; // Ajusta para não ultrapassar a tela
        
        // Gera coordenadas aleatórias para as posições X e Y
        const posX = Math.floor(Math.random() * largura);
        const posY = Math.floor(Math.random() * altura);
        
        // Move o botão "não" para a nova posição
        nao.style.left = posX + 'px';
        nao.style.top = posY + 'px';
        
        // Aumenta o tamanho do botão "sim" em 10px
        let larguraSim = sim.offsetWidth;
        let alturaSim = sim.offsetHeight;
        let fontSizeSim = window.getComputedStyle(sim).fontSize; // Pega o tamanho atual da fonte
        
        larguraSim += 50;  // Aumenta 10px na largura
        alturaSim += 50;   // Aumenta 10px na altura
        fontSizeSim = parseFloat(fontSizeSim) + 15 + 'px';  // Aumenta 2px no tamanho da fonte (ajuste o valor conforme necessário)
        
        // Aplica o novo tamanho ao botão "sim"
        sim.style.width = larguraSim + 'px';
        sim.style.height = alturaSim + 'px';
        sim.style.fontSize = fontSizeSim;  // Aplica o novo tamanho da fonte
    });
});

function sim(){
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f60a.svg"
    document.getElementById("camera").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f618.svg"
    document.getElementById("camera").style.opacity = 1
    document.getElementById("txt").textContent = "ooown, tmb te amo minha linda, ta liberada agr"
    document.getElementById("sim").style.display = "none"
    document.getElementById("nao").style.display = "none"
    document.getElementById("menu").style.display = "block"
}

function voltar(){
    window.location.href = "../menu/menu.html";
}