# 🍽️ Restaurant Name Generator

A simple yet creative Python project that **generates unique restaurant names** based on your chosen restaurant type — **Fast Food, Cafe, or Fine Dining**.

This program randomly picks two words from text files (`.txt`) you provide and combines them to create 5 fun and stylish restaurant name ideas. Perfect for beginners learning file handling, randomization, and colorful console output in Python.

---

## 🧠 Features

- 🔹 Choose between **Fast Food**, **Cafe**, or **Fine Dining**.  
- 🔹 Reads from external `.txt` files (so you can easily add more names).  
- 🔹 Generates **5 unique name ideas** every time you run it.  
- 🔹 Colorful output using the **Colorama** library.  
- 🔹 Beginner-friendly and easy to expand.

---

## 🗂️ Project Structure

📁 Restaurant-Name-Generator
│

├── Restaurant Name Generator.py # Main Python script

├── Cafe.txt # List of cafe-related words/names

├── Fast Food.txt # List of fast food-related words/names

├── Fine Dining.txt # List of fine dining-related words/names

└── README.md # Project documentation (this file)





## ⚙️ How It Works

1. When you run the script, you’ll be asked to pick a restaurant type:
Fast Food

Cafe

Fine Dining


2. The program opens the corresponding `.txt` file (based on your choice).  
3. It randomly selects 2 words from the file.  
4. Combines them into a creative restaurant name.  
5. Repeats the process 5 times and displays the results in color.  

---

## 🧾 Example Output

Welcome To Restaurant Name Generator!

Choose restaurant type:

Fast Food

Cafe

Fine Dining
Enter your choice (1/2/3): 2

🍽️ Here are 5 Cafe restaurant names:

The Morning Dew The Cornerstone Coffee

The Afternoon Siesta The Pivot Point

The Zen Zone The Catalyst Coffee

The Philosopher's Stone The Heritage House

The Beehive Cafe The Concrete Cup

✨ Thank you for using Restaurant Name Generator!


---

## 🛠️ Requirements

Before running the program, make sure you have:

- **Python 3.8+**
- **Colorama** library (for colorful text output)

Install Colorama using pip:
```bash
pip install colorama
📚 How to Run
Clone or download this repository.

Place all three .txt files (Fast Food.txt, Cafe.txt, Fine Dining.txt) in the same folder as your .py file.

Open a terminal or command prompt in that folder.

Run the script:

bash
Copy code
python "Restaurant Name Generator.py"
Choose a restaurant type and enjoy the results!

🧩 Customization
You can easily expand the name lists:

Open any of the .txt files.

Add or remove lines (each line should be one name or phrase).

The generator will automatically use your updated list next time you run it.

💡 Example .txt File (Cafe.txt)
rust
Copy code
The Bookworm's Brew
The Writer's Block Cafe
The Artful Latte
The Palette Coffeehouse
The Midnight Oil
The Hourglass Cafe
The Chronicle Coffee
The Pen & Pour
The Curator's Cup
The Archivist's Nook
The Philosopher's Stone
The Daily Ritual
The Common Ground
The Sanctuary Cafe
The Solitude Spot
The Haven Coffee
The Retreat House
The Quiet Corner
The Backstreet Bean
👨‍💻 Author
Rakibul Islam
🌍 From Bangladesh 🇧🇩
💬 Passionate about coding, creativity, and learning Python.

📜 License
This project is open-source and free to use for learning or personal projects.
