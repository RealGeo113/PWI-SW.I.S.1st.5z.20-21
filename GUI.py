from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import project
import OCR
import filtry
import histogram
import skeletonization


def displayer(patch):
    global sourceimage
    global wyswietlacz
    global returner
    returner = patch
    sizer = patch.size
    patch.thumbnail((1280, 720), Image.ANTIALIAS)
    sourceimage = ImageTk.PhotoImage(patch)
    label = Label(root, text=sizer)
    label.grid(column=0, row=0)
    wyswietlacz = Label(image=sourceimage)
    wyswietlacz.grid(column=0, row=1)
    root.columnconfigure(0, weight=1)


def openPhoto():
    global returner
    global orginalImage
    sciezka = askopenfilename(filetypes=[("Pliki obrazów", ".png .jpg .jpe .jpeg .bmp")])
    returner = Image.open(sciezka)
    orginalImage = returner
    displayer(returner)

def doReset():
    global returner
    global orginalImage
    returner = orginalImage
    displayer(returner)


def doBLUR(source):
    filters = filtry.filtry(source, 1)
    displayer(filters)

def doCONTOUR(source):
    filters = filtry.filtry(source, 2)
    displayer(filters)


def doDETAIL(source):
    filters = filtry.filtry(source, 3)
    displayer(filters)


def doEDGE_ENHANCE(source):
    filters = filtry.filtry(source, 4)
    displayer(filters)


def doEDGE_ENHANCE_MORE(source):
    filters = filtry.filtry(source, 5)
    displayer(filters)


def doEMBOSS(source):
    filters = filtry.filtry(source, 6)
    displayer(filters)


def doFIND_EDGES(source):
    filters = filtry.filtry(source, 7)
    displayer(filters)


def doSMOOTH(source):
    filters = filtry.filtry(source, 8)
    displayer(filters)


def doSMOOTH_MORE(source):
    filters = filtry.filtry(source, 9)
    displayer(filters)


def doSHARPEN(source):
    filters = filtry.filtry(source, 10)
    displayer(filters)

def doScale(source):
    source = project.pil_to_cv(source)
    user_inp = simpledialog.askfloat(title="Test", prompt="Podaj procent skalowania (np. 110=110%)")
    user_inp = float(user_inp)
    source = project.scale_cv(source, user_inp)
    source = project.cv_to_pil(source)
    displayer(source)

def doLuminescence(source):
    user_inp = simpledialog.askfloat(title="Test", prompt="Podaj procent jasności (np. 110=110%)")
    user_inp = float(user_inp)
    source = project.luminesence(source, user_inp)
    source = project.cv_to_pil(source)
    displayer(source)

