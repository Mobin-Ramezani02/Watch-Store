# ⌚ TicArt - Online Watch Store

A complete, modern, and full-stack e-commerce project designed for selling luxury watches. This website is developed using the powerful **Django** framework on the backend and **Tailwind CSS** on the frontend, featuring cutting-edge web design trends like Glassmorphism and Neumorphism.

## ✨ Key Features & Highlights

* **Ultra-Modern UI/UX:** Features Glassmorphism (frosted glass) effects, smooth card hover animations, and appealing soft gradients instead of flat, monotonous colors.

* **Dark/Light Mode:** Full support for dark and light themes utilizing Tailwind CSS. User preferences are securely saved in the browser's `LocalStorage` to prevent color flashing during page reloads.

* **Smart Shopping Cart:** Session-based cart implementation. Users (even unregistered guests) can effortlessly add items to their carts. The total item count is dynamically displayed in the header across all pages via a Django Context Processor.

* **Authentication & User Management:**
  * Secure registration, login, and logout systems (utilizing secure POST methods for logging out).
  * Smart Login Modal: A beautiful pop-up that prompts guest users to log in or register before checking out.
  * Dedicated User Dashboard: A personalized space for users to track their order history and payment statuses.

* **Flexible Product Database:** Utilizes `ManyToMany` relationships for product categorization. This means a single watch can simultaneously belong to multiple categories (e.g., "Men's", "Classic", and "Leather Band").

* **Display Optimizations:**
  * Custom, responsive sliding sidebar menu tailored for mobile and tablet devices.
  * Standardized currency formatting (thousands separators) powered by Django's `humanize` module.
  * Uncropped product image rendering (`object-contain`) combined with smart background blending (`mix-blend`) for seamless product cards.

## 🛠️ Technology Stack

* **Backend:** Python, Django 5.x
* **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JavaScript
* **Database:** SQLite (Default - Easily upgradeable to PostgreSQL for production)
* **Image Processing:** Pillow library (For handling product image uploads in the Admin panel)

## 📁 Project Structure

```text
TicArt_Project/
├── core/                   # Main project settings and root URLs (settings.py, urls.py)
├── shop/                   # Main store app (Product models, Categories, Views)
├── cart/                   # Shopping cart app (Session management, Context Processors)
├── orders/                 # Order management app (Checkout forms, Total calculation)
├── users/                  # User authentication app (Login, Registration, Profiles)
├── templates/              # HTML templates (includes base.html and app-specific templates)
├── static/                 # Custom static files (Custom CSS, static images)
├── media/                  # User-uploaded files (Product images uploaded via Admin)
├── manage.py               # Main Django execution file
└── requirements.txt        # Python dependencies list
```

## 🚀 Local Development Setup

To run this project on your local machine, follow these steps in your terminal or command prompt:

### 1. Navigate to the Project Directory
Clone or download the source code and navigate to the root folder (where `manage.py` is located).

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
```
Activate on **Windows**:
```cmd
venv\Scripts\activate
```
Activate on **Mac/Linux**:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Ensure your virtual environment is active (you should see `(venv)` in your terminal), then run:
```bash
pip install -r requirements.txt
```

### 4. Setup the Database
Run the following commands to create the database tables (for products, orders, and users):
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
To access the Django admin panel and start adding categories and watches, create an admin account:
```bash
python manage.py createsuperuser
```
*(Follow the prompts to set your username, email, and password).*

### 6. Run the Development Server
```bash
python manage.py runserver
```
The store is now live at `http://127.0.0.1:8000`. You can access the powerful admin panel at `http://127.0.0.1:8000/admin`.

## 🌍 Production Deployment

If you plan to deploy this project to a live server or cloud platform (PaaS), ensure you complete the following checklist:

1. Open `core/settings.py` and set `DEBUG = False`.
2. Add your live domain name or server IP address to the `ALLOWED_HOSTS` list.
3. Run the `python manage.py collectstatic` command in your terminal to gather all static files into the designated `staticfiles` folder.
4. Deploy the project (excluding the `venv` folder) to your server and run the `migrate` command on your production server to set up the live database.

---
*Developed with modern web standards to create the ultimate online shopping experience.*
