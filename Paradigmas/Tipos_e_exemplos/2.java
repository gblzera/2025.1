class Pessoa {
    String nome;
    public Pessoa(String nome) {
        this.nome = nome;
    }
    public void dizerOla() {
        System.out.println("Olá, meu nome é " + nome);
    }
}
public class Main {
    public static void main(String[] args) {
        Pessoa p = new Pessoa("Gabriel");
        p.dizerOla();
    }
}
