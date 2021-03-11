"""
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
from DISClib.ADT import queue as que
from datetime import date



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
def loadVideos():
    return controller.loadVideos("videos-small.csv")
def loadCategories():
    return controller.loadCategories("category-id.csv")
def buscarTop(pais, categoria, n, categories, videos):
    return controller.buscarTop(pais, categoria, n,  categories, videos)
def buscarTrend(pais, categories, videos):
    return controller.buscarTrend(pais, categories, videos)
def buscarTrendMenor(categoria, categories, videos):
    return controller.buscarTrendMenor(categoria, categories, videos)
def topTags(tag, pais, n, videos):
    return controller.topTags(tag, pais, n, videos)




catalog = None

"""
Menu principal
"""
leido="no"
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        if leido=="no":
            print("Cargando información de los archivos ....")
            videos=loadVideos()
            categories=loadCategories()
            print("El número de videos cargados es: "+str(lt.size(videos)))
            print("El primer video cargado tiene la siguiente información:\n"+
            "Título: "+lt.firstElement(videos)['title']+
            "\nCanal: "+lt.firstElement(videos)['channel_title']+
            "\nTrending date: "+lt.firstElement(videos)['trending_date']+
            "\nPaís: "+lt.firstElement(videos)['country']+
            "\nViews: "+lt.firstElement(videos)['views']+
            "\nLikes: "+lt.firstElement(videos)['likes']+
            "\nDislikes: "+lt.firstElement(videos)['dislikes'])
            print("Las categorias cargadas son:")
            for i in range(1, lt.size(categories)+1):
                print(lt.getElement(categories, i)["id\tname"])
            leido="si"
        else:
            print("Solo se puede cargar la información una vez")

    elif int(inputs[0]) == 2:
        pais=input("Ingresar un país en minúsculas y en inglés\n")
        categoria=input("Ingresar una categoría\n")
        n=input("Ingresar número de videos a listar\n")
        topVideos=buscarTop(pais, categoria, n, categories, videos)
        print("Si")
        print("El top "+str(n)+" de videos de "+pais+" con categoría "+categoria+" es:")
        for i in range(1, lt.size(topVideos)+1):
            print(str(i)+". Trending Date: "+lt.getElement(topVideos,i)["trending_date"]+
            ". Título: "+lt.getElement(topVideos,i)["title"]+
            ". Canal: "+lt.getElement(topVideos,i)["channel_title"]+
            ". Fecha de publicación: "+lt.getElement(topVideos,i)["publish_time"]+
            ". Views: "+lt.getElement(topVideos,i)["views"]+
            ". Likes: "+lt.getElement(topVideos,i)["likes"]+
            ". Dislikes: "+lt.getElement(topVideos,i)["dislikes"])
                
    elif int(inputs[0]) == 3:
        pais=input("Ingresar un país en minúsculas y en inglés\n")
        trend=buscarTrend(pais, categories, videos)
        diaPublicacion=int(trend["publish_time"].split("T")[0].split("-")[2])
        mesPublicacion=int(trend["publish_time"].split("T")[0].split("-")[1])
        anioPublicacion=int(trend["publish_time"].split("T")[0].split("-")[0])
        diaTrend=int(trend["trending_date"].split(".")[1])
        mesTrend=int(trend["trending_date"].split(".")[2])
        anioTrend="20"+(trend["trending_date"].split(".")[0])
        anioTrend=int(anioTrend)
        fechaPublicacion=date(anioPublicacion,mesPublicacion,diaPublicacion)
        fechaTrend=date(anioTrend,mesTrend,diaTrend)
        diasTrend=abs(fechaPublicacion-fechaTrend).days
        print("El video con más días de tendencia en "+pais+" es:\n"+
        "Título: "+trend["title"]+
        "\nCanal: "+trend["channel_title"]+
        "\nPaís: "+trend["country"]+
        "\nDías de tendencia: "+str(diasTrend))
    elif int(inputs[0]) == 4:
        categoria=input("Ingresar una categoria\n")
        trend=buscarTrendMenor(categoria, categories, videos)
        diaPublicacion=int(trend["publish_time"].split("T")[0].split("-")[2])
        mesPublicacion=int(trend["publish_time"].split("T")[0].split("-")[1])
        anioPublicacion=int(trend["publish_time"].split("T")[0].split("-")[0])
        diaTrend=int(trend["trending_date"].split(".")[1])
        mesTrend=int(trend["trending_date"].split(".")[2])
        anioTrend="20"+(trend["trending_date"].split(".")[0])
        anioTrend=int(anioTrend)
        fechaPublicacion=date(anioPublicacion,mesPublicacion,diaPublicacion)
        fechaTrend=date(anioTrend,mesTrend,diaTrend)
        diasTrend=abs(fechaPublicacion-fechaTrend).days
        
        print("El video con más días de tendencia con categría "+categoria+" es:\n"+
        "Título: "+trend["title"]+
        "\nCanal: "+trend["channel_title"]+
        "\nID de categoría: "+trend["category_id"]
        +"\nDías de tendencia: "+str(diasTrend))
    elif int(inputs[0]) == 5:
        tag=input("Ingresar un tag\n")
        pais=input("Ingresar un país en minúsculas y en inglés\n")
        n=input("Ingresar número de videos para buscar el top\n")
        topVideos=topTags(tag, pais, n, videos)
        print("Los videos  con más likes en "+pais+" con el tag "+tag+" son:")
        for i in range(1, lt.size(topVideos)+1):
            print(str(i)+". Título: "+lt.getElement(topVideos,i)["title"]+
            ". Canal: "+lt.getElement(topVideos,i)["channel_title"]+
            ". Fecha de publicación: "+lt.getElement(topVideos,i)["publish_time"]+
            ". Fecha de publicación: "+lt.getElement(topVideos,i)["publish_time"]+
            ". Views: "+lt.getElement(topVideos,i)["views"]+
            ". Likes: "+lt.getElement(topVideos,i)["likes"]+
            ". Dislikes: "+lt.getElement(topVideos,i)["dislikes"]+
            ". tags: "+lt.getElement(topVideos,i)["tags"])
    else:
        sys.exit(0)
sys.exit(0)
