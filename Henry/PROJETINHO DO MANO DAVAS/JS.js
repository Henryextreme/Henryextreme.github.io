let jogos = [];
online = -1
function ifonline(x){
    online = x
    criarcards()
}
async function carregarJogos() {
    try {
        const response = await fetch('jogos.json');
        if (!response.ok) {
            throw new Error('Erro ao carregar o JSON');
        }
        jogos = await response.json();
        criarcards();
    } catch (error) {
        console.error('Erro ao carregar o JSON:', error);
    }
}

function criarcard(x) {
    jogoonline = parseInt(jogos[x].online)
    if(jogoonline === online || online === -1){
        document.getElementById("jogos").innerHTML += `
        <div class="jogo">
            <img class="foto" src="${jogos[x].foto}">
            <div class="texto">
                <div class="title" id="title${x}">${jogos[x].nome}</div>
                <div class="descricao">${jogos[x].descricao}</div>
            </div>
            <div class="download">
                <a href="${jogos[x].link_download}" class="download"><i class="gg-software-download"></i></a>
            </div>
        </div>`;
        ajustarFontSize(x);
    }
}

function criarcards() {
    document.getElementById("jogos").innerHTML = "";
    for (let x = 0; x < jogos.length; x++) {
        criarcard(x);
    }
}

function ajustarFontSize(x) {
    if (jogos[x].nome.length > 5) {
        document.getElementById("title" + x).style.fontSize = 300 / jogos[x].nome.length + 'px';
    } else {
        document.getElementById("title" + x).style.fontSize = '30px';
    }
}

function pesquisa() {
    const barra = document.getElementById("search_bar").value.toLowerCase();
    document.getElementById("jogos").innerHTML = "";
    for (let x = 0; x < jogos.length; x++) {
        const nomeJogo = jogos[x].nome.toLowerCase();
        if(barra.length == 1 && nomeJogo[0] === barra[0]){
            criarcard(x);
        }
        else {
            if (nomeJogo.includes(barra) && barra.length != 1) {
                criarcard(x);
            }
        }
    }
}

document.getElementById("search_bar").addEventListener('input', () => {
    const search = document.getElementById("search_bar").value;
    if (search === '') {
        criarcards();
    } else {
        pesquisa();
    }
});

window.onload = carregarJogos;