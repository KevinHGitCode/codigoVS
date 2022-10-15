import java.util.Scanner;

//crear clase
public class operacionesMatrices {
    //crear metodo principal
    public static void main(String[] args) {
        //declarar variables
        int matrizA[][] = new int[3][3];
        int matrizB[][] = new int[3][3];
        int matrizC[][] = new int[3][2];

        //llamar metodo para llenar matrices
        System.out.println("Matriz C");
        llenarMatriz(matrizA);
        System.out.println("Matriz E");
        llenarMatriz(matrizB);
        System.out.println("Matriz B");
        llenarMatriz(matrizC);
        
        //int[][] matrizD = ;
        System.out.println("(C + E)B:");
        mostrarMatriz(multiplicarMatrices(sumarMatrices(matrizA, matrizB), matrizC));
        
     
    }

    //crear metodo para llenar la matriz
    public static void llenarMatriz(int matriz[][]) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                matriz[i][j] = sc.nextInt();
            }
        }

    }

    //crear metodo para mostrar la matriz
    public static void mostrarMatriz(int matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print("[" + matriz[i][j] + "]");
            }
            System.out.println();
        }
    }

    //crear metodo para sumar matrices
    public static int[][] sumarMatrices(int matrizA[][], int matrizB[][]) {
        if(matrizA.length == matrizB.length && matrizA[0].length == matrizB[0].length){
            int matrizC[][] = new int[matrizA.length][matrizA[0].length];
            for (int i = 0; i < matrizA.length; i++) {
                for (int j = 0; j < matrizA[0].length; j++) {
                    matrizC[i][j] = matrizA[i][j] + matrizB[i][j];
                }
            }
            return matrizC;
    }
    else{
        System.out.println("No se pueden sumar las matrices");
        return null;
    }
    }

    //crear metodo para restar matrices
    public static int[][] restarMatrices(int matrizA[][], int matrizB[][]) {
        if (matrizA.length == matrizB.length) {
            int matrizC[][] = new int[matrizA.length][matrizA.length];
            for (int i = 0; i < matrizA.length; i++) {
                for (int j = 0; j < matrizA[0].length; j++) {
                    matrizC[i][j] = matrizA[i][j] - matrizB[i][j];
                }
            }
            return matrizC;
        } else {
            System.out.println("No se pueden restar las matrices");
            return null;
        }
    }

    //crear metodo para multiplicar matrices
    public static int[][] multiplicarMatrices(int matrizA[][], int matrizB[][]) {
        if (matrizA[0].length == matrizB.length) {
            int matrizC[][] = new int[matrizA.length][matrizB[0].length];
            for (int i = 0; i < matrizA.length; i++) {
                for (int j = 0; j < matrizB[0].length; j++) {
                    for (int k = 0; k < matrizA[0].length; k++) {
                        matrizC[i][j] += matrizA[i][k] * matrizB[k][j];
                    }
                }
            }
            return matrizC;
        } else {
            System.out.println("No se pueden multiplicar las matrices");
            return null;
        }
            
    }


}