/** 
Ejercicio 5: Adivina el número
Desarrolla un juego en el que la computadora 
elija un número aleatorio entre 1 y 100, 
y el jugador debe adivinarlo. 
Proporciona pistas (más alto, más bajo) 
después de cada intento del jugador y 
cuenta la cantidad de intentos. 

Utiliza un bucle while para permitir 
que el jugador adivine hasta que lo logre o se 
quede sin intentos.

*/

const numeroAleatorio = Math.floor(
    Math.random() * 100
) + 1


while (true) {
    const intento = parseInt(prompt("Adiviuna el número del 1 al 100: "))

    if (intento === numeroAleatorio) {
        alert("Felicidades, adivinaste el número")
        break;
    } else if (intento < numeroAleatorio) {
        // Si el numero es más pequeño
        alert("El número es más alto...")
    } else {
        alert("El número es más pequeño...")
    }
}