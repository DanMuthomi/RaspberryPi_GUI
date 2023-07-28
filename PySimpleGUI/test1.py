import PySimpleGUI as sg
import firstGUI

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='-NAME-')],
            [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='-ADDRESS-')],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='-PHONE-')],
            [sg.Submit(), sg.Cancel()]
            ]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
firstGUI.firstWin()

#sg.Popup(event, values, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])

#print(values['-NAME-'])
name = (values['-NAME-'])
add = (values['-ADDRESS-'])
no = (values['-PHONE-'])
info = [name, add, no]
print (info)
