from sqlalchemy import or_
from sqlalchemy.orm import selectinload

from apps.models import Material, Project, SourcingLocation, Tool
from apps.utils.serializers import to_date, to_number


def _project_to_dict(project):
    return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "status": project.status,
        "start_date": to_date(project.start_date),
        "end_date": to_date(project.end_date),
        "location": project.location,
        "volunteer_count": project.volunteer_count,
        "photo_url": project.photo_url,
        "created_at": to_date(project.created_at),
        "updated_at": to_date(project.updated_at),
        "materials": [
            {
                "id": item.id,
                "item_name": item.item_name,
                "quantity": item.quantity,
                "unit": item.unit,
                "estimated_price": to_number(item.estimated_price),
                "total_cost": to_number(item.total_cost),
            }
            for item in project.materials
        ],
        "tools": [
            {
                "id": tool.id,
                "icon_id": tool.icon_id,
                "svg_path": tool.icon.svg_path if tool.icon else None,
                "name": tool.name,
                "category": tool.category,
            }
            for tool in project.tools
        ],
        "sourcing_locations": [
            {
                "id": location.id,
                "store_name": location.store_name,
                "address": location.address,
                "distance_km": to_number(location.distance_km),
                "provides": location.provides,
                "google_maps_url": location.google_maps_url,
            }
            for location in project.sourcing_locations
        ],
    }


def list_projects(
    db,
    page=1,
    page_size=10,
    status=None,
    location=None,
    title=None,
    search=None,
):
    query = db.query(Project)

    if status:
        query = query.filter(Project.status == status)
    if location:
        query = query.filter(Project.location.ilike(f"%{location}%"))
    if title:
        query = query.filter(Project.title.ilike(f"%{title}%"))
    if search:
        query = query.filter(
            or_(
                Project.title.ilike(f"%{search}%"),
                Project.description.ilike(f"%{search}%"),
            )
        )

    total_items = query.count()
    page = max(page, 1)
    page_size = max(min(page_size, 100), 1)
    items = (
        query.options(
            selectinload(Project.materials),
            selectinload(Project.tools).selectinload(Tool.icon),
            selectinload(Project.sourcing_locations),
        )
        .order_by(Project.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return {
        "items": [_project_to_dict(project) for project in items],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": (total_items + page_size - 1) // page_size,
        },
    }


def get_project(db, project_id):
    project = (
        db.query(Project)
        .options(
            selectinload(Project.materials),
            selectinload(Project.tools).selectinload(Tool.icon),
            selectinload(Project.sourcing_locations),
        )
        .filter(Project.id == project_id)
        .first()
    )
    if not project:
        return None
    return _project_to_dict(project)


def create_project(db, data):
    project = Project(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status"),
        start_date=data.get("start_date"),
        end_date=data.get("end_date"),
        location=data.get("location"),
        volunteer_count=data.get("volunteer_count"),
        photo_url=data.get("photo_url"),
    )
    db.add(project)
    db.flush()

    _replace_materials(db, project.id, data.get("materials", []))
    _replace_tools(db, project.id, data.get("tools", []))
    _replace_sourcing_locations(db, project.id, data.get("sourcing_locations", []))

    db.refresh(project)
    return _project_to_dict(project)


def update_project(db, project_id, data):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    for field in [
        "title",
        "description",
        "status",
        "start_date",
        "end_date",
        "location",
        "volunteer_count",
        "photo_url",
    ]:
        if field in data:
            setattr(project, field, data[field])

    if "materials" in data:
        _replace_materials(db, project.id, data.get("materials", []))
    if "tools" in data:
        _replace_tools(db, project.id, data.get("tools", []))
    if "sourcing_locations" in data:
        _replace_sourcing_locations(db, project.id, data.get("sourcing_locations", []))

    db.flush()
    db.refresh(project)
    return _project_to_dict(project)


def delete_project(db, project_id):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return False

    db.query(Material).filter(Material.project_id == project_id).delete()
    db.query(Tool).filter(Tool.project_id == project_id).delete()
    db.query(SourcingLocation).filter(SourcingLocation.project_id == project_id).delete()
    db.delete(project)
    return True


def _replace_materials(db, project_id, materials):
    db.query(Material).filter(Material.project_id == project_id).delete()
    for item in materials:
        db.add(
            Material(
                project_id=project_id,
                item_name=item.get("item_name"),
                quantity=item.get("quantity"),
                unit=item.get("unit"),
                estimated_price=item.get("estimated_price"),
                total_cost=item.get("total_cost"),
            )
        )


def _replace_tools(db, project_id, tools):
    db.query(Tool).filter(Tool.project_id == project_id).delete()
    for item in tools:
        db.add(
            Tool(
                project_id=project_id,
                icon_id=item.get("icon_id"),
                name=item.get("name"),
                category=item.get("category"),
            )
        )


def _replace_sourcing_locations(db, project_id, locations):
    db.query(SourcingLocation).filter(SourcingLocation.project_id == project_id).delete()
    for item in locations:
        db.add(
            SourcingLocation(
                project_id=project_id,
                store_name=item.get("store_name"),
                address=item.get("address"),
                distance_km=item.get("distance_km"),
                provides=item.get("provides"),
                google_maps_url=item.get("google_maps_url"),
            )
        )
