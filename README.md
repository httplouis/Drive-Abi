# Drive.Abi 🚗

A modern, full-featured car rental and sales web application built with Django. Drive.Abi provides a seamless experience for customers to browse, rent, and purchase vehicles, with a comprehensive admin dashboard for managing inventory.

![Django](https://img.shields.io/badge/Django-5.0.4-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

## 🌟 Features

### Public Features
- **Car Browsing**: Browse available cars with detailed information
- **Car Rental**: Rent cars with easy-to-use interface
- **Car Sales**: Purchase vehicles directly through the platform
- **Membership System**: Join membership program for exclusive benefits
- **User Registration**: Create account and manage profile
- **Responsive Design**: Modern, mobile-friendly interface
- **Blog & News**: Stay updated with latest news and blog posts

### Admin Features
- **Admin Dashboard**: Comprehensive overview with statistics
- **Car Management**: Full CRUD operations for car inventory
  - Create new car entries
  - Update car information
  - Delete cars
  - View detailed car information
- **Statistics Tracking**: Monitor total cars, memberships, and users
- **Clean Admin Interface**: Professional sidebar navigation

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/httplouis/Drive-Abi.git
   cd Drive-Abi
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for Django admin)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Public site: http://127.0.0.1:8000/
   - Admin dashboard: http://127.0.0.1:8000/admin/
   - Django admin: http://127.0.0.1:8000/admin/ (Django's built-in admin)

## 📁 Project Structure

```
Drive-Abi/
├── myapp/                    # Main application
│   ├── templates/
│   │   └── myapp/
│   │       ├── admin/        # Admin templates
│   │       │   ├── dashboard.html
│   │       │   ├── car_manage.html
│   │       │   └── ...
│   │       └── ...          # Public templates
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   ├── forms.py             # Django forms
│   └── admin.py             # Django admin configuration
├── myproject/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                  # Static files (CSS, images)
├── manage.py               # Django management script
└── README.md               # This file
```

## 🎯 Key URLs

### Public Routes
- `/` - Homepage
- `/cars/` - Browse all cars
- `/cars/<id>/` - Car details
- `/rentcar/` - Rent a car
- `/buycar/` - Buy a car
- `/membership/` - Membership registration
- `/about/` - About page
- `/blog/` - Blog page

### Admin Routes
- `/admin/` - Admin dashboard
- `/admin/cars/` - Manage cars
- `/admin/cars/create/` - Add new car
- `/admin/cars/<id>/update/` - Edit car
- `/admin/cars/<id>/delete/` - Delete car

## 🛠️ Technologies Used

- **Backend**: Django 5.0.4
- **Frontend**: HTML5, Tailwind CSS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Inter (body), Montserrat (headings)
- **Database**: SQLite (default)

## 📊 Models

- **Car**: Vehicle information (brand, model, year, price, seats, image, description)
- **Membership**: Customer membership details
- **Addbook**: Book management
- **sign1**: User authentication

## 🎨 Design Features

- Modern, clean interface
- Responsive design for all devices
- Professional color scheme (red gradient primary)
- Smooth transitions and hover effects
- Accessible navigation

## 👨‍💻 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**httplouis**
- GitHub: [@httplouis](https://github.com/httplouis)

## 🙏 Acknowledgments

- Django community for excellent documentation
- Tailwind CSS for the utility-first CSS framework
- Font Awesome for beautiful icons

---

⭐ If you find this project helpful, please consider giving it a star!

