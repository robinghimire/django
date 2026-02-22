# Robin Ghimire – Django Portfolio

A modern, responsive portfolio website built with Django and Tailwind CSS. Features user authentication, admin dashboard, and smooth animations for a professional presentation.

## Features

- 🎨 **Modern UI** - Built with Tailwind CSS with warm color theme
- 🔐 **User Authentication** - Login, logout, and sign-up functionality
- 📊 **Admin Dashboard** - Django admin interface for content management
- ✨ **Smooth Animations** - Scroll effects, hover animations, and transitions
- 📱 **Responsive Design** - Mobile-first approach with adaptive layouts
- 🎯 **SEO Optimized** - Proper meta tags and semantic HTML
- 🌙 **Theme Support** - Light warm theme with CSS variables

## Tech Stack

- **Backend**: Django 4.x
- **Frontend**: Tailwind CSS 3.x, HTML5, JavaScript
- **Styling**: PostCSS, Autoprefixer
- **Package Manager**: npm for CSS build tools

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+ (for CSS build tools)

### 1. Clone & Setup Python Environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
npm install
```

### 3. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser  # Create admin user
```

### 4. Build CSS
```bash
npm run dev    # Watch mode for development
npm run build  # Minified for production
```

### 5. Run Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

## Project Structure

```
Robin_Ghimire_Django_Portfolio/
├── accounts/              # User authentication (login/signup)
├── core/                  # Main application views
├── rg_portfolio/          # Django project settings
├── templates/             # HTML templates
├── static/                # Compiled CSS/JS
├── assets/src/            # Source CSS files
│   ├── index.css         # Main Tailwind entry
│   └── app.css           # Component styles
├── manage.py
├── requirements.txt
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## Available URLs

### Public Routes
- `/` - Home page
- `/accounts/login/` - Login page
- `/accounts/signup/` - Sign up page
- `/accounts/logout/` - Logout

### Admin
- `/admin/` - Django admin interface

## Development Workflow

### CSS Development
```bash
npm run dev    # Watches for CSS changes and rebuilds automatically
```

### Django Development
```bash
python manage.py runserver
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Customization

### Theme Colors
Edit CSS variables in [assets/src/index.css](assets/src/index.css):
```css
:root {
  --primary: 45 100% 60%;        /* Yellow/Gold */
  --background: 220 20% 7%;      /* Dark Blue */
  --foreground: 210 20% 92%;     /* Light Text */
}
```

### Tailwind Configuration
Modify [tailwind.config.js](tailwind.config.js) to customize:
- Color schemes
- Typography
- Spacing
- Responsive breakpoints

## Production Deployment

1. Set `DEBUG=False` in Django settings
2. Configure `ALLOWED_HOSTS` for your domain
3. Use environment variables for `SECRET_KEY`
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Set up HTTPS with SSL certificates
7. Configure a reverse proxy (Nginx)

## Environment Variables

Create a `.env` file:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@localhost/dbname
```

## Deployment & Maintenance

This is a private portfolio project. For questions about the code or deployment, contact the owner.

## License

This is a private portfolio. All rights reserved.

## Contact

- LinkedIn: [Robin Ghimire](https://www.linkedin.com/in/robinghimire)
- GitHub: [@robinghimire](https://github.com)
- Email: robin@example.com

---

**Built with ❤️ by Robin Ghimire**
