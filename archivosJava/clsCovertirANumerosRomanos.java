
// class
public class clsCovertirANumerosRomanos {
    // method
    public static void main(String[] args) {
        // variables
        int numero;
        String romano;
        // code
        boolean continuar = true;
        while (continuar){
            System.out.println("Ingrese un numero entero: ");
            numero = Integer.parseInt(System.console().readLine());
            romano = convertirANumerosRomanos(numero);
            if (romano.equals("Error")){
                System.out.println("Error, el numero ingresado no es valido");
            } else {
                System.out.println("El numero romano es: " + romano);
            }
            //linea de separacion
            System.out.println("-----------------------------------------------------");
            System.out.println("Desea continuar? (s/n)");
            String respuesta = System.console().readLine();
            //String respuesta = "s";
            if (respuesta.equals("s")){
                continuar = true;
            } else {
                continuar = false;
            }
        }
    }
    // method
    public static String convertirANumerosRomanos(int numero) {
        // variables
        String romano = "";
        // code
        // numero menor a 3999 para convertir a romanos
        // si el numero es mayor a 3999, se muestra un mensaje de error
        if (numero > 3999){
            System.out.println("El numero ingresado es mayor a 3999");
            return "Error";
        } else {
            // numero menor a 3999
            // si el numero es menor a 1000, se convierte a romanos
            if (numero < 1){
                    System.out.println("El numero ingresado es menor a 1");
                    return "Error";
            }else{
            while (numero > 0) {
                if (numero >= 1000) {
                    romano = romano + "M";
                    numero = numero - 1000;
                } else if (numero >= 900) {
                    romano = romano + "CM";
                    numero = numero - 900;
                } else if (numero >= 500) {
                    romano = romano + "D";
                    numero = numero - 500;
                } else if (numero >= 400) {
                    romano = romano + "CD";
                    numero = numero - 400;
                } else if (numero >= 100) {
                    romano = romano + "C";
                    numero = numero - 100;
                } else if (numero >= 90) {
                    romano = romano + "XC";
                    numero = numero - 90;
                } else if (numero >= 50) {
                    romano = romano + "L";
                    numero = numero - 50;
                } else if (numero >= 40) {
                    romano = romano + "XL";
                    numero = numero - 40;
                } else if (numero >= 10) {
                    romano = romano + "X";
                    numero = numero - 10;
                } else if (numero >= 9) {
                    romano = romano + "IX";
                    numero = numero - 9;
                } else if (numero >= 5) {
                    romano = romano + "V";
                    numero = numero - 5;
                } else if (numero >= 4) {
                    romano = romano + "IV";
                    numero = numero - 4;
                } else if (numero >= 1) {
                    romano = romano + "I";
                    numero = numero - 1;
                }
            }
            return romano;
        }
    }
}
}

