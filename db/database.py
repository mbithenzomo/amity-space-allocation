from models.amity import my_amity, spacer
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String, Boolean

db = create_engine('sqlite:///amity.db')

db.echo = False


metadata = MetaData(bind=db)


class Database(object):

    already_added = []

    def add_people(self):
        people = Table(
                'people', metadata,
                Column('employee_id', Integer, primary_key=True),
                Column('name', String(80)),
                Column('is_fellow', Boolean),
                Column('is_allocated', Boolean),
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
        rooms = Table(
                'rooms', metadata,
                Column('name', String, primary_key=True),
                Column('is_office', Boolean),
                Column('is_vacant', Boolean),
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
        print self.already_added

    def save_state(self, args):
        # if args['--db']:
        #     db = create_engine('sqlite:///%s') % (args['--db'])
        self.add_people()
        self.add_rooms()
        print spacer
        print "Application data has been stored in the following database: "
        if args['--db']:
            print args['--db']
        else:
            print "amity.db"
        print spacer

    def load_state(self, args):
        pass

my_database = Database()
