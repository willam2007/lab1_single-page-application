from flask import Blueprint, render_template
from sqlalchemy import func
from .models import TypeBuilding, Structure
from .extensions import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    type_buildings = (
        db.session.query(
            TypeBuilding.id,
            TypeBuilding.name.label("Тип здания"),
        )
        .select_from(TypeBuilding)
    )

    structures = (
        db.session.query(
            Structure.id,
            Structure.name.label("Название"),
            Structure.height.label("Высота (м)"),
            Structure.city.label("Город"),
            Structure.country.label("Страна"),
            Structure.year.label("Год"),
            TypeBuilding.name.label("Тип здания"),
        )
        .join(TypeBuilding, Structure.type_id == TypeBuilding.id)
    )

    stats_by_type = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Structure.height).label("Максимальная высота"),
            func.min(Structure.height).label("Минимальная высота"),
            func.round(func.avg(Structure.height), 1).label("Средняя высота"),
        )
        .join(TypeBuilding, Structure.type_id == TypeBuilding.id)
        .group_by(TypeBuilding.name)
        .order_by(TypeBuilding.name)
    )

    stats_by_country = (
        db.session.query(
            Structure.country.label("Страна"),
            func.max(Structure.height).label("Максимальная высота"),
            func.min(Structure.height).label("Минимальная высота"),
            func.round(func.avg(Structure.height), 1).label("Средняя высота"),
        )
        .group_by(Structure.country)
        .order_by(Structure.country)
    )

    stats_by_city = (
        db.session.query(
            Structure.city.label("Город"),
            func.max(Structure.height).label("Максимальная высота"),
            func.min(Structure.height).label("Минимальная высота"),
            func.round(func.avg(Structure.height), 1).label("Средняя высота"),
        )
        .group_by(Structure.city)
        .order_by(Structure.city)
    )

    return render_template(
        'index.html',
        type_buildings_head=type_buildings.statement.columns.keys(),
        type_buildings_body=type_buildings.all(),
        structures_head=structures.statement.columns.keys(),
        structures_body=structures.all(),
        stats_by_type_head=stats_by_type.statement.columns.keys(),
        stats_by_type_body=stats_by_type.all(),
        stats_by_country_head=stats_by_country.statement.columns.keys(),
        stats_by_country_body=stats_by_country.all(),
        stats_by_city_head=stats_by_city.statement.columns.keys(),
        stats_by_city_body=stats_by_city.all(),
    )