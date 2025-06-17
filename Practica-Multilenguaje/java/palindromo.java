public class palindromo {
    public static boolean esPalindromo(String cadena) {
        cadena = cadena.replaceAll("\\s+", "").toLowerCase();
        StringBuilder invertida = new StringBuilder(cadena).reverse();
        return cadena.equals(invertida.toString());
    }

    public static void main(String[] args) {
        String ejemplo = "Anita lava la tina";
        System.out.println("\"" + ejemplo + "\" ¿es palíndromo? " + esPalindromo(ejemplo));
    }
}
