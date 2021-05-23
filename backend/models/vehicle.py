import datetime
from firebase_admin import credentials, firestore, initialize_app

class Vehicle:

    vehicle_ref = "" # we could set this later at runtime
    
    def __init__(self, make="", model="", total_miles=int, tire_miles=int, 
                    tire_purchase_date="", rotation_miles=int, color="", user_id=None, vehicle_id=None):

        self.make = make
        self.model = model
        self.total_miles = total_miles
        self.tire_miles = tire_miles
        self.tire_purchase_date = tire_purchase_date
        self.rotation_miles = rotation_miles
        self.color = color
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        


    def to_json(self):
        return {"make": self.make, 
                "model": self.model, 
                "total_miles": int(self.total_miles),
                "tire_miles": int(self.tire_miles),
                "tire_purchase_date": self.tire_purchase_date,
                "rotation_miles": int(self.rotation_miles),
                "color": self.color,
                "user_id": self.user_id,
                "vehicle_id": self.vehicle_id
               }

    def insert(self):
        response = self.vehicle_ref.document().set(self.to_json())
        print(response)
    def update(self):
        self.vehicle_ref.document(self.vehicle_id).set(self.to_json())

    def delete(self):
        self.vehicle_ref.document(self.vehicle_id).delete(self.to_json())

    @classmethod
    def vehicles_for_user(cls, user_id):
        vehicles = cls.vehicle_ref.where("user_id", "==", user_id).get()
        return [(vehicle.id, vehicle.to_dict()) for vehicle in vehicles]

    # @classmethod
    # def vehicles_all_for_user(cls, user_id):
    #     return cls.vehicle_ref.where("user_id", "==", user_id).get()
        



if __name__ == "__main__":
    pass