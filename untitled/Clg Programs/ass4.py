import nltk

stopwords = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same',"shan't",'she',"she'd","she'll","she's",'should',"shouldn't",'so','some','such','than','that',"that's",'the','their','theirs','them','themselves','then','there',"there's",'they',"they'd","they'll","they're","they've",'this','those','through','to','too','under','until','up','very','was',"wasn't",'we',"we'd","we'll","we're","we've",'were',"weren't",'what',"what's",'when',"when's",'where',"where's",'which','while','who',"who's",'whom','why',"why's",'with',"won't",'would',"wouldn't",'you',"you'd","you'll","you're","you've",'your','yours','yourself','yourselves']
print("What is answer for given Question: short note on python?\n")

ans=input("Enter Answer:\n")

data1=open('model.txt','r')
list1=data1.read()

tokenizer = nltk.RegexpTokenizer(r"\w+")
w1 = tokenizer.tokenize(list1)
w2 = tokenizer.tokenize(ans)


w11=[]
w22=[]
for word in w1:
    if word not in stopwords:
        w11.append(word)
for word in w2:
    if word not in stopwords:
        w22.append(word)

print()
print("After tokenize, punctuation and stopwords removal: ")
print("model answer: ",w11)
print()
print("student answer: ",w22)

#lemmatizer on words (verbs)
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
print()
print("After lemmatization: ")
w11lem=[]
for w in w11:
    w11lem.append(lem.lemmatize(w, "v") )
print("model answer: ",w11lem)
print()
w22lem=[]
for w in w22:
    w22lem.append(lem.lemmatize(w, "v") )
print("student answer: ",w22lem)


w1122=[]
for word in w22lem:
    if word in w11lem:
        w1122.append(word)


a=len(w1122)
b=len(w11lem)
c=a/b*100
print()
print("Percentage of correctness is ",c)