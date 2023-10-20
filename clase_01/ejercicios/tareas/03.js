/** 
Ejercicio 3: Números primos
Escribe un programa que verifique si un número
 ingresado por el usuario es primo o no. 
 Un número primo es aquel que solo es divisible por 1
  y por sí mismo. 
  Utiliza un bucle for y una estructura condicional 
  para determinar si el número es primo.

  Ejemplos:4
*/

const numero = parseInt(prompt("Ingresa un número para verificar si es un número primo"))
let esPrimo = true;

if (numero <= 1) {
    esPrimo = false;
} else {
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) { // Es par
            esPrimo = false;
            break;
        }
    }
}
console.log(esPrimo)
