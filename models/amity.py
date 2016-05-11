import random
from rooms import Room
from people import Person

spacer = "-" * 80

class Amity():
	def __init__(self):
		self.rooms = []
		self.offices = []
		self.livingspaces = []
		self.people = []
		self.fellows = []
		self.staff = []

	def create_room(self, args):
		"""Create new room(s)"""
		print spacer
		print "You have successfully added the following rooom(s):"
		for room in args["<room_name>"]:
			new_room = Room() # create new Room object
			new_room.name = room # set room name
			self.rooms.append(new_room) # add to list of rooms
			if args["Office"]:
				new_room.room_type = "Office" # set room type
				new_room.capacity = 6 # set capacity
				self.offices.append(new_room) # add to list of offices
			elif args["Living"]:
				new_room.room_type = "Living" # set room type
				new_room.capacity = 4 # set capacity
				self.livingspaces.append(new_room) # add to list of living spaces
			print "Name: " + ''.join(new_room.name) + " | Type: " + new_room.room_type
		print spacer

	def add_person(self, args):
		"""Add new person"""
		print spacer
		print "You have successfully added the following person:"
		for person in args["<first_name>"]:
			new_person = Person() # create new Person object
			name = person + " " + args["<last_name>"] # set full name
			job_type = "Staff" if args["Staff"] else "Fellow" # set job type
			wants_space = "Yes" if args["<wants_space>"] is "Y" else "No" # set wants_space
			self.people.append(new_person)# add to list of people
			print "Name: " + name + " | Job Type: " + job_type + \
			" | Wants Space?:"  + " " + wants_space
			print spacer
			"""Allocation to rooms"""
			if job_type == "Staff":
				self.staff.append(new_person) # add to list of staff
			elif job_type == "Staff" and wants_space == "Yes":
				if len(my_amity.offices) != 0:
					office_choice = random.choice(my_amity.offices)
					office_choice.occupants.append(new_person) # add to list of occupants for office
					print "You have successfully allocated " + name + \
					" to the following office: " + office_choice.name
				else:
					print "Unfortunately there are no offices in the system,\nso " + name + \
					" cannot be assigned to one.\nAdd a new office using the create_room command."
			elif job_type == "Fellow" and wants_space == "Yes":
				if len(my_amity.livingspaces) != 0:
					living_choice = random.choice(my_amity.livingspaces)
					living_choice.occupants.append(new_person)
					self.staff.append(new_person) # add to list of fellows
					print "You have successfully allocated " + name + \
					" to the following living space: " + living_choice.name
				else:
					print "Unfortunately there are no living spaces in the system,\nso " + name + \
					" cannot be assigned to one.\nAdd a new living space using the create_room command."
		print spacer

my_amity = Amity() # create new Amity object
