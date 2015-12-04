import middleware
from middleware import plagiot

#post_obj = {u'corpus_files': {u'0': u'TheChildrenOfForest.txt'}, u'algorithm': u'lcss', u'pattern_files': u'TheChild_10Line_Pattern..txt'}
#p1 = plagiot(post_obj)

post_obj = {u'corpus_files': {u'0': u'TheChildrenOfForest.txt'}, u'algorithm': u'lcss', u'pattern_files': u'TheChild_50_Line_Pattern.txt'}
p1 = plagiot(post_obj)
f =open("50vs12k.txt","w")
f.write(str(post_obj["execution_time"]))
f.close()
