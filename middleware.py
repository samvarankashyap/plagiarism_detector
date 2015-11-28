import time
from string_algos import *
def plagiot(post_obj):
    print "inside plag_check"
    output_obj = "nothing"
    return output_obj

def pattern_check(post_obj):
    output_obj= post_obj
    print "inside the pattern check"
    print "processing the pattern match algorithm"
    p_text = post_obj['patterntext']
    p_algo = post_obj['pattern_algorithm']
    a_text = post_obj['actualtext']
    algo_obj = get_algo(p_algo)
    start_time = time.time()
    output_obj = algo_obj.search_pattern()
    execution_time = time.time() - start_time
    output_obj['execution_time']=execution_time
    return output_obj

def get_algo(p_algo):
    if p_algo == 'nss':
        return NaiveSearch.NaiveSearch(text,pattern)
    elif p_algo == 'kmp':
        return KMP.KMP(text,pattern)
    elif p_algo == 'lcss':
        return  LCSS.LCSS(text,pattern) 
    elif p_algo == 'bm':
        return "not implemented" 
