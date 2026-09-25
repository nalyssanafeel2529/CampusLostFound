from flask import Flask, request

app = Flask(__name__)

items = []

@app.route("/")
def home():
    html = """
    <h1>Campus Lost & Found</h1>
    <h2>SaaS & PaaS Demo</h2>

    <p>Report a lost or found item.</p>

    <form action="/add" method="POST">

        Item Name:
        <input type="text" name="item">
        <br><br>

        Lost or Found:
        <select name="type">
            <option>Lost</option>
            <option>Found</option>
        </select>
        <br><br>

        Location:
        <input type="text" name="location">
        <br><br>

        Description:
        <input type="text" name="description">
        <br><br>

        <button type="submit">Submit Report</button>

    </form>

    <h3>Recent Reports</h3>
    """

    for item in items:
        html += f"""
        <hr>
        <b>Item:</b> {item["item"]}<br>
        <b>Type:</b> {item["type"]}<br>
        <b>Location:</b> {item["location"]}<br>
        <b>Description:</b> {item["description"]}<br>
        """

    return html


@app.route("/add", methods=["POST"])
def add():
    items.append({
        "item": request.form["item"],
        "type": request.form["type"],
        "location": request.form["location"],
        "description": request.form["description"]
    })

    return """
    <h1>Report Submitted!</h1>
    <p>Your item has been added.</p>
    <a href="/">View Reports</a>
    """


if __name__ == "__main__":
    app.run()
