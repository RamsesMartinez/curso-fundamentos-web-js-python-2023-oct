/** 
Ejercicio 2: Tabla de multiplicar
Crea un programa que solicite al usuario un número y luego
 muestre la tabla de multiplicar de ese número del 1 al 10.
  Utiliza un bucle for para generar la tabla.

*/

const numero = parseInt(prompt("Ingresa un número para generar la tabla de multiplicar"))

for (let i = 1; i <= 10; i++) {
    console.log(`${numero} x ${i} = ${numero * i}`)
}
