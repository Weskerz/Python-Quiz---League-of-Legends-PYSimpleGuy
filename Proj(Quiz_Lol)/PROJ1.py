import PySimpleGUI as sg

sg.theme('Black')  
layout = [
          [sg.Image(r"C:\Users\Usuario\Documents\Python\PROJ_LOL\lol1.png")],
          [sg.Button('Vamos lá!',font='arial',size=(63,1),button_color='Gold',key='play')],
          [sg.Button('Sair',font='arial',size=(63,1),button_color='Gold')],
          ]
#------------------------------------------------------
window = sg.Window('WG', layout)
#------------------------------------------------------
while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'play':
        sg.execute_py_file(pyfile='PROJ_LOL/JANELAUM.py',wait=True)

window.close()

