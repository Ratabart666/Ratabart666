from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from prettytable import MSWORD_FRIENDLY

x = PrettyTable()
x.set_style(MSWORD_FRIENDLY)
x = ColorTable(theme=Themes.OCEAN)
x.add_row(['Hola',1])
x.add_row([1,1])
x.add_row(['python','fuerza'])
x.field_names=['Datos','prueba 2']
x.border = True
x.header = True

print(x)
print((x.get_string(fields=["Datos"])))
print(x.get_string(start=0, end=2))