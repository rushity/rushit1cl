from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Input values from the form
        total_leaves = int(request.form['total_leaves'])
        leaves_per_month = int(request.form['leaves_per_month'])
        num_months = int(request.form['num_months'])

        # Initialize data structure
        data = [[0 for _ in range(5)] for _ in range(num_months)]
        
        for i in range(num_months):
            data[i][1] = int(request.form[f'leaves_month_{i+1}'])
            data[i][0] = i + 1

        # Calculate leave details
        remaining_leaves = total_leaves
        for i in range(num_months):
            data[i][4] = remaining_leaves
            
            if data[i][1] >= leaves_per_month:
                data[i][2] = min(leaves_per_month, remaining_leaves)
            else:
                data[i][2] = min(data[i][1], remaining_leaves)
            
            data[i][3] = data[i][1] - data[i][2]
            data[i][4] = remaining_leaves - data[i][2]
            remaining_leaves = data[i][4]

        # Pass data to the result template
        return render_template('result.html', data=data)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
