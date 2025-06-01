function mostrarMensajeIfAnidado(){
    var estatura = parseFloat(document.getElementById("estatura").value);
    var peso = parseFloat(document.getElementById("peso").value);
    var estadoCivil = document.getElementById("estadoCivil").value;

    const parametroEstatura = 1.30
    const parametroPeso = 100
    const parametroEstadoCivil = "soltero"

    if (estatura >= parametroEstatura){ //comparativas
        if (peso <= parametroPeso){
            if (estadoCivil == parametroEstadoCivil){
                resultado = "Saludable"
            }else{
                resultado = "No saludable, no es soltero manin"
            }
        }else{
            resultado = "No saludable, Peso elevado"
        }
    }else{
        resultado = "No saludable, Estatura baja"
    }
    document.getElementById("resultadoAT").innerHTML = resultado;
}

// if(estatura >= parametroEstatura && peso <= parametroPeso && estadoCivil == parametroEstadoCivil){
//     resultado = "Saludable"
// }else{
//     resultado = "No saludable"}