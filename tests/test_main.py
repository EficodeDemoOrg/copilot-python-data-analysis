#!/usr/bin/env python3
"""
Yarr! These be the tests for our enhanced FastAPI analytics treasure, matey!
Making sure our data analysis ship sails smooth as silk for all data analysts aboard!
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a test client - like having a loyal crew member test our analytical ship!
client = TestClient(app)


def test_data_sources_endpoint():
    """
    Yarr! Test that we can get information about available data sources
    Perfect for data analysts who want to know what treasures are available!
    """
    response = client.get("/api/data-sources")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list), "Response should be a list of data sources"
    
    # Should have at least one data source (stackoverflow_2023)
    assert len(data) >= 1, "Should have at least one data source available"
    
    # Check structure of data source info
    for source in data:
        assert "name" in source, "Each data source should have a name"
        assert "description" in source, "Each data source should have a description"
        assert "available_columns" in source, "Each data source should list available columns"


def test_technology_analysis_endpoint():
    """
    Yarr! Test the main analysis endpoint with default parameters
    """
    response = client.get("/api/analysis/technology-usage")
    
    # Should work with default parameters or return proper error
    assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        
        # Check response structure
        required_fields = ["labels", "values", "total_responses", "unique_technologies", "analysis_column", "data_source"]
        for field in required_fields:
            assert field in data, f"Response should contain '{field}' field"
        
        # Check data types
        assert isinstance(data["labels"], list), "Labels should be a list"
        assert isinstance(data["values"], list), "Values should be a list"
        assert isinstance(data["total_responses"], int), "Total responses should be an integer"
        assert isinstance(data["unique_technologies"], int), "Unique technologies should be an integer"
    

def test_technology_analysis_with_parameters():
    """
    Yarr! Test the analysis endpoint with custom parameters
    """
    response = client.get("/api/analysis/technology-usage?source=stackoverflow_2023&column=LanguageHaveWorkedWith&top_n=5")
    
    assert response.status_code in [200, 404, 400], f"Expected 200, 404, or 400, got {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        
        # Should return exactly 5 results or fewer
        assert len(data["labels"]) <= 5, "Should return at most 5 results"
        assert len(data["values"]) <= 5, "Should return at most 5 values"
        assert len(data["labels"]) == len(data["values"]), "Labels and values should have same length"


def test_invalid_data_source():
    """
    Yarr! Test that invalid data source returns proper error
    """
    response = client.get("/api/analysis/technology-usage?source=nonexistent_source")
    
    assert response.status_code == 400, "Should return 400 for invalid data source"
    
    data = response.json()
    assert "detail" in data, "Error response should contain detail field"


def test_invalid_column():
    """
    Yarr! Test that invalid column returns proper error
    """
    response = client.get("/api/analysis/technology-usage?source=stackoverflow_2023&column=NonexistentColumn")
    
    assert response.status_code in [400, 404], "Should return 400 or 404 for invalid column"


def test_legacy_languages_endpoint():
    """
    Yarr! Test backward compatibility endpoint
    """
    response = client.get("/api/languages/popular")
    
    # Should work or return proper error
    assert response.status_code in [200, 404, 500], f"Expected 200, 404, or 500, got {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        
        # Should have old format for backward compatibility
        assert "labels" in data, "Legacy endpoint should return 'labels'"
        assert "values" in data, "Legacy endpoint should return 'values'"
        assert isinstance(data["labels"], list), "Labels should be a list"
        assert isinstance(data["values"], list), "Values should be a list"


def test_schema_endpoint():
    """
    Yarr! Test schema information endpoint
    """
    response = client.get("/api/schema/stackoverflow_2023")
    
    assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        assert "source" in data, "Schema response should contain source"
        assert "schema" in data, "Schema response should contain schema data"


def test_root_endpoint():
    """
    Yarr! Test that our root endpoint serves the analytics dashboard
    """
    response = client.get("/")
    
    assert response.status_code == 200, f"Expected 200 status code for root endpoint, got {response.status_code}"
    assert "text/html" in response.headers.get("content-type", ""), "Root endpoint should return HTML content"


def test_api_parameter_validation():
    """
    Yarr! Test that API validates parameters properly
    """
    # Test invalid top_n parameter
    response = client.get("/api/analysis/technology-usage?top_n=0")
    assert response.status_code == 422, "Should return 422 for invalid top_n parameter"
    
    # Test very large top_n parameter
    response = client.get("/api/analysis/technology-usage?top_n=100")
    assert response.status_code == 422, "Should return 422 for top_n parameter exceeding limit"
