/** 
Ejercicio 6: Calculadora de factorial
Escribe un programa que calcule el factorial
 de un número ingresado por el usuario.
  El factorial de un número es el producto
   de todos los enteros positivos desde 1
    hasta ese número. 
    
    Utiliza un bucle for 
    para calcular el factorial.
3 -> 3*2*1 -> 1*2*3
5 -> 5*4*3*2*1 -> 1*2*3*4*5
4 -> 4*3*2*1 -> 12*2 -> 24
5
*/

const numero = parseInt(prompt("Ingresa un número para obtener el factorial"))

let factorial = 1;

for (let index = 1; index <= numero; index++) {
    factorial *= index;
}

console.log("El factorial de " + numero + " es: " + factorial)

