import random
from indexer_file import Indexer

indexer=Indexer()


questions_list = ["What steps are being taken to address the issue of corruption in the government?","What measures are being taken to prevent corruption?","How are these measures being implemented?","Are there any specific initiatives to reduce corruption?",
"What is the government doing to improve the economy?","What are the key economic indicators being tracked?","How are these indicators being used to inform policy decisions?","Are there any specific economic policies being implemented?",
"What is the government doing to address the issue of poverty?","What programs are being implemented to reduce poverty?","How are these programs being funded?","Are there any specific initiatives to address poverty?",
"What is the current state of the healthcare system in India?","What are the key challenges facing the healthcare system?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare?",
"What is the government doing to address the issue of education?","What programs are being implemented to improve education?","How are these programs being funded?","Are there any specific initiatives to improve education?",
"What is the current state of the infrastructure in India?","What are the key challenges facing infrastructure development?","How is the government addressing these challenges?","Are there any specific initiatives to improve infrastructure?",
"What is the government doing to address the issue of unemployment?","What programs are being implemented to reduce unemployment?","How are these programs being funded?","Are there any specific initiatives to address unemployment?",
"What is the current state of the environment in India?","What are the key environmental challenges facing the country?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental sustainability?",
"What is the government doing to address the issue of women's empowerment?","What programs are being implemented to empower women?","How are these programs being funded?","Are there any specific initiatives to promote women's empowerment?",
"What is the current state of the agricultural sector in India?","What are the key challenges facing the agricultural sector?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural productivity?",
"What is the government doing to address the issue of national security?","What measures are being taken to ensure national security?","How are these measures being implemented?","Are there any specific initiatives to improve national security?",
"What is the current state of the Indian economy in terms of GDP growth?","What are the key drivers of GDP growth?","How is the government addressing the challenges to GDP growth?","Are there any specific initiatives to boost GDP growth?",
"What is the government doing to address the issue of income inequality?","What programs are being implemented to reduce income inequality?","How are these programs being funded?","Are there any specific initiatives to address income inequality?",
"What is the current state of the Indian education system in terms of literacy rates?","What are the key challenges facing the education system?","How is the government addressing these challenges?","Are there any specific initiatives to improve literacy rates?",
"What is the government doing to address the issue of rural development?","What programs are being implemented to improve rural development?","How are these programs being funded?","Are there any specific initiatives to address rural development?",
"What is the current state of the Indian healthcare system in terms of access to healthcare?","What are the key challenges facing access to healthcare?","How is the government addressing these challenges?","Are there any specific initiatives to improve access to healthcare?",
"What is the government doing to address the issue of urbanization?","What programs are being implemented to address urbanization?","How are these programs being funded?","Are there any specific initiatives to address urbanization?",
"What is the current state of the Indian environment in terms of pollution?","What are the key environmental challenges facing the country?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental sustainability?",
"What is the government doing to address the issue of climate change?","What programs are being implemented to address climate change?","How are these programs being funded?","Are there any specific initiatives to address climate change?",
"What is the current state of the Indian agricultural sector in terms of crop yields?","What are the key challenges facing crop yields?","How is the government addressing these challenges?","Are there any specific initiatives to improve crop yields?",
"What is the government doing to address the issue of agricultural subsidies?","What programs are being implemented to address agricultural subsidies?","How are these programs being funded?","Are there any specific initiatives to address agricultural subsidies?",
"What is the current state of the Indian education system in terms of student enrollment?","What are the key challenges facing student enrollment?","How is the government addressing these challenges?","Are there any specific initiatives to improve student enrollment?",
"What is the government doing to address the issue of education for all?","What programs are being implemented to achieve education for all?","How are these programs being funded?","Are there any specific initiatives to achieve education for all?",
"What is the current state of the Indian healthcare system in terms of healthcare infrastructure?","What are the key challenges facing healthcare infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare infrastructure?",
"What is the government doing to address the issue of healthcare for all?","What programs are being implemented to achieve healthcare for all?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare for all?",
"What is the current state of the Indian environment in terms of waste management?","What are the key environmental challenges facing waste management?","How is the government addressing these challenges?","Are there any specific initiatives to improve waste management?",
"What is the government doing to address the issue of environmental sustainability?","What programs are being implemented to achieve environmental sustainability?","How are these programs being funded?","Are there any specific initiatives to achieve environmental sustainability?",
"What is the current state of the Indian agricultural sector in terms of agricultural productivity?","What are the key challenges facing agricultural productivity?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural productivity?",
"What is the government doing to address the issue of agricultural development?","What programs are being implemented to achieve agricultural development?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural development?",
"What is the current state of the Indian education system in terms of teacher training?","What are the key challenges facing teacher training?","How is the government addressing these challenges?","Are there any specific initiatives to improve teacher training?",
"What is the government doing to address the issue of teacher training?","What programs are being implemented to achieve teacher training?","How are these programs being funded?","Are there any specific initiatives to achieve teacher training?",
"What is the current state of the Indian healthcare system in terms of healthcare services?","What are the key challenges facing healthcare services?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare services?",
"What is the government doing to address the issue of healthcare services?","What programs are being implemented to achieve healthcare services?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare services?",
"What is the current state of the Indian environment in terms of environmental conservation?","What are the key environmental challenges facing environmental conservation?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental conservation?",
"What is the government doing to address the issue of environmental conservation?","What programs are being implemented to achieve environmental conservation?","How are these programs being funded?","Are there any specific initiatives to achieve environmental conservation?",
"What is the current state of the Indian agricultural sector in terms of agricultural research?","What are the key challenges facing agricultural research?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural research?",
"What is the government doing to address the issue of agricultural research?","What programs are being implemented to achieve agricultural research?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural research?",
"What is the current state of the Indian education system in terms of education for all?","What are the key challenges facing education for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve education for all?",
"What is the government doing to address the issue of education for all?","What programs are being implemented to achieve education for all?","How are these programs being funded?","Are there any specific initiatives to achieve education for all?",
"What is the current state of the Indian healthcare system in terms of healthcare for all?","What are the key challenges facing healthcare for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve healthcare for all?",
"What is the government doing to address the issue of healthcare for all?","What programs are being implemented to achieve healthcare for all?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare for all?",
"What is the current state of the Indian environment in terms of environmental sustainability?","What are the key environmental challenges facing environmental sustainability?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental sustainability?",
"What is the government doing to address the issue of environmental sustainability?","What programs are being implemented to achieve environmental sustainability?","How are these programs being funded?","Are there any specific initiatives to achieve environmental sustainability?",
"What is the current state of the Indian agricultural sector in terms of agricultural development?","What are the key challenges facing agricultural development?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural development?",
"What is the government doing to address the issue of agricultural development?","What programs are being implemented to achieve agricultural development?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural development?",
"What is the current state of the Indian education system in terms of education infrastructure?","What are the key challenges facing education infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve education infrastructure?",
"What is the government doing to address the issue of education infrastructure?","What programs are being implemented to achieve education infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve education infrastructure?",
"What is the current state of the Indian healthcare system in terms of healthcare infrastructure?","What are the key challenges facing healthcare infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare infrastructure?",
"What is the government doing to address the issue of healthcare infrastructure?","What programs are being implemented to achieve healthcare infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare infrastructure?",
"What is the current state of the Indian environment in terms of environmental conservation?","What are the key environmental challenges facing environmental conservation?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental conservation?",
"What is the government doing to address the issue of environmental conservation?","What programs are being implemented to achieve environmental conservation?","How are these programs being funded?","Are there any specific initiatives to achieve environmental conservation?",
"What is the current state of the Indian agricultural sector in terms of agricultural productivity?","What are the key challenges facing agricultural productivity?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural productivity?",
"What is the government doing to address the issue of agricultural productivity?","What programs are being implemented to achieve agricultural productivity?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural productivity?",
"What is the current state of the Indian education system in terms of education for all?","What are the key challenges facing education for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve education for all?",
"What is the government doing to address the issue of education for all?","What programs are being implemented to achieve education for all?","How are these programs being funded?","Are there any specific initiatives to achieve education for all?",
"What is the current state of the Indian healthcare system in terms of healthcare for all?","What are the key challenges facing healthcare for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve healthcare for all?",
"What is the government doing to address the issue of healthcare for all?","What programs are being implemented to achieve healthcare for all?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare for all?",
"What is the current state of the Indian environment in terms of environmental sustainability?","What are the key environmental challenges facing environmental sustainability?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental sustainability?",
"What is the government doing to address the issue of environmental sustainability?","What programs are being implemented to achieve environmental sustainability?","How are these programs being funded?","Are there any specific initiatives to achieve environmental sustainability?",
"What is the current state of the Indian agricultural sector in terms of agricultural development?","What are the key challenges facing agricultural development?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural development?",
"What is the government doing to address the issue of agricultural development?","What programs are being implemented to achieve agricultural development?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural development?",
"What is the current state of the Indian education system in terms of education infrastructure?","What are the key challenges facing education infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve education infrastructure?",
"What is the government doing to address the issue of education infrastructure?","What programs are being implemented to achieve education infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve education infrastructure?",
"What is the current state of the Indian healthcare system in terms of healthcare infrastructure?","What are the key challenges facing healthcare infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare infrastructure?",
"What is the government doing to address the issue of healthcare infrastructure?","What programs are being implemented to achieve healthcare infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare infrastructure?",
"What is the current state of the Indian environment in terms of environmental conservation?","What are the key environmental challenges facing environmental conservation?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental conservation?",
"What is the government doing to address the issue of environmental conservation?","What programs are being implemented to achieve environmental conservation?","How are these programs being funded?","Are there any specific initiatives to achieve environmental conservation?",
"What is the current state of the Indian agricultural sector in terms of agricultural productivity?","What are the key challenges facing agricultural productivity?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural productivity?",
"What is the government doing to address the issue of agricultural productivity?","What programs are being implemented to achieve agricultural productivity?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural productivity?",
"What is the current state of the Indian education system in terms of education for all?","What are the key challenges facing education for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve education for all?",
"What is the government doing to address the issue of education for all?","What programs are being implemented to achieve education for all?","How are these programs being funded?","Are there any specific initiatives to achieve education for all?",
"What is the current state of the Indian healthcare system in terms of healthcare for all?","What are the key challenges facing healthcare for all?","Are there any specific initiatives to achieve healthcare for all?",
"What is the current state of the Indian environment in terms of environmental sustainability?","What are the key environmental challenges facing environmental sustainability?","How is the government addressing these challenges?","Are there any specific initiatives to achieve healthcare for all?",
"What is the government doing to address the issue of healthcare for all?","What programs are being implemented to achieve healthcare for all?","How are these programs being funded?","A the government addressing these challenges?","Are there any specific initiatives to improve environmental sustainability?",
"What is the government doing to address the issue of environmental sustainability?","What programs are being implemented to achieve environmental sustainability?","How are these programs being funded?","Are there any specific initiatives to achieve environmental sustainability?",
"What is the current state of the Indian agricultural sector in terms of agricultural development?","What are the key challenges facing agricultural development?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural development?",
"What is the government doing to address the issue of agricultural development?","What programs are being implemented to achieve agricultural development?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural development?",
"What is the current state of the Indian education system in terms of education infrastructure?","What are the key challenges facing education infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve education infrastructure?",
"What is the government doing to address the issue of education infrastructure?","What programs are being implemented to achieve education infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve education infrastructure?",
"What is the current state of the Indian healthcare system in terms of healthcare infrastructure?","What are the key challenges facing healthcare infrastructure?","How is the government addressing these challenges?","Are there any specific initiatives to improve healthcare infrastructure?",
"What is the government doing to address the issue of healthcare infrastructure?","What programs are being implemented to achieve healthcare infrastructure?","How are these programs being funded?","Are there any specific initiatives to achieve healthcare infrastructure?",
"What is the current state of the Indian environment in terms of environmental conservation?","What are the key environmental challenges facing environmental conservation?","How is the government addressing these challenges?","Are there any specific initiatives to improve environmental conservation?",
"What is the government doing to address the issue of environmental conservation?","What programs are being implemented to achieve environmental conservation?","How are these programs being funded?","Are there any specific initiatives to achieve environmental conservation?",
"What is the current state of the Indian agricultural sector in terms of agricultural productivity?","What are the key challenges facing agricultural productivity?","How is the government addressing these challenges?","Are there any specific initiatives to improve agricultural productivity?",
"What is the government doing to address the issue of agricultural productivity?","What programs are being implemented to achieve agricultural productivity?","How are these programs being funded?","Are there any specific initiatives to achieve agricultural productivity?",
"What is the current state of the Indian education system in terms of education for all?","What are the key challenges facing education for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve education for all?",
"What is the government doing to address the issue of education for all?","What programs are being implemented to achieve education for all?","How are these programs being funded?","Are there any specific initiatives to achieve education for all?",
"What is the current state of the Indian healthcare system in terms of healthcare for all?","What are the key challenges facing healthcare for all?","How is the government addressing these challenges?","Are there any specific initiatives to achieve healthcare for all?"]


question=[]
follow1=[]
follow2=[]
follow3=[]
for i in range (len(questions_list)):
    a=i%4
    if a==1:
        question.append(questions_list[i])
    elif a==2:
        follow1.append(questions_list[i])
    elif a==3:
        follow2.append(questions_list[i])
    else:
        follow3.append(questions_list[i])

#indexing
all_questions=question+follow1+follow2+follow3
unique_questions = []
for ele in all_questions:
    if ele not in unique_questions:
        unique_questions.append(ele)

all_questions=unique_questions

random.shuffle(all_questions)

all_questions_dict={}
for i in range(len(all_questions)):
    all_questions_dict.update({all_questions[i]: i+1})

#making training data
q= []
f1= []
f2= []
f3= []

for i in range (len(question)):
    q.append(all_questions_dict[question[i]])

for i in range (len(follow1)):
    f1.append(all_questions_dict[follow1[i]])

for i in range (len(follow2)):
    f2.append(all_questions_dict[follow2[i]])

for i in range (len(follow3)):
    f3.append(all_questions_dict[follow3[i]])


next_question_vectors=[indexer.get_vector(text) for text in questions_list]