# import tkinter as tk
# from tkinter import filedialog
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
# import pickle
import numpy as np
import os
# import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# import joblib

from data_processing import f1,f2,f3,q


# def upload_file():
#     # Create a root window and hide it
#     root = tk.Tk()
#     root.withdraw()

#     # Prompt the user to select a file
#     file_path = filedialog.askopenfilename()

#     # If a file was selected
#     if file_path:
#         try:
#             with open(file_path, 'r') as file:
#                 data = file.read()

#             # Process the file content
#             all_questions, all_questions_dict, questions_list=model_train(data)
#         except Exception as e:
#             print(f"Error reading file: {e}")
#     else:
#         print("No file selected")
#     return all_questions, all_questions_dict

def model_train(f1,f2,f3,q):
    #prepping data
    # data = data.replace('"', '').replace('\n', '')
    # questions_list = data.split(',')
    # print(questions_list[:5])

    #segregating dataset

    input_id=[]
    output_id=[]

    min_v=min(len(f1),len(f2),len(f3))

    for j in range (4):
        for i in range (min_v):
            id=[]
            id.append(f1[i])
            id.append(f2[i])
            id.append(f3[i])
            input_id.append(id)


        for i in range (min_v):
            id=[]
            output_id.append(q[i])

        c=q
        q=f1
        f1=f2
        f2=f3
        f3=c


    total_q=q+f1+f2+f3
    unique_questions = []
    for ele in total_q:
        if ele not in unique_questions:
            unique_questions.append(ele)

    total_q=unique_questions
    output_size = len(total_q) +1

    X=input_id
    y=output_id

    X = np.array(X)
    y = np.array(y)

    y= to_categorical(y, num_classes= output_size)

    #MODEL
    model = Sequential()
    model.add(Embedding(output_size, 10, input_length=3))
    model.add(LSTM(1000, return_sequences=True))
    model.add(LSTM(1000))
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(output_size, activation='softmax'))

    model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))
    model.fit(X, y, epochs=2, batch_size=64)

    #Model Training
    model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))
    model.fit(X, y, epochs=20, batch_size=64)

    model.evaluate(X,y)
    model.save('trained_model.keras')



# if __name__ == "__main__":
#     all_questions, all_questions_dict, questions_list=model_train(questions_list)

# all_questions = all_questions
# all_questions_dict = all_questions_dict
# questions_list = questions_list
model_train(f1,f2,f3,q)