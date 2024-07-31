import benepar, nltk, spacy
import ssl
subjects = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]

tests = {
	"je manger une pomme": ["je"],
	"tu manger une pomme": ["tu"],
	"leurs avions voler de paris": ["ils"],
	"marc et luis manger une pomme": ["ils"],
	"mon fils voler une pomme": ["il"],
	"marc et luis manger des pommes et vous manger des bananes": ["ils", "vous"],
	"je aller manger une pomme": ["je"],
	"marc et luis aller manger des pommes": ["ils"],
	"ma famille et moi aller manger une pomme ce soir": ["nous"],
	"il aller manger des oranges que boire de l'eau": ["il", "ils"],
	"Romaine et Cristophe choisir un vol air france": ["ils"],
	"quand Romaine faire enregistrer ses bagages, il choisir aussi sa place": ["il", "il"],
	"pendant le voyage, les deux garçons avoir faim. Ils finir tout leur repas": ["ils", "ils"],
	"après, ils remplir leur carte de débarquement": ["ils"],
	"leur avion atterir à new york à 2 h 45": ["il"],
	"on vendre des billets de train au guichet": ["il"],
	"les voyageurs attendre dans la salle d'attente": ["ils"],
	"je entendre l'annonce du départ de notre train": ["je"],
	"nous perdre patience quand le train du retard": ["nous"],
	"le contrôleur répondre aux questions des voyageurs": ["il"],
	"vous descendre à quell arrêt": ["vous"],
	"moi, je descendre à toulouse": ["je"]
}

# Used to download language models
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# benepar.download('benepar_fr2') # French Model

parser = benepar.Parser("benepar_fr2")
nlp = spacy.load('fr_core_news_lg')

# if spacy.__version__.startswith('2'):
#     nlp.add_pipe(benepar.BeneparComponent("benepar_fr2"))
# else:
#     nlp.add_pipe("benepar", config={"model": "benepar_fr2"})
# def subconvert(tree):
# 	print(tree)
# 	subs = []
# 	if len(tree) > 1:

# 		for i in tree:
# 			if i.label() == "COORD":
# 				subs.append(subconvert(i[1]))
# 			else:
# 				subs.append(i[0])
# 	else:
# 		return None
# 	if "moi" in subs or "nous" in subs:
# 		return "nous"
# 	if "toi" in subs or "vous" in subs:
# 		return "vous"
# 	if len(subs) == 1:
# 		if subs[0] in subjects:
# 			return subs[0]
# 		return "il"
# 	else:
# 		return "ils"

# def vnhassub(tree):
# 	if type(tree.child)
# 	for i in tree:
# 		if i.label() == "NC" or i.label() == "CLS":
# 			return True
# 	return False
# 	#when in doubt do a recursive a1out

# def subverb(parenttree):
	
# 	npfound = None
# 	coordfound = None
# 	vfound = False
# 	for i in parenttree:
# 		if i.label() == "VN" and vnhassub(i):
# 			npfound = subverb(i)
# 		if i.label() == "NPP" or i.label() == "NP" or i.label() == "NC" or i.label() == "CLS" and npfound == None:
# 			npfound = i
# 		if "V" in i.label():
# 			vfound = True
# 		if i.label() == "COORD": 
# 			coordfound = i
# 		if "Srel" == i.label() or i.label() == "Ssub":
# 			subverb(i)
# 	if vfound and coordfound != None:
# 		return npfound, subverb(coordfound)
# 	elif vfound:
# 		return npfound
# 	else:
# 		return None

def parsesub(strthing):
	#sentence = "pommes et toi adorer manger des pommes, et pommes aimer manger des pommes"
	sentence_words = strthing.split(" ")
	input_sentence = benepar.InputSentence(
		words = sentence_words
		)
	parsley = parser.parse(input_sentence)
	sent = parsley[0]
	print("sent:",sent)
	# nps = subverb(sent)
	# compressedsubs = []
	# if len(nps) == 2:
	# 	compressedsubs.append(subconvert(nps))
	# else:
	# 	for np in nps:
	# 		compressedsubs.append(subconvert(np)) 
	# return compressedsubs

czech = input("would you like to manually enter a test? -> ").lower()
if czech == "yes":
	strthing = input("enter a sentence to conjugate -> ").lower()
else:
	for test in tests:
		strthing = test
		answer = parsesub(strthing)
		if answer == tests[test]:
			print("test: <" + test + "> has passed")
		else:
			print("test: <" + test + "> has failed, returned: ", answer)

print(parsesub(strthing))
#look for VINF checking (VN in vinf), Ssub, Srel
#we need to get the location of the subjects that we are returning, so that we can append it to the subjects key in the dictionary. for multiple subjects, it should just work if we take the farthest part of the subject to the right as the index.