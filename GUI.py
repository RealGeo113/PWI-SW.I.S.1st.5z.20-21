from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import project
import OCR
import filtry
import cv2 as cv
import numpy
import histogram


def displayer(patch):
    global sourceimage
    global wyswietlacz
    sizer = patch.size
    patch.thumbnail((1280, 720), Image.ANTIALIAS)
    sourceimage = ImageTk.PhotoImage(patch)
    label = Label(root, text=sizer)
    label.grid(row=0)
    wyswietlacz = Label(image=sourceimage)
    wyswietlacz.grid(row=1)


def openPhoto():
    patch = Image.open(askopenfilename(filetypes=[("Pliki obrazów", ".png .jpg .jpe .jpeg .bmp")]))
    print(patch)
    displayer(patch)
    return patch


def doBLUR(source):
    filters = filtry.filtry(source, 1)
    displayer(filters)


obrazek = openPhoto

root = Tk()
root.title('Skanowanie tablicy suchościeralnej')
root.geometry("1296x729")

menubar = Menu(root)
plikmenu = Menu(menubar, tearoff=0)
plikmenu.add_command(label="Otwórz obraz", command=openPhoto)
plikmenu.add_command(label="Zapisz obraz")
plikmenu.add_separator()
plikmenu.add_command(label="Wyjdź", command=root.quit)
menubar.add_cascade(label="Plik", menu=plikmenu)

filtrmenu = Menu(menubar, tearoff=0)
filtrmenu.add_command(label="Odcienie szarosci")
filtrmenu.add_command(label="Negatyw")
filtrmenu.add_separator()
filtrmenu.add_command(label="BLUR", command=lambda: doBLUR(obrazek))
filtrmenu.add_command(label="CONTOUR")
filtrmenu.add_command(label="DETAIL")
filtrmenu.add_command(label="EDGE_ENHANCE")
filtrmenu.add_command(label="EDGE_ENHANCE_MORE")
filtrmenu.add_command(label="EMBOSS")
filtrmenu.add_command(label="FIND_EDGES")
filtrmenu.add_command(label="SMOOTH")
filtrmenu.add_command(label="SMOOTH_MORE")
filtrmenu.add_command(label="SHARPEN")
menubar.add_cascade(label="Filtry", menu=filtrmenu)

obrazmenu = Menu(menubar, tearoff=0)
obrazmenu.add_command(label="Skalowanie")
obrazmenu.add_command(label="Zmiana jasności")
obrazmenu.add_command(label="Transformacja")
menubar.add_cascade(label="Obraz", menu=obrazmenu)

obrotmenu = Menu(obrazmenu, tearoff=0)
obrotmenu.add_command(label="Obrót o 90 stopni")
obrotmenu.add_command(label="Obrót o 180 stopni")
obrotmenu.add_command(label="Obrót o 270 stopni")
obrazmenu.add_cascade(label="Obrót", menu=obrotmenu)

funkcjemenu = Menu(menubar, tearoff=0)
funkcjemenu.add_command(label="Normalizacja histogramu")
funkcjemenu.add_command(label="Progowanie")
funkcjemenu.add_command(label="Detekcja krawędzi")
funkcjemenu.add_command(label="Szkieletyzacja")
funkcjemenu.add_command(label="Detekcja OCR")
funkcjemenu.add_command(label="Segmentacja")
funkcjemenu.add_command(label="Erozja")
funkcjemenu.add_command(label="Dylatacja")
funkcjemenu.add_command(label="Klasyfikator cech")
menubar.add_cascade(label="Funkcje", menu=funkcjemenu)

root.config(menu=menubar)
root.mainloop()
