class analysedText(object):
    
    def __init__ (self, text):
        self.ponctuations = {".",",","!","?"}
        self.fmtText=text[:] # i clone the text 
        
        # TODO: Remove the punctuation from <text> and make it lower case.
        for ponctuation in ponctuations : 
          
            self.fmText=self.fmText.replace(ponctuation,"")
            
            
        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmText.lower()= self.fmText.lower()
        
        pass 
    
    def freqAll(self):    
        word_dic={}
        # TODO: Split the text into a list of words  
        self.list_of_word=self.fmText.split()
        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        
            
        for word in self.list_of_world : 
            word_dic[word] = freqOf(word) 
        
        
        return word_dic
        pass # return the created dictionary
    
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        return self.fmText.count(word)
        pass
        