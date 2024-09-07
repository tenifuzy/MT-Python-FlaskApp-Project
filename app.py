from flask import Flask, render_template
import os

app = Flask(__name__)

# File to store visitor count
count_file = 'count.txt'

# Function to read the current visitor count from file
def read_count():
    if os.path.exists(count_file):
        try:
            with open(count_file, 'r') as file:
                count = int(file.read())
        except (ValueError, IOError) as e:
            print(f"Error reading count: {e}")
            count = 0
    else:
        count = 0
    return count

# Function to write the current visitor count to file
def write_count(count):
    try:
        with open(count_file, 'w') as file:
            file.write(str(count))
    except IOError as e:
        print(f"Error writing count: {e}")

@app.route('/')
def index():
    # Read the current visitor count
    count = read_count()

    # Increment the count
    count += 1

    # Write the new count back to the file
    write_count(count)

    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
