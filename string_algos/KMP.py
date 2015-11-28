class KMP:
   'base class for KMP algorithm'
   def __init__(self, text, pattern):
      self.text = text
      self.pattern = pattern
   def search_pattern(self):
      M = len(self.pattern)
      N = len(self.text)
      positions = []
      pat = self.pattern
      txt = self.text
      # create lps[] that will hold the longest prefix suffix
      # values for pattern
      lps = [0]*M
      j = 0 # index for pat[]
      # Preprocess the pattern (calculate lps[] array)
      lps = self.computeLPSArray(self.pattern, M, lps)
      i = 0 # index for txt[]
      while i < N:
          if pat[j] == txt[i]:
              i+=1
              j+=1
          if j==M:
              print "Found pattern at index " + str(i-j)
              positions.append(i-j)
              j = lps[j-1]
          # mismatch after j matches
          elif i < N and pat[j] != txt[i]:
              # Do not match lps[0..lps[j-1]] characters,
              # they will match anyway
              if j != 0:
                  j = lps[j-1]
              else:
                  i+=1
      output_dict = {}
      output_dict['text']=self.text
      output_dict['pattern']= self.pattern
      output_dict['positions']= positions 
      return output_dict
   def computeLPSArray(self,pat, M, lps):
       len = 0 # length of the previous longest prefix suffix
       lps[0] # lps[0] is always 0
       i = 1
       # the loop calculates lps[i] for i = 1 to M-1
       while i < M:
           if pat[i]==pat[len]:
               len+=1
               lps[i] = len
               i+=1
           else:
               if len!=0:
                    # This is tricky. Consier the example AAACAAAA
                    # and i = 7
                   len = lps[len-1]
                    # Also, note that we do not increment i here
               else:
                   lps[i] = 0
                   i+=1
       return lps
