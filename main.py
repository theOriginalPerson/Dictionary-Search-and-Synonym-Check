
sample_dict = {
    "alphabet" : "a set of letters or symbols in a fixed order, used to represent the basic sounds of a language",
    "bistro" : "a small restaurant",
    "country" : "a nation with its own government, occupying a particular territory",
    "dapper" : "neat and trim in dress and appearance",
    "eudaimonia" : "a Greek word literally translating to the state or condition of 'good spirit', and which is commonly translated as 'happiness' or 'welfare'",
    "fiddle-faddle" : "trivial matters; nonsense",
    "gallant" : "having or displaying great dignity or nobility",
    "heyday" : "the period of a person's or thing's greatest success, popularity, or vigor",
    "ignite" : "catch fire or cause to catch fire",
    "majestic" : "having or displaying great dignity or nobility"
}

# goal of this task to to try to find all the synonyms in this dictionary

def search(key):
    return sample_dict[key]

def synonym_checker():
    for key in sample_dict:
        key_holder = sample_dict.get(key) # stores the value of each key temporarily until it checks if there are any other keys with the same value; if none, moves onto next key
        key_index = list(sample_dict.keys()).index(key)
        for possible_synonym in sample_dict:
            synonym_index = list(sample_dict.keys()).index(possible_synonym)
            if (sample_dict.get(possible_synonym) == key_holder) and (key_index != synonym_index):
                return (f"The first synonyms for this dictionary are: '{key}' and '{possible_synonym}'.")
            
    return ("There are no synonyms here...") # if the process has been entirely completed without any synonyms, then we'll return this line


# please copy the code below and change the function names appropriately to whatever you named your functions

init = input("Do you wish to use the search or synonym check? Press 1 for search, 2 for synonym check. >")
if init == str(1):
    init2 = input("What's the word you wish to search for?")
    print(search(init2))

elif init == str(2):
    print(synonym_checker())