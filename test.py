
def tokenize (input: str):
    s = ""
    tokens = []

    for c in input:
        if c != " " and c != "." and c != "!" and c != "?":
            s = s + c
        else:
            tokens.append(s)
            s = ""

    tokens.append(input[len(input) - 1])
    return tokens

#Words categorised by attitude/simple mood (happy, sad, love, hate, etc)
bad = ["black", "old", "stop", "cold", "cut", "fall", "far", "hot", "hurt", "never",
        "bear", "fire", "night", "rain", "snow", "wind", "hate", "bad", "die", "death"]

good = ["funny", "eat", "good", "pretty", "white", "fly", "know", "live", "thank", "best", "fast", "first", "sing", "sleep", "better", "clean",
         "full", "drink", "kind", "laugh", "light", "own", "start", "together", "warm",
         "apple", "baby", "bed", "bird, birthday", "cake", "children", "Christmas", "father", "flower", "game", "garden", "home", "kitty", "money",
         "mother", "party", "Santa Claus", "song", "sun", "toy", "beautiful", "like", "love"]

def score(input):
    points = 0
    for s in input:
        if s in bad:
            points -= 1
        elif s in good:
            points += 1
    return points

def score_words(input):
    default = score(input)
    points = []
    for s in input:
        if s in bad:
            points.append(default - 1)
        elif s in good:
            points.append(default + 1)
        else:
            points.append(default)
    return points

def show (input):
    i = 0
    points = score_words(input)
    for s in input:
        print(f"{s}     : {points[i]}")
        i += 1
    print(score(input))

def find_positive(input):
    points = score_words(input)
    i = 0
    better = []
    default = score(input)
    for s in input:
        if points[i] > default:
            better.append(s)
        i += 1

    better.sort()
    return better

def find_negative(input):
    points = score_words(input)
    i = 0
    worse = []
    default = score(input)
    for s in input:
        if points[i] < default:
            worse.append(s)
        i += 1

    worse.sort()
    return worse

#print(find_positive(input))
#print(find_negative(input))

input = "I like white men in the sun."
input = tokenize(input)
show(input)

#TODO: create these word categories
""" verbs = []

nouns = []

adjectives = []

adverbs = []

conjuctions = []

pronouns = []

interjections = []

prepostions = [] """
