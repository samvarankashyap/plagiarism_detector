import time
from string_algos import NaiveSearch
from string_algos import KMP
from string_algos import LCSS
from string_algos import BoyerMore
from timeit import default_timer as timer

def plagiot(post_obj):
    print "inside plag_check"
    c_files = post_obj['corpus_files']
    algo = post_obj['algorithm']
    p_file = post_obj['pattern_files']
    print post_obj
    output_obj = plagarism_check(c_files,algo,p_file)
    return output_obj

def pattern_check(post_obj):
    output_obj= post_obj
    print "inside the pattern check"
    print "processing the pattern match algorithm"
    p_text = post_obj['patterntext']
    p_algo = post_obj['patternalgorithm']
    a_text = post_obj['actualtext']
    algo_obj = get_algo(p_algo,a_text,p_text)
    start_time = timer()
    output_obj = algo_obj.search_pattern()
    end_time = timer()
    execution_time = end_time - start_time
    output_obj['execution_time']=execution_time
    print output_obj
    return output_obj

def plagarism_check(corpus,algo,pfile):
    obj = {}
    p_fd = open("./uploads/"+pfile)
    c = 1
    for key in corpus:
        f = open("./uploads/"+corpus[key])
        totaltext = f.read()
        for line in p_fd:
            algo_obj = get_algo(algo,totaltext,line)
            o_obj = algo_obj.search_pattern()
            obj[c]=o_obj
            c = c+1
    return obj

def get_algo(p_algo,text,pattern):
    if p_algo == 'nss':
        return NaiveSearch.NaiveSearch(text,pattern)
    elif p_algo == 'kmp':
        return KMP.KMP(text,pattern)
    elif p_algo == 'lcss':
        return  LCSS.LCSS(text,pattern) 
    elif p_algo == 'bm':
        return BoyerMore.BoyerMore(text,pattern) 
