import detector
import tkinter
import os
from datetime import datetime, timedelta
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

def chatbot(chain, prompt = None, feeling = None):
    # this is where the AI stuff would happen if it didn't cost money
    if prompt: 
        return chain.run(prompt)
    elif feeling == "sad":
        return chain.run("I am sad. Ask me how you can help. ")
    elif feeling == "tired":
        return chain.run("I have been working for a long time. Ask me how you can help. ")
    elif feeling == "angry":
        return chain.run("I am angry. Ask me how you can help. ")
    elif feeling == "happy":
        return "You seem really happy lately! Whatever the hell you're doing, keep it up."

def window(feeling):
    # Creating LLM, change PATH. 
    PATH = 'C:/Users/28550/AppData/Local/nomic.ai/GPT4All/gpt4all-falcon-q4_0.gguf'
    llm = GPT4All(model=PATH, verbose=True)
    prompt = PromptTemplate(input_variables = ['action'], 
                            template = """
                            ### Instruction: 
                            You are an emotional support chatbot. The prompt below is a question to answer, 
                            a task to complete, or a conversation to respond to; 
                            decide which and write an appropritate response. 
                            ### Prompt: 
                            {action}
                            ### Response: 
                            The response should be in first person from the perspective up an emotional support chatbot. 
                            Return a response with no leading spaces.
                            """)
    
    chain = LLMChain(prompt=prompt, llm=llm)

    root = tkinter.Tk()
    root.title("Chatbot")
    
    # Create the chatbot's text area
    text_area = tkinter.Text(root, bg="white", width=50, height=20)
    text_area.pack()
    input_field = tkinter.Entry(root, width=50)
    input_field.pack()
    response = chatbot(chain, None, feeling)
    text_area.insert(tkinter.END, f"Chatbot: {response}\n") 

    send_button = tkinter.Button(root, text="Send", command=lambda: send_message())
    send_button.pack()

    def send_message():
        prompt = input_field.get()
        input_field.delete(0, tkinter.END)
        response = chatbot(chain, prompt=prompt, feeling=feeling)
        text_area.insert(tkinter.END, f"User: {prompt}\n")
        text_area.insert(tkinter.END, f"Chatbot: {response}\n")
    root.mainloop()


def main(): 
    init_time = datetime.now()
    time_thr = 15 #seconds

    # run the detector
    # main_emotion is a string containing the most used emotion at our threshold. We may want this in a loop but thats for later. 
    threshold = 5
    while (True): 
        # return to main with emotion after like 10-20 of the same emotions
        main_emotion = detector.detector(threshold, init_time, time_thr) 
        if main_emotion=="tired": 
            init_time = datetime.now()
        # then prompt the user after it sees enough emotions determined by threshold
        window(main_emotion)


if __name__ == '__main__':
    main()