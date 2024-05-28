/* Programa Menu Vertical. Cuando se pulsa hacemos desplegar el menu */
function toggleMenu() {
    var menuItems = document.getElementById("menuItems");
    if (menuItems.style.display === "none") {
        menuItems.style.display = "block";
    } else {
        menuItems.style.display = "none";
    }
}


document.getElementById('aumentar').addEventListener('click', function (event) {
    let elementos = document.querySelectorAll("a, p, h1, h2, h3, h4, th, td");
    for (let i in elementos) {
        let estilo = window.getComputedStyle(elementos[i]);
        let tamano = estilo.getPropertyValue("font-size");
        let num_tamano = parseFloat(tamano);
        elementos[i].style.fontSize = (num_tamano + 1) + 'px';
    }
});

document.getElementById('reducir').addEventListener('click', function (event) {
    let elementos = document.querySelectorAll("a, p, h1, h2, h3, h4, th, td, button");
    for (let i in elementos) {
        let estilo = window.getComputedStyle(elementos[i]);
        let tamano = estilo.getPropertyValue("font-size");
        let num_tamano = parseFloat(tamano);
        elementos[i].style.fontSize = (num_tamano - 1) + 'px';
    }
});