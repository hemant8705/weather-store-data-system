# Weather Record ADT
class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date      # format: "dd/mm/yyyy"
        self.city = city
        self.temperature = temperature

    def __repr__(self):
        return f"{self.date} | {self.city} | {self.temperature}°C"


# Data Storage Class
class WeatherStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        self.city_index = {city: idx for idx, city in enumerate(cities)}

        # 2D array: rows = years, cols = cities
        # Initialize with None (sentinel value for sparse data)
        self.data = [[None for _ in cities] for _ in years]

    def insert(self, record: WeatherRecord):
        year = int(record.date.split("/")[-1])
        if year in self.years and record.city in self.city_index:
            row = self.years.index(year)
            col = self.city_index[record.city]
            self.data[row][col] = record.temperature
            print(f"Inserted {record}")
        else:
            print("Invalid city or year")

    def delete(self, date, city):
        year = int(date.split("/")[-1])
        if year in self.years and city in self.city_index:
            row = self.years.index(year)
            col = self.city_index[city]
            self.data[row][col] = None
            print(f"Deleted record for {city} in {year}")

    def retrieve(self, city, year):
        if year in self.years and city in self.city_index:
            row = self.years.index(year)
            col = self.city_index[city]
            return self.data[row][col]
        return None

    def row_major_access(self):
        print("\nRow-major access:")
        for row in range(len(self.years)):
            for col in range(len(self.cities)):
                print(f"Year {self.years[row]}, City {self.cities[col]} -> {self.data[row][col]}")

    def column_major_access(self):
        print("\nColumn-major access:")
        for col in range(len(self.cities)):
            for row in range(len(self.years)):
                print(f"City {self.cities[col]}, Year {self.years[row]} -> {self.data[row][col]}")

    def handle_sparse_data(self):
        print("\nSparse Data Representation (year, city, temp):")
        sparse_matrix = []
        for row in range(len(self.years)):
            for col in range(len(self.cities)):
                if self.data[row][col] is not None:
                    sparse_matrix.append((self.years[row], self.cities[col], self.data[row][col]))
        print(sparse_matrix)
        return sparse_matrix

    def analyze_complexity(self):
        print("\nTime & Space Complexity Analysis:")
        print("Insert: O(1)")
        print("Delete: O(1)")
        print("Retrieve: O(1)")
        print("Row/Column Access: O(n*m) where n = years, m = cities")
        print("Space: O(n*m) for dense, O(k) for sparse (k = non-empty records)")


# -------------------------------
# Example Usage
# -------------------------------

years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Chennai"]

storage = WeatherStorage(years, cities)

# Insert some records
storage.insert(WeatherRecord("01/01/2023", "Delhi", 15.5))
storage.insert(WeatherRecord("05/06/2024", "Mumbai", 32.0))
storage.insert(WeatherRecord("12/12/2025", "Chennai", 28.3))

# Retrieve
print("\nRetrieve:", storage.retrieve("Delhi", 2023))

# Delete
storage.delete("01/01/2023", "Delhi")

# Row-major vs Column-major
storage.row_major_access()
storage.column_major_access()

# Handle sparse data
storage.handle_sparse_data()

# Complexity analysis
storage.analyze_complexity()
