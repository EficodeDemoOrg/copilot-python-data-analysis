#!/usr/bin/env python3
"""
Yarr! This be the main FastAPI application for the Codebase Insights Analyzer MVP
A data analyst's treasure chest for exploring developer survey data, arrr!
"""

import os
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel

from .data_config import data_manager

# Yarr! Initialize our analytical ship!
app = FastAPI(
    title="Codebase Insights Analyzer", 
    description="A data analyst's treasure chest for exploring developer insights and survey data!",
    version="1.0.0"
)


class AnalysisResponse(BaseModel):
    """Response model for technology analysis"""
    labels: List[str]
    values: List[int]
    total_responses: int
    unique_technologies: int
    analysis_column: str
    data_source: str


class DataSourceInfo(BaseModel):
    """Information about available data sources"""
    name: str
    description: str
    available_columns: List[str]


@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    """
    Yarr! Serve the main treasure map to data analysts who visit our port!
    Returns the main HTML page for our analytics dashboard.
    """
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    
    if not os.path.exists(template_path):
        raise HTTPException(status_code=404, detail="Arrr! The dashboard template be missing!")
    
    return FileResponse(template_path, media_type="text/html")


@app.get("/api/data-sources", response_model=List[DataSourceInfo])
async def get_data_sources():
    """
    Yarr! Get information about all available data sources
    Perfect for data analysts who want to know what treasures are available!
    """
    sources = []
    for name, description in data_manager.get_available_sources().items():
        available_columns = data_manager.get_available_analysis_columns(name)
        sources.append(DataSourceInfo(
            name=name,
            description=description,
            available_columns=available_columns
        ))
    return sources


@app.get("/api/analysis/technology-usage", response_model=AnalysisResponse)
async def analyze_technology_usage(
    source: str = Query("stackoverflow_2023", description="Data source to analyze"),
    column: str = Query("LanguageHaveWorkedWith", description="Technology column to analyze"),
    top_n: int = Query(10, ge=1, le=50, description="Number of top technologies to return")
):
    """
    Yarr! The main analysis endpoint - flexible technology usage analysis!
    
    This endpoint allows data analysts to:
    - Choose different data sources
    - Analyze different technology categories (languages, databases, platforms, etc.)
    - Adjust the number of results
    
    Perfect for exploratory data analysis!
    """
    try:
        # Validate that the source exists
        available_sources = data_manager.get_available_sources()
        if source not in available_sources:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown data source '{source}'. Available sources: {list(available_sources.keys())}"
            )
        
        # Get available columns for validation
        available_columns = data_manager.get_available_analysis_columns(source)
        if column not in available_columns:
            raise HTTPException(
                status_code=400,
                detail=f"Column '{column}' not available for analysis in source '{source}'. Available columns: {available_columns}"
            )
        
        # Perform the analysis
        result = data_manager.analyze_technology_usage(source, column, top_n)
        
        return AnalysisResponse(
            labels=result["labels"],
            values=result["values"],
            total_responses=result["total_responses"],
            unique_technologies=result["unique_technologies"],
            analysis_column=column,
            data_source=source
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


# Backward compatibility endpoint for the original specification
@app.get("/api/languages/popular")
async def get_popular_languages() -> Dict[str, List]:
    """
    Yarr! Legacy endpoint for backward compatibility
    Redirects to the new flexible analysis system
    """
    try:
        result = data_manager.analyze_technology_usage("stackoverflow_2023", "LanguageHaveWorkedWith", 10)
        return {
            "labels": result["labels"],
            "values": result["values"]
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.get("/api/schema/{source_name}")
async def get_data_schema(source_name: str):
    """
    Yarr! Get schema information for a data source
    Useful for data analysts who want to understand the data structure
    """
    try:
        schema_info = data_manager.get_schema_info(source_name)
        if schema_info is None:
            raise HTTPException(status_code=404, detail=f"No schema information available for '{source_name}'")
        
        # Clean up NaN values for JSON serialization
        schema_dict = schema_info.fillna("").to_dict('records')
        
        return {
            "source": source_name,
            "schema": schema_dict
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve schema: {str(e)}")


# Yarr! This be how we run our ship when called directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
