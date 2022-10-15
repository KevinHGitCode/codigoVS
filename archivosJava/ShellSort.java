import java.util.Arrays;

public class ShellSort {
    

    public static void main(String[] args) {
        // array desordenado de 10 elementos
        int[] array = { 5, 3, 1, 2, 4, 6, 8, 7, 9, 0 };
        System.out.println("Array desordenado: " + Arrays.toString(array));

        // llamada al método de ordenamiento
        shellSort(array);

        // impresión del array ordenado
        System.out.println("Array ordenado: " + Arrays.toString(array));
    }


    // Metodo shell sort 
    public static void shellSort(int[] array) {
        int longitud = array.length; // Longitud del array
        int separacion = longitud / 2; // Separacion inicial
        
        while (separacion > 0) { // Mientras la separacion sea mayor a 0

            for (int i = separacion; i < longitud; i++) { // Recorremos el array
                
                int temporal = array[i]; // Elemento a temporal
                int j; // Indice

                for (j = i; j >= separacion && array[j - separacion] > temporal; j -= separacion) { 
                    array[j] = array[j - separacion]; // Intercambiamos los elementos
                }
                array[j] = temporal; // Asignamos el elemento temporal

            }
            separacion /= 2; // Reducimos la separacion

        }

    }



}
