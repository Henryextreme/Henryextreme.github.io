setTimeout(function() {
    document.getElementById ("txt").textContent = "Te manca vai!";
    document.getElementById("camera").style.opacity = 0
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f620.svg"
}, 2000);

setTimeout(function() {
    document.getElementById("emoji").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f60a.svg"
    document.getElementById("camera").style.opacity = 1
    document.getElementById("camera").src = "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f447.svg"
    document.getElementById ("txt").textContent = "To brincando amor, nunca ia te tratar assim, é só clicar no botão abaixo pra voltar pro menu"
}, 4000);