# Desafio Target
Resolução das questões do desafio da Target Sistemas
<details><summary>Questão 2</summary>
<p>

#### Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
    
```csharp
    
using System;

public class Program {
    public static void Main(string[] args) {
        Console.WriteLine("Digite um número:");

        int numero = int.Parse(Console.ReadLine());

        int a = 0;

        int b = 1;

        while (b <= numero) {
            if (b == numero) {
                Console.WriteLine($"O número informado {numero} pertence a sequência de Fibonacci!");
                return;
            }

            int temp = a + b;

            a = b;
            b = temp;
        }

        Console.WriteLine($"O número informado {numero} não pertence à sequência de Fibonaci.");
    }
}
                          
```

</p>
</details>
