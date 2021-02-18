﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Determinar n videos con más views dada una categoría y un país")
    print("3- Determinar el video que más días ha sido trending para un país")
    print("4- Determinar el video que más días ha sido trending para una categoría")
    print("5- Determinar n videos con más views dado un tag")



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        pais=input("Ingresar un país\n")
        categoria=input("Ingresar una categoría\n")
        numeroVideos=input("Ingresar número de videos para buscar el top\n")
        trending_date="18.13.05"
        title="Childish Gambino-This is America (Official Video)"
        channel_title="Childish GambinoVEVO"
        publish_time="2018-0506T04:00:07.000Z"
        views="98938809"
        likes="3037318"
        dislikes="161813"
        print("Trending date: "+trending_date+", "+ "Título: "+title+", "+"Título del canal: "+channel_title+", "+"Fecha de publicación: "+publish_time+", "+"Views: "+views+", "+"Likes: "+likes+", "+"Dislikes: "+dislikes)
    elif int(inputs[0]) == 3:
        pais=input("Ingresar un país\n")
        title="Marvel Studios' Avengers: Infinity War Official Trailer"
        channel_title="Marvel Entertainment"
        numeroDias="8"
        print("Título: "+title+", "+"Título del canal: "+channel_title+", "+"País: "+pais+", "+"Número de días: "+numeroDias)
    elif int(inputs[0]) == 4:
        categoria=input("Ingresar una categoria\n")
        title="Childish Gambino-This is America (Official Video)"
        channel_title="Childish GambinoVEVO"
        category_id="10"
        numeroDias="92"
        print("Título: "+title+", "+"Título del canal: "+channel_title+", "+"ID de categoría: "+category_id+", "+"Número de días: "+numeroDias)
    elif int(inputs[0]) == 5:
        tag=input("Ingresar un tag\n")
        numeroVideos=input("Ingresar número de videos para buscar el top\n")
        title="Childish Gambino-This is America (Official Video)"
        channel_title="Childish GambinoVEVO"
        publish_time="2018-0506T04:00:07.000Z"
        views="98938809"
        likes="3037318"
        dislikes="161813"
        tags="Childish"+" | "+tag
        print("Título: "+title+", "+"Título del canal: "+channel_title+", "+"Fecha de publicación: "+publish_time+", "+"Views: "+views+", "+"Likes: "+likes+", "+"Dislikes: "+dislikes+"Tags: "+tags)
    else:
        sys.exit(0)
sys.exit(0)