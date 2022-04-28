#!/bin/sh
#Obtener directorio actual
cd .
#Entrar a directorio Actividad que contiene los directorios
cd 'Actividad 2 Descargar 11 de febrero de 2022 1200'

#En el directorio actual Actividad busca todos los subdirectorios
a=1

for dir in */ ; do
    dir="${dir%/}"
    #Imprimir nombre de la carpeta 
    echo "Nombre carpeta " $a ":" "${dir##*/}" >> ../Resultados.txt
    #Ir al subdirectorio
    cd "${dir##*/}"
    i=1
    
    #En el subdirectorio actual busca todos los archivos e imprime su nombre
    for file in *; do

        file="${file%/}"
        #Imprimir nombre del archivo en archivo txt dentro de el directorio principal
        echo "Archivo"  $i ":" "${file##*/}" >> ../../Resultados.txt
        i=$((i+1))

    done
    #Volver al directorio de directorios
    cd ..
    a=$((a+1))

done