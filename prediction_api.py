import uvicorn
from prediction_api import FastAPI
import numpy as np
import pickle
import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from model.py import all_questions, all_questions_dict, questions_list

app = FastAPI()

pickle_in = open('trained_model.pkl')
trained_model=pickle.load(pickle_in)

nlp = spacy.load("en_core_web_lg")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    return " ".join(tokens)

def get_vector(text):
  preprocessed_text = preprocess_text(text)
  return nlp(preprocessed_text).vector

next_question_vectors=[get_vector(text) for text in questions_list]

def model1(current_question, questions, question_vectors):
  current_question_vector = get_vector(current_question)
  similarity = cosine_similarity([current_question_vector], question_vectors)[0]

  dictionary = dict (zip(similarity,questions))

  similarity = np.sort(similarity)
  similarity = similarity[::-1]

  key=similarity[0]
  input_q= dictionary[key]

  if similarity[0] >= 0.5:
    return input_q
  else:
    return None

all_questions_permanent=all_questions_dict

@app.get('/')
def index():
    return{'message':'Hello, World'}


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to the Chatbot ' : f'{name}' }

@app.post('/predict')
def predict_text(current_question:str):

    while True:

        l_q_asked=[]

        predicted_q = model1(current_question, all_questions, next_question_vectors)

        if current_question=='end':
            all_questions_dict=all_questions_permanent
            break

        if predicted_q != None:
            for i in range (0,3):
                input_token=all_questions_dict[predicted_q]
                input_arr=[]
                input_arr.append([input_token])
                input_token=np.array(input_arr)
                prediction_arr=(trained_model.predict(input_token))
                prediction=np.argmax(prediction_arr)
                predicted_q = [i for i in all_questions_dict if all_questions_dict[i]==prediction]
                for i in predicted_q:
                    predicted_q=i

                while predicted_q in l_q_asked:
                    input_token=all_questions_dict[predicted_q]
                    input_arr=[]
                    input_arr.append([input_token])
                    input_token=np.array(input_arr)
                    prediction_arr=(trained_model.predict(input_token))
                    prediction=np.argmax(prediction_arr)
                    predicted_q = [i for i in all_questions_dict if all_questions_dict[i]==prediction]
                    for i in predicted_q:
                        predicted_q=i

            l_q_asked.append(predicted_q)
            return {
                'prediction' : predicted_q
            }
        else:
            print('ERROR: Enter a relevant question!')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

