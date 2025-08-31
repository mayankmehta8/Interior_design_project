🏡 Interior Design Project

A Flask web application that transforms room images into new interior design styles using ControlNet on a fine-tuned Stable Diffusion XL (SDXL) model.
The app takes an input image, preserves the room’s layout, and re-renders it according to a user-selected design style (e.g., modern, minimalist, classic).

✨ Features

Upload an image of a room (living room, bedroom, etc.)

Choose from multiple interior design styles

Generates a new image while preserving the layout

Powered by ControlNet + Fine-tuned SDXL

Flask-based simple web UI

🛠️ Tech Stack

Backend: Flask (Python)

ML Model: Stable Diffusion XL (fine-tuned) + ControlNet

Libraries:

diffusers / transformers (Hugging Face)

PyTorch

OpenCV, Pillow

Flask, Werkzeug

Frontend: HTML, CSS, JavaScript (Flask templates)

📂 Project Structure
Interior_design_project/
│── app.py                # Flask entry point
│── static/               # Static files (CSS, JS, images)
│── templates/            # HTML templates for UI
│── models/               # Pretrained & fine-tuned models
│── uploads/              # User-uploaded images
│── outputs/              # Generated images
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation

⚡ Installation & Setup

Clone the repository

git clone https://github.com/mayankmehta8/Interior_design_project.git
cd Interior_design_project


Create a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Download models

Place your fine-tuned SDXL model and ControlNet weights inside the models/ directory.

You may need a Hugging Face access token to download.

Run the app

python app.py


Open in browser:

http://127.0.0.1:5000/

🎨 Usage

Upload a room image (e.g., bedroom.jpg).

Select a design style from the dropdown (e.g., Modern, Minimalist, Classic).

Click Generate.

Wait while the model processes the image.

View/download the AI-styled interior design.

📸 Example (before → after)
Input	


<img width="461" height="494" alt="Screenshot 2025-08-31 at 4 16 22 PM" src="https://github.com/user-attachments/assets/c944950d-d8f3-4fd2-9e3f-308a86607ff2" />

Output



<img width="543" height="441" alt="Screenshot 2025-08-31 at 4 14 59 PM" src="https://github.com/user-attachments/assets/934c9954-64fc-4f93-ae85-55cc6a3c6ee9" />
	
🤝 Contributing

Contributions are welcome!
If you’d like to add new styles, improve UI, or optimize inference:

Fork the repo

Create a new branch (feature-new-style)

Commit changes and push

Submit a PR 🚀

📜 License

This project is licensed under the MIT License.

📧 Contact

👤 Mayank Mehta

GitHub: mayankmehta8

LinkedIn: Mayank Mehta

