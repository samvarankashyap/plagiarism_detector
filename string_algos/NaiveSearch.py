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
       
       for i in range(0,len_of_text):
           if  self.text[i:i+len_of_pattern] == self.pattern:
               output_dict["positions"].append(i)
       return output_dict
      
