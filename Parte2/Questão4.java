import java.util.Random;
public class Questão4 {


    public static int[] gerarPerturbacao(int[] solucao) {
        int[] perturbada = solucao.clone();
        Random rand = new Random();

        int coluna1 = rand.nextInt(solucao.length);
        int coluna2 = rand.nextInt(solucao.length);

        int temp = perturbada[coluna1];
        perturbada[coluna1] = perturbada[coluna2];
        perturbada[coluna2] = temp;

        return perturbada;
    }

    public static void main(String[] args) {
        int n = 8;
        int[] solucaoAtual = {0, 4, 7, 5, 2, 6, 1, 3}; 
        int[] solucaoPerturbada = gerarPerturbacao(solucaoAtual);

        System.out.println("Solução Original:");
        for (int i = 0; i < n; i++) {
            System.out.println("Coluna " + i + ": Linha " + solucaoAtual[i]);
        }

        System.out.println("Solução Perturbada:");
        for (int i = 0; i < n; i++) {
            System.out.println("Coluna " + i + ": Linha " + solucaoPerturbada[i]);
}
}
}
