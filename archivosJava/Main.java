import java.util.Scanner;

public class Main {
    public static Scanner sc = new Scanner(System.in);

    // metodo para pedir los datos del vector
    public static clsVector pedirDatos(){
        System.out.println("Ingrese el modulo: ");
        double modulo = sc.nextDouble();
        System.out.println("Ingrese la angulo: ");
        double angulo = sc.nextDouble();
        // asignar los datos
        clsVector v1 = new clsVector(modulo, angulo);
        return v1;
    }


    public static void main(String args[]){
        clsVector v1 = pedirDatos();
        
        v1.mostrar();
        
    }

}
