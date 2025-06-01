console.log('Inicio');

setTimeout(()=> {
    console.log("Esto se ejecuta en 2 segundos")
}, 2000)

setTimeout(()=> {
    console.log("Esto se ejecuta en 0 segundos, despues de Inicio")
}, 0)

console.log("Final")