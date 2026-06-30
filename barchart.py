import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
sales = [120, 90, 75, 50, 30]
colors = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF', "#631160"]

plt.figure(figsize=(8, 5))
plt.bar(fruits, sales, color=colors)
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Units Sold')
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('fruit_sales.png')
plt.show()

plt.pie(sales, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Fruit Sales Distribution')
plt.axis('equal')
plt.tight_layout()
plt.savefig('fruit_sales_pie.png')
plt.show()
