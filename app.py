import pandas as pd
from flask import Flask, request, render_template_string
import plotly.express as px
import plotly.io as pio
from utils.data_processing import load_and_preprocess_data, summarize_dataset


data = load_and_preprocess_data('datasets/sales_data.csv')


app = Flask(__name__)
app.title = "Dynamic Graph Generator"


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1 style="text-align: center;">Dynamic Graph Generator</h1>

    <!-- Input field for user query -->
    <div style="margin: 20px;">
        <form method="POST" action="/">
            <label>Enter your query:</label>
            <input type="text" name="user_input" placeholder="e.g., Show the trend of sales over time" style="width: 100%;" />
            <button type="submit" style="margin-top: 10px;">Generate</button>
        </form>
    </div>

    <!-- Graph display area -->
    <div style="margin-top: 20px;">
        {{ graph|safe }}
    </div>

    <!-- Summary display area -->
    <div style="margin-top: 40px;">
        <h3>Data Summary:</h3>
        <p>{{ summary }}</p>
    </div>
</body>
</html>
"""


def generate_graph(user_input):
    if not user_input:
      
        fig = px.bar(data, x='Product_Category', y='Sales', color='Product_Category', title='Total Sales by Product Category')
        return fig

    user_input = user_input.lower()

    if "trend" in user_input or "time" in user_input:
        fig = px.line(data, x='Date', y='Sales', title='Sales Trend Over Time')
    elif "compare" in user_input and "region" in user_input:
        fig = px.bar(data, x='Region', y='Sales', color='Region', barmode='group', title='Sales Comparison Across Regions')
    elif "rating" in user_input or "satisfaction" in user_input:
        avg_ratings = data.groupby('Region')['Customer_Rating'].mean().reset_index()
        fig = px.bar(avg_ratings, x='Region', y='Customer_Rating', title='Average Customer Ratings by Region')
    elif "profit" in user_input:
        fig = px.pie(data, values='Profit', names='Product_Category', title='Profit Distribution by Product Category')
    elif "salesperson" in user_input:
        sales_by_person = data.groupby('Salesperson')['Sales'].sum().reset_index()
        fig = px.bar(sales_by_person, x='Salesperson', y='Sales', title='Sales by Salesperson')
    elif "discount" in user_input:
        filtered_data = data[data['Discount'] > 15]
        fig = px.bar(filtered_data, x='Product', y='Sales', title='Sales for Products with Discounts > 15%')
    else:
        fig = px.bar(data, x='Product_Category', y='Sales', color='Product_Category', title='Total Sales by Product Category')

    return fig


@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")


    fig = generate_graph(user_input)
    graph_html = pio.to_html(fig, full_html=False)
    summary = summarize_dataset(data)
    summary_text = (
        f"Total Sales: ${summary['Total Sales']}, "
        f"Average Sales: ${summary['Average Sales']:.2f}, "
        f"Top Region: {summary['Top Region']}, "
        f"Top Product: {summary['Top Product']}"
    )

    return render_template_string(HTML_TEMPLATE, title=app.title, graph=graph_html, summary=summary_text)


if __name__ == "__main__":
    app.run(debug=True)
