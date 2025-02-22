from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class GigiBot:
    def __init__(self, root):
        self.root = root
        self.root.title("GigiBot")
        self.root.geometry("600x600+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='#1e1e1e', width=500)
        main_frame.pack()

        img_chat = Image.open('images/chat.png') 
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.picture = ImageTk.PhotoImage(img_chat)

        title_lbl = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=600, compound=LEFT, image=self.picture,
                          text='GigiBot', font=('Arial', 20, 'bold'), fg='white', bg='#0078D7', padx=10)
        title_lbl.pack(side=TOP, fill=X)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=60, height=23, bd=3, relief=RAISED, font=('Arial', 12), fg='white',
                         bg='#252526', yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='#1e1e1e', width=600)
        btn_frame.pack()

        label = Label(btn_frame, text="Type your message:", font=('Arial', 12, 'bold'), fg='white', bg='#1e1e1e')
        label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=35, font=('Arial', 12))
        self.entry1.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.send = Button(btn_frame, text="Send", command=self.send, font=('Arial', 10, 'bold'), width=8,
                           bg='#0078D7', fg='white')
        self.send.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Chat", command=self.clear, font=('Arial', 10, 'bold'), width=10,
                            bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.label1 = Label(btn_frame, text="", font=('Arial', 12, 'bold'), fg='skyblue', bg='#1e1e1e')
        self.label1.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.init_bot()

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_message = self.entry.get().strip()
        if user_message:
            self.text.insert(END, f'\n\nYou: {user_message}', 'user')
            self.text.tag_config('user', foreground='lightblue')
            self.text.yview(END)
            response = self.get_bot_response(user_message)
            self.text.insert(END, f'\nGigiBot: {response}', 'bot')
            self.text.tag_config('bot', foreground='lightgreen')
            self.text.yview(END)
        else:
            self.label1.config(text='Please enter some input', fg='red')

    def get_bot_response(self, message):
        responses = {
            'hi': 'Hello! Welcome to GigiBot! How can I assist you?',
            'hey': 'Hello! Welcome to GigiBot! How can I assist you?',
            'hello': 'Hello! Welcome to GigiBot! How can I assist you?',
            'how are you': 'I am just a program, but I am always here to help you! 😊',
            'register face': 'Please stand in front of the camera and follow the instructions to register your face.',
            'add face': 'Please stand in front of the camera and follow the instructions to register your face.',
            'registration status': 'Checking database... Please wait.',
            'is my face registered': 'Checking database... Please wait.',
            'is my data safe': 'All face data is encrypted and stored securely. We follow strict privacy protocols.',
            'check my attendance': 'Generating CSV file for attendance records. Please wait...',
            'view attendance': 'Opening attendance records. Please check the screen.',
            'who can access my data': 'Only authorized administrators can access attendance records.',
            'face not detected': 'Try the following steps:\n1. Check if the webcam is connected.\n2. Ensure proper lighting.\n3. Restart the application.',
            'camera not working': 'Try the following steps:\n1. Check if the webcam is connected.\n2. Ensure proper lighting.\n3. Restart the application.',
            'attendance not marked': 'Try rescanning your face or check with the administrator.',
            'clear database': 'Warning! This action will erase all records. Are you sure?',
            'reset attendance': 'Warning! This action will erase all records. Are you sure?',
            'privacy policy': 'All face data is encrypted and stored securely. We follow strict privacy protocols.',
            'which algorithm is used': 'The system uses the HOG (Histogram of Oriented Gradients) + SVM model or CNN-based face embeddings for accurate recognition.',
            'database backup': 'Use MySQL export commands or manually copy from the CSV file for backup.',
            'remote attendance': 'Yes! The system can be hosted on a server, allowing remote attendance marking via an IP camera.',
            'upcoming features': 'Planned features include:\n - Mobile app integration\n - Live face detection alerts\n - Auto-sync with cloud attendance systems.',
        }
        return responses.get(message.lower(), "I'm not sure about that. Can you rephrase?")

    def init_bot(self):
        self.text.insert(END, "GigiBot: Hi there, Welcome to GigiBot! 👋 If you need any assistance, I'm always here.", 'bot')
        self.text.tag_config('bot', foreground='lightgreen')
        self.text.yview(END)

if __name__ == '__main__':
    root = Tk()
    obj = GigiBot(root)
    root.mainloop()
