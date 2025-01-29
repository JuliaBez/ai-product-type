AI Product Type
📌 Description
AI Product Type is an API built with Django and Django REST Framework.

The project includes a simple frontend (index.html) that interacts with the API.

🚀 Technologies Used
Django 4.2.7 – A high-level Python web framework.
Django REST Framework 3.14.0 – Toolkit for building Web APIs in Django.
g4f 0.4.3.5 – AI-based tool for free chatbot access.
ReportLab 3.4.0 & 3.5.34 – Library for generating PDFs in Python.

📂 Installation and Setup

1️⃣ Clone the repository

git clone https://github.com/JuliaBez/ai-product-type.git
cd ai-product-type

2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Apply database migrations

python manage.py migrate

5️⃣ Run the Django API

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

🌍 Running the Frontend (index.html)

The project includes a simple HTML frontend (index.html). To run it:
Navigate to the folder where index.html is located.
Open the file in a browser.


🔧 API Endpoints
Method	Endpoint	Description
GET	/tasks/	List all tasks
POST	/tasks/	Create a new task
GET	/tasks/<id>/	Retrieve a specific task
PUT	/tasks/<id>/	Update a specific task
DELETE	/tasks/<id>/	Delete a specific task
GET	/export/pdf/	Export tasks as a PDF
POST	/chatbot/	Interact with the chatbot AI


