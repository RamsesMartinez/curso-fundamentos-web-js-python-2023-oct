// Operaciones aritmeticos

const num1 = 5;
const num2 = 10;
const num3 = 20;

// Suma
let suma = num1 + num2

// Resta
let resta = num1 - num2

// Multiplicación
let mult = num1*num2;

// División
let divi = num1 / num2;

// Módulo
let modulo = num1 % num2;



// OPERADORES LÓGICOS
const esMayor = num1 > num2;
// console.log(num1, num2, esMayor)

const esMenor = num1 < num2;
// console.log(num1, num2, esMenor)

const esIgual = num1 === num3;
// console.log(num1, num3, esIgual)

const esNumDiferente = num1 !== num2;
// console.log(num1, num2, esNumDiferente)

let cadena1 = "Gato";
let cadena2 = "Perro";
const esStrDiferente = cadena1 !== cadena2;
const esStrIgual = cadena1 === cadena2;

// AND y OR

const esAnd = (num1 < num2) && (num2 < num3) // &&

const esOr = !((num1 > num2) || (num2 < num3))
console.log(esOr);