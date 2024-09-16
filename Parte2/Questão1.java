public class Questão1 {

    public static double funcaoAptidao(int[] solucao) {
        int paresAtacantes = contarParesAtacantes(solucao);
        return 28 - paresAtacantes; 
    }

    public static int contarParesAtacantes(int[] solucao) {
        int count = 0;
        int tamanho = solucao.length;

        for (int i = 0; i < tamanho; i++) {
            for (int j = i + 1; j < tamanho; j++) {
                if (estaoAtacando(solucao[i], solucao[j], i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    private static boolean estaoAtacando(int linha1, int linha2, int coluna1, int coluna2) {
        return linha1 == linha2 || 
               coluna1 == coluna2 || 
               Math.abs(linha1 - linha2) == Math.abs(coluna1 - coluna2);
    }

    public static void main(String[] args) {
        int[] solucao = {0, 4, 7, 5, 2, 6, 1, 3};
        double aptidao = funcaoAptidao(solucao);
        System.out.println("Aptidão da solução: " + aptidao);
    } 
}
