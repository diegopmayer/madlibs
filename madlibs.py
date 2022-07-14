
# Importing Libraries
from random import choice as rd


class MadLibs:
    def __init__(self):
        pass


    def bag_of_words(self):
        # loading words
        # loading all words to compose with the text
        adj = open('bag_of_words/adjectives.txt', 'r').read().split()
        body = open('bag_of_words/bodies.txt', 'r').read().split()
        pl_noun = (open('bag_of_words/plural_nouns.txt', 'r')
                    .read().replace(',', '').split())
        sg_noun = open('bag_of_words/sg_nouns.txt', 'r').read().split()
        verb = open('bag_of_words/verbs.txt', 'r').read().split()

        # creating a "bag of words" as "bw" to be used into the text
        bw = {'adj': adj, 'body': body, 'pl_noun': pl_noun, 
            'sg_noun': sg_noun, 'verb': verb}

        return bw
    

    def building_madlibs(self, bw):
        madlibs_text = f"""
        I love data science because it's {rd(bw['adj'])}! The journey to becoming a
        good data scientist starts with hope in your mind and a dream in your {rd(bw['body'])}. Through blood,
        sweat, and {rd(bw['pl_noun'])}, hopefully it never ends. Yes, once you learn to {rd(bw['verb'])}, it becomes
        a part of your life identity and you can become a super {rd(bw['adj'])} data professional. Knowledge of statistics
        lets you take control of your {rd(bw['sg_noun'])}. You can create your own personal {rd(bw['pl_noun'])}, anything
        from developing {rd(bw['adj'])} data solutions to analyzing data and making predictions about the {rd(bw['sg_noun'])}. 
        You can maybe even recreate currency prediction or profit prediction and make him extra {rd(bw['adj'])}. 
        I hope you'll start your {rd(bw['adj'])} journey by coding studying statistics, SQL and python with me :)\n"""

        return madlibs_text

    
    def madlibs_output(self, text):
        with open('madlibs_text.txt', 'w') as file:
            file.write(text)
        print(open('madlibs_text.txt', 'r').read())
