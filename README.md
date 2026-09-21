Multilingual NLP Text Analyzer
A desktop NLP tool (Tkinter GUI) that analyzes English text using spaCy —
performing Part-of-Speech tagging, Named Entity Recognition, basic rule-based
grammar correction, and a template-based Hindi/Telugu translation demo for a
sample set of sentences.
Features
POS Tagging & Named Entity Recognition (NER) — uses spaCy's pretrained
en_core_web_sm model to tag each word with its part of speech and detect
named entities (people, places, organizations, etc.)
Rule-Based Grammar Correction — capitalizes the first letter and applies
simple past-tense word substitutions (e.g., "go" → "went") when the word
"yesterday" appears in the sentence
Sample Translation — maps a fixed set of 10 pre-defined English
sentences to their Hindi and Telugu translations, for demonstration purposes
Simple GUI — built with Tkinter for entering text and viewing results
Scope & Limitations
This is a learning/demo project, not a production translation or grammar
correction system:
Translation only works for the 10 exact sentences defined in the
dictionary — it is not a general-purpose translator
Grammar correction uses simple string substitution rules, not a trained
grammar model
The POS tagging and NER components are genuine, using spaCy's real
pretrained pipeline
Tech Stack
Python
spaCy (en_core_web_sm pretrained model)
Tkinter (GUI)
Setup
Bash
How It Works
User enters an English sentence in the input box
The app applies basic grammar correction rules
spaCy processes the corrected text to extract POS tags and named entities
If the sentence matches one of the 10 sample sentences, its Hindi and
Telugu translation is displayed
Results are shown in the output panel: corrected text, translation, and a
word-by-word POS/NER breakdown
Future Scope
Replace the fixed translation dictionary with a real translation API or
trained neural machine translation model
Replace rule-based grammar correction with a trained grammar-correction
model
Expand language support beyond Hindi and Telugu
