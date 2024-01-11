import copy

def find_combinations(primary_item, books, ench_data):
    ## combination in format [book, book, book] in order to combine to item
    # combinations = {f'[]': combine_all(primary_item, books)}
    cheapestCombination = None
    shuffles = shuffle(books)
    for eachShuffle in shuffles:
        for i in range(1, len(eachShuffle)): # num of brackets
            brackets = [0 for n in range(i)]
            for j in range(i): # Iterate through brackets
                for k in range(len(eachShuffle)-(j+1)): # Create brackets
                    brackets[j] = k
                    item_copy = copy.deepcopy(primary_item)
                    books_copy = [copy.deepcopy(book) for book in eachShuffle]
                    books_copy[k].add_enchantment(books_copy[k+1], ench_data)
                    del books_copy[k+1]
                    book_combination = combine_all(item_copy, books_copy, ench_data)
                    if cheapestCombination != None:
                        if book_combination.levels_spent < cheapestCombination[0].levels_spent:
                            cheapestCombination = [copy.deepcopy(book_combination), [copy.deepcopy(eachShuffle), copy.deepcopy(brackets)]]
                                                   
                    else:
                        cheapestCombination = [book_combination, brackets]

    return cheapestCombination

def combine_all(item_copy, books, ench_data):
    for book in books:
        item_copy.add_enchantment(book, ench_data)
    return item_copy

def shuffle(myArray):
    shuffles = []
    myArrayCopy = list(myArray)
    if len(myArray) == 1:
        return [myArray]
    for i in range(len(myArray)):
        myArrayCopy = list(myArray)
        myArrayCopy.insert(0, myArrayCopy.pop(i))
        newShuffle = shuffle(myArrayCopy[1:])
        for item in newShuffle:
            item.insert(0, myArrayCopy[0])
            shuffles.append(item)
    return shuffles

def stringify(books):
    booksCopy = copy.deepcopy(books)
    for i in range(len(booksCopy)):
        if type(booksCopy[i]) == list:
            booksCopy[i] = stringify(booksCopy[i])
        else:
            booksCopy[i] = list(booksCopy[i].enchantments.keys())[0]
    return booksCopy

def createBrackets(books, brackets):
    books = stringify(books)
    for i in range(len(brackets)):
        books[brackets[i]] = [books[brackets[i]], books[brackets[i]+1]]
        del books[brackets[i]+1]
    return books