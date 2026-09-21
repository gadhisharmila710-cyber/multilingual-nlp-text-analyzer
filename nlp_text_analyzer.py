import spacy
import tkinter as tk
from tkinter import scrolledtext

# ===============================
# Load Model
# ===============================
print("Loading model...")
nlp = spacy.load("en_core_web_sm")
print("Model loaded successfully")


# ===============================
# Grammar Correction (Rule-Based)
# ===============================
def grammar_correct(text):
    text = text.strip()

    if text:
        text = text[0].upper() + text[1:]

    words = text.lower().split()

    # Past tense corrections
    if "yesterday" in words:
        text = text.replace("go", "went")
        text = text.replace("goes", "went")
        text = text.replace("eat", "ate")
        text = text.replace("eats", "ate")
        text = text.replace("play", "played")
        text = text.replace("plays", "played")
        text = text.replace("come", "came")
        text = text.replace("comes", "came")
        text = text.replace("see", "saw")
        text = text.replace("sees", "saw")

    return text


# ===============================
# Translation Dictionary (10 sample sentences)
# ===============================
def translate_text(text):
    text = text.lower()

    translations = {
        "he went to school yesterday":
            ("वह कल स्कूल गया था", "అతను నిన్న పాఠశాలకు వెళ్లాడు"),

        "she ate food yesterday":
            ("उसने कल खाना खाया", "ఆమె నిన్న భోజనం చేసింది"),

        "they played cricket yesterday":
            ("उन्होंने कल क्रिकेट खेला", "వారు నిన్న క్రికెట్ ఆడారు"),

        "i went to market yesterday":
            ("मैं कल बाजार गया था", "నేను నిన్న మార్కెట్‌కు వెళ్లాను"),

        "we came home yesterday":
            ("हम कल घर आए", "మేము నిన్న ఇంటికి వచ్చాము"),

        "he saw a movie yesterday":
            ("उसने कल एक फिल्म देखी", "అతను నిన్న సినిమా చూశాడు"),

        "she played in park yesterday":
            ("वह कल पार्क में खेली", "ఆమె నిన్న పార్క్‌లో ఆడింది"),

        "they ate mango yesterday":
            ("उन्होंने कल आम खाया", "వారు నిన్న మామిడి తిన్నారు"),

        "i saw my friend yesterday":
            ("मैंने कल अपने दोस्त को देखा", "నేను నిన్న నా స్నేహితుడిని చూశాను"),

        "we went to temple yesterday":
            ("हम कल मंदिर गए", "మేము నిన్న ఆలయానికి వెళ్లాము")
    }

    if text in translations:
        hi, te = translations[text]
        return f"Hindi: {hi}\nTelugu: {te}"

    return "Hindi: Translation not available\nTelugu: Translation not available"


# ===============================
# Processing
# ===============================
def process_text(text):
    output = ""

    corrected = grammar_correct(text)
    doc = nlp(corrected)

    # Corrected text
    output += "CORRECTED TEXT\n----------------\n"
    output += corrected + "\n\n"

    # Translation
    output += "TRANSLATION\n----------------\n"
    output += translate_text(corrected) + "\n\n"

    # POS + NER
    output += "TOKEN ANALYSIS\n----------------\n"
    output += "WORD\tPOS\tNER\n"

    for token in doc:
        ner = token.ent_type_ if token.ent_type_ else "OTHER"
        output += f"{token.text}\t{token.pos_}\t{ner}\n"

    return output


# ===============================
# GUI
# ===============================
def run_app():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter text.")
        return

    result = process_text(text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


# ===============================
# UI
# ===============================
root = tk.Tk()
root.title("Multilingual NLP App")
root.geometry("700x600")

title = tk.Label(root, text="Multilingual NLP App", font=("Arial", 16, "bold"))
title.pack(pady=10)

input_label = tk.Label(root, text="Enter Text:")
input_label.pack()

input_text = scrolledtext.ScrolledText(root, height=5)
input_text.pack(padx=10, pady=5, fill="x")

run_button = tk.Button(root, text="Process", command=run_app)
run_button.pack(pady=10)

output_label = tk.Label(root, text="Output:")
output_label.pack()

output_box = scrolledtext.ScrolledText(root, height=15)
output_box.pack(padx=10, pady=5, fill="both", expand=True)

root.mainloop()
