Minimax Battle Game 🎮

A turn-based battle game where an AI opponent uses the Minimax algorithm to decide its next move — built as my first university project for AIEN 201 Principles of AI.

How it works:

The AI looks 3 moves ahead and simulates every possible future:

What if it attacks?
What if it heals?
What if it blocks?


It then picks the move that gives it the best outcome, assuming you also play professionally. This is the core idea behind the Minimax algorithm.

Game Rules:

Both you and the enemy start at 100 HP
First to reach 0 HP loses
Block absorbs one hit then disappears
Heal cannot exceed 100 HP

What I learned

This project was my first hands-on experience with classical AI. Implementing Minimax taught me how an AI can "think ahead" by building a decision tree and choosing the path with the best outcome. The hardest part was understanding the maximizing and minimizing logic — how the AI assumes you will always play optimally against it.

Course:

AIEN 201 — Principles of AI

3rd Semester

Special thanks to Asst. Prof. Dr. Tolga Yırtıcı for making classical AI concepts clear and approachable.


Requirements:

Python 3.x
No external libraries needed
