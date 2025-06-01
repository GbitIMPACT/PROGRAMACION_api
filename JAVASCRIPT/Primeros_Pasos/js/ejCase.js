
function productPrice() {
    var productName = document.getElementById("productName").value;
    var price = 0;

    switch (productName.toUpperCase()){
        case 'AREPAS':
            price = 1.500;
            break;
        case 'EMPANADAS':
            price = 2.400;
            break;
        case 'QUESITO':
            price = 4.500;
            break;
        default:
            alert("Nombre de producto invalido, ingresa AREPAS, EMPANADAS o QUESITO");
            break;
    }
    document.getElementById("price").innerHTML = price;

}