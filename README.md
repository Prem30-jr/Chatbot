# Graph Generator

A web application that allows users to input natural language queries and dynamically generates visualizations based on the input. The app provides insights and summaries of the data using interactive graphs and a user-friendly interface.

---

## Features

- **Dynamic Graph Generation**: Generates graphs based on user queries.
- **Interactive Visualizations**: Graphs are interactive, built using Plotly.js.
- **Data Summary**: Displays key metrics and summaries of the dataset.
- **Responsive Design**: Mobile-friendly layout for accessibility on all devices.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Plotly.js
- **Styling**: Custom CSS
- **Dataset**: CSV file (`datasets/sales_data.csv`)

---

## Directory Structure
    Dynamic-Graph-Generator/
    │
    ├── app.py                   
    ├── datasets/
    │   └── sales_data.csv        
    ├── static/
    │   └── css/
    │       └── style.css          
    ├── utils/
    │   └── data_processing.py         
    ├── README.md            
    └── requirements.txt     

## How to Run the Project




### 1. Clone the repository:

```bash
  git clone https://github.com/your-username/dynamic-graph-generator.git
  cd dynamic-graph-generator
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the application:
```bash
python app.py
Open in your browser: Visit http://127.0.0.1:5000/ to view the app.
```


## Sample Queries
#### Here are some example queries you can try:
- "Show the trend of sales over time."
- "Compare the revenue across regions."
- "Show average customer ratings for each region."
- "Show profit distribution across product categories."
- "Who is the top-performing salesperson?"


## Screenshots
### 1. Home Page
![App Screenshot](https://github.com/Prem30-jr/Chatbot/blob/main/graph.png?raw=true)

## Dataset
### The application uses a sample dataset sales_data.csv, which contains the following columns:

- Date: Date of sale
- Sales: Sales amount
- Region: Region of sale
- Product_Category: Category of product
- Customer_Rating: Customer ratings for products
- Discount: Discount offered

## Future Improvements
- Add natural language processing (NLP) for more robust query parsing.
- Support multiple datasets uploaded by the user.
- Enhance data preprocessing for broader dataset compatibility.
- Add user authentication for a personalized experience.

## Contributing
### Contributions are welcome! If you'd like to improve this project, please:

- Fork the repository.
- Create a feature branch: git checkout -b feature-name.
- Commit your changes: git commit -m "Add a new feature".
- Push to the branch: git push origin feature-name.
- Create a pull request.
