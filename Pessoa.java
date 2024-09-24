package projeto_kayo;

public abstract class Pessoa {
    protected String nome;  // protected para acesso pelas subclasses
    int idade;  // acesso default (padrão)
    private TipoDocumento tipoDocumento;
    private static int contadorPessoas = 0;  // Elemento static

    public enum TipoDocumento {
        CPF, RG, CNH
    }

    public Pessoa(String nome, int idade, TipoDocumento tipoDocumento) throws IdadeInvalida {
        if (idade < 0) {
            throw new IdadeInvalida("A idade fornecida (" + idade + ") não é válida. Deve ser maior que zero.");
        }
        this.nome = nome;
        this.idade = idade;
        this.tipoDocumento = tipoDocumento;
        contadorPessoas++;  // Incrementa o contador sempre que uma nova pessoa for criada
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public TipoDocumento getTipoDocumento() {
        return tipoDocumento;
    }

    public static int getContadorPessoas() {  // Método estático
        return contadorPessoas;
    }

    public abstract void exibirInformacoes();  // Método abstrato

    public abstract String getTipoPessoa();
}
