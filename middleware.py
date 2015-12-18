import time
from string_algos import NaiveSearch
from string_algos import KMP
from string_algos import LCSS
from string_algos import BoyerMore
from timeit import default_timer as timer

#function for routing the request towards the algorithm
def plagiot(post_obj):
    c_files = post_obj['corpus_files']
    algo = post_obj['algorithm']
    p_file = post_obj['pattern_files']
    start_time = timer()
    output_obj = plagarism_check2(c_files,algo,p_file)
    end_time = timer()
    output_obj['execution_time'] = end_time - start_time
    output_obj['algorithm'] = algo
    return output_obj

#runs the pattern check on the given post object
def pattern_check(post_obj):
    output_obj= post_obj
    p_text = post_obj['patterntext']
    p_algo = post_obj['patternalgorithm']
    a_text = post_obj['actualtext']
    algo_obj = get_algo(p_algo,a_text,p_text)
    start_time = timer()
    output_obj = algo_obj.search_pattern()
    end_time = timer()
    execution_time = end_time - start_time
    output_obj['execution_time']=execution_time
    output_obj['patterntext']=p_text
    output_obj['algorithm']=p_algo
    output_obj['actualtext']=a_text
    return output_obj

#runs the plagiarism check
def plagarism_check2(corpus,algo,pfile):
    obj = {}
    p_fd = open("./uploads/"+pfile)
    p_counter = 1
    for p_line in p_fd:
	p_line=p_line.rstrip("\r\n")       
	p_line=p_line.lstrip("\xef\xbb\xbf")
	if p_line == "":
	    continue	 
	obj[p_counter] = []
        for key in corpus:
            t_file = open("./uploads/"+corpus[key])
            t_counter = 1
            for t_line in t_file:
		t_line=t_line.rstrip("\r\n")
		t_line=t_line.lstrip("\xef\xbb\xbf")
		if t_line == "":
			continue
                algo_obj = get_algo(algo,t_line,p_line)
                o_obj = algo_obj.search_pattern()
                if len(o_obj["positions"]) > 0 or len(o_obj["sequence"]) > 0:
                    o_obj["line"] = t_counter
                    o_obj["filename"] = corpus[key]
                    obj[p_counter].append(o_obj)
                t_counter += 1
        p_counter += 1    
    return obj

#serves the algo according to the posted object
def get_algo(p_algo,text,pattern):
    if p_algo == 'nss':
        return NaiveSearch.NaiveSearch(text,pattern)
    elif p_algo == 'kmp':
        return KMP.KMP(text,pattern)
    elif p_algo == 'lcss':
        return  LCSS.LCSS(text,pattern) 
    elif p_algo == 'bm':
        return BoyerMore.BoyerMore(text,pattern) 

