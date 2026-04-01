Atanya Kumari – Web Developer Portfolio

This is my personal portfolio website showcasing my skills, projects, and certifications as a frontend developer. The project includes a Flask backend for handling contact form submissions and storing messages in a PostgreSQL database.

Live Website:
https://69cb7db067eeec5994d71dbc--gleaming-sundae-7eb36d.netlify.app/

DB:
https://console.neon.tech/app/projects/billowing-water-26071935/branches/br-soft-mode-anrqe6vn/sql-editor?database=neondb

## About the Project

This portfolio is designed to highlight my journey as a BCA student and frontend developer, focusing on:

- Clean UI/UX design
- Responsive layouts
- Structured and maintainable code
- Real-world project presentation
- Backend integration for contact form

## Features

- Fully responsive design (mobile and desktop)
- Smooth scrolling navigation
- Minimal and modern UI
- Skills visualization with progress bars
- Project showcase section
- Certificates section
- Contact form with backend integration (stores messages in database)
- CORS enabled for cross-origin requests

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python Flask
- PostgreSQL (NeonDB)
- Flask-CORS for cross-origin support

## Prerequisites

Before running this application locally, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/taniecore25-source/my-portfolio.git
   cd my-portfolio
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `backend` directory with your database URL:
   ```
   DATABASE_URL=your_neon_db_connection_string_here
   ```

## Running the Application

1. Start the backend server:
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python app.py
   ```
   The backend will run on `http://127.0.0.1:5001`

2. Start the frontend server (in a new terminal):
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   The frontend will be available at `http://localhost:8000`

3. Open your browser and navigate to `http://localhost:8000` to view the portfolio.

## API Endpoints

- `POST /send_message`: Accepts JSON with `name`, `email`, and `message` fields to store contact form submissions in the database.

## Hosting

This project is hosted on Netlify for the frontend, with the backend deployed separately.

## Sections Included

- Home
- About Me
- Skills
- Projects
- Certificates
- Contact

## Contact

- Email: atanyakumari109@gmail.com
- LinkedIn: https://linkedin.com/in/atanya-kumari

## Future Improvements

- Add real project links (GitHub or live demos)
- Improve animations and transitions
- Add dark mode toggle
- Enhance backend with additional features

## Acknowledgment

This portfolio is part of my continuous learning journey in web development and reflects my dedication to improving my skills every day.
