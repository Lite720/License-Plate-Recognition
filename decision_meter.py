
from statistics import mode

## DECISION METER

class Dmeter:
    """
        Uses a mode algorithm to sort the best outcome from OCR.
        Args: 
            None
    """    
    def __init__(self) -> None:        
        self.best : str = None
        self.batch : list[str] = []
        pass
    
    def new(self):
        """Refreshes the Dmeter.batch
        """
        print('!! NEW !!')
        self.batch = []
    
    def sublist(string : str):
        """Creates a string into sublist of list
        according to set the rule:
        list[0]: alpha
        list[1]: digit
        list[2]: alpha
        Args:
            string (str): len(string) should be >2

        Returns:
            list[[str]]: _description_
        """
        l_main = []
        l_sub = []
        toggleA= False
        toggleD= False

        # This set of instruction seperates the alphabetical and numerical chars
        # result [['A','B'],['1','2','3','4'],['X','Y','Z']]
        
        for char in string:
            if char.isalpha():
                toggleA = True
                if toggleD == True:
                    l_main.append(l_sub)
                    l_sub = []
                    toggleA, toggleD = False, False
                l_sub.append(char)
            
            if char.isdigit():
                if toggleA == True:
                    l_main.append(l_sub)
                    l_sub = []
                    toggleA, toggleD = False, False
                l_sub.append(char)
                toggleD = True
                
        l_main.append(l_sub)
        return l_main

    def add(self, string : str , as_checker=False):
        """Perform checks if string is usable, then adds to Dmeter.batch

        Args:
            string (str): String that should be added
            as_checker (bool, optional): Used if string doesn't want to be added to Dmeter.batch.
                                        Defaults to False.

        Returns:
            None
        """
        ## this series of statements are regulated for the purpose of license plates.
        if string == None: return f'String is not possible'
        string = string.replace(" ",'')
        if len(string) <3 : return f'String is too short'
        if len(string) >10 : return f'String is too long'
        if string[0].isdigit() : return f'First char not suppoesd to be digit'
        if string[2].isalpha() and string[1].isalpha() : return f'Third char not supposed to be alpha'
        if string[-1].isdigit() : return f'Last char not supposed to be digit'
        for char in string:
            if char.islower():
                return f'One char is lower'
        
        ## this is if just want to check without adding
        if as_checker == True:
            return string
        
        ## create a sublist for alpha and digit
        string = Dmeter.sublist(string)
        print(f'Meter added {string}')
        self.batch.append(string)
        return f'Successfully appended {string}'

    def calculate(self):
        """Mode algoritm that conforms to specific license plate.
        Takes in Dmeter.batch as main argument. And returns to Dmeter.best
        Mainly tailored to Indonesian license plate.
        """
                
        if len(self.batch) == 0: return f'No str in batch'
        
        bestbg = []
        bestdig = []
        bestlast = []
        
        # The first (BG)
        for i in range(2):
            temp_batch = []
            for l in self.batch:
                try:
                    temp_batch.append(l[0][i])
                except Exception as e:
                    temp_batch.append(None)
            bestbg.append(mode(temp_batch))
        
        bestbg = [thing for thing in bestbg if thing is not None]
        bestbg = [''.join(map(str, bestbg))]
        
        # The second (DIGITS)
        for i in range(4):
            temp_batch = []
            for l in self.batch:
                try:
                    temp_batch.append(l[1][i])
                except Exception as e:
                    temp_batch.append(None)
            bestdig.append(mode(temp_batch))
        
        bestdig = [thing for thing in bestdig if thing is not None]
        bestdig = [''.join(map(str, bestdig))]
         
        # The first (BG)
        for i in range(3):
            temp_batch = []
            for l in self.batch:
                try:
                    temp_batch.append(l[2][i])
                except Exception as e:
                    temp_batch.append(None)
            bestlast.append(mode(temp_batch))
        
        bestlast = [thing for thing in bestlast if thing is not None]
        bestlast = [''.join(map(str, bestlast))]
        
        self.best = f'{str(bestbg[0])} {str(bestdig[0])} {str(bestlast[0])}'
        
        
        # There are possible unwanted outcomes when it comes to OCR
        # to change the result directly you can use this hack
        # replace directly from the resulting calculation of Dmeter.best
        
        # C to G hack 👇
        enable_replace_hack = True
        i_replace = 1
        replace_from = 'C'
        replace_to = 'G'
        
        i_replace_based_on = 0
        replace_based_on = 'B'
        
        temp_best = ''
        
        if enable_replace_hack and len(self.best) >= 3 and self.best[i_replace_based_on] == replace_based_on and self.best[i_replace] == replace_from:
            for i, char in enumerate(self.best):
                if i == i_replace and char == replace_from:
                    char = replace_to
                temp_best += char

            self.best = temp_best
        
        #self.best = str(bestbg[0])+str(bestdig[0])+str(bestlast[0])
        
"""
# Creates new meter.
    # meter.new()
# Adds new string that can be compared to the one before.
    # meter.add()
# Compares the result string of before, and the ones before that. 
    # meter.calculate()

    - EXAMPLE USE -
meter = Dmeter()
meter.add('BA 1231 XO')
meter.add('BA 1231 X')
meter.add('BA 1231 X')
meter.calculate()
print(meter.best)
"""
