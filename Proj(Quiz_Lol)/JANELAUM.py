import PySimpleGUI as sg
#VARIAVEIS-----------------------------------------------------------------------------------------------
r1,r2,r3,r4,r5,r6=0,0,0,0,0,0
resultado=0
#JANELAUM-------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE JOGA EM UMA LANE SOLO?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='1'),sg.Button('NÃO',key='2')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '1':
        r1 = "SIM" 
        break
        
    else:
        r1 = "NÃO"
        break 
janela.close()    
#JANELAUM-------------------------------------------------------------------------------------------------

#JANELA---------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE JOGA COM PERSONAGENS ENCANTADORES?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='3'),sg.Button('NÃO',key='4')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '3':
        r2 = "SIM" 
        break
        
    else:
        r2 = "NÃO"
        break 
janela.close()  
#JANELA---------------------------------------------------------------------------------------------------

#JANELA---------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE DÁ COVER PARA O TIME?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='5'),sg.Button('NÃO',key='6')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '5':
        r3 = "SIM" 
        break
        
    else:
        r3 = "NÃO"
        break 
janela.close()  
#JANELA---------------------------------------------------------------------------------------------------
#JANELA---------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE CAUSA BASTANTE DANO?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='7'),sg.Button('NÃO',key='8')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '7':
        r4 = "SIM" 
        break
        
    else:
        r4 = "NÃO"
        break 
janela.close()  
#JANELA---------------------------------------------------------------------------------------------------

#JANELA---------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE ABSORVE BASTANTE DANO?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='9'),sg.Button('NÃO',key='10')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '9':
        r5 = "SIM" 
        break
        
    else:
        r5 = "NÃO"
        break 
janela.close()  
#JANELA---------------------------------------------------------------------------------------------------
#JANELA---------------------------------------------------------------------------------------------------
sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol2.png")],
          [sg.Text('                         VOCE DEPENDE DE ATAQUES BASICOS?',font='arial',size=(63,1))],
          [sg.Button('SIM',key='11'),sg.Button('NÃO',key='12')],
            ]
janela = sg.Window('primeira pergunta',layout,no_titlebar=True)

while True: 
    event, values =janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '11':
        r6 = "SIM" 
        break
        
    else:
        r6 = "NÃO"
        break 
janela.close()  
#JANELA---------------------------------------------------------------------------------------------------

# LOGICA DAS RESPOSTAS------------------------------------------------------------------------------------

if r1 == "SIM" and r2 == "SIM" and r4 == "SIM":
    resultado = "MIDLANER"
    print('MIDLANER')
elif r2 == "SIM" and r3 == "SIM":
    resultado='SUPORTE'
    print('SUPORTE')
elif r3 == "SIM" and r5 == "SIM":
    resultado ='JUNGLER'
    print('JUNGLER')
elif r1 == "SIM" and r5 == "SIM":
    resultado='TOPLANER'
    print('TOPLANER')
elif r4 == "SIM" and r6 == "SIM":
    resultado = 'ADC'
    print('ADC')
else:
    print('em manutenção')
#---------------------------------------------------------------------------------------------------------
#APLICAR RESULTADO FINAL COM A IMAGEM---------------------------------------------------------------------
sg.theme('Black')  
layout=[
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol3.png")],
          [sg.Text('                         A ROTA PERFEITA PARA VOCÊ É ',resultado)],
            ]
#------------------------------------------------------
window = sg.Window('WG', layout,no_titlebar=True)
#------------------------------------------------------
while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
#-------------------------------------------------------------------------------------------------------- 