/** 
Ejercicio 1: Suma de números pares
Escribe un programa que calcule la suma de todos
 los números pares del 1 al 100.
  Utiliza un bucle for para iterar a través de los números
   y una estructura condicional if para verificar si un número es par.

let suma = 0;

for (let i = 2; i <= 100; i += 2) {
    suma += i;
}

console.log(suma)

*/

let suma = 0;

for (let i = 1; i <= 100; i++) {
    if (i % 2 === 0) {
        suma += i;
    }
}

console.log(suma)