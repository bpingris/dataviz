import csv
import matplotlib.pyplot as plt


filename = 'data.csv'

def read_file():
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        next(reader)
        d = []
        # Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
        for row in reader:
            d.append({
                'id': row[0],
                'car': row[1],
                'mpg': float(row[2]),
                'cylinders': row[3],
                'displacement': float(row[4]),
                'hp': float(row[5]),
                'weight': float(row[6]),
                'acc': float(row[7]),
                'model': row[8],
                'origin': row[9],
                })
        return d

def histogram(data):
    plt.hist([item['hp'] for item in data], edgecolor='black')
    plt.legend()
    plt.xlabel('Chevaux')
    plt.ylabel('Quantite')
    plt.title('Nombre de voiture/chevaux')
    plt.show()

def scatter(data):
    plt.scatter([item['hp'] for item in data], [item['acc']
                                                    for item in data])
    plt.xlabel('Chevaux')
    plt.ylabel('Acceleration')
    plt.show()

def main():
    data = read_file()
    # histogram(data)
    scatter(data)

if __name__ == "__main__":
    main()
