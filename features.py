import librosa
import numpy as np
import joblib
import train_formants
import train_spectral_centroid 
import train_prosody
import train_amplitude_envelope

def form(path):
    svm_model = joblib.load('svm_model_formants.pkl')
    formants = train_formants.extract_formants(path)

    formants = np.array(formants).reshape(1, -1) 
    if svm_model.predict(formants) == 1:
        i=1
    else:
        i=0

    return(i)

def spec_centroid(path):
    features = train_spectral_centroid.extract_features(path)

    model = joblib.load('spec_centroid.joblib')


    prediction = model.predict([features])[0]

    if prediction=="machine":
        a=1
    else:a=0
    return a


def mfc(path):
    svm_model = joblib.load('svm_model_mfcc.pkl')

    y, sr = librosa.load(path,sr=None)

    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    mfcc_mean = np.mean(mfcc, axis=1)

    feature_vector = np.concatenate((mfcc_mean.reshape(20,1)))

    if svm_model.predict([feature_vector])[0] == 1:
        a=1
    else:
        a=0
    return(a)

def prosody(path):
    features = train_prosody.extract_features(path)

    model = joblib.load('prosody_1.joblib')

    prediction = model.predict([features])[0]

    if prediction=="machine":
        a=1
    else:a=0
    return a


def amplitude_env(path):
    svm_model = joblib.load('svm_model_amp_envelope.pkl')
    enve = train_amplitude_envelope.extract_amplitude_envelope(path)

    enve = np.array(enve).reshape(1, -1) 
    if svm_model.predict(enve) == 1:
        i=1
    else:
        i=0
    
    return(i)

def spec_flux(path):
    model = joblib.load('spectral_flux.joblib')

    y, sr = librosa.load(path)
    max_length=model.coef_.shape[1]
    spectral_flux = librosa.onset.onset_strength(y=y, sr=sr)
    pad_width = max_length - len(spectral_flux)
    padded_flux = np.pad(spectral_flux, (0, pad_width), mode='constant')

    prediction = model.predict(padded_flux.reshape(1, -1))[0]


    if prediction == "machine":
        a = 1
    else:
        a = 0

    return a
