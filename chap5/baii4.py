import matplotlib.pyplot as plt

cities = ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco',
          'Fresno', 'Sacramento', 'Long Beach', 'Oakland',
          'Bakersfield', 'Anaheim']

areas = [1302, 964, 469, 121, 300, 259, 133, 202, 388, 131]  # km2 (ví dụ)

# Sắp xếp giảm dần
cities, areas = zip(*sorted(zip(cities, areas), key=lambda x: x[1], reverse=True))

plt.barh(cities, areas)
plt.xlabel('Diện tích (km2)')
plt.title('Top 10 thành phố lớn nhất California')

plt.gca().invert_yaxis()  # Thành phố lớn nhất ở trên

plt.show()