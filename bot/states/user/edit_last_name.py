from aiogram.dispatcher.filters.state import StatesGroup, State


class EditLastName(StatesGroup):
    InsertLastName = State()