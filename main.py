from typing import Optional
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# создайте подключение к базе данных
engine = create_engine('postgresql://admin:video3308@89.108.124.137:5432/postgres')

# создайте сессию
Session = sessionmaker(bind=engine)
session = Session()

# определите таблицу
metadata = MetaData()
inventory_foto_form = Table('inventory_foto_form', metadata, autoload_with=engine)

# Определите модель данных
class Item(BaseModel):
    login: str
    date: str
    name: str
    phone: str
    date_create: str
    date_control: str
    store_id: str
    date_delivery: str
    time_start: str
    time_finish: str
    comment: str
    sent_logistic: str
    q1_plan_v_sr: str
    q2_boxes_place: str
    q3_documents_table: str
    q4_gates: str
    q5_other_people: str
    q6_keys: str
    q7_touch_items: str
    q8_spoil_item: str
    q9_drink: str
    q10_exit_no_reason: str
    spent_time: str


class Item2(BaseModel):
    login: str
    date: str
    name: str
    phone: str
    

app = FastAPI()

@app.post("/inventory")
async def create_item(
    item: Item2,
    x_form_id: Optional[str] = Header(None),
    x_form_answer_id: Optional[str] = Header(None)
):
    # Проверьте, соответствует ли заголовок x_form_id ожидаемому значению
    if x_form_id != "65e6a95a693872251cfdb042":
        # Если нет, возвратите HTTP-статус ошибки 400
        raise HTTPException(status_code=400, detail="Invalid X-FORM-ID header")

    # преобразуйте данные в требуемые типы
    date_timestamp = datetime.strptime(item.date, "%Y-%m-%d")
    x_form_answer_id_int = int(x_form_answer_id)

    # создайте новую запись
    new_entry = inventory_foto_form.insert().values(
        date=date_timestamp,
        login=item.login,
        name=item.name,
        phone_number=item.phone,
        id=x_form_answer_id,
        

    )

    # сохраните новую запись
    session.execute(new_entry)
    session.commit()

    # Если заголовок верный, верните полученные данные
    return {"status": 'ok'}

# создайте подключение к базе данных
engine2 = create_engine('postgresql://admin:video3308@89.108.124.137:5432/lpaction')

# создайте сессию
Session2 = sessionmaker(bind=engine2)
session2 = Session2()

# определите таблицу
metadata2 = MetaData()
night_table = Table('night_delivery_answers', metadata2, autoload_with=engine2)

#night_delivery
@app.post("/night_delivery")
async def create_item(
    item: Item,
    x_form_id: Optional[str] = Header(None),
    x_form_answer_id: Optional[str] = Header(None)
):
    # Проверьте, соответствует ли заголовок x_form_id ожидаемому значению
    if x_form_id != "65c5c55250569048d3e1d186":
        # Если нет, возвратите HTTP-статус ошибки 400
        raise HTTPException(status_code=400, detail="Invalid X-FORM-ID header")

    # преобразуйте данные в требуемые типы
    date_timestamp1 = datetime.strptime(item.date_control, "%Y-%m-%d")
    date_timestamp2 = datetime.strptime(item.date_delivery, "%Y-%m-%d")
    date_timestamp3 = datetime.strptime(item.date_create, "%d.%m.%Y")
    answer_id_int = int(x_form_answer_id)
    store_id_integer = int(item.store_id)

    # создайте новую запись
    new_entry2 = night_table.insert().values(
    login=item.login,
    date_create=date_timestamp3,
    date_control=date_timestamp1,
    store_id=store_id_integer,
    date_delivery=date_timestamp2,
    time_start=item.time_start,
    time_finish=item.time_finish,
    comment=item.comment,
    sent_logistic=item.sent_logistic,
    id_answer = answer_id_int,
    q1_plan_v_sr=item.q1_plan_v_sr,
    q2_boxes_place=item.q2_boxes_place,
    q3_documents_table=item.q3_documents_table,
    q4_gates=item.q4_gates,
    q5_other_people=item.q5_other_people,
    q6_keys=item.q6_keys,
    q7_touch_items=item.q7_touch_items,
    q8_spoil_item=item.q8_spoil_item,
    q9_drink=item.q9_drink,
    q10_exit_no_reason=item.q10_exit_no_reason,
    spent_time=item.spent_time,   
    )

    # сохраните новую запись
    session2.execute(new_entry2)
    session2.commit()

    # Если заголовок верный, верните полученные данные
    return {"status": 'ok'}



