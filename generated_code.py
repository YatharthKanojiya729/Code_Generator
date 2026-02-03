```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to our website</h1>
    <p>This is the home page.</p>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
</body>
</html>
```

```html
<!-- about.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>About Us</h1>
    <p>This is the about page.</p>
    <a href="/">Home</a>
    <a href="/contact">Contact</a>
</body>
</html>
```

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>This is the contact page.</p>
    <a href="/">Home</a>
    <a href="/about">About</a>
</body>
</html>
```

```bash
# Install Flask
pip install flask

# Run the application
python app.py
```

Open your web browser and navigate to `http://localhost:5000` to view the webpage.