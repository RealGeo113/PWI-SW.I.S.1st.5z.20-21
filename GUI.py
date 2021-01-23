from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Skanowanie tablicy suchościeralnej')

menubar = Menu(root)
plikmenu = Menu(menubar, tearoff=0)
plikmenu.add_command(label="Otwórz obraz")
plikmenu.add_command(label="Resetuj obraz")
plikmenu.add_command(label="Zapisz obraz")
plikmenu.add_separator()
plikmenu.add_command(label="Wyjdź", command=root.quit)
menubar.add_cascade(label="Plik", menu=plikmenu)

filtrmenu = Menu(menubar, tearoff=0)
filtrmenu.add_command(label="Odcienie szarosci")
filtrmenu.add_command(label="Negatyw")
filtrmenu.add_separator()
filtrmenu.add_command(label="BLUR")
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
