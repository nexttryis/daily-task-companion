from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container, Vertical
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date, timedelta
import json

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    date = Column(Date, default=date.today)

class UserStats(Base):
    __tablename__ = 'user_stats'
    id = Column(Integer, primary_key=True)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    streak = Column(Integer, default=0)
    last_date = Column(Date, default=date.today)

engine = create_engine('sqlite:///daily_companion.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class DailyCompanionApp(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            Static("Welcome back! Ready for today's tasks?", id="motivation"),
            Vertical(id="task_list"),
            id="main"
        )

    def on_mount(self):
        self.load_tasks()
        self.update_stats()

    def load_tasks(self):
        session = Session()
        tasks = session.query(Task).filter_by(date=date.today()).all()
        # TODO: Populate task list
        session.close()

    def update_stats(self):
        # TODO: Load and display stats
        pass

if __name__ == "__main__":
    app = DailyCompanionApp()
    app.run()
