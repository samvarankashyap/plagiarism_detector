class BoyerMore:
   'base class for BoyerMore algorithm'
   def __init__(self, text, pattern):
      self.text = text
      self.pattern = pattern
   def search_pattern(self):
      n=len(self.text)
      m=len(self.pattern)
      text = self.text
      pattern = self.pattern
      hits=[]
      i=0
      q=m
      badMTable= self.generateBadMatchTab(pattern)
      while((i+q-1)<n):
	  val=i+q-1
          while(pattern[q-1]==text[i+q-1] and q>0):
              q=q-1
          if(q<=0):
              hits.append(i)
              i=i+1
          elif(pattern[q-1]!=text[i+q-1]):
              if(badMTable.has_key(text[val])):
                  i=i+badMTable[text[val]]
              else:
                  i=i+m
          q=m
      output_dict = {}
      output_dict['text']=self.text
      output_dict['pattern']= self.pattern
      output_dict['positions']= hits
      output_dict['sequence']= ""
      return output_dict
   def generateBadMatchTab(self,pattern):
       badMList = {}
       for i in range(0, len(pattern)-1):
           badMList[pattern[i]] = len(pattern) - i - 1
       #print badMList
       return badMList

