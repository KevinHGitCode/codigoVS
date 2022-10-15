public class clsProducto {
    // atributos: nombre, precio, cantidad, marca, fecha de caducidad
    private String nombre;
    private double precio;
    private int cantidad;
    private String marca;
    private String fechaCaducidad;

    public static void main(String[] args) {
        // write your code here
        
        clsProducto producto1 = new clsProducto("Leche", 1.5, 10, "Lacteo", "01/01/2020");

        // producto2
        clsProducto producto2 = new clsProducto("Huevos", 1.5, 10, "Lacteo", "01/01/2020");

        // producto3
        clsProducto producto3 = new clsProducto("Pan", 1.5, 10, "Lacteo", "01/01/2020");

        // producto4
        clsProducto producto4 = new clsProducto("Queso", 1.5, 10, "Lacteo", "01/01/2020");

        // mostrar datos xml
        producto1.mostrarDatos();
        producto2.mostrarDatosCSV();
        producto3.mostrarDatosXML();
        producto4.mostrarDatosJSON();

    }

    // constructor por defecto
    public clsProducto(String nombre, double precio, int cantidad, String marca, String fechaCaducidad) {
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
        this.marca = marca;
        this.fechaCaducidad = fechaCaducidad;
    }

    // getters y setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public int getCantidad() {
        return cantidad;
    }  

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getFechaCaducidad() {
        return fechaCaducidad;
    }

    public void setFechaCaducidad(String fechaCaducidad) {
        this.fechaCaducidad = fechaCaducidad;
    }


    // funcion mostrar datos
    public void mostrarDatos() {
        // linea de separacion
        System.out.println("----------------------------------------------------");
        System.out.println("Nombre: " + nombre);
        System.out.println("Precio: " + precio);
        System.out.println("Cantidad: " + cantidad);
        System.out.println("Marca: " + marca);
        System.out.println("Fecha de caducidad: " + fechaCaducidad);
        System.out.println("----------------------------------------------------");
    }

    // funcion mostrar datos en formato CSV
    public void mostrarDatosCSV() {
        // linea de separacion
        System.out.println("----------------------------------------------------");
        System.out.println("Nombre: " + nombre + "," + precio + "," + cantidad + "," + marca + "," + fechaCaducidad);
        System.out.println("----------------------------------------------------");
    }

    // funcion mostrar datos en formato XML
    public void mostrarDatosXML() {
        // linea de separacion
        System.out.println("----------------------------------------------------");
        System.out.println("<producto>");
        System.out.println("<nombre>" + nombre + "</nombre>");
        System.out.println("<precio>" + precio + "</precio>");
        System.out.println("<cantidad>" + cantidad + "</cantidad>");
        System.out.println("<marca>" + marca + "</marca>");
        System.out.println("<fechaCaducidad>" + fechaCaducidad + "</fechaCaducidad>");
        System.out.println("</producto>");
        System.out.println("----------------------------------------------------");
    }

    // funcion mostrar datos en formato JSON
    public void mostrarDatosJSON() {
        // linea de separacion
        System.out.println("----------------------------------------------------");
        System.out.println("{");
        System.out.println("\"nombre\":\"" + nombre + "\",");
        System.out.println("\"precio\":" + precio + ",");
        System.out.println("\"cantidad\":" + cantidad + ",");
        System.out.println("\"marca\":\"" + marca + "\",");
        System.out.println("\"fechaCaducidad\":\"" + fechaCaducidad + "\"");
        System.out.println("}");
        System.out.println("----------------------------------------------------");
    }

}