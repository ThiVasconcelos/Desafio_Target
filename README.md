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
<details><summary>Questão 3</summary>
<p>

#### Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


```python
   import json

class Faturamento:

    def __init__(self, file_path):
        with open(file_path , 'r') as file:
            self.data = json.load(file)
        self.menor_faturamento = float('inf')
        self.maior_faturamento = 0
        self.media_faturamento = 0
        self.dias_acima_da_media = 0
        self.calcular_faturamento()

    def calcular_faturamento(self):
        soma_total_faturamento = 0
        dias_com_faturamento = 0
        for dia in self.data:
            if dia['valor'] > 0:
                soma_total_faturamento += dia['valor']
                dias_com_faturamento += 1
                if dia['valor'] < self.menor_faturamento:
                    self.menor_faturamento = dia['valor']
                if dia['valor'] > self.maior_faturamento:
                    self.maior_faturamento = dia['valor']
        self.media_faturamento = soma_total_faturamento / dias_com_faturamento
        self.dias_acima_da_media = len([dia for dia in self.data if dia['valor'] > self.media_faturamento])

    def mostrar_calculos(self):
        print('Menor faturamento: R$', self.menor_faturamento)
        print('Maior faturamento: R$', self.maior_faturamento)
        print('Número de dias com faturamento acima da média mensal:', self.dias_acima_da_media)


faturamento = Faturamento('scr\data\dados1.json')
faturamento.mostrar_calculos()



```

</p>
</details>



<details><summary>Questão 4</summary>
<p>

#### Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


```python
   import pandas as pd

Faturamento_Mensal =  {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

Total_Faturamento_Mensal = sum(Faturamento_Mensal.values())
df_percentual_mensal = pd.DataFrame.from_dict(Faturamento_Mensal, orient='index', columns=['Faturamento Mensal'])
df_percentual_mensal.index.name = 'Estado'
df_percentual_mensal.reset_index(inplace=True)
df_percentual_mensal['Percentual Mensal'] = df_percentual_mensal['Faturamento Mensal'] / Total_Faturamento_Mensal * 100

print(df_percentual_mensal)


```

</p>
</details>

<details><summary>Questão 5</summary>
<p>

#### Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;



```python
   string_normal = input("Digite um texto para ser invertido: ") 


conjunto_caracteres = list(string_normal)

i = 0
j = len(conjunto_caracteres) - 1

while i < j:
    conjunto_caracteres[i], conjunto_caracteres[j] = conjunto_caracteres[j], conjunto_caracteres[i]
    i += 1
    j -= 1


string_invertida = ''.join(conjunto_caracteres)

print("O texto invertida é:", string_invertida)

```

</p>
</details>

