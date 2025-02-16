let senhaCerta = '2606';

const display = document.getElementById("senha")


function digitar(input){
    display.value += input;
}

function apagar(){
    display.value = display.value.slice(0,-1)
}


document.getElementById('botao').onclick = function(){
    if (document.getElementById ("senha").value == senhaCerta){
        
        document.getElementById ("senha").style.opacity = 0

        document.querySelector(".barra").classList.add("ativar");

        document.querySelector(".certo").classList.add("ativar")


        setTimeout(() => {
            window.location.href = "../Netflix/deborapage.html"
        }, 5000);
        }

   else {
    
    document.getElementById ("senha").style.opacity = 0
       
    document.querySelector(".barraX").classList.add("ativar")
       
    document.querySelector(".errado").classList.add("ativar")

    setTimeout(() => {
        location.reload()
    }, 4000);

   }
}

