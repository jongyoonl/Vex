from os.path import join
from os import listdir
from uuid import uuid4
from PIL import Image, ImageDraw
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
import pickle
import numpy as np
import base64

flagpath = "../static/flags"
outputpath = "../static/data"
datapath = "../static/data.pickle"
training = "training"
abspath = "/Users/jongyoonlee/Documents/Projects/Vex/Vex/backend/"
test = "test"
numtraining = 1170
numtest = 48
num_classes = 195

size = (60, 60)

def main():
    createImages()
    createData()

def generateId():
    return str(uuid4())[-12:]

def createImages():

    labeldict, _ = csvToDicts("../static/countries.csv")
    labelfile = open("../static/training.csv", "w+")
    labelfile.write("Id,Label\n")

    for filename in listdir(flagpath):

        country, _ = filename.split(".")
        label = labeldict[country]

        try:
            image = Image.open(join(flagpath, filename))
            image.close()
        except OSError:
            continue

        for width in range(1, 4):

            image = Image.open(join(flagpath, filename)).convert("RGB").resize(size)
            draw = ImageDraw.ImageDraw(image, mode="RGB")
            fileid0 = generateId()

            for i in range(size[0] // width // 2):
                draw.line((0, width * 2 * i, size[0], width * 2 * i), fill="white", width=width)
            with open(join(outputpath, training, fileid0 + ".png"), "wb+") as file:
                image.save(file, "PNG")
            image.close()

            image = Image.open(join(flagpath, filename)).convert("RGB").resize(size)
            draw = ImageDraw.ImageDraw(image, mode="RGB")
            fileid1 = generateId()

            for i in range(size[1] // width // 2):
                draw.line((width * 2 * i, 0, width * 2 * i, size[1]), fill="white", width=width)
            with open(join(outputpath, training, fileid1 + ".png"), "wb+") as file:
                image.save(file, "PNG")
            image.close()

            labelfile.write(fileid0 + "," + str(label) + "\n")
            labelfile.write(fileid1 + "," + str(label) + "\n")


    labelfile.close()

def createData():

    traindict, _ = csvToDicts("../static/training.csv")
    testdict, _ = csvToDicts("../static/test.csv")

    x_train = np.zeros((numtraining,) + size + (3,))
    i = 0
    y_train = [0] * numtraining

    for filename in listdir(join(outputpath, training)):
        try: 
            image = Image.open(join(outputpath, training, filename))
            x_train[i] = np.array(image)
            image.close()
            id, _ = filename.split(".")
            y_train[i] = int(traindict[id])
            i += 1
        except OSError:
            continue

    x_test = np.zeros((numtest,) + size + (3,))
    i = 0
    y_test = [0] * numtest

    for filename in listdir(join("../static", "images")):
        try:
            image = Image.open(join("../static", "images", filename)).convert("RGB").resize(size)
            x_test[i] = np.array(image)
            image.close()
            id, _ = filename.split(".")
            y_test[i] = int(testdict[id])
            i += 1
        except OSError:
            continue

    with open(datapath, "wb+") as ofile:
        pickle.dump(((x_train, y_train), (x_test, y_test)), ofile)

def csvToDicts(csvpath, outpath=None):

    kvdict = {}
    vkdict = {}

    with open(csvpath, "r") as csvfile:
        csvfile.readline()
        for line in csvfile.readlines():
            key, value = line.strip().split(",")
            kvdict[key] = value
            vkdict[value] = key

    if outpath:
        with open(outpath, "wb+") as ofile:
            pickle.dump((kvdict, vkdict), ofile)
    else:
        return (kvdict, vkdict)

def reverseDict(dictionary):

    newdic = {}
    
    for key in dictionary:
        newdic[dictionary[key]] = key

    return newdic

def listToJsonDict(predictions):

    jsondict = {}

    with open(abspath + "static/labels.pickle", "rb") as file:
        dic = reverseDict(pickle.load(file))
        for i in range(len(predictions)):
            country = dic[predictions[i]]
            with open(abspath + join("static", "flags", country + ".png"), "rb") as flagfile:
                jsondict["sugg" + str(i)] = str(base64.standard_b64encode(flagfile.read()))
                jsondict["tag" + str(i)] = country.replace(" ", "_")

    return jsondict


def loadData():

    with open(datapath, "rb") as dfile:
        return pickle.load(dfile)

if __name__ == "__main__":
    main()
