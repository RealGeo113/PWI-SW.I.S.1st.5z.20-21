from project import scale, gray, lumi


source = "./2.png"

scaled = scale(source, 2);
grayed = gray(source);
lumichange = lumi(source, 200)

scaled.show()
grayed.show()
lumichange.show()