mensagens_codificadas = [
    "O8L0A3!G0A3L1E9R6A8,V5A1M7O0S1D8E4B8O5C9H2A0R3L0E7G2A8L9.",
    "P4O7P6C0O7R7N3A0N2D3E1I4C7E9C6L9E1A5N1.", #Crie uma lista contendo pelo menos 3 mensagens codicadas. As mensagens
    "T6H2E1T8A9R2D2E8I5N4B1R6A3Z2I5L4." #devem conter letras maiúsculas, minúsculas, números e símbolos.
]

def decifrar(mensagem_codificada):
    mensagem_decifrada = "" #Crie uma nova string vazia para armazenar a mensagem decifrada.
    for caractere in mensagem_codificada: #Utilize um loop for para iterar sobre cada mensagem da lista.
        if caractere.isalpha(): #Utilize outro loop for (aninhado) para iterar sobre cada caractere da mensagem codicada.
            mensagem_decifrada += caractere.lower() #Se o caractere for uma letra minúscula, adicione-o à mensagemdecifrada.
    return mensagem_decifrada #Ignore números e símbolos

print("Mensagens Codificadas:")
for codificada in mensagens_codificadas: #Imprima a mensagem codicada original e a mensagem decifrada
    print(codificada)

print("\nMensagens Decifradas:")
for codificada in mensagens_codificadas:
    decifrada = decifrar(codificada)
    print(decifrada)
