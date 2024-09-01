
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
         "mother", "party", "Santa Claus", "song", "sun", "toy", "beautiful", "like", "love", "well"]

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
nouns = ["apple", "baby", "back", "ball", "bear", "bed", "bell", "bird", "birthday", "boat", "box",
          "boy", "bread", "brother", "cake", "car", "cat", "chair", "chicken", "children", "Christmas",
          "coat", "corn", "cow", "day", "death", "dog", "doll", "door", "duck", "egg", "eye", "farm", "farmer",
          "father", "feet", "fire", "fish", "floor", "flower", "game", "garden", "girl", "goat",
          "grass", "ground", "hand", "head", "hill", "home", "horse", "house", "kitty", "leg",
          "letter", "man", "men", "milk", "money", "morning", "mother", "name", "nest", "night",
          "paper", "party", "picture", "pig", "rabbit", "rain", "ring", "robin", "Santa Claus",
          "school", "seed", "sheep", "shoe", "sister", "snow", "song", "squirrel", "stick", "street",
          "sun", "table", "thing", "time", "top", "toy", "tree", "watch", "water", "way", "wind",
          "window", "woman", "women", "wood"]

verbs = ["am", "are", "ask", "ate", "be", "been", "bring", "buy", "call", "came",
         "can", "carry", "come", "could", "cut", "did", "die", "do", "does", "done", "don't",
         "draw", "drink", "eat", "fall", "find", "fly", "found", "gave", "get", "give",
         "go", "goes", "going", "got", "grow", "had", "has", "have", "help", "hold",
         "hurt", "is", "jump", "keep", "know", "laugh", "let", "like", "live", "look",
         "made", "make", "may", "must", "open", "pick", "play", "please", "pull", "put",
         "ran", "read", "ride", "run", "said", "saw", "say", "see", "shall", "show",
         "sing", "sit", "sleep", "start", "stop", "take", "tell", "thank", "think", "try",
         "use", "walk", "want", "was", "wash", "went", "were", "will", "wich", "work", "would", "write"]

adjectives = ["a", "all", "an", "any", "best", "better", "big", "black", "blue", "both",
              "brown", "clean", "cold", "eight", "every", "five", "four", "full", "funny", "good",
              "green", "hot", "kind", "light", "little", "long", "many", "new", "old", "one",
              "own", "pretty", "red", "right", "round", "seven", "six", "small", "some", "ten",
              "the", "three", "two", "warm", "white", "yellow"]

adverbs = ["again", "always", "around", "away", "before", "far", "fast", "first", "here", "how",
           "just", "much", "never", "no", "not", "now", "off", "once", "only", "out",
           "so", "soon", "then", "there", "today", "together", "too", "up", "very", "well",
           "when", "where", "why", "yes"]

question_words = ["how", "much", "what", "when", "where", "which", "who", "why"]
# "much" will be a special case of using "how"

conjuctions = ["and", "as", "because", "but", "if", "or"]

pronouns_subject = ["he","i", "I", "it", "they", "we", "you"]

pronouns_object = ["him", "me", "this", "that"]

pronouns_posessive = ["his", "her", "my", "its", "thier", "our", "your"]

pronouns_reflexive = ["myself", "himself", "herself", "itself", 
                      "themselves", "ourselves", "yourself", "yourselves"]

interjections = []

prepostions = ["about", "after", "at", "by", "down", "for", "from", "on", "into", "of", "on",
               "over", "to", "under", "upon", "with"]
