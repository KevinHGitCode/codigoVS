//import
import java.util.ArrayList;
import java.util.List;

//create class
public class ArrayList_java {
    //create main method
    /**
     * @param args
     */
    public static void main(String[] args) {
        //create arraylist
        List<String> list = new ArrayList<String>();
        //fill arraylist
        list.add("Hello");
        list.add("World");
        list.add("!");
        //show arraylist
        System.out.println(list);

        //create arraylist
        ArrayList<String> list2 = new ArrayList<>();
        //fill arraylist
        list2.add("Hello");
        list2.add("World");
        list2.add("!");
        //show arraylist
        System.out.println(list2);


        System.out.println( list.size());

        System.out.println(list2.isEmpty());

        //  become int in string

        String va= convertirNumeroEString(100);
        System.out.println(va);
        System.out.println(va.getClass());

        

    }

    public static String convertirNumeroEString(int numero){
        String numeroString = String.valueOf(numero);
        return numeroString;
    }
}
