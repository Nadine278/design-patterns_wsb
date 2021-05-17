#  Language Translator

# Adaptee: Incompatible interface # 1
class English:
        def Greeting(self):
                return "Hello!"
        def Farewell(self):
                return "Good byee."
 
# Adapter Class, which takes functionality provided by English, morphs it into functionality expected by the polish person.
class Translator:
        
        _English = None
        _engphrases = {
                "Hello!": "CZEŚĆ",
                "Good byee.": "Do widzenia"
                }
                 
        def __init__(self, English):
                self._English = English
         
# polish speaker: Incompatible interface # 2
class polish_p:
        
        _englToPolish = None
 
        def __init__(self, englToPolish):
                self._englToPolish = englToPolish
 
        def exchangeGreetings(self):
                print("Hello!")
                print( self._englToPolish._engphrases[  self._englToPolish._English.Greeting()  ] )
 
        def exchangeFarewell(self):
                print("Good bye!")
                print( self._englToPolish._engphrases[  self._englToPolish._English.Farewell()  ] )
 
# Create an English Speaking person
English = English()
 
# Create a translator with popular english phrases
englToPolish = Translator(English)
 
# The polish Person can now get responses in polish
polish = polish_p(englToPolish)
 
# Two-way conversation in Polish
polish.exchangeGreetings()
polish.exchangeFarewell()
