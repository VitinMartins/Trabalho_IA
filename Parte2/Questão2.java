public class Questão2 {
    
        public static double calcularTemperaturaInicial(int custoMaximo, int custoMinimo) {
            return custoMaximo - custoMinimo;
        }
    
        public static void main(String[] args) {
            int custoMaximo = 28;
            int custoMinimo = 0;
    
            double temperaturaInicial = calcularTemperaturaInicial(custoMaximo, custoMinimo);
    
            System.out.println("Temperatura Inicial: " + temperaturaInicial);
        }
    
    
}
