# Task Breakdown — ArchiveKKN Backend PRD

## Epics
1. Project CRUD & Relations
2. Validation & Error Handling
3. Infrastructure Readiness & Documentation
4. Future Development Backlog

## Tasks (Detail)
### 1) Project CRUD & Relations
- [x] Implement `GET /api/projects/` list
- [x] Implement `POST /api/projects/` create + nested relations
- [x] Implement `GET /api/projects/<id>` detail
- [x] Implement `PUT /api/projects/<id>` update + replace-all relations
- [x] Implement `DELETE /api/projects/<id>` delete project + relations

### 2) Validation & Error Handling
- [x] Marshmallow schemas for `Project`, `Material`, `Tool`, `SourcingLocation`
- [x] Return 422 for validation errors
- [x] Return 404 when project is not found
- [x] Standardize response wrapper (`success_response`, `error_response`) in all handlers
- [x] Add minimal logging for 500 errors

### 3) Infrastructure & Documentation
- [x] `.env` with `SQLALCHEMY_DATABASE_URL`
- [x] Setup and endpoint documentation in `README.md`
- [x] Add error response examples to documentation
- [x] Add partial update payload example

### 4) Future Development Backlog
- [x] Authentication & authorization (JWT)
- [x] Pagination, filtering, search
- [x] Dedicated endpoints for icons
- [x] `photo_url` as text URL (no upload)
- [x] Database migrations (Alembic)

## Suggested Priorities
1. Standardize response wrapper
2. Minimal logging
3. Error & partial update documentation
4. Auth/JWT
5. Pagination & filters
