import matplotlib.pyplot as plt
from collections import Counter

def plot_gpa_bar_chart(students, output_path='output/visuals/gpa.png'):
    names = [s['name'] for s in students]
    gpas = [s['GPA'] for s in students]

    plt.figure(figsize=(10,6))
    bars = plt.bar(names, gpas, color='skyblue')
    plt.xlabel('Student')
    plt.ylabel('GPA')
    plt.title('Student GPA Bar Chart')
    plt.ylim(0, 4)
    plt.xticks(rotation=45)

    for bar, gpa in zip(bars, gpas):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.3, f'{gpa:.2f}',
                 ha='center', color='black', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_attendance_line_chart(students, output_path='output/visuals/attendance.png'):
    names = [s['name'] for s in students]
    attendance = [s['attendance_percent'] for s in students]

    plt.figure(figsize=(10,6))
    plt.plot(names, attendance, marker='o', linestyle='-', color='green')
    plt.xlabel('Student')
    plt.ylabel('Attendance (%)')
    plt.title('Student Attendance Over Time')
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_club_pie_chart(students, output_path='output/visuals/clubs.png'):
    club_counts = Counter()
    for s in students:
        club_counts.update(s['clubs'])

    labels = club_counts.keys()
    sizes = club_counts.values()

    plt.figure(figsize=(8,8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title('Club Participation Distribution')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
