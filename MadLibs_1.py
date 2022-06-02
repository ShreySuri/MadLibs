import random


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
plural_noun = 0
proper_noun = 0
verb = 0
past_verb = 0
adjective = 0
onomatopoeia = 0
gerund = 0



for i in range (0, word_count):
    if breakdown_list[i] == "'noun'":
        noun = noun + 1
    if breakdown_list[i] == "'plural_noun'":
        plural_noun = plural_noun + 1
    if breakdown_list[i] == "'proper_noun'":
        proper_noun = proper_noun + 1
    if breakdown_list[i] == "'verb'":
        verb = verb + 1
    if breakdown_list[i] == "'past_verb'":
        past_verb = past_verb + 1
    if breakdown_list[i] == "'adjective'":
        adjective = adjective + 1
    if breakdown_list[i] == "'onomatopoeia'":
        onomatopoeia = onomatopoeia + 1
    if breakdown_list[i] == "'gerund'":
        gerund = gerund + 1

