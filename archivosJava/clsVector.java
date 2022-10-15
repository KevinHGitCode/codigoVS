import java.util.Scanner;

// crear la clase vector
public class clsVector{
    
    // atributos de la clase (modulo, direccion, sentido, angulo)
    public static Scanner sc = new Scanner(System.in);
    private double modulo;
    private double angulo;
    private double[] XY = new double[2];
    // constructor
    public clsVector(double modulo, double angulo){
        this.modulo = modulo;
        this.angulo = angulo;
        this.XY = getXY();
    }

    //metodos de la clase
    public double getModulo(){
        return this.modulo;
    }
    public double getAngulo(){
        return this.angulo;
    }
    public void setModulo(double modulo){
        this.modulo = modulo;
    }
    public void setAngulo(double angulo){
        this.angulo = angulo;
    }

    // metodo para calcular la suma de dos vectores
    public clsVector suma(clsVector v){
        double modulo = this.modulo + v.getModulo();
        double angulo = this.angulo + v.getAngulo();
        // retorno del vector
        return new clsVector(modulo, angulo);
    }

    // metodo para calcular la resta de dos vectores
    public clsVector resta(clsVector v){
        double modulo = this.modulo - v.getModulo();
        double angulo = this.angulo - v.getAngulo();
        // retorno del vector
        return new clsVector(modulo, angulo);
    }

    // metodo para mostrar el vector
    public void mostrar(){
        System.out.println("Modulo: " + this.modulo);
        System.out.println("Angulo: " + this.angulo);
        System.out.println("X: " + this.XY[0]);
        System.out.println("Y: " + this.XY[1]);
    }

    // metodo para encontrar la 'x' y la 'y' del vector
    public double[] getXY(){
        double x = this.modulo * Math.cos(gradosRadianes(this.angulo));
        double y = this.modulo * Math.sin(gradosRadianes(this.angulo));
        return new double[]{x, y};
    }
    //funcion grados a radianes
    public static double gradosRadianes(double grados){
        return grados * Math.PI / 180;
    }





    // funciones seno coseno tangente
    public static double seno(double angulo){
        return Math.sin(angulo);
    }
    public static double coseno(double angulo){
        return Math.cos(angulo);
    }
    public static double tangente(double angulo){
        return Math.tan(angulo);
    }
}