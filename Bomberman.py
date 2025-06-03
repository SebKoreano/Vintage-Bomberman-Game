import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import tkinter as tk 
import threading
import winsound
import decimal
import random
import time


principal = tk.Tk()
principal.geometry('750x750') #750x650+100(La zona de la vida y demas stats)
principal.title('Bomberman')
principal.resizable(width=tk.NO,height=tk.NO)

vida=3
bombas=25
puntos=0
llave="Escondida"
x, y =75, 75
musica=0
tilesCajas=[]
teclaUp="w"
teclaDown="s"
teclaLeft="a"
teclaRight="d"
strbomba=0
enemigos=[]
mov=[-50,50]
enemigocoords=[]
enemigos0=[]
posfuego=[]
llaveimg2=0
puerta=(375,325)
llave2=False
nombre=""
segundos2=0

#tileslibres=[(75,75),(75,125),(75,175),(75,225),(75,275),(75,325),(75,375),(75,425),(75,475),(75,525),(75,575),(125,75),(125,175),(125,275),(125,375),(125,475),(125,575),(175,75),(175,125),(175,175),(175,225),(175,275),(175,325),(175,375),(175,425),(175,475),(175,525),(175,575),(225,75),(225,175),(225,275),(225,375),(225,475),(225,575),(275,75),(275,125),(275,175),(275,225),(275,275),(275,325),(275,375),(275,425),(275,475),(275,525),(275,575),(325,75),(325,175),(325,275),(325,375),(325,475),(325,575),(375,75),(375,125),(375,175),(375,225),(375,275),(375,375),(375,425),(375,475),(375,525),(375,575),(425,75),(425,175),(425,275),(425,375),(425,475),(425,575),(475,75),(475,125),(475,175),(475,225),(475,275),(475,325),(475,375),(475,425),(475,475),(475,525),(475,575),(525,75),(525,175),(525,275),(525,375),(525,475),(525,575),(575,75),(575,125),(575,175),(575,225),(575,275),(575,325),(575,375),(575,425),(575,475),(575,525),(575,575),(625,75),(625,175),(625,275),(625,375),(625,475),(625,575),(675,75),(675,125),(675,175),(675,225),(675,275),(675,325),(675,375),(675,425),(675,475),(675,525),(675,575)]

tileslibres=[(75,175),(75,225),(75,275),(75,325),(75,375),(75,425),(75,475),(75,525),(75,575),(125,175),(125,275),(125,375),(125,475),(125,575),(175,75),(175,125),(175,175),(175,225),(175,275),(175,325),(175,375),(175,425),(175,475),(175,525),(175,575),(225,75),(225,175),(225,275),(225,375),(225,475),(225,575),(275,75),(275,125),(275,175),(275,225),(275,275),(275,325),(275,375),(275,425),(275,475),(275,525),(275,575),(325,75),(325,175),(325,275),(325,375),(325,475),(325,575),(375,75),(375,125),(375,175),(375,225),(375,275),(375,375),(375,425),(375,475),(375,525),(375,575),(425,75),(425,175),(425,275),(425,375),(425,475),(425,575),(475,75),(475,125),(475,175),(475,225),(475,275),(475,325),(475,375),(475,425),(475,475),(475,525),(475,575),(525,75),(525,175),(525,275),(525,375),(525,475),(525,575),(575,75),(575,125),(575,175),(575,225),(575,275),(575,325),(575,375),(575,425),(575,475),(575,525),(575,575),(625,75),(625,175),(625,275),(625,375),(625,475),(625,575),(675,75),(675,125),(675,175),(675,225),(675,275),(675,325),(675,375),(675,425),(675,475),(675,525),(675,575)]

tilesindes=[(125,125),(125,225),(125,325),(125,425),(125,525),(225,125),(225,225),(225,325),(225,425),(225,525),(325,125),(325,225),(325,325),(325,425),(325,525),(425,125),(425,225),(425,325),(425,425),(425,525),(525,125),(525,225),(525,325),(525,425),(525,525),(625,125),(625,225),(625,325),(625,425),(625,525)]

img_bomba = Image.open('sprites/bomba1.png')
img_bomba = ImageTk.PhotoImage(img_bomba)

img_fuegov = ImageTk.PhotoImage(file="sprites/fuegov.png")
img_fuegoh = ImageTk.PhotoImage(file="sprites/fuegoh.png")

imgaudio1 = Image.open('sprites/audio1.png')
imgaudio1 = ImageTk.PhotoImage(imgaudio1)

