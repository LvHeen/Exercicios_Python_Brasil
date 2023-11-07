'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link.'''

arq = int(input('Qual o tamnho do arquivo em MB? '))
vel = float(input('Qual a valocidade da internet em Mbps: '))
tempo = arq / (vel/8)
print(f'Um arquivo de {arq}MB em uma conexão de {vel}Mbps levará {tempo} segundos para ser baixado.')
