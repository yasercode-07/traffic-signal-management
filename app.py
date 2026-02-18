from flask import Flask, render_template
from sensor import get_traffic_density
from traffic_logic import calculate_green_time
from sync import sync_signals

app = Flask(__name__)

@app.route('/')
def dashboard():

    north = get_traffic_density("North")
    south = get_traffic_density("South")
    east  = get_traffic_density("East")
    west  = get_traffic_density("West")

    green_times = calculate_green_time(north, south, east, west)

    sync_time = sync_signals(green_times)

    free_left = True

    data = {
        "north": north,
        "south": south,
        "east": east,
        "west": west,
        "green": green_times,
        "sync": sync_time,
        "free_left": free_left
    }

    return render_template("dashboard.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
