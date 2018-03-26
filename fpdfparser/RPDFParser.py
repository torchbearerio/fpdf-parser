from fpdfparser import parser_utils
from geopy.distance import great_circle


class RPDFParser:
    def __init__(self, filename):
        with open(filename) as file:
            self._parsed_entries = parser_utils.parse_updf_file(file)

    def all(self):
        return self._parsed_entries

    def within_distance_of(self, lat, long, distance):
        if len(self._parsed_entries) == 0:
            return

        entries_with_coords = [e for e in self._parsed_entries if e.get('latitude') and e.get('longitude')]

        # Find closest point
        closest_entry = sorted(entries_with_coords,
                               key=lambda e: great_circle(
                                   (lat, long),
                                   (e["latitude"], e["longitude"])
                               ).meters)[0]

        # Filter to entries within `distance
        return sorted((e for e in entries_with_coords if
                       great_circle(
                           (closest_entry["latitude"], closest_entry["longitude"]),
                           (e["latitude"], e["longitude"])
                       ).meters <= distance), key=lambda e: e["timestamp"])