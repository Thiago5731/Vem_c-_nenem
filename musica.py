import pygame
import time 
import sys
import os

#função para o tempo
def segundos(tempo):
    time.sleep(tempo)


#função para carregar as letras da musica
def letras(parte, intervalo):
    mensagem = parte
    for letra in mensagem:
        print(letra, end="", flush=True)
        time.sleep(intervalo)  
    print()


#inicio do py game para rodar o player de musica 
pygame.init()
pygame.mixer.music.load('Nenem_do_pai.mp3')
pygame.mixer.music.play()

#limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*30)
print ('🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺')
print('-'*30)

#letra da musica
segundos(22)
letras('Vem cá neném,', 0.1)

segundos(1) #24
letras('pros braços do papai', 0.09)

segundos(0.9) #27
letras('Papai te dá colinho,', 0.09)

segundos(0.3) #29
letras('da beijinho e muito mais', 0.09)

segundos(0.3) #31
letras('Vem vem vem, ', 0.09)

segundos(0.2) #33
letras('vem vem neném', 0.09)

segundos(0.1) #33
letras('🎺', 0.05)

segundos(0.9) #35
letras('Seu pai te ama', 0.09)

segundos(0.3) #37
letras('Vou da tapa no bumbum', 0.09)

segundos(0.5) #39
letras('Neném dorme eu levo pra cama', 0.09)

segundos(1) #39
letras('...', 0.2)

input()
pygame.event.wait()


#para matar a musica #ainda não ta funcionando :(
segundos(22)
pygame.mixer.music.stop()
