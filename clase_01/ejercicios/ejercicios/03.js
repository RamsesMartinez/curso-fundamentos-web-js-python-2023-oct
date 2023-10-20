function ejemploLet() {
    let y = 1;

    if (true) {
        let y = 2;
        console.log(y); // Resultado: 2
    }

    console.log(y); // Resultado: 1
}

ejemploLet();

