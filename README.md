# Atividades Práticas de Python do Curso de Ciências da Computação. 
Professora: Kadidja Valeria.

Integrantes do projeto
- **Suelen Marinho:** RGM: 31923160
- **Lelton Borges:** RGM: 27933091

# Atividade 1: Decifrando Mensagens Estelares com for

Cenário: Você é um(a) criptoanalista espacial e interceptou uma série de mensagens codificadas de diferentes planetas. Cada mensagem é uma string, e você precisa decifrá-las para entender as intenções dos alienígenas.

Tarefa:
- 1. Crie uma lista contendo pelo menos 3 mensagens codificadas. As mensagens devem conter letras maiúsculas, minúsculas, números e símbolos.
- 2. Utilize um loop for para iterar sobre cada mensagem da lista.
- 3. Dentro do loop, para cada mensagem:
     
**Crie uma nova string vazia para armazenar a mensagem decifrada.**

**Utilize outro loop for (aninhado) para iterar sobre cada caractere da mensagem codificada.**

**Dentro do loop aninhado, aplique as seguintes regras de decodificação:**
- Se o caractere for uma letra minúscula, adicione-o à mensagem decifrada.
- Se o caractere for uma letra maiúscula, converta-o para minúsculo e adicione-o à mensagem decifrada. 
- Ignore números e símbolos.
- Imprima a mensagem codicada original e a mensagem decifrada.

# Atividade 2: Navegação Segura em um Campo de Asteroides com while

Cenário: Você é um(a) piloto espacial e precisa navegar sua nave por um campo de asteroides perigoso. Você tem um sensor que detecta a distância do asteroide mais próximo.

Tarefa:
- 1. Dena uma distância inicial segura (um número inteiro positivo).
- 2. Utilize um loop while para simular a navegação. O loop deve continuar enquanto a
distância do asteroide mais próximo for menor que a distância segura.
- 3. Dentro do loop:
     
**Gere uma distância aleatória para o asteroide mais próximo (um número
inteiro entre 1 e 10).**

**Imprima a distância do asteroide.**

- Se a distância for menor que 3, imprima uma mensagem de "PERIGO!" e
encerre o loop usando break.
- Se a distância for menor que a metade da distância segura, imprima um aviso
de "Aproximando-se de asteroide!".
- Aumente a distância segura em um valor xo (por exemplo, 2) para simular o
piloto se afastando dos asteroides.
- 4. Se o loop terminar sem ser interrompido por break, imprima uma mensagem de
"Navegação concluída com segurança!".

# Atividade 3: Batalha Espacial Intergaláctica com for e while

Cenário: Você está no comando de uma nave espacial em uma batalha intergaláctica.
Você tem um número limitado de mísseis e precisa usá-los estrategicamente para
destruir naves inimigas.

Tarefa:
- 1. Dena o número inicial de mísseis (um número inteiro positivo).
- 2. Crie uma lista com os nomes de pelo menos 3 naves inimigas.
- 3. Utilize um loop while para simular a batalha. O loop deve continuar enquanto você
tiver mísseis E houver naves inimigas na lista.

**4. Dentro do loop:**
     
- Imprima o número de mísseis restantes e a lista de naves inimigas.
- Solicite ao usuário que escolha qual nave inimiga atacar (usando o índice da
lista).
- Implemente tratamento de erros para garantir que o usuário digite um índice
válido.
- Se o usuário digitar um índice inválido, exiba uma mensagem de erro e
continue para a próxima iteração do loop usando continue.
- Se o usuário digitar um índice válido:
- Remova a nave inimiga da lista.
- Diminua o número de mísseis em 1.
- Imprima uma mensagem informando qual nave foi destruída.
- Se o número de mísseis chegar a zero, imprima uma mensagem de "Sem
mísseis! Retirada estratégica!".
- Se todas as naves inimigas forem destruídas, imprima uma mensagem de
"Vitória! Todas as naves inimigas foram destruídas!".



