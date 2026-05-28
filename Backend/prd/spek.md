# PRD — ArchiveKKN Backend API (Projects)

## 1. Background
ArchiveKKN needs a lightweight backend to manage KKN work program (project) data and its supporting needs (materials, tools, and sourcing locations). This API is the primary data source for the frontend/admin apps.

## 2. Objectives
- Provide CRUD endpoints for project data and its related entities.
- Maintain data consistency and validation based on schema rules.
- Return response structures ready for frontend consumption.

## 3. Scope
### In-scope
- CRUD `Project`.
- Related entities: `Material`, `Tool`, `SourcingLocation` as part of the project payload.
- Payload validation with Marshmallow.
- Persistence to MySQL via SQLAlchemy.
- JWT-based authentication for write endpoints.
- Pagination, filtering, and search on project listing.
- Dedicated read endpoints for icons.
- Database migrations with Alembic.

### Out-of-scope
- User and role management.
- File upload (photo/media).
- Icon CRUD (create/update/delete).

## 4. Stakeholders
- KKN admin/operators (data entry).
- Frontend team (API consumers).
- Project supervisors (monitoring).

## 5. Assumptions & Dependencies
- MySQL database is available and configured via `.env`.
- Application runs on Python 3.x.
- Related entities are embedded as arrays in the project payload.

## 6. Technical Architecture (Brief)
- Framework: Flask.
- ORM: SQLAlchemy.
- Validation: Marshmallow.
- Database: MySQL (via PyMySQL).

## 7. Core Data Models
### Project
- `id` (int, PK)
- `title` (string, required)
- `description` (text, optional)
- `status` (string, optional)
- `start_date` (date, required)
- `end_date` (date, optional)
- `location` (string, optional)
- `volunteer_count` (int, optional)
- `photo_url` (text URL, optional; not a file upload)
- `created_at`, `updated_at` (datetime)

### Material
- `project_id` (FK)
- `item_name`, `quantity`, `unit` (required)
- `estimated_price`, `total_cost` (numeric)

### Tool
- `project_id` (FK)
- `icon_id` (FK)
- `name`, `category` (required)

### SourcingLocation
- `project_id` (FK)
- `store_name`, `address`, `distance_km` (required)
- `provides`, `google_maps_url` (optional)

## 8. API Specification
### Base URL
`/api/projects`

### Endpoints
- `GET /` → list projects
- `POST /` → create project + related entities
- `GET /<id>` → project detail
- `PUT /<id>` → update project + related entities
- `DELETE /<id>` → delete project

### Auth
- `POST /api/auth/login` → get access token

### Icons
- `GET /api/icons/` → list icons
- `GET /api/icons/<id>` → icon detail

### Response Shape (Project)
```
{
  "id": 1,
  "title": "...",
  "description": "...",
  "status": "...",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "location": "...",
  "volunteer_count": 10,
  "photo_url": "...",
  "created_at": "...",
  "updated_at": "...",
  "materials": [...],
  "tools": [...],
  "sourcing_locations": [...]
}
```

### Error Handling
- 404: project not found
- 422: validation error (Marshmallow)
- 500: unexpected server error

## 9. Non-Functional Requirements
- Maintain relationship consistency on create/update (replace-all strategy).
- Response time < 500ms for typical operations on small-to-medium datasets.
- Minimal application-level logging.

## 10. UX/Integration
- `Project` payload may include all related entities as arrays.
- Frontend does not need separate endpoints for materials/tools/locations.

## 11. Risks & Mitigations
- **Data loss on relation update**: replace-all strategy can remove omitted relations → document this clearly.
- **DB connectivity issues**: validate `.env` and add monitoring.

## 12. High-Level Milestones
- M1: Project CRUD + relations (already available)
- M2: Auth/JWT (implemented — `/api/auth/login` + JWT-protected routes)
- M3: Pagination & filters (backlog)
