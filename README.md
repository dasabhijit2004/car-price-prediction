# Car Price Prediction

A web application that predicts car prices using a linear regression machine learning model.

## Live Application

Visit the live application at: [https://car-price-prediction-ad.streamlit.app/](https://car-price-prediction-ad.streamlit.app/)

## Overview

This project implements a machine learning-based car price prediction system using linear regression. Users can input various specifications of a car (like brand, year, mileage, etc.) and get an estimated market value. The application provides an intuitive interface for both casual users interested in knowing car values and potential sellers looking to price their vehicles competitively.

## Features

- **Price Prediction**: Get accurate car price estimates based on multiple parameters
- **User-friendly Interface**: Simple, intuitive UI for inputting car details
- **Cross-platform**: Works across devices and screen sizes
- **No Login Required**: Instant access to predictions
- **Real-time Results**: Get price estimates immediately after submitting specifications

## Technology Stack

- **Framework**: Streamlit
- **Machine Learning**: Scikit-learn (Linear Regression model)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Streamlit Cloud

## How to Use

1. Visit [https://car-price-prediction-ad.streamlit.app/](https://car-price-prediction-ad.streamlit.app/)
2. Fill in the requested car specifications:
   - Brand
   - Model Year
   - Mileage
   - Engine Power
   - Fuel Type
   - Transmission Type
   - Additional features
3. Submit the form to receive your car price prediction
4. Optional: Explore how different features affect the predicted price

## Local Development

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/car-price-prediction.git
   cd car-price-prediction
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

## Model Details

- **Algorithm**: Linear Regression
- **Features**: The model considers various car attributes including age, mileage, engine specifications, brand reputation, and optional features
- **Training Data**: Trained on a comprehensive dataset of car listings with actual sale prices
- **Accuracy**: The model is regularly evaluated and updated to ensure prediction accuracy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository or contact the project maintainer.

---

*Disclaimer: The price predictions provided by this application are estimates based on historical data and should not be considered as definitive valuations. Actual market prices may vary based on additional factors not captured by the model.*
