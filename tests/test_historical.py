import pytest
from app.services.data_analysis import analyze_historical_data

def test_analyze_historical_data():
    # Sample historical data for testing
    historical_data = [
        {'timestamp': '2023-01-01', 'price': 100},
        {'timestamp': '2023-01-02', 'price': 110},
        {'timestamp': '2023-01-03', 'price': 105},
    ]
    
    # Expected result after analysis
    expected_result = {
        'average_price': 105,
        'max_price': 110,
        'min_price': 100,
    }
    
    # Call the function to test
    result = analyze_historical_data(historical_data)
    
    # Assert the result matches the expected output
    assert result == expected_result

def test_analyze_historical_data_empty():
    # Test with empty historical data
    historical_data = []
    
    # Expected result for empty data
    expected_result = {
        'average_price': None,
        'max_price': None,
        'min_price': None,
    }
    
    # Call the function to test
    result = analyze_historical_data(historical_data)
    
    # Assert the result matches the expected output
    assert result == expected_result