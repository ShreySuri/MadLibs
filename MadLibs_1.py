import random

def list_to_string(x):
    str_1 = " "
    return(str_1.join(x))





silly_string_1 = "Hey diddle diddle the 'noun' and the 'noun' the 'noun' 'past_verb' over the 'noun'"
silly_string_2 = "'proper_noun' and 'proper_noun' went up a 'noun' to fetch a 'collection_noun' of 'plural_noun'"
silly_string_3 = "'proper_noun' had a 'adjective' 'noun' whose 'noun' was 'adjective' as 'plural_noun'"
silly_string_4 = "If you're 'adjective' and you know it 'verb' your 'plural_noun'"
silly_string_5 = "The 'adjective' , 'adjective' 'noun' 'past_verb' and 'past_verb' and 'past_verb' the 'noun' down"
silly_string_6 = "'onomatopoeia', 'onomatopoeia', 'adjective' 'noun' have you any 'plural_noun'?"
silly_string_7 = "My favorite activity is 'gerund' with my 'adjective' 'noun'"
silly_string_8 = "I like eating 'adjective' 'plural_noun' with lots of 'plural_noun'"


picker = random.randint(1,8)

if picker == 1:
    breakdown_list = silly_string_1.split()
if picker == 2:
    breakdown_list = silly_string_2.split()
if picker == 3:
    breakdown_list = silly_string_3.split()
if picker == 4:
    breakdown_list = silly_string_4.split()
if picker == 5:
    breakdown_list = silly_string_5.split()
if picker == 6:
    breakdown_list = silly_string_6.split()
if picker == 7:
    breakdown_list = silly_string_7.split()
if picker == 8:
    breakdown_list = silly_string_8.split()

breakdown_list.append("placeholder")
word_count = 0

while breakdown_list[word_count] != "placeholder":
    word_count = word_count + 1

breakdown_list.remove("placeholder")

noun = 0
noun_list = []
plural_noun = 0
plural_noun_list = []
proper_noun = 0
proper_noun_list = []
verb = 0
verb_list = []
past_verb = 0
past_verb_list = []
adjective = 0
adjective_list = []
onomatopoeia = 0
onomatopoeia_list = []
gerund = 0
gerund_list = []



for i in range (0, word_count):
    if breakdown_list[i] == "'noun'":
        noun = noun + 1
        noun_list.append(i)
    if breakdown_list[i] == "'plural_noun'":
        plural_noun = plural_noun + 1
        plural_noun_list.append(i)
    if breakdown_list[i] == "'proper_noun'":
        proper_noun = proper_noun + 1
        proper_noun_list.append(i)
    if breakdown_list[i] == "'verb'":
        verb = verb + 1
        verb_list.append(i)
    if breakdown_list[i] == "'past_verb'":
        past_verb = past_verb + 1
        past_verb_list.append(i)
    if breakdown_list[i] == "'adjective'":
        adjective = adjective + 1
        adjective_list.append(i)
    if breakdown_list[i] == "'onomatopoeia'":
        onomatopoeia = onomatopoeia + 1
        onomatopoeia_list.append(i)
    if breakdown_list[i] == "'gerund'":
        gerund = gerund + 1
        gerund_list.append(i)


for i in range (0, noun):
    word = input(print("Please enter a noun. "))
    word_placement = noun_list[i]
    breakdown_list[word_placement] = word
for i in range (0, plural_noun):
    word = input(print("Please enter a plural noun. "))
    word_placement = plural_noun_list[i]
    breakdown_list[word_placement] = word
for i in range (0, proper_noun):
    word = input(print("Please enter a proper noun. "))
    word_placement = proper_noun_list[i]
    breakdown_list[word_placement] = word
for i in range (0, verb):
    word = input(print("Please enter a verb. "))
    word_placement = verb_list[i]
    breakdown_list[word_placement] = word
for i in range (0, past_verb):
    word = input(print("Please enter a past-tense verb. "))
    word_placement = past_verb_list[i]
    breakdown_list[word_placement] = word
for i in range (0, adjective):
    word = input(print("Please enter an adjective. "))
    word_placement = adjective_list[i]
    breakdown_list[word_placement] = word
for i in range (0, onomatopoeia):
    word = input(print("Please enter an onomatopoeia. "))
    word_placement = onomatopoeia_list[i]
    breakdown_list[word_placement] = word
for i in range (0, gerund):
    word = input(print("Please enter a gerund. "))
    word_placement = gerund_list[i]
    breakdown_list[word_placement] = word

print(list_to_string(breakdown_list))

    
