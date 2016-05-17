from models import my_amity
from models.amity import spacer
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String, Boolean, ForeignKey


class Database(object):

    already_added = []

    def save_state(self, args):
        """
        Save all application data to the database 'amity.db',
        or optionally, a user-defined database
        """
        if args["--db"]:
            self.db_name = "sqlite:///" + "%s" % (args["--db"])
            self.db = create_engine(self.db_name)
        else:
            self.db = create_engine("sqlite:///amity.db")
        self.db.echo = False
        self.metadata = MetaData(bind=self.db)

        self.add_people()
        self.add_rooms()
        self.add_allocations()
        print spacer
        print "Application data has been stored in the following database: "
        if args["--db"]:
            print args["--db"]
        else:
            print "amity.db"
        print spacer

    def add_people(self):
        """Add data from the People list to the database"""
        people = Table(
                "people", self.metadata,
                Column("employee_id", Integer, primary_key=True),
                Column("name", String(80)),
                Column("is_fellow", Boolean),
                Column("is_allocated", Boolean),
                extend_existing=True
        )
        if people.exists():
            people.update()
        else:
            people.create()
        i = people.insert()
        for person in my_amity.people:
            if person not in self.already_added:
                if person.job_type == "Fellow":
                    is_fellow = True
                else:
                    is_fellow = False
                if person in my_amity.allocated_people:
                    is_allocated = True
                else:
                    is_allocated = False
                i.execute(
                    employee_id=person.emp_id,
                    name=person.name,
                    is_fellow=is_fellow,
                    is_allocated=is_allocated
                )
                self.already_added.append(person)

    def add_rooms(self):
        """Add data from the Rooms list to the database"""
        rooms = Table(
                "rooms", self.metadata,
                Column("name", String, primary_key=True),
                Column("is_office", Boolean),
                Column("is_vacant", Boolean),
                extend_existing=True
        )
        if rooms.exists():
            rooms.update()
        else:
            rooms.create()
        i = rooms.insert()
        for room in my_amity.rooms:
            if room not in self.already_added:
                if room.room_type == "Office":
                    is_office = True
                else:
                    is_office = False
                if room in my_amity.vacant_rooms:
                    is_vacant = True
                else:
                    is_vacant = False
                i.execute(
                    name=room.name,
                    is_office=is_office,
                    is_vacant=is_vacant
                )
                self.already_added.append(room)

    def add_allocations(self):
        """
        Add data from the Allocations list to the database.
        Each room gets a database table with occupants as rows.
        """
        if my_amity.rooms:
            for room in my_amity.rooms:
                room_name = room.name
                room_name = Table(
                        room_name, self.metadata,
                        Column(
                            "employee_id", Integer,
                            ForeignKey("people.employee_id"),
                            nullable=False),
                        Column("name", String),
                        extend_existing=True
                )
                if room_name.exists():
                    room_name.update()
                else:
                    room_name.create()
                i = room_name.insert()
                if room.occupants:
                    for person in room.occupants:
                        i.execute(
                            employee_id=person.emp_id,
                            name=person.name
                        )

    def load_state(self, args):
        pass

my_database = Database()
