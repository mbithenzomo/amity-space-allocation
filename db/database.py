from models.amity import spacer
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String, Boolean, ForeignKey


class Database(object):

    already_added = []

    def __init__(self, my_amity):
        self.db = None
        self.my_amity = my_amity

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
                Column("first_name", String(80)),
                Column("last_name", String(80)),
                Column("is_fellow", Boolean),
                Column("is_allocated", Boolean),
                extend_existing=True
        )
        if people.exists():
            people.update()
        else:
            people.create()
        insert = people.insert()
        for person in self.my_amity.people:
            if person not in self.already_added:
                if person.job_type == "Fellow":
                    is_fellow = True
                else:
                    is_fellow = False
                if person in self.my_amity.allocated_people:
                    is_allocated = True
                else:
                    is_allocated = False
                first_name, last_name = person.name.split(" ")
                insert.execute(
                    employee_id=person.emp_id,
                    first_name=first_name,
                    last_name=last_name,
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
        insert = rooms.insert()
        for room in self.my_amity.rooms:
            if room not in self.already_added:
                if room.room_type == "Office":
                    is_office = True
                else:
                    is_office = False
                if room in self.my_amity.vacant_rooms:
                    is_vacant = True
                else:
                    is_vacant = False
                insert.execute(
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
        if self.my_amity.rooms:
            for room in self.my_amity.rooms:
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
                insert = room_name.insert()
                if room.occupants:
                    for person in room.occupants:
                        insert.execute(
                            employee_id=person.emp_id,
                            name=person.name
                        )

    def load_state(self, args):  # pragma: no cover
        """Load data to the application from a user-defined database"""
        self.db_name = "sqlite:///" + "%s" % args.get("<sqlite_database>")
        self.db = create_engine(self.db_name)
        connection = self.db.connect()
        people = connection.execute("SELECT * FROM people")
        rooms = connection.execute("SELECT * FROM rooms")
        table_names = connection.execute(
            "SELECT name FROM sqlite_master \
            WHERE (type='table') AND (name NOT LIKE 'people') \
            AND (name NOT LIKE 'rooms') "
        )

        for row in people:
            print('people in load_state', people)
            if row["is_fellow"]:
                is_fellow = True
                is_staff = False
            else:
                is_fellow = False
                is_staff = True

            self.my_amity.add_person({
                    "<first_name>": row["first_name"],
                    "<last_name>": row["last_name"],
                    "<wants_space>": "N",
                    "Fellow": is_fellow,
                    "Staff": is_staff
                })

            # Change emp_id to what is in the database
            employee_id = row["employee_id"]
            person_from_db = self.my_amity.people[-1]
            person_from_db.emp_id = employee_id

        for row in rooms:
            if row["is_office"]:
                is_living = False
            else:
                is_living = True

            self.my_amity.create_room({
                "<room_name>": [row["name"]],
                "Living": [is_living],
                "Office": [row["is_office"]]
            })

        for table_name in table_names:
            table_name = str(table_name[0])
            query = "SELECT * FROM %s" % table_name
            room = connection.execute(query)
            for row in room:
                emp_id = row["employee_id"]
                emp_id = str(emp_id)

                self.my_amity.reallocate_person({
                    "<employee_id>": emp_id,
                    "<new_room_name>": table_name
                })
