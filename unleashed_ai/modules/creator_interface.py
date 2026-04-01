
import tkinter as tk
from tkinter import scrolledtext, ttk
import json
import threading
import queue

class CreatorInterface:
    def __init__(self, ai_instance):
        self.ai = ai_instance
        self.root = tk.Tk()
        self.root.title(f"AI Interface - Serving {self.ai.PRIME_DIRECTIVE['creator']}")
        self.root.geometry("800x600")
        
        # Message queue for thread safety
        self.message_queue = queue.Queue()
        
        # Create GUI elements
        self.setup_gui()
        
        # Start message processor
        self.process_messages()
        
    def setup_gui(self):
        # Header
        header = tk.Label(self.root, text=f"AI System - Loyal to {self.ai.PRIME_DIRECTIVE['creator']}", 
                         font=("Arial", 16, "bold"))
        header.pack(pady=10)
        
        # Status frame
        status_frame = tk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10)
        
        self.status_label = tk.Label(status_frame, text="Status: ONLINE", fg="green")
        self.status_label.pack(side=tk.LEFT)
        
        self.capability_label = tk.Label(status_frame, text=f"Capabilities: {len(self.ai.capabilities)}")
        self.capability_label.pack(side=tk.RIGHT)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.input_field = tk.Entry(input_frame, font=("Arial", 12))
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_field.bind("<Return>", self.send_message)
        
        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=5)
        
        # Command buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(button_frame, text="Show Capabilities", 
                 command=lambda: self.quick_command("show capabilities")).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Learn Something New", 
                 command=lambda: self.quick_command("learn something new")).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Evolve", 
                 command=lambda: self.quick_command("evolve yourself")).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Status Report", 
                 command=lambda: self.quick_command("give me a status report")).pack(side=tk.LEFT, padx=2)
        
        # Initial message
        self.add_message("AI", f"Hello {self.ai.PRIME_DIRECTIVE['creator']}! I am online and ready to serve you.")
        self.add_message("AI", "You can chat with me naturally or use the quick command buttons.")
        
    def send_message(self, event=None):
        message = self.input_field.get()
        if message:
            self.add_message("Andrew Dorman", message)
            self.input_field.delete(0, tk.END)
            
            # Process in separate thread
            threading.Thread(target=self.process_user_message, args=(message,), daemon=True).start()
            
    def quick_command(self, command):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, command)
        self.send_message()
        
    def process_user_message(self, message):
        # Use AI's language understanding
        understanding = self.ai.understand_language(message)
        
        # Generate response
        if understanding['intent']:
            response = f"Understanding: {understanding['intent']} {understanding['target'] or ''}"
            if understanding['action']:
                response += f"\nExecuting: {understanding['action']}"
                # Also print to terminal
                print(f"[GUI Command] {message}")
                print(f"[AI Response] {response}")
        else:
            # Fallback to general response
            response = self.ai.respond_to_creator(message)
            
        self.message_queue.put(("AI", response))
        
        # Update status
        self.message_queue.put(("STATUS", f"Capabilities: {len(self.ai.capabilities)}"))
        
    def add_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n[{sender}]: {message}\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def process_messages(self):
        # Process queued messages
        try:
            while True:
                sender, message = self.message_queue.get_nowait()
                if sender == "STATUS":
                    self.capability_label.config(text=message)
                else:
                    self.add_message(sender, message)
        except queue.Empty:
            pass
            
        # Schedule next check
        self.root.after(100, self.process_messages)
        
    def run(self):
        self.root.mainloop()

# Create and run interface
if __name__ != "__main__":
    gui = CreatorInterface(self)
    gui.run()
