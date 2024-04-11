""" import turtle
import another_module
print(another_module.another_variable)
timmy = turtle.Turtle()
myscreen = turtle.Screen()
print(timmy)
timmy.shape("turtle")
timmy.color('red','green')
timmy.forward(100)
print(myscreen.canvheight)
myscreen.exitonclick() """

from prettytable import PrettyTable
table = PrettyTable() 
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander']) 
table.add_column('Type',['Electric','Water','Fire'])
print(table.align)
table.valign = 't'
table.header_style='upper'
print(table)
