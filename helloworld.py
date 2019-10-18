"""Variables y maneras de concatenar"""
variables_en_minuscula = "Siempre, sino no"
concat = "Hola %s" %(variables_en_minuscula)
concat2 = "Hola {}".format(variables_en_minuscula)
concat2 = "Hola {owo}".format(owo = variables_en_minuscula)
concat3 = f"Hola {variables_en_minuscula}"

"""Métodos del String"""
cadenalista = "está en minusculas"
uppercase = cadenalista.upper()
lowercase = cadenalista.lower()
titlecapitalize = cadenalista.title()
find = cadenalista.find("word")
match = cadenalista.count("essn")
replace = cadenalista.replace("testostherone", "estrogen")
split = cadenalista.split(" ") #Crea un nuevo indice dentro de un array cada vez que se encuentra con el carácter especificado como argumento
if match > 0:
	print("uwu")
print(concat + concat2 + concat3)


"""Variable comprehesion, if else conditionals"""
dick = "small"
size = "canute" if dick == "small" else "cock"