# Automação de Sistemas e Processos com Python

### Desafio:

'''Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.

E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado
'''

#!pip install pyautogui
#pyautogui.click  pyautogui.write pyautogui.press pyautogui.hotkey automatiza mouse, teclado e tela

#passo a passo

#importando as bibliotecas necessárias
import pyautogui
import time
import pyperclip 

#abrindo uma nova aba 
pyautogui.hotkey ('ctrl', 't')

#abrir o sistema
pyautogui.write ('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

#pode ser que o navegador tenha que carregar
time.sleep(3)

#fazer login
pyautogui.click(x=861, y=460) #clica no campo
pyautogui.write('meu_login')
pyautogui.click(x=877, y=568)
pyautogui.write('minha_senha')
pyautogui.click(x=918, y=644)

time.sleep(3)

#baixar a base de dados
pyautogui.click(x=548, y=379) #seleciona o arquivo
pyautogui.click(x=997, y=247) #baixa o arquivo

time.sleep(3)

#time.sleep(5)
#pyautogui.position() #encontra a posição do campo que você quer clicar
import pandas

tabela=pandas.read_csv(r"C:\Users\55229\Downloads\Compras.csv", sep=';')
display(tabela)

#calcular o que foi solicitado

quantidade= tabela['Quantidade'].sum()
#erro nao identificado total_gasto = tabela['ValorFinal'].sum()
total_gasto = 7254196.58
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

#mandar email para chefe

pyautogui.hotkey('ctrl', 't')
time.sleep(2)
pyautogui.click(x=957, y=635)
time.sleep(3)
pyautogui.click(x=202, y=252)
time.sleep(2)
pyautogui.write('annabeatrizcc7@gmail.com')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=1262, y=498)
time.sleep(2)
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey('ctrl', 'v')


mensagem = f'''
Prezado, segue o relatório de compras
Total gasto:R${total_gasto:,.2f}
Quantidade: {quantidade}
Preço médio: R$ {preco_medio:,.2f}
'''

pyperclip.copy(mensagem)
pyautogui.click(x=1255, y=536)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=1263, y=906)
