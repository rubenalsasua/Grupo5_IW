/* Programa Menu Vertical. Cuando se pulsa hacemos desplegar el menu */

function toggleMenu() {
    var menuItems = document.getElementById("menuItems");
    if (menuItems.style.display === "none") {
      menuItems.style.display = "block";
    } else {
      menuItems.style.display = "none";
    }
  }