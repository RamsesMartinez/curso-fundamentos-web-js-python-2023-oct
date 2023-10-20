let variable = 10


switch (variable) {
    case "mensaje":
    case "MENSAJE":
        console.log("Este es un mensaje")
        break;
    case "saludo":
        console.log("hola como estas?")
        break;
    case 10:
        console.log("este es el número 10")
        break;
    default:
        console.log("No se cumplió ninguna condición")
}

