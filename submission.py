import helper
from sklearn.feature_extraction.text import TfidfTransformer
from numpy import *
from sklearn import svm

def count_word_num(data):
    result = {}
    for word in data:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def combine_word_count(result, sample):
    for word in sample:
        if word in result:
            result[word]+=sample[word]
        else:
            result[word]=sample[word]
    return result

def total_word_count(data_set):
    result = {}
    for data in data_set:
        for word in data:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result

def modifed_data_func(weight_list):
    with open('test_data.txt','r') as test_data_file:
        test_data=[line.strip().split(' ') for line in test_data_file]
    with open('modified_data.txt', 'w') as modified_data:
        for e in test_data:
            modified_count = 0
            delete_list = set([])
            for e2 in weight_list:
                while True:
                    if e2[0] in set(e):
                        e.remove(e2[0])
                        delete_list.add(e2[0])
                    else:
                        break
                if len(delete_list) == 20:
                    break
        for e in test_data:
            line = ''
            for word in e:
                line+=word
                line+=' '
            line = line[:-1]
            line+='\n'
            modified_data.write(line)

def fool_classifier(test_data): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    
    
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance = helper.strategy()
    parameters={'gamma':'auto','C':1,'kernel':'linear','degree':3,'coef0':0.0}
    
    d1 = total_word_count(strategy_instance.class0)
    d1_copy = total_word_count(strategy_instance.class0)
    d2 = total_word_count(strategy_instance.class1)
    d3 = combine_word_count(d1_copy, d2)

    x_train = []
    y_train = []
    
    for e in strategy_instance.class0:
        vector = []
        vector_sum = 0
        word_frequency = count_word_num(e)
        for word in d3:
            if word in word_frequency:
                vector.append(word_frequency[word])
                vector_sum += word_frequency[word]
            else:
                vector.append(0)
        if vector_sum != 0:
            x_train.append(vector)
            y_train.append(0)

    for e in strategy_instance.class1:
        vector = []
        vector_sum = 0
        word_frequency = count_word_num(e)
        for word in d3:
            if word in word_frequency:
                vector.append(word_frequency[word])
                vector_sum += word_frequency[word]
            else:
                vector.append(0)
        if vector_sum != 0:
            x_train.append(vector)
            y_train.append(1)

    x_train = array(x_train)
    y_train = array(y_train)

    transformer = TfidfTransformer()

    clf = strategy_instance.train_svm(parameters, x_train, y_train)
    
    word_weight = clf.coef_.tolist()[0]
    
    i = 0
    weight_list = []
    for word in d3:
        weight_list.append((word, word_weight[i]))
        i += 1

    weight_list = sorted(weight_list, key = lambda x: x[1], reverse = True)
    for i in range(len(weight_list)):
        if weight_list[i][1]<=0:
            break
    weight_delete_list = weight_list[:i]
    modifed_data_func(weight_delete_list)

    ## You can check that the modified text is within the modification limits.
    modified_data = './modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance ## NOTE: You are required to return the instance of this class.
