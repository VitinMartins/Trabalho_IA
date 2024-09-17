package Questão3;
import java.util.Random;

public class Questão3_RaizQuadrada {


    public static int calcularCusto(int[] solucao) {
        int custo = 0;
        int n = solucao.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (solucao[i] == solucao[j] || Math.abs(solucao[i] - solucao[j]) == Math.abs(i - j)) {
                    custo++;
                }
            }
        }
        return custo;
    }

    public static int[] gerarVizinho(int[] solucao) {
        int[] vizinho = solucao.clone();
        Random rand = new Random();
        int i = rand.nextInt(solucao.length);
        int novaLinha = rand.nextInt(solucao.length);
        vizinho[i] = novaLinha;
        return vizinho;
    }

    public static void main(String[] args) {
        int n = 8;
        int maxIteracoes = 10000;
        double temperaturaInicial = 28.0;
        double taxaResfriamento = 0.1;

        Random rand = new Random();
        int[] solucaoAtual = new int[n];
        for (int i = 0; i < n; i++) {
            solucaoAtual[i] = rand.nextInt(n);
        }

        int[] melhorSolucao = solucaoAtual.clone();
        int custoAtual = calcularCusto(solucaoAtual);
        int melhorCusto = custoAtual;

        double temperatura = temperaturaInicial;

        for (int iteracao = 0; iteracao < maxIteracoes; iteracao++) {
            if (custoAtual == 0) {
                break;
            }

            int[] novaSolucao = gerarVizinho(solucaoAtual);
            int custoNovo = calcularCusto(novaSolucao);
            int deltaCusto = custoNovo - custoAtual;

            if (deltaCusto < 0 || Math.exp(-deltaCusto / temperatura) > rand.nextDouble()) {
                solucaoAtual = novaSolucao;
                custoAtual = custoNovo;
                if (custoAtual < melhorCusto) {
                    melhorCusto = custoAtual;
                    melhorSolucao = solucaoAtual.clone();
                }
            }

            temperatura = temperatura / (1 + taxaResfriamento * Math.sqrt(temperatura));
        }

        System.out.println("Melhor solução encontrada:");
        for (int i = 0; i < n; i++) {
            System.out.println("Coluna " + i + ": Linha " + melhorSolucao[i]);
        }
        System.out.println("Custo: " + melhorCusto);
}
}