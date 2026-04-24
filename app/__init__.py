import os
from flask import Flask
from .extensions import db
from .models import TypeBuilding, Structure


def create_app():
    app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance'))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'structure.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        _seed_data()

    return app


def _seed_data():
    if TypeBuilding.query.first():
        return

    types = {
        "Небоскрёб":           TypeBuilding(name="Небоскрёб"),
        "Антенная мачта":      TypeBuilding(name="Антенная мачта"),
        "Гиперболоидная башня":TypeBuilding(name="Гиперболоидная башня"),
        "Дымовая труба":       TypeBuilding(name="Дымовая труба"),
        "Решётчатая мачта":    TypeBuilding(name="Решётчатая мачта"),
        "Башня":               TypeBuilding(name="Башня"),
        "Мосты":               TypeBuilding(name="Мосты"),
    }
    db.session.add_all(types.values())
    db.session.flush()

    structures = [
        Structure(name="Бурдж-Халифа",              height=828.0,  city="Дубай",       country="ОАЭ",              year=2010, type=types["Небоскрёб"]),
        Structure(name="Шанхайская башня",           height=632.0,  city="Шанхай",      country="Китай",            year=2015, type=types["Небоскрёб"]),
        Structure(name="Абрадж аль-Бейт",           height=601.0,  city="Мекка",       country="Саудовская Аравия",year=2012, type=types["Небоскрёб"]),
        Structure(name="Пинг Ань Финанс Центр",     height=599.0,  city="Шэньчжэнь",   country="Китай",            year=2017, type=types["Небоскрёб"]),
        Structure(name="Лотте Уорлд Тауэр",         height=554.5,  city="Сеул",        country="Южная Корея",      year=2016, type=types["Небоскрёб"]),
        Structure(name="Уиллис Тауэр",              height=442.0,  city="Чикаго",      country="США",              year=1973, type=types["Небоскрёб"]),
        Structure(name="Эмпайр Стейт Билдинг",      height=354.0,  city="Нью-Йорк",    country="США",              year=1931, type=types["Небоскрёб"]),
        Structure(name="KVLY-TV мачта",             height=628.8,  city="Фарго",       country="США",              year=1963, type=types["Антенная мачта"]),
        Structure(name="KXJB-TV мачта",             height=628.8,  city="Фарго",       country="США",              year=2000, type=types["Антенная мачта"]),
        Structure(name="Останкинская башня",        height=540.1,  city="Москва",      country="Россия",           year=1967, type=types["Гиперболоидная башня"]),
        Structure(name="Гуанчжоуская башня",        height=600.0,  city="Гуанчжоу",    country="Китай",            year=2010, type=types["Гиперболоидная башня"]),
        Structure(name="Экибастузская ГРЭС-2",      height=419.7,  city="Экибастуз",   country="Казахстан",        year=1987, type=types["Дымовая труба"]),
        Structure(name="Трубa GRES-2",              height=380.0,  city="Рефтинский",  country="Россия",           year=1980, type=types["Дымовая труба"]),
        Structure(name="Труба Криворожской ГРЭС",   height=350.0,  city="Кривой Рог",  country="Украина",          year=1969, type=types["Дымовая труба"]),
        Structure(name="Варшавская мачта",          height=646.38, city="Гарбатка",    country="Польша",           year=1974, type=types["Решётчатая мачта"]),
        Structure(name="Мачта CKND",                height=385.0,  city="Виннипег",    country="Канада",           year=1960, type=types["Решётчатая мачта"]),
        Structure(name="Токийское небесное дерево", height=634.0,  city="Токио",       country="Япония",           year=2012, type=types["Башня"]),
        Structure(name="Кантонская башня",          height=604.0,  city="Гуанчжоу",    country="Китай",            year=2010, type=types["Башня"]),
        Structure(name="Башня CN",                  height=553.3,  city="Торонто",     country="Канада",           year=1976, type=types["Башня"]),
        Structure(name="Мост Миллау",               height=343.0,  city="Миллау",      country="Франция",          year=2004, type=types["Мосты"]),
        Structure(name="Мост Акаси-Кайкё",          height=298.3,  city="Кобе",        country="Япония",           year=1998, type=types["Мосты"]),
    ]
    db.session.add_all(structures)
    db.session.commit()