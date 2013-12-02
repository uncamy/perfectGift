import nltk

example = 'The little brown cat is on the mat!'
print example

token_example = nltk.word_tokenize(example)
print token_example

parts = nltk.pos_tag(token_example)
# sample sentences
# example sentence above
#compound noun --> boat captin or cup holder car pool etc


#take passage split into sentences
sentences = 'Next, in named entity detection, we segment and label the entities that might participate in interesting relations with one another. Typically, these will be definite noun phrases such as the knights who say "ni", or proper names such as Monty Python. In some tasks it is useful to also consider indefinite nouns or noun chunks, such as every student or cats, and these do not necessarily refer to entities in the same way as definite NPs and proper names.'




#? = 0 or 1,  * = 0 or more , += 1 or more

grammar = r"""
          NP: {<DT|PP\$>?<JJ>*<NN>}
              {<NNP>+}
"""

cp = nltk.RegexpParser(grammar)
result = cp.parse(parts)


#take sentences split into tokens
#take tag the tokens
#take tagged tokens and run the chunking
sentences = nltk.sent_tokenize(sentences)
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(words)
    result = cp.parse(tagged_tokens)
    print result

def print_things():
    print example
    print sentences
    print token_example
    print parts
    print result
