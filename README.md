![GitHub License](https://img.shields.io/github/license/Nabellaleen/okre-app)

# OKRE

**OKRE** is a Django-based web application designed to facilitate
the management of OKRs (Objectives and Key Results) within
organizations. It provides a user-friendly interface for
setting, tracking, and achieving goals collaboratively.

---

## Key Features

- Manage OKRs at organization and team level
- Set and track objectives and key results
- Handle multiple organizations

## Documentation

- [Quick Start Guide](docs/quickstart.md) (to be added)
- [Contributing Guide](docs/contributing.md) (to be added)

---

## Tech Stack

- **Backend**: Django
- **Frontend**: Django templates + DaisyUI (Tailwind CSS)
- **Database**: SQLite

---

## Getting Started

### Requirements

- Python 3.8 or higher
- Node 20 or higher _(used by [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html#configuration-of-the-path-to-the-npm-executable))_

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Nabellaleen/okre-app.git
   cd okre-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Development

### Run the app locally

To run the development server and start using OKRE, you need to run both the Django server and the Tailwind CSS build process.

- Start the Django server:
   ```bash
   python manage.py runserver
   ```
- Start the Tailwind CSS build process:
   ```bash
   python manage.py tailwind start
   ```

Then open http://localhost:8000 in your web browser.

### Create a superuser

To create a superuser account for accessing the Django admin interface, run the following command:

```bash
python manage.py createsuperuser
```

---

## License

This project is licensed under the GNU AGPL v3. See the [LICENSE](LICENSE.md) file for details.

## Contributing

We welcome contributions to OKRE! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
