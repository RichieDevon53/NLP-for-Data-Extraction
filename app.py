import customtkinter
import pickle
import numpy as np
from tensorflow.keras.utils import pad_sequences
from keras.models import load_model

# Load model dan tokenizer 
model = load_model('model.h5')
with open('tokenizer.pickle', 'rb') as file1:
    tokenizer = pickle.load(file1)

# Fungsi prediksi
def predict(sentence):
    '''
    Param :
        - Sentence : Kalimat yang ingin dilakukan extraksi data
    Return Value : 
        - tag_dict : Hasil extraksi data berupa jumlah barang, nama barang, motif dan lokasi
    '''
    
    tag_dict = {"JUMLAH BARANG": [], "NAMA BARANG": [], "MOTIF": [], "LOKASI": []}
    label_map = {"O": 0, "JUMLAH BARANG": 1, "NAMA BARANG": 2, "MOTIF": 3, "LOKASI": 4}
    
    tokens = sentence.split()
    sequence = tokenizer.texts_to_sequences([sentence])
    sequence_padded = pad_sequences(sequence, maxlen=20, padding='post')
    predictions = model.predict(sequence_padded)[0]
    predicted_tags = [list(label_map.keys())[np.argmax(tag)] for tag in predictions[:len(tokens)]]
    
    for token, tag in zip(tokens, predicted_tags):
        if tag in tag_dict:
            tag_dict[tag].append(token)
    return tag_dict

# Fungsi button akan prediksi 
def button_callback():
    input_words = entry.get()
    tags = predict(input_words)
    label_1.configure(text=f"JUMLAH BARANG: {tags['JUMLAH BARANG']}")
    label_2.configure(text=f"NAMA BARANG: {tags['NAMA BARANG']}")
    label_3.configure(text=f"MOTIF: {tags['MOTIF']}")
    label_4.configure(text=f"LOKASI: {tags['LOKASI']}")

# Pembuatan layout Tkinter
app = customtkinter.CTk()
app.title("Data Extractor")
app.geometry("450x320")
app.grid_columnconfigure(0, weight=1)

# Pembuatan Title, entry, label, button dan lain-lain
title_label = customtkinter.CTkLabel(app, text="Data Extractor", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, padx=20, pady=(10,0))

subtitle_label = customtkinter.CTkLabel(app, text="Kalimat akan dilakukan ektraksi data menggunakan model Deep Learning", font=("Arial", 12))
subtitle_label.grid(row=1, column=0, padx=20)

entry = customtkinter.CTkEntry(app, placeholder_text="Masukkan sebuah kalimat")
entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

button = customtkinter.CTkButton(app, text="Extract Data", command=button_callback)
button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

label_1 = customtkinter.CTkLabel(app, text="", font=("Arial", 14, "bold"))
label_1.grid(row=4, column=0, padx=20, pady=3, sticky="ew")

label_2 = customtkinter.CTkLabel(app, text="", font=("Arial", 14, "bold"))
label_2.grid(row=5, column=0, padx=20, pady=3, sticky="ew")

label_3 = customtkinter.CTkLabel(app, text="", font=("Arial", 14, "bold"))
label_3.grid(row=6, column=0, padx=20, pady=3, sticky="ew")

label_4 = customtkinter.CTkLabel(app, text="", font=("Arial", 14, "bold"))
label_4.grid(row=7, column=0, padx=20, pady=3, sticky="ew")

app.mainloop()
