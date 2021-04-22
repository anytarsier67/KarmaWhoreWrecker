import tkinter as tk
from tkinter import StringVar
import json

with open('config.json', 'r') as f:
    config = json.load(f)
    account = config["account"]
    KarmaWhore = config["KarmaWhore"]
 
class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.frame_1 = tk.Frame(master)

        self.bot_header = tk.Message(self.frame_1)
        self.bot_header.configure(background='#525252', font='{Segoe UI} 14 {bold}', foreground='#ffffff', text='bot:')
        self.bot_header.grid(column='0', row='0')
        self.bot_header.columnconfigure('0', pad='0')

        self.client_id_label = tk.Label(self.frame_1)
        self.client_id_label.configure(background='#525252', foreground='#ffffff', text='Client id:')
        self.client_id_label.grid(row='1')
        self.client_id_label.columnconfigure('0', pad='0')
        self.client_id_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=account["client_id"]))
        self.client_id_entry.grid(row='2')
        self.client_id_entry.columnconfigure('0', pad='0')

        self.client_secret_label = tk.Label(self.frame_1)
        self.client_secret_label.configure(background='#525252', borderwidth='0', foreground='#ffffff', justify='left')
        self.client_secret_label.configure(text='Client secret:')
        self.client_secret_label.grid(column='1', row='1')
        self.client_secret_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=account["client_secret"]))
        self.client_secret_entry.grid(column='1', row='2')

        self.username_label = tk.Label(self.frame_1)
        self.username_label.configure(background='#525252', foreground='#ffffff', text='Username:')
        self.username_label.grid(column='2', row='1')
        self.username_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=account["username"]))
        self.username_entry.grid(column='2', row='2')

        self.password_label = tk.Label(self.frame_1)
        self.password_label.configure(background='#525252', foreground='#ffffff', text='Password:')
        self.password_label.grid(column='3', row='1')
        self.password_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=account["password"]))
        self.password_entry.configure(show='•')
        self.password_entry.grid(column='3', row='2')

        self.user_agent_label = tk.Label(self.frame_1)
        self.user_agent_label.configure(background='#525252', foreground='#ffffff', text='User agent:')
        self.user_agent_label.grid(column='4', row='1')
        self.user_agent_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=account["user_agent"]))
        self.user_agent_entry.grid(column='4', row='2')

        self.set_config_button = tk.Button(self.frame_1, command=self.set_config)
        self.set_config_button.configure(activebackground='#525252', activeforeground='#ffffff', background='#525252', cursor='arrow')
        self.set_config_button.configure(foreground='#ffffff', text='Set config')
        self.set_config_button.grid(column='3', row='7')
        self.set_config_button.columnconfigure('0', pad='0')
        
        self.KarmaWhore_header = tk.Message(self.frame_1)
        self.KarmaWhore_header.configure(background='#525252', font='{Segoe UI} 14 {bold}', foreground='#ffffff', text='KarmaWhore:')
        self.KarmaWhore_header.configure(width='122')
        self.KarmaWhore_header.grid(column='0', row='6')
        self.KarmaWhore_header.rowconfigure('6', pad='0')
        self.KarmaWhore_header.columnconfigure('0', pad='0')

        self.karmawhore_name_label = tk.Label(self.frame_1)
        self.karmawhore_name_label.configure(background='#525252', foreground='#ffffff', text='Name:')
        self.karmawhore_name_label.grid(column='0', row='7')
        self.karmawhore_name_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=KarmaWhore["name"]))
        self.karmawhore_name_entry.grid(column='0', row='8')

        self.karmawhore_message_label = tk.Label(self.frame_1)
        self.karmawhore_message_label.configure(background='#525252', foreground='#ffffff', text='Message:')
        self.karmawhore_message_label.grid(column='1', row='7')
        self.karmawhore_message_entry = tk.Entry(self.frame_1, textvariable=StringVar(value=KarmaWhore["message"]))
        self.karmawhore_message_entry.grid(column='1', row='8')
        
        self.frame_1.configure(background='#525252', height='200')
        self.frame_1.configure(width='200')
        self.frame_1.grid(column='100', row='100')
        self.mainwindow = self.frame_1


    def run(self):
        self.mainwindow.mainloop()

    def set_config(self):
        global config, account, KarmaWhore
        account["client_id"] = self.client_id_entry.get()
        account["client_secret"] = self.client_secret_entry.get()
        account["username"] = self.username_entry.get()
        account["password"] = self.password_entry.get()
        account["user_agent"] = self.user_agent_entry.get()
        KarmaWhore["name"] = self.karmawhore_name_entry.get()
        KarmaWhore["message"] = self.karmawhore_message_entry.get()
        config["account"] = account
        config["KarmaWhore"] = KarmaWhore
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()