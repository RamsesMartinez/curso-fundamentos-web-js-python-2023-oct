/** 
Ejercicio 4: Contador de vocales
Crea un programa que cuente la cantidad de vocales
 (a, e, i, o, u) en una cadena de texto ingresada
  por el usuario.
   Utiliza un bucle for y una estructura condicional
    para verificar si cada letra es una vocal.

*/

const cadena = prompt("Ingresa una cadena de texto")

let contadorVocales = 0;

for (let index = 0; index < cadena.length; index++) {
    const letra = cadena[index].toLowerCase();
    if (letra === "a" || letra === 'e' || letra === 'i' || letra === 'o' || letra === 'u') {
        contadorVocales += 1
    }
}

console.log("La cadena " + cadena + " tiene " + contadorVocales + " vocales")