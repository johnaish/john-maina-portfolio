
# John Maina — Portfolio (Django + Frontend)

This is a starter Django project for a personal portfolio for **John Maina**.
Accent color: **grey**. Tagline chosen automatically.

## Features
- Home, About, Portfolio, Blog, Contact pages
- Admin panel to manage Profile, Projects, Posts and Contact messages
- Upload images (Pillow required)
- Animated frontend using GSAP (included via CDN)
- Tailwind-like styles via CDN for quick styling

## Quickstart (Linux / macOS / WSL / Windows PowerShell)
```bash
python -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin/` to login.

Static files are served by Django in DEBUG mode. Uploaded media will be in `media/`.



## What I added for you
- Simple custom dashboard (login at /admin-login/) to add Projects and Posts without using Django admin.
- Management command `createsampledata` to create a superuser (admin/adminpass) and sample Profile/Projects/Posts.
- Tailwind build pipeline files (package.json, tailwind.config.js). Run `npm install` and `npm run build:css` to generate `static/css/tailwind.css`.
- Deployment files for Heroku/Render (Procfile, runtime.txt). Whitenoise included in requirements.
- Improved animations using GSAP on the homepage.


## Final polish — what I completed for you
- Full CRUD for Projects and Posts in the custom dashboard (create/edit/delete).
- Local placeholder 'built' CSS included at `static/css/tailwind.css` so the site looks consistent without running npm.
- Admin site branding template added.
- Safe deletion of uploaded images when items are removed from the dashboard.

Everything is wired and ready. To get the site running locally: follow README steps, run migrations, run `python manage.py createsampledata` to create admin/adminpass and sample content, then `python manage.py runserver`.
