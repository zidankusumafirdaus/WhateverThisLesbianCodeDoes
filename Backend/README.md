# ArchiveKKN API

Minimal CRUD API for proker (projects) with related materials, tools, and sourcing locations.

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` with database connection:

```
SQLALCHEMY_DATABASE_URL=mysql+pymysql://USER:PASSWORD@HOST:3306/DBNAME
JWT_SECRET_KEY=your_jwt_secret
JWT_ACCESS_TOKEN_EXPIRES_MINUTES=60
ADMIN_USERNAME=admin
ADMIN_PASSWORD=strongpassword
```

## Run

```bash
python server.py
```

## Load Testing (Locust)

Install Locust and run the load test:

```powershell
pip install locust
locust -f locustfile.py --host http://localhost:5000
```

Open the Locust UI at `http://localhost:8089`.

### Locust environment variables
- `API_USERNAME` and `API_PASSWORD`: credentials for `/api/auth/login`.
- `LOCUST_ENABLE_WRITES`: set `false` to disable write tests.

Example (PowerShell):
```powershell
$env:API_USERNAME="admin"
$env:API_PASSWORD="strongpassword"
$env:LOCUST_ENABLE_WRITES="true"
```

## Endpoints

- `POST /api/auth/login`
- `GET /api/projects/`
- `POST /api/projects/`
- `GET /api/projects/<id>`
- `PUT /api/projects/<id>`
- `DELETE /api/projects/<id>`
- `GET /api/icons/`
- `GET /api/icons/<id>`
- `GET /api/icons/display/<path:filename>`

`/api/icons/display/<path:filename>` serves files from `Backend/apps/icons/`.

If you use **Option B** (store a relative filename in `icons.svg_path`, e.g. `education/book.png`), you can build the image URL like this:

`{{baseUrl}}/api/icons/display/{{svg_path}}`

### Example payload

```json
{
  "title": "Digitalisasi Tata Kelola Desa",
  "description": "Empowering the local community...",
  "status": "IN PROGRESS",
  "start_date": "2026-07-15",
  "end_date": "2026-08-30",
  "location": "Desa Sukamaju, West Java",
  "volunteer_count": 15,
  "photo_url": "https://example.com/photo.jpg",
  "materials": [
    {
      "item_name": "Wireless Routers",
      "quantity": 3,
      "unit": "PCS",
      "estimated_price": 450000,
      "total_cost": 1350000
    }
  ],
  "tools": [
    {
      "icon_id": 1,
      "name": "Cable Crimper",
      "category": "Networking"
    }
  ],
  "sourcing_locations": [
    {
      "store_name": "Toko Elektronik Makmur",
      "address": "Jl. Raya Provinsi No. 12, Sukamaju",
      "distance_km": 2.5,
      "provides": "Routers, Switches",
      "google_maps_url": "https://maps.google.com"
    }
  ]
}
```

### Auth
Login to get a JWT access token, then send it in the `Authorization` header.

Protected endpoints:
- `POST /api/projects/`
- `PUT /api/projects/<id>`
- `DELETE /api/projects/<id>`

**Login request**
```json
{
  "username": "admin",
  "password": "strongpassword"
}
```

**Auth header**
```
Authorization: Bearer <access_token>
```

### Pagination, filtering, search
Supported query params on `GET /api/projects/`:
- `page` (default 1)
- `page_size` (default 10, max 100)
- `status`
- `location`
- `title`
- `search` (matches title or description)

Example:
```
/api/projects?page=1&page_size=10&status=IN%20PROGRESS&search=digital
```

### Partial update payload (PUT)
```json
{
  "status": "DONE",
  "end_date": "2026-09-01",
  "volunteer_count": 20
}
```

### Error response examples
**Validation error (422)**
```json
{
  "message": "Validation error.",
  "errors": {
    "title": ["Missing data for required field."],
    "start_date": ["Not a valid date."]
  }
}
```

**Not found (404)**
```json
{
  "message": "Project not found."
}
```

### List response shape
```json
{
  "message": "OK",
  "data": {
    "items": [
      {
        "id": 1,
        "title": "..."
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 10,
      "total_items": 100,
      "total_pages": 10
    }
  }
}
```

## Migrations (Alembic)
Initialize a revision based on models:

```powershell
alembic revision --autogenerate -m "init"
```

Apply migrations:

```powershell
alembic upgrade head
```
