import spacy
import numpy as np
from indexer_file import Indexer
import tensorflow as tf
from data_processing import all_questions, all_questions_dict, questions_list, next_question_vectors


trained_model = tf.keras.models.load_model('trained_model.keras')

indexer=Indexer()

def predict_next(model, text_token):
  preds=np.argmax(model.predict(text_token))

  value = [i for i in all_questions_dict if all_questions_dict[i]==preds]
  return(value)

all_questions_permanent = all_questions_dict

def pop_item_by_value(dictionary, value):
    key_to_remove = None
    for key, val in dictionary.items():
        if val == value:
            key_to_remove = key
            break

    if key_to_remove is not None:
        removed_value = dictionary.pop(key_to_remove)
        return key_to_remove, removed_value
    else:
        return None, None



while True:

    l=[]

    current_question = input("Enter question: ")

    predicted_q = indexer.similarity_max(current_question, all_questions, next_question_vectors)

    if current_question=='end':
       all_questions_dict=all_questions_permanent
       break

    for i in range (0,3):
        input_token=all_questions_dict[predicted_q]
        input_arr=[]
        input_arr.append([input_token])
        input_token=np.array(input_arr)
        predicted_q= predict_next(trained_model,input_token)
        for i in predicted_q:
            predicted_q=i

            while predicted_q in l:
                input_token=all_questions_dict[predicted_q]
                input_arr=[]
                input_arr.append([input_token])
                input_token=np.array(input_arr)
                predicted_q= predict_next(trained_model,input_token)
                for i in predicted_q:
                    predicted_q=i

        print(predicted_q)
        l.append(predicted_q)