"""
 Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"
"""
cid = str(input('Em que cidade você nasceu? ')).strip()  # strip elimina os espaços
print(cid[:5].upper() == 'SANTO')