imgaudio2 = Image.open('sprites/audio2.png')
imgaudio2 = ImageTk.PhotoImage(imgaudio2)

imginfo = Image.open('sprites/info.png')
imginfo = ImageTk.PhotoImage(imginfo)

imgconfig = Image.open('sprites/config.png')
imgconfig = ImageTk.PhotoImage(imgconfig)

imgconfig1 = Image.open('sprites/config1.png')
imgconfig1 = ImageTk.PhotoImage(imgconfig1)

plankimg = Image.open('sprites/plank.gif')
plankimg = ImageTk.PhotoImage(plankimg)
 
llaveimg = Image.open('sprites/llave.png')
llaveimg = ImageTk.PhotoImage(llaveimg)


def quitojuego(canvasJuego,canvaStats,vidaslbl,puntoslbl,bombaslbl,llavelbl,timerlbl,ventanajuego):
    global tilesCajas, bombas, enemigo, vida, puntos, nombre
    tilesCajas=[]
    bombas=20
    enemigo=0
    vida=3
    puntos=0
    nombre=""
    canvasJuego.quit()
    canvasJuego.destroy()
    canvaStats.quit()
    canvaStats.destroy()
    vidaslbl.destroy()
    bombaslbl.destroy()
    puntoslbl.destroy()
    llavelbl.destroy()
    timerlbl.destroy()
    ventanajuego.destroy()
    ventanajuego.quit()
    winsound.PlaySound("audio/musica0.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    
def siguientelvl(canvasJuego,personaje,level,numEnemigos1,numEnemigos0,ventanajuego,bombas,nombre):
    global tilesCajas, enemigo, vida
    tilesCajas=[]
    canvasJuego.quit()
    canvasJuego.destroy()
    ventanajuego.destroy()
    ventanajuego.quit()
    return juego(personaje,level,numEnemigos1,numEnemigos0,bombas,nombre)

def iniciador(ventana_previojuego,personaje,level,numEnemigos1,numEnemigos0,bombas,entrynombre):
    global nombre
    ventana_previojuego.destroy()
    ventana_previojuego.quit()
    nombre=entrynombre
    return juego(personaje,level,numEnemigos1,numEnemigos0,bombas,nombre)

####################################-Pantalla de Juego-####################################################
def leer_calificaciones():
    try: #Para que lo abra si existe 
        with open("calificaciones.txt", "r") as file: #Lo abre con el modo r de read, el with es para que se cierre despues de usar
            calificaciones = file.readlines()
        return calificaciones
    except FileNotFoundError: #Porsi no existe
        return []
    
def podio():
    calificaciones = leer_calificaciones()
    calificaciones.sort(reverse=True)  # Ordena la lista de mayor a menor
    if calificaciones:
        mensaje = "Podio de los mejores 10:\n\n"
        i = tk.IntVar() #IntVar() es una variable especial de Tkinter que almacena valores enteros
        while i.get() < 10 and i.get() < len(calificaciones): #el i.get es para obtener el numero de calificaciones que hay, aqui se compara para que minimo hayan 10
            cal = calificaciones[i.get()].strip() #se obtiene la calificacion en la posicion i.get y el .strip quito los espacion en blanco
            mensaje += f"{i.get() + 1}. {cal}\n" #arma el mensaje con +1 para que empieze en 1 y no en cero
            i.set(i.get() + 1) #esto se hace para leer el proximo valor
        messagebox.showinfo("Podio", mensaje)
    else:
        messagebox.showinfo("Podio", "Aún no hay calificaciones registradas.")
####################################-Pantalla de Juego-####################################################
def juego(personaje,level,numEnemigos1,numEnemigos0, bombasj,nombre):

    ventanajuego = tk.Toplevel(bg="grey")
    ventanajuego.geometry('750x750') #750x650+100(La zona de la vida y demas stats)
    ventanajuego.title('Bomberman')
    ventanajuego.resizable(width=tk.NO,height=tk.NO)

    musica=2
    winsound.PlaySound("audio/musica2.wav", winsound.SND_ASYNC + winsound.SND_LOOP) 
    
    jugando=True
    segundos=0
    minutos=0
    horas=0

    global segundos2, enemigos0, teclaUp, teclaDown, teclaLeft, teclaRight, tileslibres, tilesindes, tilesCajas, plankimg, strbomba, enemigos, mov, enemigocoords, posfuego, llaveimg2, puerta, llave2, bombas, llave

    bombas=bombasj
    llave="Escondida"
    llave2=False
    
    def timer(segundos,minutos,horas):
        global segundos2
        segundos+=1
        segundos2+=1
        time.sleep(1)
        if segundos==60:
            segundos=0
            minutos+=1
        if minutos==60:
            minutos=0
            horas+=1
        timerlbl.config(text=f"Tiempo: {horas:02d}:{minutos:02d}:{segundos:02d}")#Le da formato a los numeros de almenos 2 digs (02), la d significa decimal o int. Por ejemplo, si es 5, se mostrará como 05.
        timer(segundos,minutos,horas)
    
    strtimer = threading.Thread(target=timer,args=(segundos,minutos,horas))
    strtimer.start()
    
    ################################- Stats -################################################
    
    canvaStats = tk.Canvas(ventanajuego, highlightthickness=0,height=100, width=750,bg="grey",relief="raised")
    canvaStats.place(relwidth = 10, relheight=10)
    
    vidaslbl = tk.Label(ventanajuego, text=f"Vida:{vida}")
    vidaslbl.place(x=10, y=10)
    bombaslbl = tk.Label(ventanajuego, text=f"Bombas:{bombasj}")
    bombaslbl.place(x=230, y=10)
    puntoslbl = tk.Label(ventanajuego, text=f"Puntos:{puntos}")
    puntoslbl.place(x=500, y=10)
    llavelbl = tk.Label(ventanajuego, text=f"Llave:{llave}")
    llavelbl.place(x=105, y=50)
    timerlbl = tk.Label(ventanajuego, text="Tiempo:")
    timerlbl.place(x=350, y=50)
    
    btt_quit= tk.Button(canvaStats, text="X", command= lambda:quitojuego(canvasJuego,canvaStats,vidaslbl,puntoslbl,bombaslbl,llavelbl,timerlbl,ventanajuego))
    btt_quit.place(x=723, y=10)
    btt_config= tk.Button(canvaStats, image= imgconfig1, command= lambda:config(musica))
    btt_config.place(x=720, y=50)

    ################################- Juego -################################################
    canvasJuego = tk.Canvas(ventanajuego, highlightthickness=0,bg="black")
    canvasJuego.place(relwidth = 1, relheight=1,x=0, y=100)
    
    lvlimg1 = ImageTk.PhotoImage(file=f"sprites/lvl1.png")
    lvl1 = canvasJuego.create_image(375,325, image =lvlimg1)
    
    personajeimg = Image.open(f"sprites/bomberman{personaje}3.gif") 
    personajeimg = ImageTk.PhotoImage(personajeimg)
    Personaje = canvasJuego.create_image(x,y, image =personajeimg)

    def cajas(numCajas,i,canvasJuego): #Creo las cajas en las posiciones libres
        global tilesCajas, plankimg
        if i<numCajas:
            coordenada = random.choice(tileslibres)
            tileslibres.remove(coordenada)
            tilesCajas+=[coordenada]
            plank = canvasJuego.create_image(coordenada[0],coordenada[1], image=plankimg)
            cajas(numCajas,i+1,canvasJuego)

    cajas(20,0,canvasJuego)
    
    llavecoord=random.choice(tilesCajas)

    def crearllave(x,y):
        global tilesCajas, llaveimg2, llave
        if (x,y)==llavecoord:
            llave="Expuesta"
            llavelbl.config(text=f"Llave:{llave}")
            llaveimg2=canvasJuego.create_image(llavecoord[0],llavecoord[1], image=llaveimg)
    
    def calificcionfinal():
        global vida, segundos2, puntos, bombas
        peso_tiempo = decimal.Decimal("0.5")  # Usamos Decimal para manejar números decimales precisos
        calificacion=(vida * 300) - (segundos2 * peso_tiempo) + puntos + (bombas * 50) + 1000
        print(calificacion)
        return calificacion
    
    def guardar_calificacion():
        calificacion = calificcionfinal()
        with open("calificaciones.txt", "a") as file: #Lo abre con a de append y con with para cerrar el archivo despues de usarlo
            file.write(f"{nombre}: {calificacion}\n")
    
    def win():
        quitojuego(canvasJuego,canvaStats,vidaslbl,puntoslbl,bombaslbl,llavelbl,timerlbl,ventanajuego)
        ventanaWin = tk.Toplevel(bg="grey")
        ventanaWin.geometry('600x350') 
        ventanaWin.title('YOU WIN!')
        ventanaWin.resizable(width=tk.NO,height=tk.NO)
        
        canvasWin = tk.Canvas(ventanaWin, highlightthickness=0, bg="black")
        canvasWin.place(relwidth = 1, relheight=1)

        imgWin = ImageTk.PhotoImage(file="sprites/youWin.png")
        canvasWin.imgRef = imgWin #Hace una referencia de la imagen
        imgWinn = canvasWin.create_image(300,170, image=imgWin)

        puntos_label = tk.Label(canvasWin, text=f"Calificacion final: {calificcionfinal()}", font=("Arial", 12),bg="black",fg="white") 
        puntos_label.place(x=240, y=300)
        guardar_calificacion()
    
    def loose():
        quitojuego(canvasJuego,canvaStats,vidaslbl,puntoslbl,bombaslbl,llavelbl,timerlbl,ventanajuego)
        ventanaLoose = tk.Toplevel(bg="grey")
        ventanaLoose.geometry('600x300') 
        ventanaLoose.title('GAME OVER')
        ventanaLoose.resizable(width=tk.NO,height=tk.NO)
        
        canvasLoose = tk.Canvas(ventanaLoose, highlightthickness=0, bg="black")
        canvasLoose.place(relwidth = 1, relheight=1)

        imgLoose = ImageTk.PhotoImage(file="sprites/gameOver.png")
        canvasLoose.imgRef = imgLoose #Hace una referencia de la imagen
        imgLoosee = canvasLoose.create_image(300,150, image=imgLoose)



    ##Bomba##
    def bombaquema(overlay,x,y):
        global vida
        if len(overlay)>1:
            if not overlay[1]==2:
                canvasJuego.delete(overlay[1])
                if (x,y) in tilesCajas:
                    tilesCajas.remove((x,y))
                if (x,y) in enemigos:
                    enemigos.remove((x,y))
            elif overlay[1]==2:
                vida-=1
                vidaslbl.config(text=f"Vidas:{vida}")

    def bomba():
        global strbomba, vida, posfuego, llaveimg2
        bboxPersonaje = canvasJuego.bbox(Personaje)
        bomb=canvasJuego.create_image(bboxPersonaje[2]-25,bboxPersonaje[3]-25, image=img_bomba)
        time.sleep(1)
        overlapUp=canvasJuego.find_overlapping(bboxPersonaje[0],bboxPersonaje[1]-50,bboxPersonaje[2],bboxPersonaje[3]-50)
        overlapDown=canvasJuego.find_overlapping(bboxPersonaje[0],bboxPersonaje[1]+50,bboxPersonaje[2],bboxPersonaje[3]+50)
        overlapLeft=canvasJuego.find_overlapping(bboxPersonaje[0]-50,bboxPersonaje[1],bboxPersonaje[2]-50,bboxPersonaje[3])
        overlapRight=canvasJuego.find_overlapping(bboxPersonaje[0]+50,bboxPersonaje[1],bboxPersonaje[2]+50,bboxPersonaje[3])
        bombaquema(overlapUp,bboxPersonaje[0]+25,bboxPersonaje[1]-25)
        bombaquema(overlapDown,bboxPersonaje[0]+25,bboxPersonaje[3]+25)
        bombaquema(overlapLeft,bboxPersonaje[0]-25,bboxPersonaje[1]+25)
        bombaquema(overlapRight,bboxPersonaje[2]+25,bboxPersonaje[1]+25)
        fuego1=canvasJuego.create_image(bboxPersonaje[2]-25,(bboxPersonaje[3]-25)-50, image=img_fuegov)
        fuego2=canvasJuego.create_image(bboxPersonaje[2]-25,(bboxPersonaje[3]-25)+50, image=img_fuegov)
        fuego3=canvasJuego.create_image((bboxPersonaje[2]-25)-50,bboxPersonaje[3]-25, image=img_fuegoh)
        fuego4=canvasJuego.create_image((bboxPersonaje[2]-25)+50,bboxPersonaje[3]-25, image=img_fuegoh)
        posfuego=[(bboxPersonaje[2]-25,(bboxPersonaje[3]-25)-50),(bboxPersonaje[2]-25,(bboxPersonaje[3]-25)+50),((bboxPersonaje[2]-25)-50,bboxPersonaje[3]-25),((bboxPersonaje[2]-25)+50,bboxPersonaje[3]-25)]
        winsound.PlaySound("audio/explosion.wav", winsound.SND_ASYNC) 
        time.sleep(1)
        canvasJuego.delete(fuego1)
        canvasJuego.delete(fuego2)
        canvasJuego.delete(fuego3)
        canvasJuego.delete(fuego4)
        canvasJuego.delete(bomb)
        crearllave(bboxPersonaje[0]+25,bboxPersonaje[1]-25)
        crearllave(bboxPersonaje[0]+25,bboxPersonaje[3]+25)
        crearllave(bboxPersonaje[0]-25,bboxPersonaje[1]+25)
        crearllave(bboxPersonaje[2]+25,bboxPersonaje[1]+25)
        winsound.PlaySound("audio/musica2.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

    def ponerbomba(evento):
        global strbomba, bombas
        bombas-=1
        bombaslbl.config(text=f"Bombas:{bombas}")
        if not bombas<0:
            strbomba = threading.Thread(target=bomba,args=())
            strbomba.start()
        else:
            loose()
            
    ################################- Enemigos -################################################
    enemigo0img = Image.open(f"sprites/enemigo0.png") 
    enemigo0img = ImageTk.PhotoImage(enemigo0img)
    
    enemigo1img = Image.open(f"sprites/enemigo1.png") 
    enemigo1img = ImageTk.PhotoImage(enemigo1img)
    
    def bordeenemigo(enemigo):
        bboxenemigo = canvasJuego.bbox(enemigo)
        bbboxPup=bboxenemigo[1]
        bbboxPdown=bboxenemigo[3]
        bbboxPleft=bboxenemigo[0]
        bbboxPright=bboxenemigo[2]
        if bbboxPup<50:
            canvasJuego.move(enemigo, 0,50)
        elif bbboxPdown>600:
            canvasJuego.move(enemigo, 0,-50)
        elif bbboxPleft<50:
            canvasJuego.move(enemigo, 50,0)
        elif bbboxPright>700:
            canvasJuego.move(enemigo, -50,0)
    

    def movenemigo(nombre,canvasJuego):
        global mov, enemigocoords, posfuego, enemigos0, puntos
        move1=random.choice(mov)
        move2=random.choice(mov)
        if canvasJuego.coords(nombre)==[]:
            puntos+=1000
            puntoslbl.config(text=f"Puntos:{puntos}")
            enemigos0.remove(enemigocoords)
            return None
        enemigocoordsx,enemigocoordsy=canvasJuego.coords(nombre)
        enemigocoords=(enemigocoordsx,enemigocoordsy)
        enemigos0.remove((enemigocoords))
        canvasJuego.move(nombre, move1,move2)
        bordeenemigo(nombre)
        enemigocoordsx,enemigocoordsy=canvasJuego.coords(nombre)
        enemigocoords=(enemigocoordsx,enemigocoordsy)
        enemigos0+=[enemigocoords]
        time.sleep(2)
        movenemigo(nombre,canvasJuego)
        
    def crear_enemigos0(numEnemigos,canvasJuego):
        global enemigos0
        if numEnemigos>0:
            coordenada = random.choice(tileslibres)
            enemigo = canvasJuego.create_image(coordenada[0],coordenada[1], image=enemigo0img)
            enemigos0+=[coordenada]
            strenemigo = threading.Thread(target=movenemigo,args=(enemigo,canvasJuego))
            strenemigo.start()
            crear_enemigos0(numEnemigos-1,canvasJuego)
    
    def crear_enemigos1(numEnemigos,canvasJuego):
        global enemigos, enemigo
        if numEnemigos>0:
            coordenada = random.choice(tileslibres)
            enemigos+=[coordenada]
            enemigo = canvasJuego.create_image(coordenada[0],coordenada[1], image=enemigo1img)
            crear_enemigos1(numEnemigos-1,canvasJuego)
    
    crear_enemigos1(numEnemigos1,canvasJuego)
    crear_enemigos0(numEnemigos0,canvasJuego)
    
    def detectar_cambio(lista, longitud_anterior):
        global puntos
        longitud_actual = len(lista)
        if longitud_actual < longitud_anterior:
            puntos+=100
            puntoslbl.config(text=f"Puntos:{puntos}")
        time.sleep(0.1)
        detectar_cambio(lista, longitud_actual)

    strdetectar = threading.Thread(target=detectar_cambio, args=(enemigos, len(enemigos)))
    strdetectar.start()

    ################################- Movimiento -################################################
    def borde():
        bboxPersonaje = canvasJuego.bbox(Personaje)
        bbboxPup=bboxPersonaje[1]
        bbboxPdown=bboxPersonaje[3]
        bbboxPleft=bboxPersonaje[0]
        bbboxPright=bboxPersonaje[2]
        if bbboxPup<50:
            canvasJuego.move(Personaje, 0,50)
        elif bbboxPdown>600:
            canvasJuego.move(Personaje, 0,-50)
        elif bbboxPleft<50:
            canvasJuego.move(Personaje, 50,0)
        elif bbboxPright>700:
            canvasJuego.move(Personaje, -50,0)

    def bloquesIndes(x1,y1):
        bboxPersonaje = canvasJuego.bbox(Personaje)
        if  (bboxPersonaje[2]-25,bboxPersonaje[3]-25) in tilesindes:
            canvasJuego.move(Personaje, x1,y1)

    def bloquesDes(x1,y1):
        global tilesCajas
        bboxPersonaje = canvasJuego.bbox(Personaje)
        if  (bboxPersonaje[2]-25,bboxPersonaje[3]-25) in tilesCajas:
            canvasJuego.move(Personaje, x1,y1)

    def choqueenemigo():
        global enemigos0, vida
        jugadorcoordsx,jugadorcoordsy=canvasJuego.coords(Personaje)
        jugadorcoords=(jugadorcoordsx,jugadorcoordsy)
        if jugadorcoords in enemigos0:
            vida-=1
            vidaslbl.config(text=f"Vidas:{vida}")
            if vida<0:
                loose()
    
    def choqueenemigo2():
        global enemigos, vida
        jugadorcoordsx,jugadorcoordsy=canvasJuego.coords(Personaje)
        jugadorcoords=(jugadorcoordsx,jugadorcoordsy)
        if jugadorcoords in enemigos:
            vida-=1
            vidaslbl.config(text=f"Vidas:{vida}")
            if vida<0:
                loose()

    def cogerllave():
        global llaveimg2, llave2
        bboxPersonaje = canvasJuego.bbox(Personaje)
        if (bboxPersonaje[0]+25,bboxPersonaje[1]+25)==llavecoord:
            canvasJuego.delete(llaveimg2)
            llave="En el inventario"
            llave2=True
            llavelbl.config(text=f"Llave:{llave}")

    def entrarpuerta():
        bboxPersonaje = canvasJuego.bbox(Personaje)
        if llave2==True:
            if (bboxPersonaje[0]+25,bboxPersonaje[1]+25)==puerta:
                if level==1:
                    messagebox.showinfo("¡Felicidades!", "¡Pasaste de nivel!")
                    return siguientelvl(canvasJuego,personaje,2,7,1,ventanajuego,25,nombre)
                elif level==2:
                    messagebox.showinfo("¡Felicidades!", "¡Pasaste de nivel!")
                    return siguientelvl(canvasJuego,personaje,3,10,1,ventanajuego,20,nombre)
                else:
                    return win()
            
    def direccionP(mover):
        if mover == 'up':
            canvasJuego.move(Personaje, 0,-50)
            choqueenemigo()
            bloquesIndes(0,50)
            bloquesDes(0,50)
            cogerllave()
            entrarpuerta()
            choqueenemigo2()
            borde()
        elif mover == 'down':
            canvasJuego.move(Personaje, 0,50)
            choqueenemigo()
            bloquesIndes(0,-50)
            bloquesDes(0,-50)
            cogerllave()
            entrarpuerta()
            choqueenemigo2()
            borde()
        elif mover == 'left':
            canvasJuego.move(Personaje, -50,0)
            choqueenemigo()
            bloquesIndes(50,0)
            bloquesDes(50,0)
            cogerllave()
            entrarpuerta()
            choqueenemigo2()
            borde()
        elif mover == 'right':
            canvasJuego.move(Personaje, 50,0)
            choqueenemigo()
            bloquesIndes(-50,0)
            bloquesDes(-50,0)
            cogerllave()
            entrarpuerta()
            choqueenemigo2()
            borde()

    def manejar_evento_tecla(event):
        tecla = event.char.lower()
        if tecla == f"{teclaUp}":
            direccionP('up')
        elif tecla == f"{teclaDown}":
            direccionP('down')
        elif tecla == f"{teclaLeft}":
            direccionP('left')
        elif tecla == f"{teclaRight}":
            direccionP('right')

    # Asignar la función de manejo de eventos a cada tecla
    ventanajuego.bind_all("<KeyPress>", manejar_evento_tecla)
    ventanajuego.bind_all("<space>", ponerbomba)

    bttwin= tk.Button(canvaStats, text="WIN", command= lambda:win())
    bttwin.place(x=640, y=10)

    ventanajuego.mainloop()
    
    
    
    
    
####################################-Pantalla Previa al Juego-####################################################

def previojuego(principal):
    ventana_previojuego=tk.Toplevel(bg="grey")
    ventana_previojuego.title("Personalización")
    ventana_previojuego.geometry("750x525")
    ventana_previojuego.resizable(width=tk.NO,height=tk.NO)


    canvasPrevio = tk.Canvas(ventana_previojuego, highlightthickness=0, bg="grey")
    canvasPrevio.place(relwidth = 1, relheight=1)

    titulolbl = tk.Label(ventana_previojuego, text="INTRODUZCA SU NOMBRE")
    titulolbl.pack(pady=10)

    entrynombre = tk.Entry(ventana_previojuego, width=25) #entrada de nombre
    entrynombre.pack()

    personajelbl = tk.Label(ventana_previojuego, text="CHOOSE YOUR CHARACTER!")
    personajelbl.pack(pady=30)

    def leernombre(entrynombre):
        global nombre
        nombre=str(entrynombre.get())
        return nombre
    
    botonnombre = tk.Button(ventana_previojuego, border = 0, text="Aceptar nombre",command = lambda:leernombre(entrynombre)) 
    boton_personaje1 = tk.Button(ventana_previojuego, border = 0, text="WHITE",command = lambda:iniciador(ventana_previojuego,1,1,5,1,30,str(entrynombre.get()))) 
    boton_personaje1.place(x=100, y=150)
    boton_personaje2 = tk.Button(ventana_previojuego, border = 0, text="BLACK", command = lambda:iniciador(ventana_previojuego,2,1,5,1,30,str(entrynombre.get())))
    boton_personaje2.place(x=355, y=150)
    boton_personaje3 = tk.Button(ventana_previojuego, border = 0, text="BLUE", command = lambda:iniciador(ventana_previojuego,3,1,5,1,30,str(entrynombre.get())))
    boton_personaje3.place(x=600, y=150)

    bomberman1img = ImageTk.PhotoImage(file="sprites/bomberman13i.gif")
    bomberman1 = canvasPrevio.create_image(125,350, image =bomberman1img)
    bomberman2img = ImageTk.PhotoImage(file="sprites/bomberman23i.gif")
    bomberman2 = canvasPrevio.create_image(380,350, image =bomberman2img)
    bomberman3img = ImageTk.PhotoImage(file="sprites/bomberman33i.gif")
    bomberman3 = canvasPrevio.create_image(625,350, image =bomberman3img)

    ventana_previojuego.mainloop()


####################################-Pantalla de Configuracion-####################################################

def config(musica):
    ventana_config=tk.Toplevel(bg="grey")
    ventana_config.title("Configuracion")
    ventana_config.geometry("500x220")
    ventana_config.resizable(width=tk.NO,height=tk.NO)

    boton_audio1 = tk.Button(ventana_config, border = 0, image= imgaudio1, activebackground='grey', bg= 'grey', command = lambda:winsound.PlaySound(f"audio/musica{musica}.wav", winsound.SND_ASYNC + winsound.SND_LOOP))
    boton_audio1.place(x=10, y=150)
    boton_audio2 = tk.Button(ventana_config, border = 0, image= imgaudio2, activebackground='grey', bg= 'grey', command = lambda:winsound.PlaySound(None, 0))
    boton_audio2.place(x=428, y=150)
    
    entryUP = tk.Entry(ventana_config, width=25) 
    entryUP.place(x=60, y=70) 
    entryDOWN = tk.Entry(ventana_config, width=25) 
    entryDOWN.place(x=60, y=110)
    entryLEFT = tk.Entry(ventana_config, width=25) 
    entryLEFT.place(x=335, y=70)
    entryRIGHT = tk.Entry(ventana_config, width=25) 
    entryRIGHT.place(x=335, y=110) 
    
    
    def asignar_tecla(entry, direccion):
        tecla = entry.get().lower()
        global teclaUp
        global teclaDown
        global teclaLeft
        global teclaRight
        if tecla:
            if direccion == "up":
                teclaUp = tecla
                messagebox.showinfo("Asignación de Tecla", f"Tecla UP asignada: {teclaUp}")
            elif direccion == "down":
                teclaDown = tecla
                messagebox.showinfo("Asignación de Tecla", f"Tecla DOWN asignada: {teclaDown}")
            elif direccion == "left":
                teclaLeft = tecla
                messagebox.showinfo("Asignación de Tecla", f"Tecla LEFT asignada: {teclaLeft}")
            elif direccion == "right":
                teclaRight = tecla
                messagebox.showinfo("Asignación de Tecla", f"Tecla RIGHT asignada: {teclaRight}")
        else:
            messagebox.showwarning("Error", "Por favor ingrese una tecla válida")
    
    teclas_label = tk.Label(ventana_config, text="Configuracion de teclas", font=("Arial", 12),bg="grey") #mi nombre
    teclas_label.pack(pady=10)
      
    up_button = tk.Button(ventana_config, text="UP", font=("Arial", 10), bg="grey", command=lambda: asignar_tecla(entryUP, "up"))
    up_button.place(x=20, y=68)

    down_button = tk.Button(ventana_config, text="DOWN", font=("Arial", 10), bg="grey", command=lambda: asignar_tecla(entryDOWN, "down"))
    down_button.place(x=10, y=108)

    left_button = tk.Button(ventana_config, text="LEFT", font=("Arial", 10), bg="grey", command=lambda: asignar_tecla(entryLEFT, "left"))
    left_button.place(x=293, y=68)

    right_button = tk.Button(ventana_config, text="RIGHT", font=("Arial", 10), bg="grey", command=lambda: asignar_tecla(entryRIGHT, "right"))
    right_button.place(x=290, y=108)
    

####################################-Pantalla de Info-####################################################

def info():
    ventana_info=tk.Toplevel(bg="grey")
    ventana_info.title("Informacion")
    ventana_info.resizable(width=tk.NO,height=tk.NO)

    nombre_label = tk.Label(ventana_info, text="Nombre: Sebastian Bolaños", font=("Arial", 12),bg="grey") #mi nombre
    nombre_label.pack(pady=5)

    id_label = tk.Label(ventana_info, text="ID: 2 0883 0910", font=("Arial", 12),bg="grey") 
    id_label.pack(pady=5)

    yo_image = Image.open("sprites/yo.PNG") #mi foto
    yo_image1 = ImageTk.PhotoImage(yo_image)
    Labelyoimage = tk.Label(ventana_info, image=yo_image1)
    Labelyoimage.pack(pady=5)

    itcr_label = tk.Label(ventana_info, text="Entorno académico: Instituto Tecnologico de Costa Rica (ITCR)", font=("Arial", 12),bg="grey") 
    itcr_label.pack(pady=5)

    curso_label = tk.Label(ventana_info, text="Curso: Introduccion a la programacion", font=("Arial", 12),bg="grey") 
    curso_label.pack(pady=5)

    carrera_label = tk.Label(ventana_info, text="Carrera: Ingieneria en computadores (CE)", font=("Arial", 12),bg="grey") 
    carrera_label.pack(pady=5)

    profesor_label = tk.Label(ventana_info, text="Profesor: Jason Leiton Jimenez", font=("Arial", 12),bg="grey") 
    profesor_label.pack(pady=5)

    pais_label = tk.Label(ventana_info, text="Pais de produccion: Costa Rica", font=("Arial", 12),bg="grey") 
    pais_label.pack(pady=5)

    fecha_label = tk.Label(ventana_info, text="Fecha de la ultima actualizacion: 2/05/2024", font=("Arial", 12),bg="grey") 
    fecha_label.pack(pady=5)

    version_label = tk.Label(ventana_info, text="Version: 1", font=("Arial", 12),bg="grey") 
    version_label.pack(pady=5)

    ventana_info.mainloop()
    
####################################-Pantalla de Inicio-####################################################

canvasPrincipal = tk.Canvas(principal, highlightthickness=0, bg="black")
canvasPrincipal.place(relwidth = 1, relheight=1)

imgtitulo = Image.open('sprites/titulo.png')
imgtitulo = ImageTk.PhotoImage(imgtitulo)
titulo = canvasPrincipal.create_image(375,180, image =imgtitulo)

start=tk.Button(principal,text="START",fg="black",command=lambda:previojuego(principal))# boton 
start.place(x=375, y=375)

boton_podio =tk.Button(principal,text="PODIO",fg="black",command=lambda:podio())# boton 
boton_podio.place(x=374, y=420)

boton_config = tk.Button(principal, border = 0, image= imgconfig, activebackground='black', bg= 'black', command = lambda:config(musica))
boton_config.place(x=670, y=670)

boton_info = tk.Button(principal, border = 0, image= imginfo, activebackground='black', bg= 'black', command = lambda:info())
boton_info.place(x=0, y=650)
  
    
winsound.PlaySound("audio/musica0.wav", winsound.SND_ASYNC + winsound.SND_LOOP) 


principal.call('wm', 'iconphoto', principal._w, img_bomba) #wm:metodo relacionado con la administracion de ventanas, ._w: se utiliza para identificar la ventana a nivel de sistema
principal.mainloop()
