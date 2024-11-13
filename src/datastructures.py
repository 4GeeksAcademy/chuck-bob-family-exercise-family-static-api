
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        return self._members.append(member)
    
    def update_member(self, id, updates):
        for member in self._members:                # Find the member by id
            if member.get('id') == id:              # If the member id is the same as the id being passed
                for key, value in updates.items():  # Update only the specified keys
                    member[key] = value             # Replace the key value with the new key value
                return member                       # Return the updated member data
        return None                                 # If member with the given id is not found
        

    def delete_member(self, id):
        for index, member in enumerate(self._members):  # Loop through members with index
            if member.get('id') == id:                  # If the member's id matches the given id
                return self._members.pop(index)         # Remove and return the member
        return None                                     # In case the member is not found

    def get_member(self, id):
        for member in self._members:        # Loop through members
            if member.get('id') == id:      # If the member's id matches the given id
                return member               # Return the found member
        return None                         # In case the member is not found

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
