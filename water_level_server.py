from nameko.rpc import rpc
import db
from db import WaterLevel


class WaterLevelServer():
    name = "water_level_server"

    @rpc
    def receive_water_level(self, water_level):
        water_level = round(water_level, 1)
        w = WaterLevel()
        w.value = water_level
        db.session.add(w)
        db.session.commit()
        return water_level
