/* Programa Menu Vertical. Cuando se pulsa hacemos desplegar el menu */
function toggleMenu() {
    var menuItems = document.getElementById("menuItems");
    if (menuItems.style.display === "none") {
        menuItems.style.display = "block";
    } else {
        menuItems.style.display = "none";
    }
}
document.getElementById('aumentar').addEventListener('click',function (event){
    let elementos = document.querySelectorAll("a");
        for (let i in elementos) {
            console.log(getComputedStyle(elementos[i]));
        }
});