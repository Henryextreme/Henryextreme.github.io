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

function driver(){
    document.getElementById("capa").src = "../Capas/Deba driver.png"
    document.getElementById("categoria").textContent = "Ação, Crime, Thriller"
    document.getElementById("sinopse").textContent = " Baby (Ansel Elgort) é um jovem motorista de fuga talentoso que usa a música para aprimorar suas habilidades ao volante. Trabalhando para um chefe do crime (Kevin Spacey), ele deseja sair da vida criminosa após conhecer Debora (Lily James), seu grande amor. No entanto, um último assalto coloca tudo em risco, forçando Baby a enfrentar perigosas consequências enquanto tenta se libertar do passado."
    document.getElementById("card").style.display = "block"
}

function superNat(){
    document.getElementById("capa").src = "../Capas/Supernatural.png"
    document.getElementById("categoria").textContent = "Terror, Fantasia, Drama, Ação"
    document.getElementById("sinopse").textContent = "Os irmãos Sam (Jared Padalecki) e Dean Winchester (Jensen Ackles) percorrem os Estados Unidos caçando criaturas sobrenaturais, desde fantasmas e demônios até deuses e seres mitológicos. Criados para seguir os passos do pai na luta contra o mal, eles enfrentam forças sombrias enquanto lidam com segredos de família, profecias apocalípticas e alianças inesperadas."
    document.getElementById("card").style.display = "block"
}

function anatomy(){
    document.getElementById("capa").src = "../Capas/Debs anatomy.jpg"
    document.getElementById("categoria").textContent = "Drama, Romance, Médico"
    document.getElementById("sinopse").textContent = "A série acompanha a vida pessoal e profissional dos médicos do Grey Sloan Memorial Hospital, focando na jornada da cirurgiã Meredith Grey (Ellen Pompeo). Desde sua residência até se tornar uma das médicas mais renomadas, ela e seus colegas enfrentam desafios médicos intensos, tragédias pessoais e romances complicados."
    document.getElementById("card").style.display = "block"
}

function bridgerton(){
    document.getElementById("capa").src = "../Capas/Bridgerton.jpg"
    document.getElementById("categoria").textContent = "Drama, Romance, Período Histórico"
    document.getElementById("sinopse").textContent = "Situada na alta sociedade londrina do início do século XIX, a série acompanha os Bridgertons, uma influente família aristocrática, enquanto seus membros buscam amor e casamento em meio a bailes luxuosos, escândalos e fofocas. A misteriosa Lady Whistledown, uma colunista anônima, expõe segredos da elite, tornando cada temporada um jogo de estratégia e paixão."
    document.getElementById("card").style.display = "block"
}

function linda(){
    document.getElementById("capa").src = "../Capas/A garota mais linda do mundo.jpg"
    document.getElementById("categoria").textContent = "Indonésios, Filmes de comédia romântica, Filmes de comédia"
    document.getElementById("sinopse").textContent = "Um playboy cria um reality de namro para conquistar a tão sonhada herança e realizar o último desejo do pai: se casar com a mulher mais linda do mundo"
    document.getElementById("card").style.display = "block"
}

function resgate(){
    document.getElementById("capa").src = "../Capas/Resgate 2.jpg"
    document.getElementById("categoria").textContent = "Ação, Thriller"
    document.getElementById("sinopse").textContent = "Após sobreviver aos eventos do primeiro filme, o mercenário Tyler Rake (Chris Hemsworth) recebe uma nova missão perigosa: resgatar a família de um criminoso brutal de uma prisão de segurança máxima. Com sequências de ação intensas e uma nova ameaça implacável, Tyler precisa enfrentar inimigos mortais enquanto luta para proteger os inocentes e sobreviver a mais um desafio quase impossível."
    document.getElementById("card").style.display = "block"
}