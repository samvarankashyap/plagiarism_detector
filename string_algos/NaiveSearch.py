class NaiveSearch:
   'base class for LCSS algorithm'
   def __init__(self, text, pattern):
      self.text = text
      self.pattern = pattern

   def search_pattern(self):
       len_of_text = len(self.text)
       len_of_pattern = len(self.pattern)
       output_dict = {}
       output_dict['text']=self.text
       output_dict['pattern']= self.pattern
       output_dict['positions']= []
       output_dict['sequence']= ""
       
       for i in range(0,len_of_text):
           new_string = self.get_substring(self.text,i,len_of_pattern)
           if  new_string == self.pattern:
               output_dict["positions"].append(i)
       return output_dict

   def get_substring(self,text,start,offset):
       return text[start:start+offset]
      
