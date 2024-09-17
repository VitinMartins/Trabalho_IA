import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class Questão6 {

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

    public static int[] resolverComTemperaturaSimulada(int n, double temperaturaInicial, double taxaResfriamento, int maxIteracoes) {
        int[] solucaoAtual = new int[n];
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            solucaoAtual[i] = rand.nextInt(n);
        }
        int custoAtual = calcularCusto(solucaoAtual);

        int[] melhorSolucao = solucaoAtual.clone();
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

            temperatura *= taxaResfriamento;
        }

        return melhorCusto == 0 ? melhorSolucao : null;
    }

    public static void main(String[] args) {
        int n = 8;
        double temperaturaInicial = 28.0;
        double taxaResfriamento = 0.99;
        int maxIteracoes = 10000;
        Set<String> solucoesEncontradas = new HashSet<>();
        
        long inicio = System.currentTimeMillis();

        while (solucoesEncontradas.size() < 92) {
            int[] solucao = resolverComTemperaturaSimulada(n, temperaturaInicial, taxaResfriamento, maxIteracoes);
            if (solucao != null) {
                String solucaoString = java.util.Arrays.toString(solucao);
                solucoesEncontradas.add(solucaoString);
            }
        }

        long fim = System.currentTimeMillis();
        
        System.out.println("Solucoes distintas encontradas: " + solucoesEncontradas.size());
        System.out.println("Tempo total: " + (fim - inicio) / 1000.0 + " segundos");
        
        for (String solucao : solucoesEncontradas) {
            System.out.println("Solução: " + solucao);
    }
}
}