def doNegative(source):
    source = project.negative(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doGray(source):
    source = project.pil_to_cv(source)
    source = project.gray_cv(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doRotation(source, angle):
    source
    if angle == 90:
        source = project.rotate90(source)
    if angle == 180:
        source = project.rotate180(source)
    if angle == 270:
        source = project.rotate270(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doEqualization(source):
    source = project.pil_to_cv(source)
    source = histogram.histogram(source)
    displayer(source)

def doThreshold(source):
    source = project.pil_to_cv(source)
    source = project.threshold_cv(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doEdge(source):
    source = project.pil_to_cv(source)
    source = project.edges(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doOCR(source):
    source = OCR.OCR(source)
    print(source)
    messagebox.showinfo("Information", source)

def doSegmetation(source):
    source = project.pil_to_cv(source)
    source = project.color_segmentation(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doErosion(source):
    source = project.pil_to_cv(source)
    source = project.erosion(source, 1)
    source = project.cv_to_pil(source)
    displayer(source)

def doDilatation(source):
    source = project.pil_to_cv(source)
    source = project.dilatation(source, 1)
    source = project.cv_to_pil(source)
    displayer(source)

def doSkeletonization(source):
    source = project.pil_to_cv(source)
    source = skeletonization.skeletonize(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doWhiteboard(source):
    source = project.pil_to_cv(source)
    source = project.whiteboard(source)
    source = project.cv_to_pil(source)
    displayer(source)

def doTransformation(source):
    source = project.pil_to_cv(source)
    source = project.transformation(source)
    source = project.cv_to_pil(source)
    displayer(source)


root = Tk()
root.title('Skanowanie tablicy suchościeralnej')
root.geometry("1296x750")


menubar = Menu(root)
plikmenu = Menu(menubar, tearoff=0)
plikmenu.add_command(label="Otwórz obraz", command= lambda: openPhoto())
plikmenu.add_command(label="Reset", command=lambda: doReset())
plikmenu.add_separator()
plikmenu.add_command(label="Wyjdź", command=root.quit)
menubar.add_cascade(label="Plik", menu=plikmenu)

filtrmenu = Menu(menubar, tearoff=0)
filtrmenu.add_command(label="Odcienie szarosci", command=lambda: doGray(returner))
filtrmenu.add_command(label="Tranformacja do HSV", command=lambda: doTransformation(returner))
filtrmenu.add_command(label="Negatyw", command=lambda: doNegative(returner))
filtrmenu.add_separator()
filtrmenu.add_command(label="BLUR", command=lambda: doBLUR(returner))
filtrmenu.add_command(label="CONTOUR", command=lambda: doCONTOUR(returner))
filtrmenu.add_command(label="DETAIL", command=lambda: doDETAIL(returner))
filtrmenu.add_command(label="EDGE_ENHANCE", command=lambda: doEDGE_ENHANCE(returner))
filtrmenu.add_command(label="EDGE_ENHANCE_MORE", command=lambda: doEDGE_ENHANCE_MORE(returner))
filtrmenu.add_command(label="EMBOSS", command=lambda: doEMBOSS(returner))
filtrmenu.add_command(label="FIND_EDGES", command=lambda: doFIND_EDGES(returner))
filtrmenu.add_command(label="SMOOTH", command=lambda: doSMOOTH(returner))
filtrmenu.add_command(label="SMOOTH_MORE", command=lambda: doSMOOTH_MORE(returner))
filtrmenu.add_command(label="SHARPEN", command=lambda: doSHARPEN(returner))
menubar.add_cascade(label="Filtry", menu=filtrmenu)

obrazmenu = Menu(menubar, tearoff=0)
obrazmenu.add_command(label="Skalowanie", command=lambda: doScale(returner))
obrazmenu.add_command(label="Zmiana jasności", command=lambda: doLuminescence(returner))
obrazmenu.add_command(label="Transformacja")
menubar.add_cascade(label="Obraz", menu=obrazmenu)

obrotmenu = Menu(obrazmenu, tearoff=0)
obrotmenu.add_command(label="Obrót o 90 stopni", command=lambda: doRotation(returner, 90))
obrotmenu.add_command(label="Obrót o 180 stopni", command=lambda: doRotation(returner, 180))
obrotmenu.add_command(label="Obrót o 270 stopni", command=lambda: doRotation(returner, 270))
obrazmenu.add_cascade(label="Obrót", menu=obrotmenu)

funkcjemenu = Menu(menubar, tearoff=0)
funkcjemenu.add_command(label="Normalizacja histogramu", command=lambda: doEqualization(returner))
funkcjemenu.add_command(label="Progowanie", command=lambda: doThreshold(returner))
funkcjemenu.add_command(label="Detekcja krawędzi", command=lambda: doEdge(returner))
funkcjemenu.add_command(label="Szkieletyzacja", command=lambda: doSkeletonization(returner))
funkcjemenu.add_command(label="Detekcja OCR", command=lambda: doOCR(returner))
funkcjemenu.add_command(label="Segmentacja", command=lambda: doSegmetation(returner))
funkcjemenu.add_command(label="Erozja", command=lambda: doErosion(returner))
funkcjemenu.add_command(label="Dylatacja", command=lambda: doDilatation(returner))
funkcjemenu.add_command(label="Wykrywanie tablicy", command=lambda: doWhiteboard(returner))
menubar.add_cascade(label="Funkcje", menu=funkcjemenu)


root.config(menu=menubar)
root.mainloop()
