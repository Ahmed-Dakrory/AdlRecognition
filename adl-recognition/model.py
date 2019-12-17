from keras.models import model_from_json
import os.path
import zipfile

def getModel(path):
    if not(os.path.isfile(path+'.h5') or os.path.isfile(path+'.json')):
        zip = zipfile.ZipFile(path+'.zip')
        zip.extractall()
    json_file = open(path+'.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    # load weights into new model
    model.load_weights(path+".h5")
    return model
