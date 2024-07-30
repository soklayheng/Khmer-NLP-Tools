from khnlp.segment import Tokenizer

def test_tokenizer():
    tokenizer = Tokenizer('model/compound_model.bin')

    sent = ['ការទាមទារចំពោះអង្គការ', 'ខ្ញុំស្រឡាញ់កម្ពុជា']
    
    result = tokenizer.tokenize(sent)
    
    print(result)

if __name__ == '__main__':
    test_tokenizer()

