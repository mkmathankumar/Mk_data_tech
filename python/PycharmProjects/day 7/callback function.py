def on_button_click(callback):
    print('button clicked')
    callback()

def show_message():
    print('hello mk, welcome')
    
on_button_click(show_message)