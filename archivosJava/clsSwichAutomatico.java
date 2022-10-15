public class clsSwichAutomatico {
    //main
    public static void main(String[] args) {
        //variables
        int opciones;
        //code
        boolean continuar = true;
        while (continuar){
            System.out.println("Ingrese el nuemro de opciones que desea en su swich: ");
            opciones = Integer.parseInt(System.console().readLine());

            //llamar al metodo generarUnMenuConNOpciones
            generarUnMenuConNOpciones(opciones);

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

    //metodo para generar un menu con N opciones
    public static void generarUnMenuConNOpciones(int opciones){
        //code
        // si opciones es menor a 1, se muestra un mensaje de error
        if (opciones < 1){
            System.out.println("Error, el numero de opciones es menor a 1");
        } else {
            // si opciones es mayor a 1, se muestra un menu con N opciones
            if (opciones > 1){
                // se muestra el menu con N opciones
                System.out.println("// swich con " + opciones + " opciones\nswitch (opcion){");
                for (int i = 1; i <= opciones-1; i++){
                    System.out.println("\tcase " + i + ":\n\t    System.out.println(" + "\"Opcion " + i + "\");\n\t    break;");
                }
                System.out.println("\tdefault:\n\t    System.out.println(" + "\"Opcion no valida\"" + ");\n\t    break;");
                System.out.println("}");
            }
        }
    }
}