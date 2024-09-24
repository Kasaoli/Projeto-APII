package projeto_kayo;

public class Cliente extends Pessoa {
    private String preferenciaProduto;

   
    public Cliente(String nome, int idade, TipoDocumento tipoDocumento, String preferenciaProduto) throws IdadeInvalida {
        super(nome, idade, tipoDocumento);
        this.preferenciaProduto = preferenciaProduto;
    }

   
    public Cliente(String nome, int idade, TipoDocumento tipoDocumento) throws IdadeInvalida {
        this(nome, idade, tipoDocumento, "Indefinido");
    }

    public void setPreferenciaProduto(String preferenciaProduto) {
        this.preferenciaProduto = preferenciaProduto;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Nome: " + getNome());
        System.out.println("Idade: " + getIdade());
        System.out.println("Preferência de Produto: " + preferenciaProduto);
        System.out.println("Tipo de Documento: " + getTipoDocumento());
    }

    @Override
    public String getTipoPessoa() {
        return "Cliente";
    }
}
