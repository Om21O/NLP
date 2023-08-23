from transformers import pipeline
nlp=pipeline("question-answering",model="deepset/roberta-base-squad2",tokenizer="deepset/roberta-base-squad2")
#first= task need to perform
#modelname that we have to use
#tokenizer also same as model
while True:
    with open("q.txt", "r", encoding="utf-8") as file:
        context = file.read()
    question=input("Enter your question ? (or type exit to quit) :")
    #what question we have to ask whic paragragh we need for answer and dictionery 
    config={
        "question":question,
        "context":context
    }

    result=nlp(config)
    answer=result["answer"]
    print("Answer:",answer)
   
    if question.lower() == 'exit':
        break  # Exit the loop if the user types 'exit