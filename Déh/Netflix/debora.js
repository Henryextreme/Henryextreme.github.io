function sair(){
    document.getElementById ("card").style.display = "none"
}

const toggle = document.getElementById("like");
const mao = document.getElementById("mao")

toggle.addEventListener("click",function() {
    if (mao.className === "fa fa-thumbs-o-up"){
        mao.className = "fa fa-thumbs-up";
    } else{
        mao.className = "fa fa-thumbs-o-up"
    }

});


const lista = document.getElementById("lista");
const mais = document.getElementById("mais")

lista.addEventListener("click", function(){
    if (mais.className === "fa fa-plus"){
        mais.className = "fa fa-check";
    }else {
        mais.className = "fa fa-plus";
    }
    
})

function bomDia(){
    document.getElementById("capa").src = "../Capas/Bom dia deba.jpg"
    document.getElementById("categoria").textContent = "Comédia, Crime, Suspense, Drama, Mistério, Ficção criminal, Policial"
    document.getElementById("sinopse").textContent = "Uma policial investiga um predador sexual e acaba descobrindo um casal com um segredo horrível e um esquema de corrupção sinistro. Com Tainá Müller, Camila Morgado e Eduardo Moscovis. Baseada no livro de Raphael Montes e Ilana Casoy."
    document.getElementById("card").style.display = "block"
}

function crepusculo(){
    document.getElementById("capa").src = "../Capas/Crepulsculo.png"
    document.getElementById("categoria").textContent = "Comédia, Crime, Suspense, Drama, Mistério, Ficção criminal, Policial"
    document.getElementById("sinopse").textContent = "Isabella Swan (Kristen Stewart) e seu pai, Charlie (Billy Burke), mudaram-se recentemente. No novo colégio ela logo conhece Edward Cullen (Robert Pattinson), um jovem admirado por todas as garotas locais e que mantém uma aura de mistério em torno de si. Eles aos poucos se apaixonam, mas Edward sabe que isto põe a vida de Isabella em risco."
    document.getElementById("card").style.display = "block"
}

function capAme(){
    document.getElementById("capa").src = "../Capas/Capitao america.png"
    document.getElementById("categoria").textContent = "Ação, Super-herói, Ficção Cientifica, Aventura, Espião, Ficção Criminal "
    document.getElementById("sinopse").textContent = "Dois anos após os acontecimentos em Nova York (Os Vingadores - The Avengers), Steve Rogers (Chris Evans) continua seu dedicado trabalho com a agência S.H.I.E.L.D. e também segue tentando se acostumar com o fato de que foi descongelado e acordou décadas depois de seu tempo. Em parceria com Natasha Romanoff (Scarlett Johansson), também conhecida como Viúva Negra, ele é obrigado a enfrentar um poderoso e misterioso inimigo chamado Soldado Invernal, que visita Washington e abala o dia a dia da S.H.I.E.L.D., ainda liderada por Nick Fury (Samuel L. Jackson)."
    document.getElementById("card").style.display = "block"
}

function bomDia(){
    document.getElementById("capa").src = "../Capas/Bom dia deba.jpg"
    document.getElementById("categoria").textContent = "Comédia, Crime, Suspense, Drama, Mistério, Ficção criminal, Policial"
    document.getElementById("sinopse").textContent = "Uma policial investiga um predador sexual e acaba descobrindo um casal com um segredo horrível e um esquema de corrupção sinistro. Com Tainá Müller, Camila Morgado e Eduardo Moscovis. Baseada no livro de Raphael Montes e Ilana Casoy."
    document.getElementById("card").style.display = "block"
}

function bomDia(){
    document.getElementById("capa").src = "../Capas/Bom dia deba.jpg"
    document.getElementById("categoria").textContent = "Comédia, Crime, Suspense, Drama, Mistério, Ficção criminal, Policial"
    document.getElementById("sinopse").textContent = "Uma policial investiga um predador sexual e acaba descobrindo um casal com um segredo horrível e um esquema de corrupção sinistro. Com Tainá Müller, Camila Morgado e Eduardo Moscovis. Baseada no livro de Raphael Montes e Ilana Casoy."
    document.getElementById("card").style.display = "block"
}