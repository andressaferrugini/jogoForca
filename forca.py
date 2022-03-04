import random
import numpy as np

tabuleiro = ['''
>>>>>>>>>>Jogo da forca<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    dica=[]
    encontrado=[]
    naoEncontrado=[]
    cont=0
    # Método Construtor
    def __init__(self, word):
        self.word = word
        print(tabuleiro[Hangman.cont])
        for letra in word:
            Hangman.dica.append('_')
        print('Palavra: ' + ''.join(Hangman.dica))
        self.defLetter()

    #Método para receber letra
    def defLetter(self):
        letra = input('Por favor informe uma letra: ')
        if letra not in Hangman.naoEncontrado and letra not in Hangman.encontrado:
            self.guess(letra)
        else:
            letra = input('Letra já consultada, por favor informe uma nova letra: ')
            self.guess(letra)

    # Método para adivinhar a letra
    def guess(self, letter):
        listaPos = []
        if(letter not in self.word):
            Hangman.naoEncontrado.append(letter)
            print('Letra %s não encontrada na palavra' %letter)
            print('Letras não encontradas: ' + ','.join(Hangman.naoEncontrado))
            Hangman.cont+=1
            print(tabuleiro[Hangman.cont])
            print('Palavra: ' + ''.join(Hangman.dica))
        else:
            for pos, char in enumerate(self.word):
                if (char == letter):
                    listaPos.append(pos)
            for item in listaPos:
                Hangman.dica[item]=letter
            Hangman.encontrado.append(letter)
            print('Letra %s encontrada na palavra' % letter)
            print('Letras não encontradas: ' + ','.join(Hangman.naoEncontrado))
            print(tabuleiro[Hangman.cont])
            print('Palavra: ' + ''.join(Hangman.dica))
        self.verificaFim()

    def verificaFim(self):
        if Hangman.cont == 6:
            print('Fim de jogo, você foi enforcado. A palavra era: ', self.word)
        elif '_' not in Hangman.dica:
            print('Parabéns, você venceu! A palavra era: ', self.word)
        else:
            self.defLetter()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())


# Executa o programa
if __name__ == "__main__":
    main()

