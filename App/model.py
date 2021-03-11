"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.ADT import queue as que
from datetime import date


def addVideos(videosfile):
    videos=lt.newList(datastructure="SINGLE_LINKED", filename=videosfile)
    return videos
def addCategories(categoriesfile):
    categories=lt.newList(datastructure="SINGLE_LINKED", filename=categoriesfile)
    return categories
def buscarTop(pais, categoria, n,  categories, videos):
    top=lt.newList(datastructure="SINGLE_LINKED")
    id=0
    for i in range(1, lt.size(categories)):
        actual=lt.getElement(categories, i)["id\tname"]
        actual=actual.split(" ",1)
        if actual[1]==categoria:
            id=actual[0]
            break
    id=int(id)
    for i in range(1, lt.size(videos)):
        if int(lt.getElement(videos, i)["category_id"])==id and pais==lt.getElement(videos, i)["country"]:
            if lt.size(top)<int(n):
                lt.addLast(top, lt.getElement(videos, i))
            else:
                minimo=lt.getElement(top, 0)
                posMin=0
                for j in range(0, lt.size(top)):
                    if int(lt.getElement(top, j)["views"])<int(minimo["views"]):
                        minimo=lt.getElement(top, j)
                        posMin=j
                if int(lt.getElement(top, posMin)["views"])<int(lt.getElement(videos, i)["views"]):
                    lt.deleteElement(top, posMin)
                    lt.addLast(top, lt.getElement(videos, i))
                
    return top
def buscarTrend(pais, categories, videos):
    trend=""
    for i in range(1, lt.size(videos)):
        if pais==lt.getElement(videos, i)["country"]:
            if trend=="":
                trend=lt.getElement(videos, i)
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
            else:
                diaPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[2])
                mesPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[1])
                anioPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[0])
                diaTrend=int(lt.getElement(videos, i)["trending_date"].split(".")[1])
                mesTrend=int(lt.getElement(videos, i)["trending_date"].split(".")[2])
                anioTrend="20"+(lt.getElement(videos, i)["trending_date"].split(".")[0])
                anioTrend=int(anioTrend)
                fechaPublicacion=date(anioPublicacion,mesPublicacion,diaPublicacion)
                fechaTrend=date(anioTrend,mesTrend,diaTrend)
                diasActual=abs(fechaPublicacion-fechaTrend).days
                if diasActual>diasTrend:
                    trend=lt.getElement(videos, i)
                    diasTrend=diasActual
    return trend
def buscarTrendMenor(categoria, categories, videos):
    for i in range(1, lt.size(categories)):
        actual=lt.getElement(categories, i)["id\tname"]
        actual=actual.split(" ",1)
        if actual[1]==categoria:
            id=actual[0]
            break
    trend=""
    for i in range(1, lt.size(videos)):
        if int(id)==int(lt.getElement(videos, i)["category_id"]):
            if trend=="":
                trend=lt.getElement(videos, i)
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
            else:
                diaPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[2])
                mesPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[1])
                anioPublicacion=int(lt.getElement(videos, i)["publish_time"].split("T")[0].split("-")[0])
                diaTrend=int(lt.getElement(videos, i)["trending_date"].split(".")[1])
                mesTrend=int(lt.getElement(videos, i)["trending_date"].split(".")[2])
                anioTrend="20"+(lt.getElement(videos, i)["trending_date"].split(".")[0])
                anioTrend=int(anioTrend)
                fechaPublicacion=date(anioPublicacion,mesPublicacion,diaPublicacion)
                fechaTrend=date(anioTrend,mesTrend,diaTrend)
                diasActual=abs(fechaPublicacion-fechaTrend).days
                if diasActual>diasTrend:
                    trend=lt.getElement(videos, i)
                    diasTrend=diasActual
    return trend
def topTags(tag, pais, n, videos):
    top=lt.newList(datastructure="SINGLE_LINKED")
    for i in range(1, lt.size(videos)):
       if pais==lt.getElement(videos, i)["country"]: 
           tags=lt.getElement(videos,i)["tags"].split("|")
           for j in range(1, len(tags)):
               tags[j]=tags[j].replace('"', "")
               if tags[j]==tag:
                    if lt.size(top)<int(n):
                       lt.addLast(top, lt.getElement(videos,i))
                       break
                    else:
                        menor=lt.firstElement(top)
                        posMenor=0
                        for k in range(1, lt.size(top)):
                            if int(lt.getElement(top, k)["likes"])<int(menor["likes"]):
                                menor=lt.getElement(top, k)
                                posMenor=k
                        if int(menor["likes"])<int(lt.getElement(videos,i)["likes"]):
                            lt.deleteElement(top, posMenor)
                            lt.addLast(top, lt.getElement(videos, i))
                        break
    return top






               



