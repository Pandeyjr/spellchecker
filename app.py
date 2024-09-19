from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self,text):
        words =text.split()
        correct_words = []

        for word in words:
            correct_word = self.spell.correction(word)
            if correct_word != word.lower():
                print(f'correcting"{word}" to "{correct_word}"')
                correct_words.append(correct_word)
            
        return ''.join(correct_words) 
    
    def run(self):
        print("\n---Spell Checker---")
        
        while True:
            text = input('Enter text to check or type "exit to quit"')

            if text.lower() == 'exit':
                print('closing the prrogram....')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected Text :{corrected_text}')

if  __name__=="__main__":
    SpellCheckerApp().run()