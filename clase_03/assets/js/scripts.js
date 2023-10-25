
// let etiqueta = document.getElementById("etiqueta-de-ejemplo")

// let etiquetasPorClase = document.getElementsByClassName("container")

// let etiquetasPorTag = document.getElementsByTagName("p");

// let etiquetasPorQuery = document.querySelectorAll(".container p")
// console.log(etiquetasPorQuery)

// let elemento = document.getElementById("square-container");
// console.log(elemento.childNodes)
// console.log(elemento.parentNode)


let box = document.getElementById("box1")
let nuevoElemento = document.createElement("p")
let texto =  document.createTextNode("Hola desde JS")
nuevoElemento.appendChild(texto)
box.appendChild(nuevoElemento)

let box2 = document.getElementById("box2")
box.insertAdjacentHTML("beforebegin", "<div><p>un parrafo nuevo!!!</p></div>")
