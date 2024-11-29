const link = document.getElementById('inicio');

link.addEventListener('transition', function() {
    window.location.href = link.href;
});
