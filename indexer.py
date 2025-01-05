from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np

nlp = spacy.load("en_core_web_lg")

class Indexer():

    def preprocess_text(self,text):
        doc = nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]
        return " ".join(tokens)

    def get_vector(self,text):
        preprocessed_text = self.preprocess_text(text)
        return nlp(preprocessed_text).vector

    def similarity_max(self,current_question, questions, question_vectors):
        current_question_vector = self.get_vector(current_question)
        similarity = cosine_similarity([current_question_vector], question_vectors)[0]

        dictionary = dict (zip(similarity,questions))

        similarity = np.sort(similarity)
        similarity = similarity[::-1]

        key=similarity[0]
        input_q= dictionary[key]
        return input_q

