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
