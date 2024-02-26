import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("600x400")
        self.master.configure(bg="#2c3e50")
        self.questions_asked = []
        
        # Topics and questions
        self.questions = {
            "History": [
                {
                    "question": "Who was the first President of the United States?",
                    "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                    "answer": "George Washington",
                    "hint": "He led the American Revolutionary War."
                },
                {
                    "question": "Which year did World War II end?",
                    "options": ["1945", "1939", "1941", "1950"],
                    "answer": "1945",
                    "hint": "It ended with the surrender of Japan."
                },
                {
                    "question": "Who wrote the famous book 'To Kill a Mockingbird'?",
                    "options": ["Harper Lee", "Jane Austen", "Mark Twain", "F. Scott Fitzgerald"],
                    "answer": "Harper Lee",
                    "hint": "The book was published in 1960."
                },
                {
                    "question": "What year did the Titanic sink?",
                    "options": ["1912", "1915", "1917", "1919"],
                    "answer": "1912",
                    "hint": "It sank after hitting an iceberg."
                },
                {
                    "question": "Which ancient civilization built the Machu Picchu?",
                    "options": ["Inca Civilization", "Maya Civilization", "Aztec Civilization", "Egyptian Civilization"],
                    "answer": "Inca Civilization",
                    "hint": "It's located in Peru."
                }
            ],
            "Science": [
                {
                    "question": "What is the chemical symbol for water?",
                    "options": ["H2O", "CO2", "NaCl", "O2"],
                    "answer": "H2O",
                    "hint": "It consists of two hydrogen atoms and one oxygen atom."
                },
                {
                    "question": "Who discovered penicillin?",
                    "options": ["Alexander Fleming", "Marie Curie", "Isaac Newton", "Albert Einstein"],
                    "answer": "Alexander Fleming",
                    "hint": "He accidentally discovered it in 1928."
                },
                {
                    "question": "What is the process by which plants make their own food called?",
                    "options": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"],
                    "answer": "Photosynthesis",
                    "hint": "It involves sunlight, carbon dioxide, and water."
                },
                {
                    "question": "What is the largest organ in the human body?",
                    "options": ["Skin", "Liver", "Brain", "Heart"],
                    "answer": "Skin",
                    "hint": "It covers the entire body."
                },
                {
                    "question": "Which gas is most abundant in the Earth's atmosphere?",
                    "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Argon"],
                    "answer": "Nitrogen",
                    "hint": "It makes up about 78% of the atmosphere."
                }
            ],
            "General Knowledge": [
                {
                    "question": "What is the capital of France?",
                    "options": ["Paris", "London", "Berlin", "Rome"],
                    "answer": "Paris",
                    "hint": "It's known as the 'City of Love'."
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Earth", "Mars", "Jupiter", "Venus"],
                    "answer": "Mars",
                    "hint": "It's named after the Roman god of war."
                },
                {
                    "question": "What is the world's longest river?",
                    "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
                    "answer": "Nile",
                    "hint": "It flows through northeastern Africa."
                },
                {
                    "question": "In which country would you find the Great Barrier Reef?",
                    "options": ["Australia", "Brazil", "Indonesia", "India"],
                    "answer": "Australia",
                    "hint": "It's the world's largest coral reef system."
                },
                {
                    "question": "What is the currency of Japan?",
                    "options": ["Yen", "Euro", "Dollar", "Pound"],
                    "answer": "Yen",
                    "hint": "It consists of coins and banknotes."
                }
            ]
        }
        
        # Variables
        self.current_topic = tk.StringVar()
        self.current_difficulty = tk.StringVar()
        self.current_question = 0
        self.score = 0
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Select Topic frame
        self.select_topic_frame = tk.Frame(self.master, bg="#2c3e50")
        self.select_topic_frame.pack(pady=20)
        
        topic_label = tk.Label(self.select_topic_frame, text="Select Topic:", bg="#2c3e50", fg="#ffffff", font=("Helvetica", 14))
        topic_label.pack(side="left", padx=10)
        
        self.topic_menu = tk.OptionMenu(self.select_topic_frame, self.current_topic, *self.questions.keys())
        self.topic_menu.config(bg="#34495e", fg="#ffffff", font=("Helvetica", 12))
        self.topic_menu.pack(side="left", padx=10)
        
        # Select Difficulty frame
        self.select_difficulty_frame = tk.Frame(self.master, bg="#2c3e50")
        self.select_difficulty_frame.pack(pady=20)
        
        difficulty_label = tk.Label(self.select_difficulty_frame, text="Select Difficulty:", bg="#2c3e50", fg="#ffffff", font=("Helvetica", 14))
        difficulty_label.pack(side="left", padx=10)
        
        self.difficulty_menu = tk.OptionMenu(self.select_difficulty_frame, self.current_difficulty, "Easy", "Medium", "Hard")
        self.difficulty_menu.config(bg="#34495e", fg="#ffffff", font=("Helvetica", 12))
        self.difficulty_menu.pack(side="left", padx=10)
        
        # Start button
        self.start_button = tk.Button(self.master, text="Start Quiz", bg="#16a085", fg="#ffffff", font=("Helvetica", 12), command=self.start_quiz)
        self.start_button.pack(pady=20)
        
        # Next button
        self.next_button = tk.Button(self.master, text="Next", bg="#16a085", fg="#ffffff", font=("Helvetica", 12), command=self.next_question)
        
        # Quit button
        quit_button = tk.Button(self.master, text="Quit", bg="#c0392b", fg="#ffffff", font=("Helvetica", 12), command=self.master.destroy)
        quit_button.pack(pady=5)
        
        # Hide select topic and difficulty frames initially
        self.select_topic_frame.pack_forget()
        self.select_difficulty_frame.pack_forget()
        self.next_button.pack_forget()  # Hide the Next button initially
    
    def start_quiz(self):
        self.score = 0
        self.questions_asked = []
        self.current_question = 0
        
        # Randomly select topic and difficulty
        self.current_topic.set(random.choice(list(self.questions.keys())))
        self.current_difficulty.set(random.choice(["Easy", "Medium", "Hard"]))
        
        # Display select topic and difficulty frames
        self.select_topic_frame.pack(pady=20)
        self.select_difficulty_frame.pack(pady=20)
        self.start_button.pack_forget()  # Hide the Start button
        self.next_button.pack(pady=20)  # Show the Next button
        
    def display_question(self):
        topic = self.current_topic.get()
        difficulty = self.current_difficulty.get()
        
        # Randomly select a question that hasn't been asked yet
        available_questions = [q for q in self.questions[topic] if q not in self.questions_asked]
        question_data = random.choice(available_questions)
        self.questions_asked.append(question_data)
        
        question_label = tk.Label(self.master, text=question_data["question"], bg="#2c3e50", fg="#ffffff", font=("Helvetica", 14))
        question_label.pack(pady=10)
        
        # Display options
        for option in question_data["options"]:
            option_button = tk.Button(self.master, text=option, bg="#34495e", fg="#ffffff", font=("Helvetica", 12), width=30, command=lambda o=option: self.check_answer(o, question_data["answer"]))
            option_button.pack(pady=5)
        
        # Hint button
        hint_button = tk.Button(self.master, text="Hint", bg="#3498db", fg="#ffffff", font=("Helvetica", 12), command=lambda: self.show_hint(question_data["hint"]))
        hint_button.pack(pady=10)
    
    def check_answer(self, selected_option, correct_answer):
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct.")
        else:
            messagebox.showinfo("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")
        
        self.next_question()
    
    def next_question(self):
        self.current_question += 1
        
        if self.current_question < 5:  # Show 5 questions
            self.clear_widgets()
            self.display_question()
        else:
            self.show_final_score()
    
    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
    
    def show_hint(self, hint):
        messagebox.showinfo("Hint", hint)
    
    def show_final_score(self):
        final_score_label = tk.Label(self.master, text=f"Final Score: {self.score}/5", bg="#2c3e50", fg="#ffffff", font=("Helvetica", 16))
        final_score_label.pack(pady=20)
        
        # Replay button
        replay_button = tk.Button(self.master, text="Replay", bg="#16a085", fg="#ffffff", font=("Helvetica", 12), command=self.replay_quiz)
        replay_button.pack(pady=10)
        
        # Quit button
        quit_button = tk.Button(self.master, text="Quit", bg="#c0392b", fg="#ffffff", font=("Helvetica", 12), command=self.master.destroy)
        quit_button.pack(pady=5)
    
    def replay_quiz(self):
        self.clear_widgets()
        self.create_widgets()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
