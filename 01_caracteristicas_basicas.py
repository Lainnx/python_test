"""
CARACTERISTICAS BÁSICAS DE PYTHON

##Variables
Una variable es un espacio en memeoria para guardar datos
por tanto es un contenedor

Para crear una variable...
identificador = valor

Hay reglas para llamar a los identificadores (nombre variable)

Las variables tienen tipo
    --numeros (int, float...)
    --texto (sting)
    --booleanos (True, False)
Python es de tipado dinamico, las variables pueden tener cualquier tipo, el tipo se asigna en el momento de ejecución
    n = 1   #int
    n = "uno"   #string
Python tiene tipàdo fuerte
    suma = n+2 #ERROR, no se puede sumar numeros y texto
    concatenacion = n + srt(2)  #convertir el int 2 en string
    suma_numerica = int("1") + 2 #convertir el srting "1" en int
No se puede hacer:
1var (empezar por numero, pueded contener)
$var || va$r (contener caracteres especiales)

No DEBEMOS hacer (no son exactamente errores):
Contener caracteres fuera del ASCII
Empezar por guion bajo(reservado para determinadas situaciones, por convenio)

Que DEBEMOS hacer
Nombrar a nuestras variables con palabras descriptivas
Podemons usar mas de una palabra separadas por un guion bajo (directiva PEP-8)

"""
git config #para configurar git, SOLO SE HACE UNA VEZ
--global # para todos los proyectos git, sin especificar estandard
git config --global user.name "user name" #sino hi ha espais no cal ""
git config --global user.email "email"
git config core.autocrlf true   #true para windows | input para mac i linux
    autocrlf #windows añade un caracter al final, esto hace que git lidie con él automaticamente al subir/descargar
             #correccion del salto de linea
git config --global core.editor "code --wait" #para elegir editor

git config --global -e #para ver la configuracion actual abre fichero git.config (e, editar)

git init #inicia un repositorio git vacío

fases de git
 |--------------------------------------------------------------|------|
    git                                                         |github
 |working/unstage   |stage          |commit                     |server|
 ---------U----------------A--------------------M------------------------------------
 |donde estan to-   |los ficheros   |mueves ficheros de stage   |subir al servidor
 |dos los ficheros  |que pasas para |y añades descripcion       |push, 
 |                  |control de ver |
                    |(contraseñas o |
                    |ficheros muy   |
                    |pesados no,    |
                    |config files)  |

git status #da info de como esta en este momento el repositorio

#crear fichero ".gitignore" lista de ficheros que queremos que git ignore (gitignore.io)

git add 
    .   #todo menos lo del gitignore
    0*  #todo lo que empieze por 0
        #o nombres de fichero separados con espacios
git add 0* code0.py

git rm --cache filename #para quitarlo de la fase stage a Untracked

git commit -m "mensaje" #pasa de fase, a punto para subirlo que ya estan i no se deberian editar
            #-m message
            #pasar a commit (ficheros validados)

git remote add origin https://github.com/nom_conta/nom_repo.git #donde quieres enviar los ficheros de origen en hdd a web SOLO UNA VEZ
git branch -M main  #para cambiar nombre de master a main SOLO UNA VEZ
git push -u origin main #sube la info a la nube

################################################
