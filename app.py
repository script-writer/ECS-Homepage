from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog/frontend-master')
def blog_frontend_master():
    return render_template('blog_frontend_master.html')

@app.route('/blog/business-projects')
def blog_business_projects():
    return render_template('blog_business_projects.html')

@app.route('/blog/japan-migration')
def blog_japan_migration():
    return render_template('blog_japan_migration.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
