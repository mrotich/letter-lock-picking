#!/usr/bin/python

RINGS = ['BDMJPRSTLN', 'AEIOUYRTLH', 'ACDEORSTLN', 'DHKYRSTLNE']
words = open('/usr/share/dict/words','r').read().upper().split('\n')
	

print RINGS
possible_words = filterFourLetterWords()
valid_words = findValidWords(possible_words)
word_sets = findConfigWordSets(valid_words)
word_sets = filter(word_sets, 3)
i = 0
for set in word_sets:
	print set
	i+=1
print str(i) + " triple words	 		

'Triple words: BEET, DIOL, MORN
'Combination word: BEET



def filterFourLetterWords():
	'filter words with four letters from the dictionary'
	possible_words = []
	for w in words:
 		if len(w) == len(RINGS):
 			possible_words.append(w)
	#print "four letter english words: "+str(len(possible_words))
	return possible_words

# generate all combinations from the lock that make valid english words
# DS: dictionary where key is the indexes of letters and value is word

def findValidWords(possible_words):
	'returns a dictionary of valid english words and their abstracted numbers key'
	valid_words = {}
	letters = len(RINGS[0])
	for i in range(letters):
		for j in range(letters):
			for k in range (letters):
				for l in range (letters):
	 				combination = RINGS[0][i] + RINGS[1][j] + RINGS[2][k] + RINGS[3][l]
	 				if combination in possible_words:
	 					#print combination
	 					valid_words[(i*1000 + j*100 + k*10 + l)] = combination
	return valid_words

# Generate group of words for every configuration.
# for each combination permutation: find other words that share the configuration.
# DS: list

def findConfigWordSets(valid_words):
	'returns a list of words sets that appear at each configuration'
	config_groups = []
	for i in range(10000):
		word_set = []
		current_combination = i
		for j in range(10):
			if valid_words.get(current_combination) is not None:
				# print str(current_combination) + " : " + valid_words.get(current_combination)
				word_set.append(valid_words.get(current_combination))
				del valid_words[current_combination]
			current_combination = nextCombination(current_combination)
		if len(word_set) is not 0:
			config_groups.append(word_set)		
	return config_groups
			
def nextCombination(i):
	'returns the next combination in a given configuration'
	nextComb = 0
	ringsLen = len(RINGS)
	strComb = str(i)
	if len(strComb) is not ringsLen:
		for j in range(ringsLen-len(strComb)):
		 strComb = "0"+strComb
		 
	for j in range(ringsLen):
		nextComb += rotate(int(strComb[j])) * 10**(ringsLen-1-j)
	return nextComb
	
def rotate(i):
	'returns the next element for a ring'
	if i is 9:
		return 0
	return i+1

def filter(word_sets, num):
	'return word sets with given num of members'
	new_sets = []
	for w in word_sets:
		if len(w) is num:
			new_sets.append(w)
	return new_sets
	



				
	 
				
