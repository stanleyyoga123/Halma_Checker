from PyInquirer import Token
def get_style():
    return {
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '', 
        Token.Answer: '#2196f3 bold',
        Token.Question: ''
    }