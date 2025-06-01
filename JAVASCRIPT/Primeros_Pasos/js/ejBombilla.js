function prenderApagarBombilla( interruptor ){
    let pic;

    if ( interruptor == "0" ){
        pic = "static/bombilla_apagada.png";
    } else {
        pic = "static/bombilla_encendida.png";
    }
    document.getElementById("bombilla").src = pic;
}