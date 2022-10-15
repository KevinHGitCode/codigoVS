// Este archivo contiene una serie de funciones de manipulación de strings

var string = "Hola mundo";

string.length; // Devuelve el número de caracteres que tiene el string

string.charAt(0); // Devuelve el caracter que se encuentra en la posición indicada

string.charCodeAt(0); // Devuelve el código ASCII del caracter que se encuentra en la posición indicada

string.indexOf("o"); // Devuelve la posición del caracter indicado en el string

string.lastIndexOf("o"); // Devuelve la posición del caracter indicado en el string, desde el final

string.substring(0, 3); // Devuelve una subcadena del string, desde la posición indicada hasta la posición indicada

string.substr(0, 3); // Devuelve una subcadena del string, desde la posición indicada hasta la posición indicada

string.slice(0, 3); // Devuelve una subcadena del string, desde la posición indicada hasta la posición indicada

string.replace("Hola", "Adios"); // Reemplaza una subcadena del string por otra

string.toUpperCase(); // Convierte el string a mayúsculas

string.toLowerCase(); // Convierte el string a minúsculas

string.trim(); // Elimina los espacios en blanco al inicio y al final del string

string.split(" "); // Divide el string en un array, separando cada palabra por el caracter indicado

string.concat(" ", "Hola", " ", "mundo"); // Concatena dos o más strings

string.includes("Hola"); // Devuelve true si el string contiene el string indicado

string.startsWith("Hola"); // Devuelve true si el string empieza con el string indicado

string.endsWith("Hola"); // Devuelve true si el string termina con el string indicado

string.repeat(3); // Devuelve un string repetido el número de veces indicado

string.match(/[a-z]/g); // Devuelve un array con todos los caracteres que coinciden con el patrón indicado

string.search(/[a-z]/g); // Devuelve la posición del primer caracter que coincida con el patrón indicado

string.replace(/[a-z]/g, "*"); // Reemplaza todos los caracteres que coincidan con el patrón indicado por el string indicado

