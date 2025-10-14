import matplotlib.pyplot as plt
# # x = [1, 2, 3, 4, 5]
# x = ["Nadir", "Ali", "Ihsan", "Janzeb", "Kumail"]
# y = [10, 20, 25, 30, 35]
# plt.xlabel("Name")
# plt.ylabel("Age")
# plt.title("Age of different persons")
# plt.bar(x, y)
# plt.show()

x = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
y = [2, 5, 7, 9, 12]
# plt.bar(x, y)
# plt.xlabel('Days')
# plt.ylabel('Tasks Completed')
# plt.title('Task Completion by Day')
# plt.show()


y2 = [3, 6, 8, 10, 15]
# plt.plot(x, y, label='Completed Tasks')
# plt.plot(x, y2, label='New Tasks Added')
# plt.xlabel('Days')
# plt.ylabel('Number of Tasks')
# plt.title('Comparison of Task Completion and New Tasks Added')
# plt.legend()
# plt.show()




# plt.plot(x, y, label='Completed Tasks', linestyle='-',
# color='r', linewidth=3)
# plt.plot(x, y2, label='New Tasks Added', linestyle=':',
# color='black', linewidth=4)
# plt.xlabel('Days')
# plt.ylabel('Number of Tasks')
# plt.title('Task Data with Customized Lines')
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt

# # Data
# investors = ['Nadir', 'Majid', 'Janzeb', 'Ihsan']
# shares = [50, 20, 20, 10]

# # Colors (optional)
# # colors = ['pink', '#3498db', '#f1c40f', '#e74c3c']

# # Plot
# plt.figure(figsize=(6,6))
# plt.pie(
#     shares,
#     labels=investors,
#     autopct='%1.1f%%',
#     startangle=140,
# )

# plt.title('Project Investment Distribution', fontsize=14)
# plt.axis('equal')  # Ensures the pie is a circle
# plt.show()



# labels = 'Completed', 'Pending'
# sizes = [75, 25]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('Task Completion Status')
# plt.show()



plt.plot(x, y)
plt.xlabel('Days')
plt.ylabel('Tasks Completed')
plt.title('Task Completion with Grid Lines')
plt.xticks(rotation=45)
plt.yticks(range(1, 15))
plt.grid(True)
plt.show()