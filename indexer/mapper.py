#!/bin/python3

import sys

def term_frequency(term, document):
    # Count occurrences of term in document
    term_count = document.count(term)
    # Total number of terms in document
    total_terms = len(document)
    # Return term frequency
    return term_count / total_terms if total_terms > 0 else 0

def inverse_document_frequency(term, corpus):
    # Number of documents containing term
    doc_count = sum(1 for document in corpus if term in document)
    # Return inverse document frequency
    return doc_count

def tf_idf(term_id, document, corpus):
    term = id_to_word[term_id]
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term, corpus)
    return tf * idf

docs = []
for line in sys.stdin:
    corpus = []
    
    # Create a mapping from words to unique integers
    word_to_id = {word: i for i, word in enumerate(set(word for doc in corpus for word in doc))}
    id_to_word = {i: word for word, i in word_to_id.items()}

    # Calculate TF-IDF for each term in each document
    tfidf_scores = []
    for doc_index, document in enumerate(corpus):
        doc_tfidf = []
        for word in set(document):
            term_id = word_to_id[word]
            tfidf = tf_idf(term_id, document, corpus)
            doc_tfidf.append((term_id, tfidf))
        tfidf_scores.append(doc_tfidf)

    # Print TF-IDF scores for each term in each document
    for doc_index, doc_tfidf in enumerate(tfidf_scores):
        print(f"Document {doc_index + 1}:")
        for term_id, score in doc_tfidf:
            print(f"  Term '{id_to_word[term_id]}' (ID: {term_id}): TF-IDF = {score}")
