class KMP:
   'base class for KMP algorithm'
   def __init__(self, text, pattern):
      self.text = text
      self.pattern = pattern
   def search_pattern(self):
      n=len(self.text)
      m=len(self.pattern)
      sText=" "+self.text
      spattern=" "+self.pattern
      prefixTable= self.generatePrefixTable(spattern)
      q=0
      hits =[]
      for i in range(1,n+1):
          while(q>0 and spattern[q+1] != sText[i]):
              q = prefixTable[q]
          if(spattern[q+1]==sText[i]):
              q=q+1
          if(q==m):
              hits.append(str(i-m))
              q=prefixTable[q]
      output_dict = {}
      output_dict['text']=self.text
      output_dict['pattern']= self.pattern
      output_dict['positions']= hits
      return output_dict
   def generatePrefixTable(self,pattern):
       pstring=pattern
       i=0
       pref ={}
       pref[1]=0
       for j in range(2,len(pstring)):
           while(i>0 and pstring[i+1] != pstring[j]):
               i=pref[i]
           if pstring[i+1] == pstring[j]:
               i=i+1
           pref[j]=i
       return pref
