/** 
Ejercicio 7: Números del 1 al 100
Imprime todos los números del 1 al 100 en la consola,
 pero para los múltiplos de 3, muestra "Fizz" en lugar del número, 
 y para los múltiplos de 5, muestra "Buzz".
  Para los números que son múltiplos de ambos (por ejemplo, 15), 
  muestra "FizzBuzz".
*/

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz")
    } else if (i % 3 === 0) { // Múltiplos -> módulo -> %
        console.log("Fizz")
    } else if (i % 5 === 0) {
        console.log("Buzz")
    } else {
        console.log(i)
    }
}
