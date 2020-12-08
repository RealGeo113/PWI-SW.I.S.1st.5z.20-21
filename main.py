import project


source = input("Enter path to image: ")

scaled = project.scale(source, 2)
grayed = project.gray(source)
luminesence = project.lumi(source, 200)
negative = project.negative(source)

scaled.show()
grayed.show()
luminesence.show()
negative.show()
