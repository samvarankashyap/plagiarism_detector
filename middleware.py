import time
from string_algos import NaiveSearch
from string_algos import KMP
from string_algos import LCSS
from string_algos import BoyerMore
from timeit import default_timer as timer
import pdb

def plagiot(post_obj):
    #print "inside plag_check"
    c_files = post_obj['corpus_files']
    algo = post_obj['algorithm']
    p_file = post_obj['pattern_files']
    #print post_obj
    #output_obj = plagarism_check(c_files,algo,p_file)
    start_time = timer()
    output_obj = plagarism_check2(c_files,algo,p_file)
    end_time = timer()
    output_obj['execution_time'] = end_time - start_time
    output_obj['algorithm'] = algo
    return output_obj

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
    #print output_obj
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

def plagarism_check2(corpus,algo,pfile):
    obj = {}
    # obj {line : [ {filename , line no , positions , text , pattern } , ... }
    p_fd = open("./uploads/"+pfile)
    p_counter = 1
    #pdb.set_trace()
    for p_line in p_fd:
	p_line=p_line.rstrip("\r\n")       
	p_line=p_line.lstrip("\xef\xbb\xbf")
	if p_line == "":
	    continue	 
	obj[p_counter] = []
        for key in corpus:
	    #print "./uploads/"+corpus[key]
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

def get_algo(p_algo,text,pattern):
    if p_algo == 'nss':
        return NaiveSearch.NaiveSearch(text,pattern)
    elif p_algo == 'kmp':
        return KMP.KMP(text,pattern)
    elif p_algo == 'lcss':
        return  LCSS.LCSS(text,pattern) 
    elif p_algo == 'bm':
        return BoyerMore.BoyerMore(text,pattern) 

#post_obj = {u'corpus_files': {u'0': u'TheChildrenOfForest.txt'}, u'algorithm': u'lcss', u'pattern_files': u'TheChild_10Line_Pattern..txt'}
#print plagiot(post_obj)
