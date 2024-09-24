package projeto_kayo;

import java.util.List;
import java.util.Scanner;

public class main {
    
     public static void atualizarPessoa(List<Pessoa> listaPessoas, Scanner scanner) {
        System.out.print("Digite o nome da pessoa a ser atualizada: ");
        String nome = scanner.nextLine();
        Pessoa pessoaEncontrada = null;

        for (Pessoa pessoa : listaPessoas) {
            if (pessoa.getNome().equalsIgnoreCase(nome)) {
                pessoaEncontrada = pessoa;
                break;
            }
        }

        if (pessoaEncontrada != null) {
            try {
                System.out.print("Digite a nova idade: ");
                int novaIdade = Integer.parseInt(scanner.nextLine());

                if (pessoaEncontrada instanceof Funcionario) {
                    Funcionario funcionario = (Funcionario) pessoaEncontrada;
                    System.out.print("Digite o novo cargo: ");
                    String novoCargo = scanner.nextLine();
                    funcionario.setCargo(novoCargo);
                    funcionario.idade = novaIdade;
                    System.out.println("Funcionário atualizado com sucesso!");
                } else if (pessoaEncontrada instanceof Cliente) {
                    Cliente cliente = (Cliente) pessoaEncontrada;
                    System.out.print("Digite a nova preferência de produto: ");
                    String novaPreferencia = scanner.nextLine();
                    cliente.setPreferenciaProduto(novaPreferencia);
                    cliente.idade = novaIdade;
                    System.out.println("Cliente atualizado com sucesso!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Erro: idade inválida.");
            }
        } else {
            System.out.println("Pessoa não encontrada.");
        }
    }

    public static void removerPessoa(List<Pessoa> listaPessoas, Scanner scanner) {
        System.out.print("Digite o nome da pessoa a ser removida: ");
        String nome = scanner.nextLine();
        Pessoa pessoaRemover = null;

        for (Pessoa pessoa : listaPessoas) {
            if (pessoa.getNome().equalsIgnoreCase(nome)) {
                pessoaRemover = pessoa;
                break;
            }
        }

        if (pessoaRemover != null) {
            listaPessoas.remove(pessoaRemover);
            System.out.println("Pessoa removida com sucesso!");
        } else {
            System.out.println("Pessoa não encontrada.");
        }
    }
}
