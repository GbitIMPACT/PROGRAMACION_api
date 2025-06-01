

const fs = require('fs');

console.log("Inicio de la lectura del archivo");

fs.readFile('archivo.txt', 'utf8', (err, data) => {
  if (err) throw err; 
  console.log("Contenido del archivo: " + data);

});

console.log("Fin de la lectura del archivo");