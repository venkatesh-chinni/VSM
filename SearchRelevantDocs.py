# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:47:39 2018

@author: C.Grandhi
"""


def SearchEngine(query):
    import re
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    
    
    with open('Docs/lotr.txt','r') as myfile:
        data1=myfile.read()
    
    with open('Docs/rainbows_end.txt','r') as myfile:
        data2=myfile.read()
                
    with open('Docs/silmarillion.txt','r') as myfile:
        data3=myfile.read()
                 
    with open('Docs/the_hobbit.txt','r') as myfile:
        data4=myfile.read()
           
    
    
 #   data = [data1,data2,data3,data4,query]
    
    data = {
            0:data1,
            1:data2,
            2:data3,
            3:data4,
            4:query,
            }
    
    
    finalCorpus = []
    
    for i in range(0,5):
        review = re.sub('[^a-zA-Z]', ' ', data[i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        finalCorpus.append(review)
    
    
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(finalCorpus)
    
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_index = cosine_similarity(tfidf_matrix[4], tfidf_matrix[0:4])
    return similarity_index
    
SearchEngine('fiction')
     
