import detector
import tkinter

def chatbot(user_in_text, feeling):
    # this is where the AI stuff would happen if it didn't cost money
    if feeling == "sad":
        return "I've noticed you seem to show the symptons of being sad. May I suggest some things to cheer you up?"
    elif feeling == "angry":
        return "You seem to be mad about something. May I suggest some things to calm you down?"
    elif feeling == "happy":
        return "You seem really happy lately! Whatever the hell you're doing, keep it up."

def window(feeling):
    root = tkinter.Tk()
    root.title("Chatbot")

    # Create the chatbot's text area
    text_area = tkinter.Text(root, bg="white", width=50, height=20)
    text_area.pack()
    input_field = tkinter.Entry(root, width=50)
    input_field.pack()
    user_input = "This is where you'd prompt the AI"
    response = chatbot(user_input, feeling)
    text_area.insert(tkinter.END, f"Chatbot: {response}\n") 

    send_button = tkinter.Button(root, text="Send", command=lambda: send_message())
    send_button.pack()

    def send_message():
        text_area.insert(tkinter.END, f"Chatbot: {response}\n")
        user_input = input_field.get()
        input_field.delete(0, tkinter.END)
        response = chatbot(user_input, feeling)
        text_area.insert(tkinter.END, f"User: {user_input}\n")
        text_area.insert(tkinter.END, f"Chatbot: {response}\n")
    root.mainloop()

def main():
    # run the detector
    # main_emotion is a string containing the most used emotion at our threshold. We may want this in a loop but thats for later. 
    threshold = 5
    # return to main with emotion after like 10-20 of the same emotions
    main_emotion = detector.detector(threshold) 
    # then prompt the user after it sees enough emotions determined by threshold
    window(main_emotion)


if __name__ == '__main__':
    main()